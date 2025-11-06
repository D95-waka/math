#!/usr/bin/env python3

import logging
import matplotlib.pyplot as plt
import numpy as np
logger = logging.getLogger(__name__)

class BinaryPerceptron(object):
    def __init__(self, weights: np.array):
        if weights.ndim != 2:
            raise Exception('Supports weight matrix only')

        self._weights = weights

    def predict(self, x: np.array) -> bool:
        prod = np.matmul(np.transpose(self._weights), x)
        for i in prod:
            i[0] = int(i[0] >= 0)

        return prod

    def update(self, example: np.array, example_prediction: np.array) -> bool:
        current_prediction = self.predict(example)
        if np.array_equal(current_prediction, example_prediction):
            return True

        a = np.diag(np.transpose(example_prediction - current_prediction)[0])
        b = np.tile(example, (1, len(example_prediction)))
        added_value = np.matmul(b, a)
        self._weights += added_value

class BinaryPerceptronTrainer(object):
    def __init__(self):
        pass

    def fit(self, examples: list[np.array], example_predictions: list[np.array]):
        initial_weights = np.ones((len(examples[0]), len(example_predictions[0])))
        bp = BinaryPerceptron(initial_weights)
        keep_iterating = True
        while keep_iterating:
            logger.debug("Starting new training iteration")
            keep_iterating = False
            for example_input, example_prediction in zip(examples, example_predictions):
                if not bp.update(example_input, example_prediction):
                    keep_iterating = True

        return bp

def tests_run(bp: BinaryPerceptron, tests):
    for vector, classification in tests:
        actual = bp.predict(vector)
        if np.array_equal(classification, actual):
            print(f"{np.transpose(vector)} was classified correctly")
        else:
            print(f"Vector: {np.transpose(vector)}, Correct: {classification}, Actual: {binary_perceptron.predict(vector)}")

def tests():
    print(" --- BEGIN Single Neuron Manual Test Section ---")
    binary_perceptron = BinaryPerceptron(np.array([[-1], [1]]))
    print("weights:\n", binary_perceptron._weights)
    tests = [
            (np.transpose([[2, 1]]), np.transpose([[0]])),
            (np.transpose([[-1, 1]]), np.transpose([[1]])),
            (np.transpose([[-2, -1]]), np.transpose([[1]])),
            (np.transpose([[-1, -2]]), np.transpose([[0]])),
            (np.transpose([[1, -1]]), np.transpose([[0]]))]
    tests_run(binary_perceptron, tests)
    print("\n --- BEGIN Single Neuron Train Section ---")
    binary_perceptron_factory = BinaryPerceptronTrainer()
    binary_perceptron = binary_perceptron_factory.fit(
            [
                np.transpose([[2, 1]]),
                np.transpose([[-1, -2]]),
                np.transpose([[1, -1]])],
            [
                np.transpose([[0]]),
                np.transpose([[0]]),
                np.transpose([[0]])])
    print("weights:\n", binary_perceptron._weights)
    print("\n --- BEGIN Single Neuron Trained Test Section ---")
    tests = [
            (np.transpose([[2, 1]]), np.transpose([[0]])),
            (np.transpose([[-1, 1]]), np.transpose([[1]])),
            (np.transpose([[-2, -1]]), np.transpose([[1]])),
            (np.transpose([[-1, -2]]), np.transpose([[0]])),
            (np.transpose([[1, -1]]), np.transpose([[0]]))]
    tests_run(binary_perceptron, tests)
    print("\n --- BEGIN Manual Test Section ---")
    binary_perceptron = BinaryPerceptron(np.array([[-1, 0], [1, 1]]))
    print("weights:\n", binary_perceptron._weights)
    tests = [
            (np.transpose([[2, 1]]), np.transpose([[0, 1]])),
            (np.transpose([[-1, 1]]), np.transpose([[1, 1]])),
            (np.transpose([[-2, -1]]), np.transpose([[1, 0]])),
            (np.transpose([[-1, -2]]), np.transpose([[0, 0]])),
            (np.transpose([[1, -1]]), np.transpose([[0, 0]]))]
    tests_run(binary_perceptron, tests)
    print("\n --- BEGIN Train Section ---")
    binary_perceptron_factory = BinaryPerceptronTrainer()
    binary_perceptron = binary_perceptron_factory.fit(
            [
                np.transpose([[2, 1]]),
                np.transpose([[-1, -2]]),
                np.transpose([[1, -1]])],
            [
                np.transpose([[0, 1]]),
                np.transpose([[0, 0]]),
                np.transpose([[0, 0]])])
    print("weights:\n", binary_perceptron._weights)
    print("\n --- BEGIN Trained Test Section ---")
    tests = [
            (np.transpose([[2, 1]]), np.transpose([[0, 1]])),
            (np.transpose([[-1, 1]]), np.transpose([[1, 1]])),
            (np.transpose([[-2, -1]]), np.transpose([[1, 0]])),
            (np.transpose([[-1, -2]]), np.transpose([[0, 0]])),
            (np.transpose([[1, -1]]), np.transpose([[0, 0]]))]
    tests_run(binary_perceptron, tests)

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

    # Question_4
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
