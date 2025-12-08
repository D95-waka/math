#!/usr/bin/env python3

from pca import *
import logging
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

logger = logging.getLogger(__name__)
from gradient_linear_perceptron import LinearPerceptron

def random_prediction(prod: np.ndarray) -> np.ndarray:
    v = 1 - 1 / (1 + np.exp(-1 * prod))
    r = np.random.rand(len(prod), len(prod[0]))
    return (r >= v) + 0

def calc_delta(perceptron: LinearPerceptron, x: np.ndarray, label: int) -> np.ndarray:
    prod = perceptron.predict(x)
    y = random_prediction(prod)
    R = (y == label) + 0
    delta = R * x * ((y - 1) + (np.exp(-prod)) / (1 + np.exp(-prod)))
    return delta

def calc_precision(perceptron: 'LinearPerceptron', test_data: np.ndarray, test_labels: list[int], initial_index: int, to: int):
    sum = np.array([[np.float64(0)]])
    for i in range(initial_index, to):
        x = data[:, i:i + 1]
        label = test_labels[i]
        sum += (random_prediction(perceptron.predict(x)) == label)

    return (100 * sum / (to - initial_index))[0][0]

if __name__ == "__main__":
    logging.basicConfig(
            level = logging.INFO,
            handlers = [
                logging.StreamHandler()
            ]
        )

    # Question 1
    print('--- BEGIN DATA PREPERATION ---')
    data = np.array([[np.float64(x) for x in l[:-1].split(',')] for l in open('./data/data.csv', 'r').readlines()])
    labels = [int(x) for x in open('./data/labels.csv', 'r').readline().split(',')]
    test_data = np.array([[np.float64(x) for x in l[:-1].split(',')] for l in open('./data/test_data.csv', 'r').readlines()])
    test_labels = [int(x) for x in open('./data/test_labels.csv', 'r').readline().split(',')]
    N = len(data)
    eta = 0.01
    perceptron = LinearPerceptron(np.random.random((N, 1)) * 0.01 - 0.005)
    P_tests = 2000
    c = 0
    print('--- BEGIN DATA TRAINING ---')
    precision_data = []
    for i in range(len(data[0]) - P_tests):
        if i % 50 == 0:
            precision_tests_data = calc_precision(perceptron, test_data, test_labels, 0, len(test_labels))
            precision_value = calc_precision(perceptron, data, labels, len(data[0]) - P_tests, len(data[0]))
            precision_data.append([i, precision_value, precision_tests_data])
            print(100 * i / (len(data[0]) - P_tests))

        x = data[:, i:i + 1]
        label = labels[i]
        perceptron.weights += eta * calc_delta(perceptron, x, label)

    # Question 3
    fig, ax = plt.subplots(layout='constrained')
    precision_data = np.array(precision_data)
    ax.plot(precision_data[:,0], precision_data[:,1], alpha = 0.6, color = 'blue')
    plt.title('Precision of the neuron over test data')
    plt.xlabel('samples learned')
    plt.ylabel('precision in percentage')
    plt.savefig('bin/out5_1.jpg')

    # Question 3 - the right way
    fig, ax = plt.subplots(layout='constrained')
    precision_data = np.array(precision_data)
    ax.plot(precision_data[:,0], precision_data[:,2], alpha = 0.6, color = 'red')
    plt.title('Precision of the neuron over test data')
    plt.xlabel('samples learned')
    plt.ylabel('precision in percentage')
    plt.savefig('bin/out5_2.jpg')

    # Question 4
    w = perceptron.weights.reshape((28, 28))
    fig, ax = plt.subplots()
    im = ax.imshow(w)
    ax.set_title("Heatmap of trained perceptron weights")
    fig.tight_layout()
    plt.savefig('bin/out5_3.jpg')

