import cv2
import numpy as np

# Read the crop image
image = cv2.imread('image.png')
if image is None:
    print("Image not found.")
    exit()

# Resize the image
image = cv2.resize(image, (640, 480))

# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the color range for detecting pests (brown shades)
lower_brown = np.array([10, 100, 20])
upper_brown = np.array([20, 255, 200])

# Create a mask based on the defined color range
mask = cv2.inRange(hsv, lower_brown, upper_brown)

# Apply the mask to the original image
result = cv2.bitwise_and(image, image, mask=mask)

# Find contours of detected pest-like regions
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
pest_count = len(contours)

# Print the number of possible pest instances
print(f"Possible pest instances detected: {pest_count}")

# Display the resulting masked image
cv2.imshow("Detected Pests", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
