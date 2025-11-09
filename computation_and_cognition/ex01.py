#!/usr/bin/env python3

from binary_perceptron import *
import logging
import matplotlib.pyplot as plt
import numpy as np
logger = logging.getLogger(__name__)

# Example usage: question_1([[1, 0], [0, 1]], [1, 0]) -> [1, -1]
def question_1(examples: list[list[float]], predictions: list[float]) -> np.array:
    bpt = BinaryPerceptronTrainer()
    bp = bpt.fit([np.transpose([x]) for x in examples], [[[x]] for x in predictions])
    return bp._weights

def question_2(P, N):
    mat = np.random.rand(P, N) + np.random.randint(-10, 10, (P, N))
    pred = [x >= y for x, y in mat]
    return mat, pred

if __name__ == "__main__":
    logging.basicConfig(
            level = logging.INFO,
            handlers = [
                logging.StreamHandler()
            ]
        )

    # Question 2:
    mat, pred = question_2(1000, 2)
    
    # Question 3:
    weights = question_1(mat, pred)
    fig, ax = plt.subplots(figsize = (6, 6))
    x = np.linspace(-10, 10)
    ax.plot(x, x, color = "black", linewidth=1)
    ax.scatter([x for x, y in mat if x > y], [y for x, y in mat if x > y], color = "blue")
    ax.scatter([x for x, y in mat if x <= y], [y for x, y in mat if x <= y], color = "red")
    ax.quiver(weights[0][0], weights[1][0], color = 'green')
    plt.savefig('bin/out.jpg')

    # Question 4:
    optimal_weights = np.array([[1], [-1]])
    K = np.linalg.norm(optimal_weights)
    M = 100
    data = []
    for P in [5, 20, 30, 50, 100, 150, 200, 500]:
        sum = 0
        for i in range(M):
            mat, preds = question_2(P, 2)
            weights = question_1(mat, preds)
            sum += (np.matmul(weights.transpose(), optimal_weights) / (np.linalg.norm(weights) * K))[0][0]

        sum /= M
        data.append([P, sum])

    data = np.transpose(data)
    fig, ax = plt.subplots(layout='constrained')
    bars = ax.bar([f"P={x}" for x in data[0]], data[1])
    ax.bar_label(bars, labels = [f"{x:.4f}" for x in data[1]], padding=3)
    plt.savefig('bin/out4.jpg')
