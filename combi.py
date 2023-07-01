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
WINDOW_WIDTH = 1900
WINDOW_HEIGHT = 1000



def main():
    inicio.show_welcome_screen()
    pygame.init()
    pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
    gluOrtho2D(0, WINDOW_WIDTH, 0, WINDOW_HEIGHT)  # Definir el sistema de coordenadas
    pygame.display.set_caption("Brick Breacker")
    color_rectangle = (1, 1, 1)
    rectangle = Rectangle(400, 0, 100, 20,color_rectangle)


    all_position = fractales.gen_positions()

    squares_nivel1 = [] # se rompen de 1 golpe
    squares_nivel2 = [] # se rompen de 2 golpe

#    for ele in all_position :
 #       print(ele[0],ele[1])
    all_position2 = list(all_position)
    mitad = len(all_position2) // 2
    
    
    color =  (0, 1, 0)
    for ele in all_position2[:mitad] : 
        squares_nivel1.append(Rectangle(ele[0], ele[1], 20, 20,color))

    color2 = (1, 1, 0)
    for ele in all_position2[mitad:] : 
        squares_nivel2.append(Rectangle(ele[0], ele[1], 20, 20,color2))
    

    #squares = [Rectangle(200, 200, 50, 50), Rectangle(500, 200, 50, 50)]
    ball = Ball(400, 60, 15)
    ball.speed_x = 0.4
    ball.speed_y = 0.4
    golpes_cuadrados_nivel2 = [2] * mitad
    while True:
        i = -1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        glClear(GL_COLOR_BUFFER_BIT)

        # Movimiento del rectángulo
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and rectangle.x >0:
            rectangle.x -= 2
        if keys[pygame.K_RIGHT] and rectangle.x < WINDOW_WIDTH:
            rectangle.x += 2

        # Movimiento de la bola
        ball.move(WINDOW_HEIGHT, WINDOW_WIDTH)

        # Colisiones entre la bola y el rectángulo
        if ball.collides_with_rectangle(rectangle):
            #print(len(squares))
            ball.speed_y *= -1

        # Colisiones entre la bola y los cuadrados ROMPIBLES
        for square in squares_nivel1:
            if ball.collides_with_rectangle(square):
                #print("tocaste cuadrado level 1")
                squares_nivel1.remove(square)
                ball.speed_y *= -1
                ball.speed_x *= -1
        # Colisiones entre la bola y los cuadrados ROMPIBLES NIVEL 2
       
        for square in squares_nivel2:
            i+=1
            
            if ball.collides_with_rectangle(square):
                square.change_color(color)
                golpes_cuadrados_nivel2[i] -= 1
                ball.speed_y *= -1
                ball.speed_x *= -1
                print("tocaste cuadrado nivel 2: ",i)
                if golpes_cuadrados_nivel2[i] == 0:
                    squares_nivel2.remove(square)
                    print("Rompiste cuadrado nivel 2: ",i)
                
        


        # Colisiones entre la bola y los cuadrados NIVEL 1
        

        # SI COLICISIOA CON EL SUELO LA PELOTA
        if ball.collide_with_floor():
            derrota.show_welcome_screen()
        #SI LOS CUADRADOS SON 0
        if len(squares_nivel1) == 0:
            victoria.show_welcome_screen()
        # Dibujar el rectángulo
        rectangle.draw()

        # Dibujar los cuadrados
        for square in squares_nivel1+squares_nivel2:
            square.draw()

        # Dibujar la bola
        ball.draw()

        pygame.display.flip()

if __name__ == '__main__':
    main()

#xd prueba
