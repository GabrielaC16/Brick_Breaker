from math import sin,cos,sqrt
import fractales

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from math import sqrt

# Dimensiones de la ventana
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 1200

# Clase para el rectángulo
class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self):
        glColor3f(0, 1, 0)
        glBegin(GL_QUADS)
        glVertex2f(self.x, self.y)  # Esquina superior izquierda
        glVertex2f(self.x + self.width, self.y)  # Esquina superior derecha
        glVertex2f(self.x + self.width, self.y + self.height)  # Esquina inferior derecha
        glVertex2f(self.x, self.y + self.height)  # Esquina inferior izquierda
        glEnd()

    def collides_with_ball(self, ball):
        # Calcula el punto más cercano del rectángulo al centro de la bola
        closest_x = max(self.x, min(ball.x, self.x + self.width))
        closest_y = max(self.y, min(ball.y, self.y + self.height))

        # Calcula la distancia entre el punto más cercano y el centro de la bola
        distance = sqrt((closest_x - ball.x) ** 2 + (closest_y - ball.y) ** 2)

        return distance <= ball.radius

# Clase para la bola
class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = 0.2
        self.speed_y = 0.2

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x <= 0 or self.x >= WINDOW_WIDTH:
            self.speed_x *= -1
        if self.y <= 0 or self.y >= WINDOW_HEIGHT:
            self.speed_y *= -1

    def draw(self):
        glColor3f(1, 0, 0)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(self.x, self.y)  # Centro de la bola
        num_segments = 100
        for i in range(num_segments + 1):
            angle = 2.0 * 3.1415926 * i / num_segments
            x = self.x + self.radius * cos(angle)
            y = self.y + self.radius * sin(angle)
            glVertex2f(x, y)
        glEnd()

    def collides_with_rectangle(self, rectangle):
        # Calcula el punto más cercano del rectángulo al centro de la bola
        closest_x = max(rectangle.x, min(self.x, rectangle.x + rectangle.width))
        closest_y = max(rectangle.y, min(self.y, rectangle.y + rectangle.height))

        # Calcula la distancia entre el punto más cercano y el centro de la bola
        distance = sqrt((closest_x - self.x) ** 2 + (closest_y - self.y) ** 2)

        return distance <= self.radius

def main():
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)  # Definir el sistema de coordenadas

    rectangle = Rectangle(300, 400, 100, 50)


    all_position = fractales.gen_positions()

    for ele in all_position:
        print(ele[0],ele[1])

    squares = [] 

    for ele in all_position : 
        squares.append(Rectangle(ele[0], ele[1], 50, 50))

    #squares = [Rectangle(200, 200, 50, 50), Rectangle(500, 200, 50, 50)]

    ball = Ball(400, 300, 20)
    ball.speed_x = 0.2
    ball.speed_y = 0.2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT)

        # Movimiento del rectángulo
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rectangle.x -= 1
        if keys[pygame.K_RIGHT]:
            rectangle.x += 1

        # Movimiento de la bola
        ball.move()

        # Colisiones entre la bola y el rectángulo
        if ball.collides_with_rectangle(rectangle):
            ball.speed_y *= -1

        # Colisiones entre la bola y los cuadrados
        for square in squares:
            if ball.collides_with_rectangle(square):
                squares.remove(square)
                ball.speed_y *= -1

        # Dibujar el rectángulo
        rectangle.draw()

        # Dibujar los cuadrados
        for square in squares:
            square.draw()

        # Dibujar la bola
        ball.draw()

        pygame.display.flip()

if __name__ == '__main__':
    main()

