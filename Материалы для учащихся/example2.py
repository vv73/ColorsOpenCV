# RGB эффект

import cv2
import numpy as np

# Загружаем и сразу показываем изображение
image = cv2.imread("pics/cat2.png")
cv2.imshow("Image", image)

image[:, ::3, 0] = 0
image[:, ::3, 1] = 0

image[:, 1::3,  1] = 0
image[:, 1::3, 2] = 0

image[:, 2::3, 0] = 0
image[:, 2::3, 2] = 0

# Показываем результат
cv2.imshow("RGB", image)
# Задерживаем программу до нажатия на кнопку
cv2.waitKey(0)