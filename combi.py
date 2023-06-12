import pygame
import fractales
from OpenGL.GL import *
from OpenGL.GLU import *

import victoria
from funciones.ball import Ball
from funciones.rectangle import Rectangle
import inicio
import derrota
# Dimensiones de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600



def main():
    inicio.show_welcome_screen()
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)  # Definir el sistema de coordenadas
    pygame.display.set_caption("Brick Breacker")

    rectangle = Rectangle(400, 0, 100, 20)


    all_position = fractales.gen_positions()

    squares = [] 


#    for ele in all_position :
 #       print(ele[0],ele[1])

    for ele in all_position : 
        squares.append(Rectangle(ele[0], ele[1], 20, 20))
    

    #squares = [Rectangle(200, 200, 50, 50), Rectangle(500, 200, 50, 50)]
    ball = Ball(400, 60, 15)
    ball.speed_x = 0.6
    ball.speed_y = 0.6

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT)

        # Movimiento del rectángulo
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and rectangle.x >0:
            rectangle.x -= 2
        if keys[pygame.K_RIGHT] and rectangle.x < 700:
            rectangle.x += 2

        # Movimiento de la bola
        ball.move(WINDOW_HEIGHT, WINDOW_WIDTH)

        # Colisiones entre la bola y el rectángulo
        if ball.collides_with_rectangle(rectangle):
            print(len(squares))
            ball.speed_y *= -1

        # Colisiones entre la bola y los cuadrados
        for square in squares:
            if ball.collides_with_rectangle(square):
                squares.remove(square)
                ball.speed_y *= -1

        # SI COLICISIOA CON EL SUELO LA PELOTA
        if ball.collide_with_floor():
            derrota.show_welcome_screen()
        #SI LOS CUADRADOS SON 0
        if len(squares) == 0:
            victoria.show_welcome_screen()
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

#xd prueba