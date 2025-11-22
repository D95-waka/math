#!/usr/bin/env python3

from linear_perceptron import *
import logging
import matplotlib.pyplot as plt
import numpy as np

logger = logging.getLogger(__name__)

def calculate_training_error(x, y0, weights) -> np.float64:
    C = (1 / P) * np.matmul(x, x.transpose())
    u = (1 / P) * np.matmul(x, y0)
    a = (1 / (2 * P)) * (y0.transpose() @ y0)
    training_error = (1 / 2) * (weights.transpose() @ C @ weights) - (weights.transpose() @ u) + a
    return training_error[0][0]

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

if __name__ == "__main__":
    logging.basicConfig(
            level = logging.INFO,
            handlers = [
                logging.StreamHandler()
            ]
        )

    # Question 1:
    P = 500
    x = np.random.rand(1, P) + np.random.randint(-1, 1, (1, P))
    x = np.vstack([x, [[1] * P]])
    y0 = np.array([[ x1 ** 3 - x1 ** 2 for x1, _ in x.transpose()]]).transpose()

    # Question 2:
    trainer = LinearPerceptronTrainer()
    lp = trainer.inner_fit(x, y0)
    print(f"Weights: {lp._weights}")

    # Question 3:
    weights = lp._weights
    fig, ax = plt.subplots(figsize = (6, 6))
    z = np.linspace(-1, 1)
    ax.plot(z, z**3 - z**2, color = "black", linewidth = 1, label = "x^3 - x^2")
    ax.plot(z, weights[0] * z + weights[1], color = "red", linewidth = 1, label = "Trained liear perceptron")
    ax.set_title('Actual function & linear approximation')
    ax.legend(title = 'functions:', loc = 'lower right')
    plt.savefig('bin/out2_3.jpg')

    # Question 4:
    training_error = calculate_training_error(x, y0, weights)
    print(f"Training error: {training_error}")

    # This formula is given by the calculation of question 1:
    generalization_error = calculate_generalization_error(-1, 1, lambda z: weights.transpose() @ np.array([[z], [1]]), lambda z: z ** 3 - z ** 2)
    print(f"Generalization error: {generalization_error}")

    # Question 5:
    M = 100
    data = []
    for P in range(5, 101, 5):
        sum_generalization_error = 0
        sum_training_error = 0
        for i in range(M):
            x = np.random.rand(1, P) + np.random.randint(-1, 1, (1, P))
            x = np.vstack([x, [[1] * P]])
            y0 = np.array([[ x1 ** 3 - x1 ** 2 for x1, _ in x.transpose()]]).transpose()
            weights = trainer.inner_fit(x, y0)._weights
            sum_training_error += calculate_training_error(x, y0, weights)
            sum_generalization_error += calculate_generalization_error(-1, 1, lambda z: weights.transpose() @ np.array([[z], [1]]), lambda z: z ** 3 - z ** 2)

        sum_training_error /= M
        sum_generalization_error /= M
        data.append([P, sum_training_error, sum_generalization_error])

    data = np.array(data)
    x, y1, y2 = data.T
    fig, ax = plt.subplots(layout='constrained')
    ax.scatter(x, y1, color = 'blue', label = 'Training Error')
    ax.plot(x, y1, lw = 1, alpha = 0.6, color = 'blue')
    ax.scatter(x, y2, color = 'red', label = 'Generalization Error')
    ax.plot(x, y2, lw = 1, alpha = 0.6, color = 'red')
    ax.legend(title = 'value', loc = 'center right')
    plt.title('Average error for 100 tests with P examples')
    plt.xlabel('P - Number of examples per test')
    plt.ylabel('Error probability')
    plt.savefig('bin/out2_5.jpg')
