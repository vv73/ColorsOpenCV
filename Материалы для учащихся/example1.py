# Grayscale вручную

import cv2
import numpy as np

# Загружаем и сразу показываем изображение
image = cv2.imread("pics/cat2.png")
cv2.imshow("Image", image)
# Узнаем его ширину и высоту
width = image.shape[1]
height = image.shape[0]
# Обесцвечиваем вручную
for y in range(height):
    for x in range(width):
        image[y, x] = int(np.average(image[y, x]))

# Показываем результат
cv2.imshow("Grayscale", image)

# Задерживаем программу до нажатия на кнопку
cv2.waitKey(0)