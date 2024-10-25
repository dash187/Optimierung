import matplotlib.pyplot as plt
import numpy as np

def optimize(xk, eps):
    history = [(xk, gradf_xk := gradf(xk))]
    while abs(gradf_xk) > eps:
        dk = -gradf_xk
        tau = backtracking_line_search(xk, dk, 0.5)
        xk += tau * dk
        history += [(xk, gradf_xk := gradf(xk))]    
    return history

def is_armijo_satisfied(xk, next_xk, dk, tau, delta):
    return f(next_xk) - f(xk) <= delta * tau * gradf(xk) * dk

def backtracking_line_search(xk, dk, beta):
    tau = 1
    while not is_armijo_satisfied(xk, xk + tau * dk, dk, tau, 0.0001):
        tau *= beta
    return tau

def f(x):
    return 1/4 * x**4 + 2 * x**3 - 3 * x - 4

def gradf(x):
    return x**3 + 6 * x**2 - 3


def render_function(start, end):
    fig, ax = plt.subplots()
    x_vals = np.linspace(start, end, 100)
    f_vals = np.array([f(x) for x in x_vals])
    gradf_vals = np.array([gradf(x) for x in x_vals])

    ax.plot(x_vals, f_vals, label='f')
    ax.plot(x_vals, gradf_vals, label='gradf')
    ax.legend()
    plt.show() 


if __name__ == '__main__':
    history = optimize(3.0, 0.00001)
    for line in history:
        print(line)
    # render_function(-10, 5)

