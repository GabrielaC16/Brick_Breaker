import pygame

import combi


def show_welcome_screen():
    pygame.init()

    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Brick Breacker")

    white = (255, 255, 255)
    black = (0, 0, 0)

    welcome = True

    # Cargar la imagen de fondo
    background_image = pygame.image.load("img/pantalla.jpg").convert()
    background_image = pygame.transform.scale(background_image, (window_width, window_height))

    while welcome:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Dibujar la imagen de fondo
        window.blit(background_image, (0, 0))


        # Crear un botón de inicio con esquinas redondeadas
        button_width = 200
        button_height = 50
        button_radius = 10
        start_button = pygame.Rect(window_width / 2 - button_width / 2, window_height -230, button_width, button_height)
        pygame.draw.rect(window, black, start_button, border_radius=button_radius)

        # Dibujar el texto del botón de inicio
        font = pygame.font.Font(None, 24)
        text = font.render("Iniciar", True, white)
        text_rect = text.get_rect(center=start_button.center)
        window.blit(text, text_rect)

        # Detectar el clic del botón de inicio
        mouse_pos = pygame.mouse.get_pos()
        if start_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                pygame.display.quit()
                break
                # Abrir una nueva ventana
                #game_window = combi.main()
        pygame.display.update()

#PROMPT CHAT GPT
'''
Crea un programa en Python utilizando la biblioteca Pygame para crear una pantalla de bienvenida para un juego. 
La pantalla debe tener una ventana con dimensiones de 800x600 píxeles y el título 'Arkanoid'. 
El fondo debe ser de color blanco. Muestra el texto 'Bienvenido' en color negro en el centro de la ventana. 
Crea un botón rectangular con la etiqueta 'Iniciar' en el centro de la ventana, de color negro. 
El texto del botón debe ser de color blanco. Cuando se haga clic en el botón 'Iniciar', sal de la pantalla de bienvenida."
'''
