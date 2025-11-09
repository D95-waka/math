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
        logger.debug(f"Update Linear Perceptron called, X = {example}, y = {example_prediction}")
        P = len(example)
        C = (1 / P) * np.matmul(example, example.transpose())
        u = (1 / P) * np.matmul(example, example_prediction)
        # TODO: Is this part necessary?
        a = (1 / (2 * P)) * np.matmul(example_prediction.transpose(), example_prediction)
        logger.debug(f"Updating Linear Perceptron, C = {C}")
        w = np.matmul(np.linalg.inv(C), u)
        self._weights = w
        return True

class LinearPerceptronTrainer(object):
    def __init__(self):
        pass

    def fit(self, examples: list[np.array], example_predictions: list[float]):
        lp = LinearPerceptron(np.array([[]]))
        X = np.column_stack(examples)
        y = np.column_stack(example_predictions).transpose()
        lp.update(X, y)
        return lp

def tests_run(perceptron: LinearPerceptron, tests):
    for vector, classification in tests:
        actual = perceptron.predict(vector)
        if np.allclose(classification, actual):
            print(f"{np.transpose(vector)} was classified correctly")
        else:
            print(classification - perceptron.predict(vector))
            print(f"Vector: {np.transpose(vector)}, Correct: {classification}, Actual: {actual}")

def colvec(*values: list[float]) -> np.array:
    return np.array([values]).transpose()

def tests():
    print(" --- BEGIN Single Neuron Manual Test Section ---")
    perceptron = LinearPerceptron(colvec(2, 3))
    print("weights:\n", perceptron._weights)
    tests = [
            (colvec(1, 0), colvec(2)),
            (colvec(0, 2), colvec(6)),
            (colvec(2, 2), colvec(10)),
            (colvec(1, -1), colvec(-1)) ]
    tests_run(perceptron, tests)
    print("\n --- BEGIN Single Neuron Train Section ---")
    trainer = LinearPerceptronTrainer()
    perceptron = trainer.fit(
            [
                colvec(1, -1),
                colvec(2, 2)
            ], [
                colvec(-1),
                colvec(10),
            ])
    expected_weights = colvec(2., 3.)
    print("expected weights:\n", expected_weights)
    print("actual weights:\n", perceptron._weights)
    print(f"Match: {np.allclose(expected_weights, perceptron._weights)}")
    print("\n --- BEGIN Single Neuron Trained Test Section ---")
    tests = [
            (colvec(1, 0), colvec(2.)),
            (colvec(0, 2), colvec(6.)),
        ]
    tests_run(perceptron, tests)
    print("\n --- BEGIN Manual Test Section ---")
    perceptron = LinearPerceptron(np.array([[2, -1], [3, 1]]))
    print("weights:\n", perceptron._weights)
    tests = [
            (colvec(1, 1), colvec(5, 0)),
            (colvec(2, 1), colvec(7, -1)),
            (colvec(-1, 2), colvec(4, 3)),
        ]
    tests_run(perceptron, tests)
    print("\n --- BEGIN Train Section ---")
    perceptron = trainer.fit(
            [
                colvec(1, 0),
                colvec(0, 1),
                colvec(1, 1),
            ], [
                colvec(2, -1),
                colvec(3, 1),
                colvec(5, 0),
            ])
    expected_weights = np.array([[2, -1], [3, 1]])
    print("expected weights:\n", expected_weights)
    print("actual weights:\n", perceptron._weights)
    print(f"Match: {np.allclose(expected_weights, perceptron._weights)}")
    print("\n --- BEGIN Trained Test Section ---")
    tests = [
            (colvec(1, 1), colvec(5, 0)),
            (colvec(-1, -1), colvec(-5, 0)),
            (colvec(-3, 2), colvec(0, 5)),
        ]
    tests_run(perceptron, tests)

if __name__ == "__main__":
    logging.basicConfig(
            level = logging.DEBUG,
            handlers = [
                logging.StreamHandler()
            ]
        )

    tests()
