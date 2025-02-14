import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# sigmoid regression (manual)

# Sample data
x_data = np.linspace(-10, 10, 100)  # Predictor variable
y_data = 1 / (1 + np.exp(-0.8 * (x_data - 2)))  # True sigmoid function
# Adding some noise to simulate real-world data
y_noisy = y_data + 0.05 * np.random.normal(size=len(x_data))


# Define the sigmoid function
def sigmoid(x, beta_0, beta_1):
    return 1 / (1 + np.exp(-(beta_0 + beta_1 * x)))


# Fit the sigmoid curve to the noisy data
popt, _ = curve_fit(sigmoid, x_data, y_noisy, p0=[0, 1])  # Initial guesses for beta_0 and beta_1

# Extract fitted parameters
beta_0, beta_1 = popt
print(f"Fitted Parameters: beta_0 = {beta_0}, beta_1 = {beta_1}")

# Generate the fitted sigmoid curve
x_fit = np.linspace(-10, 10, 100)  # Predictor variable for smooth curve
y_fit = sigmoid(x_fit, beta_0, beta_1)

# Plot original data and the fitted sigmoid curve
plt.scatter(x_data, y_noisy, color='blue', label="Noisy Data")
plt.plot(x_fit, y_fit, color='red', label="Fitted Sigmoid Curve")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Sigmoid Regression Fit")
plt.show()


# logistic regression w scikit-learn

from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Sample data
x = np.linspace(-10, 10, 100).reshape(-1, 1)  # Feature data
y = (x > 0).astype(int).ravel()  # Binary target: 1 if x > 0, 0 otherwise

# Fit Logistic Regression
model = LogisticRegression()
model.fit(x, y)

# Predict probabilities
x_new = np.linspace(-10, 10, 1000).reshape(-1, 1)
y_prob = model.predict_proba(x_new)[:, 1]  # Probability of class 1

# Plot results
plt.scatter(x, y, color="blue", label="Data")
plt.plot(x_new, y_prob, color="red", label="Sigmoid Curve (Logistic Regression)")
plt.xlabel("x")
plt.ylabel("Probability")
plt.legend()
plt.title("Sigmoid Regression: Logistic Regression Fit")
plt.show()
