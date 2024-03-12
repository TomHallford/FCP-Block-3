import sys
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def input_handler():
    prey = 100
    pred = 100
    alpha = 0.9
    beta = 1
    delta = 0.75
    gamma = 0.9
    save = False
    name = ""
    arg = iter(sys.argv[1:])
    for args in sys.argv[1:]:
        if args == "--initial":
            prey = int(next(arg))
            pred = int(next(arg))
        elif args == "--alpha":
            alpha = int(next(arg))
        elif args == "--beta":
            beta = int(next(arg))
        elif args == "--delta":
            delta = int(next(arg))
        elif args == "gamma":
            gamma = int(next(arg))
        elif args == "save_plot":
            save = True
            name = str(next(arg))
    return prey, pred, alpha, beta, gamma, delta, save, name


def diff_lotka_volterra(pop, t, alpha, beta, gamma, delta):
    x = pop[0]
    y = pop[1]
    dxdt = (alpha*x) - (beta*x*y)
    dydt = (delta*x*y) - (gamma*y)
    gradient = [dxdt, dydt]
    return gradient


def solve_lotka_volterra(pop, t_max, alpha, beta, gamma, delta):
    t = np.linspace(0, t_max, 1000)
    lotka_volterra = odeint(diff_lotka_volterra, pop, t, (alpha, beta, gamma, delta))
    return lotka_volterra, t


def plot_lotka_volterra(t, data, save, name):
    fig = plt.figure()
    plt.plot(t, data[:, 0])
    plt.plot(t, data[:, 1])
    plt.xlabel("time")
    plt.ylabel("population")
    plt.legend(["prey", "predator"])
    if save:
        plt.savefig(name)
    plt.show()


def main():
    prey, pred, alpha, beta, gamma, delta, save, name = input_handler()
    t_max = 500
    pop = [prey, pred]
    data, t = solve_lotka_volterra(pop, t_max, alpha, beta, gamma, delta)
    save = True
    name = "x"
    plot_lotka_volterra(t, data, save, name)


if __name__ == "__main__":
    main()