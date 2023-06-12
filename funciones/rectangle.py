
from OpenGL.GL import *
from math import sqrt

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

