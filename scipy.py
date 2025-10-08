# scipy_tutorial.py
# Run: python scipy_tutorial.py
# Requires: pip install scipy numpy matplotlib

import numpy as np
from scipy import integrate, optimize
import math

# 1. Numerical integration: integrate sin(x) from 0 to pi
result, error = integrate.quad(lambda x: np.sin(x), 0, np.pi)
print("Integral of sin(x) from 0 to pi =", result, "error estimate:", error)

# 2. Root finding example: solve x^3 - 2x - 5 = 0 near x=2
f = lambda x: x**3 - 2*x - 5
root = optimize.newton(f, x0=2.0)
print("Root of x^3 - 2x -5 near 2:", root)

# 3. Curve fitting (least squares): fit noisy quadratic y = a*x^2 + b*x + c
true_params = (2.0, -1.0, 0.5)
x = np.linspace(-3, 3, 50)
y_true = true_params[0]*x**2 + true_params[1]*x + true_params[2]
rng = np.random.default_rng(0)
y_noisy = y_true + rng.normal(scale=1.0, size=x.shape)

def model(x, a, b, c):
    return a*x**2 + b*x + c

popt, pcov = optimize.curve_fit(model, x, y_noisy, p0=(1, 0, 0))
print("\nFitted params (a,b,c):", popt)
print("True params:", true_params)

# (Optional) Quick plot if you want to visualize (requires matplotlib)
try:
    import matplotlib.pyplot as plt
    plt.scatter(x, y_noisy, label="data")
    plt.plot(x, model(x, *popt), color="red", label="fit")
    plt.plot(x, y_true, color="green", linestyle="--", label="true")
    plt.legend()
    plt.title("Curve fit example (SciPy)")
    plt.show()
except Exception:
    pass
