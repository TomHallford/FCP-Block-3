import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import argparse


def input_handler():
    '''
    Takes in inputs from the terminal,
    returns the values for the variables and whether you want it to be saved or not
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--initial", type=int, default=100)
    parser.add_argument("--alpha", type=float, default=0.9)
    parser.add_argument("--beta", type=float, default=1)
    parser.add_argument("--gamma", type=float, default=0.75)
    parser.add_argument("--delta", type=float, default=0.9)
    parser.add_argument("--save_plot", type=str, default="null")
    args = parser.parse_args()

    prey = args.initial
    pred = args.initial
    alpha = args.alpha
    beta = args.beta
    gamma = args.gamma
    delta = args.delta
    name = args.save_plot
    if name != "null":
        save = True
    else:
        save = False

    return prey, pred, alpha, beta, gamma, delta, save, name


def diff_lotka_volterra(pop, t, alpha, beta, gamma, delta):
    '''
    equation of the differential for the lotka volterra model,
    the constants being alpha beta gamma and delta
    something to make note, currently the model breaks when these
    constants leave the range of 0.5 < c < 1, this may be due to
    scipy.
    '''
    x = pop[0]
    y = pop[1]
    dxdt = (alpha*x) - (beta*x*y)
    dydt = (delta*x*y) - (gamma*y)
    gradient = [dxdt, dydt]
    return gradient


def solve_lotka_volterra(pop, t_max, alpha, beta, gamma, delta):
    '''
    solves the differential equation using scipy
    '''
    t = np.linspace(0, t_max, t_max*2)
    lotka_volterra = odeint(diff_lotka_volterra, pop, t, (alpha, beta, gamma, delta))
    return lotka_volterra, t


def plot_lotka_volterra(t, data, save, name):
    '''
    plots the graph, plotting the population of the predator
    and prey on the same graph ,as the y-axis, against time
    '''
    fig = plt.figure()
    plt.plot(t, data[:, 0])
    plt.plot(t, data[:, 1])
    plt.xlabel("time")
    plt.ylabel("population")
    plt.legend(["prey", "predator"])
    if save:
        plt.savefig(name)
    plt.show()


def main(t_max):
    prey, pred, alpha, beta, gamma, delta, save, name = input_handler()
    pop = [prey, pred]
    data, t = solve_lotka_volterra(pop, t_max, alpha, beta, gamma, delta)
    plot_lotka_volterra(t, data, save, name)


if __name__ == "__main__":
    main(500)
