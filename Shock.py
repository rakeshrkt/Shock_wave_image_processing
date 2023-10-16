import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# image = cv2.imread(r'C:\Users\rakes\Downloads\bulletshock.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.imread(r'bulletshock.jpg', cv2.IMREAD_GRAYSCALE)

blurred = cv2.GaussianBlur(image, (47, 47), 0)
edges = cv2.Canny(blurred, 50, 100)

#Plot the edges using matplotlib
plt.imshow(edges, cmap='gray')
plt.title('Canny Edges')
plt.axis('off')
plt.show()

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

all_points = []
# Loop through the detected contours and collect all points
for contour in contours:
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)
    approx = np.squeeze(approx, axis=1)  # Remove unnecessary axis
    # Add (x, y) values to the list
    all_points.extend(approx.tolist())

# Convert points to numpy arrays
all_points = np.array(all_points)
plt.figure()
plt.imshow(edges, cmap= 'gray')

# Define a function for linear regression (y = mx + b)
def linear_func(x, m, b):
    return m * x + b

# Fit a linear regression line using curve_fit
x_data = all_points[:, 0]
y_data = all_points[:, 1]
params, _ = curve_fit(linear_func, x_data, y_data)
slope, intercept = params
y = slope*x_data + intercept

# Calculate the regression line points
x_range = np.array([min(x_data), max(x_data)])
y_range = linear_func(x_range, slope, intercept)

plt.plot(x_range, y_range, 'red')
plt.axis('off')
plt.show()

# Mach number calculation using slope
mach_number = abs(np.sqrt(slope**2+1)/slope)
print('Mach Number: %f' %mach_number)
