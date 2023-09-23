import cv2
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread(r'c:\Users\rakes\Downloads\1920px-F4_p4_red_planedrop.jpg', cv2.IMREAD_GRAYSCALE)

# Resize the image to fit the screen dimensions (adjust these values as needed)
desired_width = 1920
desired_height = 1080

# Calculate the aspect ratio
aspect_ratio = image.shape[1] / image.shape[0]

# Resize the image while maintaining the aspect ratio
if aspect_ratio > 1:
    new_width = desired_width
    new_height = int(desired_width / aspect_ratio)
else:
    new_height = desired_height
    new_width = int(desired_height * aspect_ratio)

resized_image = cv2.resize(image, (new_width, new_height))

# Convert the resized image to grayscale
#gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(resized_image, (5, 5), 0)

# Apply edge detection using the Canny method
edges = cv2.Canny(blurred, 30, 150)

# Find contours in the edge-detected image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

all_points = []

# Loop through the detected contours and collect all points
for contour in contours:
    if len(contour) >= 2:
        points = np.squeeze(contour, axis=1)  # Remove redundant dimensions
        all_points.extend(points)

# Approximate the shock line as a polygon using cv2.approxPolyDP
epsilon = 5  # Adjust the epsilon value as needed
shock_polygon = cv2.approxPolyDP(np.array(all_points), epsilon, True)

# Draw the shock polygon on the resized image
result = image.copy()
cv2.polylines(result, [shock_polygon], isClosed=True, color=(0, 0, 255), thickness=2)

# Calculate the Mach number based on the slope of the approximated shock line
line_params = cv2.fitLine(shock_polygon, cv2.DIST_L2, 0, 0.01, 0.01)
slope = line_params[1] / line_params[0]

mach_number = abs(1 / slope)  # Assuming a weak shock

print("Mach Number: %f" %mach_number)

# Display the result
cv2.imshow('Shock Detection', result)
cv2.waitKey(0)
cv2.destroyAllWindows()





