from OpenGL.GL import *
from math import sin,cos,sqrt

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = 0.2
        self.speed_y = 0.2

    def move(self, WINDOW_HEIGHT,WINDOW_WIDTH):
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
