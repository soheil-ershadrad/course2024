import numpy as np
import matplotlib.pyplot as plt

# Sample data points (x, y)
x = np.array([7.08, 7.09, 7.1])
y = np.array([-.15673142E+03, -.15673257E+03, -.15673169E+03])

# Fit a parabola (second-degree polynomial) to the points
coefficients = np.polyfit(x, y, 2)

# Create a polynomial from the coefficients
polynomial = np.poly1d(coefficients)

# Find the vertex (minimum) of the parabola
# For a parabola ax^2 + bx + c, the minimum or maximum occurs at x = -b / (2a)
a = coefficients[0]
b = coefficients[1]
minimum_x = -b / (2 * a)
minimum_y = polynomial(minimum_x)

# Print the minimum point
print(f"Minimum occurs at x = {minimum_x}, y = {minimum_y}")

# Plot the points and the fitted parabola
x_fine = np.linspace(min(x), max(x), 100)
y_fine = polynomial(x_fine)

plt.scatter(x, y, color='red', label='Data points')
plt.plot(x_fine, y_fine, label='Fitted parabola')
plt.scatter(minimum_x, minimum_y, color='blue', label=f'Minimum at x={minimum_x:.2f}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Parabola Fitting and Minimum')
#plt.show()
plt.savefig('fig_minima.png')
