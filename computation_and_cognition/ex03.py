#!/usr/bin/env python3

import linear_perceptron as LP
from gradient_linear_perceptron import *
import logging
import matplotlib.pyplot as plt
import numpy as np

logger = logging.getLogger(__name__)

def calculate_training_error(x, y0, weights, limit: int = 0) -> np.float64:
    sum: np.ndarray = np.zeros((1, 1))
    limit = limit if limit > 0 else len(x)
    for sample, label in zip(x[:limit], y0[:limit]):
        sum += ((weights.transpose() @ sample) - label) ** 2

    return sum[0][0] / (2 * len(x))

def calculate_generalization_error(from_value: float, to_value: float, trained_func, actual_func) -> np.float64:
    P = 0.01
    sum: np.ndarray = np.zeros((1, 1))
    p = from_value
    c = 0
    while p < to_value:
        sum += (trained_func(p) - actual_func(p)) ** 2
        p += P
        c += 1

    return (sum / (2 * c))[0][0]

def f(x):
    return 1 + x + x**2 + x**3

def d(dictionary, key, value):
    dictionary[key] = value

if __name__ == "__main__":
    logging.basicConfig(
            level = logging.INFO,
            handlers = [
                logging.StreamHandler()
            ]
        )

    # Question 1:
    P = 100
    x = np.random.rand(1, P) + np.random.randint(-5, 5, (1, P))
    x = np.vstack([x, [[1] * P]]).transpose()
    x = [np.transpose([i]) for i in x]
    y0 = [np.array([[ f(x1)[0] ]]) for x1, _ in x]

    # Batch training:
    trainer = LinearPerceptronTrainer()
    states = {}
    trainer.fit_batch(x, y0, eta = lambda _: 0.01, max_iterations = P, collect = lambda m, i: d(states, i, m.copy()))
    states.pop(0)
    data_batch = np.transpose([[i, calculate_training_error(x, y0, states[i], i), calculate_generalization_error(-5, 5, lambda t: states[i].transpose() @ np.transpose([[t, 1]]), f)] for i in states.keys()])

    # Online training:
    states = {}
    trainer.fit_online(x, y0, eta = lambda _: 0.01, collect = lambda m, i: d(states, i, m.copy()))
    states.pop(0)
    data_online = np.transpose([[i, calculate_training_error(x, y0, states[i], i), calculate_generalization_error(-5, 5, lambda t: states[i].transpose() @ np.transpose([[t, 1]]), f)] for i in states.keys()])

    # Matrix correlation training:
    trainer = LP.LinearPerceptronTrainer()
    matrix_trained_perceptron = trainer.fit(x, y0)
    matrix_trained_error = (calculate_training_error(x, y0, matrix_trained_perceptron._weights, 0), calculate_generalization_error(-5, 5, lambda t: matrix_trained_perceptron._weights.transpose() @ np.transpose([[t, 1]]), f))

    # Question 2:
    fig, ax = plt.subplots(layout='constrained')
    ax.plot(data_batch[0], data_batch[1], lw = 1, alpha = 0.6, color = 'red', label = 'Batch Training')
    ax.plot(data_batch[0], data_batch[2], lw = 1, alpha = 0.6, color = 'red', linestyle = 'dashed', label = 'Batch Generalization')
    ax.plot(data_online[0], data_online[1], lw = 1, alpha = 0.6, color = 'blue', label = 'Online Training')
    ax.plot(data_online[0], data_online[2], lw = 1, alpha = 0.6, color = 'blue', linestyle = 'dashed', label = 'Online Generalization')
    plt.axhline(matrix_trained_error[0], color = 'black', label = 'Correlation Matrix Training')
    plt.axhline(matrix_trained_error[1], color = 'black', linestyle = 'dashed', label = 'Correlation Matrix Generalization')
    ax.legend(title = 'Error Graph')
    plt.title('Error per iteration of training')
    plt.xlabel('Iteration number')
    plt.ylabel('Error value')
    plt.savefig('bin/out3_2.jpg')

    # Question 3:
    P = 500
    x = np.random.rand(1, P) + np.random.randint(-5, 5, (1, P))
    x = np.vstack([x, [[1] * P]]).transpose()
    x = [np.transpose([i]) for i in x]
    y0 = [np.array([[ f(x1)[0] ]]) for x1, _ in x]

    # Training:
    trainer = LinearPerceptronTrainer()
    data_batch = {}
    data_online = {}
    for eta in [0.002, 0.005, 0.01, 0.02, 0.05]:
        print(f"Batch eta = {eta}")
        states = {}
        trainer.fit_batch(x, y0, eta = lambda _: eta, max_iterations = P, collect = lambda m, i: d(states, i, m.copy()))
        states.pop(0)
        data_batch[eta] = np.transpose([[i, calculate_training_error(x, y0, states[i], i), calculate_generalization_error(-5, 5, lambda t: states[i].transpose() @ np.transpose([[t, 1]]), f)] for i in states.keys()])

        # This optimization should not affect the final result, but while doing do it reduces running time significantly.
        trainer.fit_online(x, y0, eta = lambda _: eta, collect = lambda m, i: d(states, i, m.copy()))
        states.pop(0)
        data_online[eta] = np.transpose([[i, calculate_generalization_error(-5, 5, lambda t: states[i].transpose() @ np.transpose([[t, 1]]), f)] for i in states.keys()])

    # Question 4:
    # Batch Training:
    fig, ax = plt.subplots(layout='constrained')
    for eta, data in data_batch.items():
        ax.plot(data[0], data[1], alpha = 0.6, label = eta)

    ax.legend(title = 'eta =')
    plt.title('Training Error Graph for Batch learning using different learning rates')
    plt.xlabel('Iteration number')
    plt.ylabel('Error value')
    plt.savefig('bin/out3_4_1.jpg')

    # Batch Generalization:
    fig, ax = plt.subplots(layout='constrained')
    for eta, data in data_batch.items():
        ax.plot(data[0], data[2], alpha = 0.6, label = eta)

    ax.legend(title = 'eta =')
    plt.title('Generalization Error Graph for Batch learning using different learning rates')
    plt.xlabel('Iteration number')
    plt.ylabel('Error value')
    plt.savefig('bin/out3_4_2.jpg')

    # Online Generalization:
    fig, ax = plt.subplots(layout='constrained')
    for eta, data in data_online.items():
        ax.plot(data[0], data[1], alpha = 0.6, label = eta)

    ax.legend(title = 'eta =')
    plt.title('Generalization Error Graph for Online learning using different learning rates')
    plt.xlabel('Iteration number')
    plt.ylabel('Error value')
    plt.savefig('bin/out3_4_3.jpg')
