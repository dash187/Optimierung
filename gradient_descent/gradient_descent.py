import matplotlib.pyplot as plt
import numpy as np

def grad_descent(f):
    pass

def is_armijo_satisfied(f, grad_f, xk, dk, tau, delta) -> bool:
    h_tau = np.polyval(f, (xk + tau * dk))
    f_xk = np.polyval(f, xk)
    gradf_xk = np.polyval(grad_f, xk)
    linear_approx = f_xk + tau * delta * gradf_xk * dk
    return h_tau <= linear_approx

def backtracking_line_search(f, gradf, h, xk, dk, beta) -> float:
    tau = 1
    while not is_armijo_satisfied(f, grad_f, xk, dk, tau, 0.0001):
        tau *= beta
    return tau


def render_function(f, start, end) -> None:
    fig, ax = plt.subplots()
    x_vals = np.linspace(start, end, 100)
    y_vals = np.array([np.polyval(f, x) for x in x_vals])
    ax.plot(x_vals, y_vals)
    plt.show() 


if __name__ == '__main__':
    f = np.array([1/4, 2, 0, -3, -4])
    grad_f = np.array([1, 6, 0, -3])
    print(np.gradient([2, 0, 0]))
    render_function(f, -10, 5)

