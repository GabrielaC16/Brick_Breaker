import cv2

# id de la cámara
cam = cv2.VideoCapture(0)

while True:
    check, img = cam.read()
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break