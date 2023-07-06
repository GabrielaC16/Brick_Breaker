import cv2
import mediapipe as mp
import numpy as np

# Configurar la cámara
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Inicializar el reconocimiento de la mano
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Dimensiones de la ventana del juego
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Características de la plataforma
platform_width = 100
platform_height = 20
platform_x = WINDOW_WIDTH // 2 - platform_width // 2
platform_y = WINDOW_HEIGHT - 50

# Crear una ventana para el juego
cv2.namedWindow('Game')

while True:
    ret, frame = cap.read()

    # Voltear horizontalmente la imagen de la cámara
    frame = cv2.flip(frame, 1)

    # Convertir la imagen a RGB para MediaPipe
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Realizar la detección de la mano
    results = hands.process(image_rgb)

    # Comprobar si se detectaron manos
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Obtener la posición del dedo índice
            index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            x, y = int(index_finger.x * frame.shape[1]), int(index_finger.y * frame.shape[0])

            # Mover la plataforma de acuerdo al movimiento de la mano
            platform_x = x - platform_width // 2

            # Limitar los límites de movimiento de la plataforma
            if platform_x < 0:
                platform_x = 0
            elif platform_x > WINDOW_WIDTH - platform_width:
                platform_x = WINDOW_WIDTH - platform_width

            # Dibujar los puntos clave y la conexión entre ellos en la imagen
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Crear un fondo negro para la ventana del juego
    game_frame = np.zeros((WINDOW_HEIGHT, WINDOW_WIDTH, 3), dtype=np.uint8)

    # Dibujar el rectángulo amarillo en el fondo negro
    cv2.rectangle(game_frame, (platform_x, platform_y), (platform_x + platform_width, platform_y + platform_height),
                  (0, 255, 255), -1)

    # Mostrar la ventana de la cámara con la orientación corregida
    cv2.imshow('Camera', frame)

    # Mostrar la ventana del juego
    cv2.imshow('Game', game_frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()