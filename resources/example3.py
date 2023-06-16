# Осветление в HSV
import cv2
import numpy as np

# Загружаем и сразу показываем изображение
image = cv2.imread("pics/cat3.png")
cv2.imshow("Image", image)

# Переводим в HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Увеличиваем яркость (третью компоненту)
image_hsv[:, :, 2] = np.clip(image_hsv[:,:,2].astype(np.int32) + 30, 0, 255)

# Переводим обратно в BGR
light_image = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

# Показываем результат
cv2.imshow("Lighten", light_image)
# Задерживаем программу до нажатия на кнопку
cv2.waitKey(0)