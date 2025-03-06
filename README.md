# Linear Regression from Scratch 🚀

This project implements **Linear Regression** from scratch using **NumPy**, without relying on high-level machine learning libraries like **scikit-learn**. The goal is to understand the inner workings of the algorithm, including **gradient descent** and **parameter optimization**, which are fundamental techniques in machine learning.

## 🔹 Project Overview:
- **Problem:** Linear regression is a simple yet powerful algorithm used to model the relationship between a dependent variable (y) and one or more independent variables (X).
- **Approach:** Implemented the linear regression model from scratch, applying gradient descent to optimize the model's parameters (slope and intercept).
- **Key Concepts Covered:**  
  - **Gradient Descent:** Optimizing the cost function (Mean Squared Error) to minimize prediction errors.
  - **Model Training:** Understanding how the model is iteratively trained to learn the best-fitting line.
  - **Data Visualization:** Using **Matplotlib** to plot data points and the regression line for better understanding.

## 🔹 Why This Project Matters:
- Provides a strong foundation in machine learning algorithms.
- Introduces fundamental concepts such as **cost functions**, **optimization**, and **gradient descent**.
- Shows how linear regression can be applied to real-world datasets, and forms the basis for more complex machine learning models.

## 🔹 How It Works:
- **Data:** Generates synthetic data (or optionally, uses `dataset.csv`).
- **Model Training:** Optimizes parameters using **gradient descent** over multiple iterations.
- **Visualization:** Plots the training data and the regression line.

## 🔹 Requirements:
- **Python 3.x**
- **NumPy**
- **Matplotlib**

To install dependencies, run:
```bash
pip install numpy matplotlib
