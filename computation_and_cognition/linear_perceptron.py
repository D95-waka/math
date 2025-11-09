#!/usr/bin/env python3

import logging
import numpy as np

logger = logging.getLogger(__name__)

class LinearPerceptron(object):
    def __init__(self, weights: np.array):
        if weights.ndim != 2:
            raise Exception('Supports weight matrix only')

        self._weights = weights

    def predict(self, x: np.array) -> np.array:
        prod = np.matmul(self._weights.transpose(), x)
        logger.debug(f"Liner Perceptron Predict called for w = {self._weights}, x = {x}, wx = {prod}")
        return prod

    def update(self, example: np.array, example_prediction: np.array) -> bool:
        # example is of the form of matrix such that each column is an example vector
        # example_prediction is a matrix such that each column is a desired result
        P = len(example)
        C = (1 / P) * np.matmult(example, example.transpose())
        u = (1 / P) * np.matmult(example.transpose(), y)
        a = (1 / (2 * P)) * np.matmult(y.transpose(), y)
        w = np.matmult(np.linalg.inv(C), u)
        self._weights = w

class LinearPerceptronTrainer(object):
    def __init__(self):
        pass

    def fit(self, examples: list[np.array], example_predictions: list[float]):
        lp = LinearPerceptron(initial_weights)
        X = np.array(examples).transpose()
        y = np.array(number).transpose()
        lp.update(X, y)
        return lp

def tests_run(perceptron: LinearPerceptron, tests):
    for vector, classification in tests:
        actual = perceptron.predict(vector)
        if np.array_equal(classification, actual):
            print(f"{np.transpose(vector)} was classified correctly")
        else:
            print(f"Vector: {np.transpose(vector)}, Correct: {classification}, Actual: {perceptron.predict(vector)}")

def colvec(*values: list[float]) -> np.array:
    return np.array([values]).transpose()

def tests():
    print(" --- BEGIN Single Neuron Manual Test Section ---")
    perceptron = LinearPerceptron(np.array([[2], [3]]))
    print("weights:\n", perceptron._weights)
    tests = [
            (colvec(1, 0), colvec(2)),
            (colvec(0, 2), colvec(6)),
            (colvec(1, -1), colvec(-1)) ]
    tests_run(perceptron, tests)
    return
    print("\n --- BEGIN Single Neuron Train Section ---")
    binary_perceptron_factory = BinaryPerceptronTrainer()
    perceptron = binary_perceptron_factory.fit(
            [
                np.transpose([[2, 1]]),
                np.transpose([[-1, -2]]),
                np.transpose([[1, -1]])],
            [
                np.transpose([[0]]),
                np.transpose([[0]]),
                np.transpose([[0]])])
    print("weights:\n", perceptron._weights)
    print("\n --- BEGIN Single Neuron Trained Test Section ---")
    tests = [
            (np.transpose([[2, 1]]), np.transpose([[0]])),
            (np.transpose([[-1, 1]]), np.transpose([[1]])),
            (np.transpose([[-2, -1]]), np.transpose([[1]])),
            (np.transpose([[-1, -2]]), np.transpose([[0]])),
            (np.transpose([[1, -1]]), np.transpose([[0]]))]
    tests_run(perceptron, tests)
    print("\n --- BEGIN Manual Test Section ---")
    perceptron = LinearPerceptron(np.array([[-1, 0], [1, 1]]))
    print("weights:\n", perceptron._weights)
    tests = [
            (np.transpose([[2, 1]]), np.transpose([[0, 1]])),
            (np.transpose([[-1, 1]]), np.transpose([[1, 1]])),
            (np.transpose([[-2, -1]]), np.transpose([[1, 0]])),
            (np.transpose([[-1, -2]]), np.transpose([[0, 0]])),
            (np.transpose([[1, -1]]), np.transpose([[0, 0]]))]
    tests_run(perceptron, tests)
    print("\n --- BEGIN Train Section ---")
    binary_perceptron_factory = BinaryPerceptronTrainer()
    perceptron = binary_perceptron_factory.fit(
            [
                np.transpose([[2, 1]]),
                np.transpose([[-1, -2]]),
                np.transpose([[1, -1]])],
            [
                np.transpose([[0, 1]]),
                np.transpose([[0, 0]]),
                np.transpose([[0, 0]])])
    print("weights:\n", perceptron._weights)
    print("\n --- BEGIN Trained Test Section ---")
    tests = [
            (np.transpose([[2, 1]]), np.transpose([[0, 1]])),
            (np.transpose([[-1, 1]]), np.transpose([[1, 1]])),
            (np.transpose([[-2, -1]]), np.transpose([[1, 0]])),
            (np.transpose([[-1, -2]]), np.transpose([[0, 0]])),
            (np.transpose([[1, -1]]), np.transpose([[0, 0]]))]
    tests_run(perceptron, tests)

if __name__ == "__main__":
    logging.basicConfig(
            level = logging.DEBUG,
            handlers = [
                logging.StreamHandler()
            ]
        )

    tests()
