import numpy as np
import cv2

print(cv2.COLOR_HSV2BGR)

def on_trackbar(value, image):
    v1 = cv2.getTrackbarPos('v1', 'Image')
    v2 = cv2.getTrackbarPos('v2', 'Image')
    v3 = cv2.getTrackbarPos('v3', 'Image')

    # Create an HSV image with the adjusted values
    image2 = cv2.cvtColor(image, 40)
    image2[:,:,0] = v1
    image2[:,:,1] = v2
    image2[:,:,2] = v3
    image3 = cv2.cvtColor(image2, 54)

    # Display the RGB image in the OpenCV window
    cv2.imshow('Image', image3)


# Create a black image
image = np.zeros((200, 500, 3), dtype=np.uint8)
cv2.imshow('Image', image)

# Check if the image was loaded successfully
if image is None:
    print('Error: Failed to load the image')
    exit()

# Create a window
cv2.namedWindow('Image')

# Create trackbars
cv2.createTrackbar('v1', 'Image', 100, 179, lambda x: on_trackbar(x, image))
cv2.createTrackbar('v2', 'Image', 128, 255, lambda x: on_trackbar(x, image))
cv2.createTrackbar('v3', 'Image', 128, 255, lambda x: on_trackbar(x, image))

# Wait for the user to press 'q' to exit
while cv2.waitKey(1) & 0xFF != ord('q'):
    pass

# Destroy the window
cv2.destroyAllWindows()