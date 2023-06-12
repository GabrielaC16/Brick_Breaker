import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from funciones.ball import Ball
from funciones.rectangle import Rectangle

# Dimensiones de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600



def main():
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)  # Definir el sistema de coordenadas
    pygame.display.set_caption("Arkanoid")

    rectangle = Rectangle(300, 400, 100, 50)
    squares = [Rectangle(200, 200, 50, 50), Rectangle(500, 200, 50, 50)]
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
        ball.move(WINDOW_WIDTH, WINDOW_HEIGHT)

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

