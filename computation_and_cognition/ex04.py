#!/usr/bin/env python3

from pca import *
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

    # Question 0.1
    P = 0
    s = np.vstack([
        np.array(np.random.normal(0, 1, P)),
        np.array(np.random.normal(0, 4, P))
    ])
    fig, ax = plt.subplots(layout='constrained')
    ax.scatter(s[0], s[1], alpha = 0.6, s = 10)
    ax.quiver(0, 3, color = 'red')
    plt.title('Random points distributed (N(0, 1), N(0, 4))')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('bin/out4_0_1.jpg')

    # Question 1
    data = [[float(y) for y in x[:-1].split(',')] for x in open('./wine.csv', 'r').readlines()[1:]]
    logger.debug(data)

    # Question 2
    fig, ax = plt.subplots(layout='constrained')
    for r in data:
        match r[0]:
            case 1:
                color = 'red'
            case 2: 
                color = 'blue'
            case 3:
                color = 'green'
            case _:
                color = 'black'
        ax.scatter(r[1], r[2], alpha = 0.6, s = 10, color = color)
    plt.title('Wine DataSet partitioned by producer')
    plt.xlabel('Property 1')
    plt.ylabel('Property 2')
    plt.savefig('bin/out4_2.jpg')

    # Question 3
    data = np.array(data).T[1:]
    mean = np.mean(data, axis=0)
    std_dev = np.std(data, axis=0)
    data = ((data - mean) / std_dev)
    pca_factory = PCAFactory()
    pca, C, values, vectors = pca_factory.inner_fit_batch(data, 2)

    # Question 5
    total = sum(values)
    variances = [100 * sum(values[:i + 1]) / total for i in range(len(values))]
    fig, ax = plt.subplots(layout='constrained')
    ax.scatter(range(len(variances)), variances, alpha = 0.6, s = 10)
    plt.title('')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('bin/out4_5.jpg')

    # Question 6
    projections = np.array([pca.project(p) for p in data.T]).T
    fig, ax = plt.subplots(layout='constrained')
    ax.scatter(projections[0], projections[1], alpha = 0.6, s = 10)
    print("A", vectors[0])
    for v in range(len(data.T)):
        w = pca.project(np.array([data.T[v]]).T)
        if w[0] > -2.2:
            print(v)
        #ax.scatter(w[0][0], w[1][0], alpha = 0.6, s = 10)

    plt.title('')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('bin/out4_6.jpg')
