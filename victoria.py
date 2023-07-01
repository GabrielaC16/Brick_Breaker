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
    background_image = pygame.image.load("img/win.jpg").convert()
    background_image = pygame.transform.scale(background_image, (window_width, window_height))

    while welcome:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Dibujar la imagen de fondo
        window.blit(background_image, (0, 0))

        # Crear un botón de reiniciar con esquinas redondeadas
        button_width = 200
        button_height = 50
        button_radius = 10
        restart_button = pygame.Rect((window_width - button_width )/4, window_height / 2 +200, button_width, button_height)
        pygame.draw.rect(window, (255, 255, 255), restart_button, border_radius=button_radius)
        # Dibujar el texto del botón de reiniciar
        font = pygame.font.Font(None, 24)
        restart_text = font.render("Reiniciar", True, (0, 0, 0))
        restart_text_rect = restart_text.get_rect(center=restart_button.center)
        window.blit(restart_text, restart_text_rect)

        # Crear un botón de salir con esquinas redondeadas
        quit_button = pygame.Rect(window_width  - button_width -150, window_height / 2 + 200, button_width, button_height)
        pygame.draw.rect(window, (255, 255, 255), quit_button, border_radius=button_radius)
        # Dibujar el texto del botón de salir
        quit_text = font.render("Salir", True, (0, 0, 0))
        quit_text_rect = quit_text.get_rect(center=quit_button.center)
        window.blit(quit_text, quit_text_rect)


        '''
        # Crear un botón de inicio con esquinas redondeadas
        button_width = 200
        button_height = 50
        button_radius = 10
        start_button = pygame.Rect(window_width / 2 - button_width / 2, window_height / 2, button_width, button_height)
        pygame.draw.rect(window, black, start_button, border_radius=button_radius)
        # Dibujar el texto del botón de inicio
        font = pygame.font.Font(None, 24)
        text = font.render("Iniciar", True, white)
        text_rect = text.get_rect(center=start_button.center)
        window.blit(text, text_rect)
        '''
        # Detectar el clic del botón de inicio
        mouse_pos = pygame.mouse.get_pos()
        if restart_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                pygame.display.quit()
                # Abrir una nueva ventana
                game_window = combi.main()
        elif quit_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                pygame.quit()
                quit()
        pygame.display.update()

# BASADO EN inicio.py