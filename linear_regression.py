import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic dataset
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # 100 data points
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3X + noise

# Initialize parameters
theta = np.random.randn(2, 1)  # Random weights (bias + slope)
learning_rate = 0.1
epochs = 1000
m = len(X)

# Add bias term (X0 = 1)
X_b = np.c_[np.ones((m, 1)), X]

# Gradient Descent
for epoch in range(epochs):
    gradients = (2/m) * X_b.T.dot(X_b.dot(theta) - y)
    theta -= learning_rate * gradients

# Predictions
y_pred = X_b.dot(theta)

# Plot results
plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_pred, color="red", label="Linear Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.title("Linear Regression from Scratch")
plt.show()
