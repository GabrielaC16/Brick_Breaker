import pygame

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Arkanoid")

white = (255, 255, 255)
black = (0, 0, 0)

def show_welcome_screen():
    welcome = True

    # Cargar la imagen de fondo
    background_image = pygame.image.load("background.png").convert()

    background_image = pygame.transform.scale(background_image, (window_width, window_height))

    while welcome:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Dibujar la imagen de fondo
        window.blit(background_image, (0, 0))

        # Dibujar el texto de bienvenida
        font = pygame.font.Font(None, 36)
        text = font.render("Bienvenidos, a \"Romper ladrillo\"", True, (0, 0, 0))
        text_rect = text.get_rect(center=(window_width / 2, window_height / 2 - 50))
        window.blit(text, text_rect)

        # Crear un botón de inicio con esquinas redondeadas
        button_width = 200
        button_height = 50
        button_radius = 10
        start_button = pygame.Rect(window_width / 2 - button_width / 2, window_height / 2, button_width, button_height)
        pygame.draw.rect(window, (0, 0, 0), start_button, border_radius=button_radius)

        # Dibujar el texto del botón de inicio
        font = pygame.font.Font(None, 24)
        text = font.render("Iniciar", True, (255, 255, 255))
        text_rect = text.get_rect(center=start_button.center)
        window.blit(text, text_rect)

        # Detectar el clic del botón de inicio
        mouse_pos = pygame.mouse.get_pos()
        if start_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                welcome = False

        pygame.display.update()



show_welcome_screen()

