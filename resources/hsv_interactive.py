import cv2
import numpy as np

# trackbar callback function
def on_trackbar(x):
    global H_low, H_high, S_low, S_high, V_low, V_high
    # установка значений H,S,V High and low
    try:
        H_low = cv2.getTrackbarPos('low H', 'controls')
        H_high = cv2.getTrackbarPos('high H', 'controls')
        S_low = cv2.getTrackbarPos('low S', 'controls')
        S_high = cv2.getTrackbarPos('high S', 'controls')
        V_low = cv2.getTrackbarPos('low V', 'controls')
        V_high = cv2.getTrackbarPos('high V', 'controls')
    except:
        print("Preparing trackbars...")

# Создаем отдельное окно для управления
cv2.namedWindow('controls', 2)
cv2.resizeWindow('controls', 550, 10);

# глобальные переменные
H_low = 0
H_high = 179
S_low = 0
S_high = 255
V_low = 0
V_high = 255

# создаем трекбары для high,low H,S,V
cv2.createTrackbar('low H', 'controls', 0, 179, on_trackbar)
cv2.createTrackbar('high H', 'controls', 179, 179, on_trackbar)

cv2.createTrackbar('low S', 'controls', 0, 255, on_trackbar)
cv2.createTrackbar('high S', 'controls', 255, 255, on_trackbar)

cv2.createTrackbar('low V', 'controls', 0, 255, on_trackbar)
cv2.createTrackbar('high V', 'controls', 255, 255, on_trackbar)

##############################################
# Загружаем картинку
img = cv2.imread("../_common_res/intro.png")
##############################################

while True:

    # Конвертируем в HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hsv_low = np.array([H_low, S_low, V_low], np.uint8)
    hsv_high = np.array([H_high, S_high, V_high], np.uint8)

    # Создаем маску
    mask = cv2.inRange(hsv, hsv_low, hsv_high)
    # Накладываем маску
    res = cv2.bitwise_and(img, img, mask=mask)

    # show image
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', res)

    # Ожидание нажатия `ESC`
    if cv2.waitKey(1) == 27:
        break

# Закрываем все окна
cv2.destroyAllWindows()