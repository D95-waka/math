#!/usr/bin/env python3

import logging
import numpy as np

logger = logging.getLogger(__name__)

class LinearPerceptron(object):
    def __init__(self, weights: np.ndarray):
        if weights.ndim != 2:
            raise Exception('Supports weight matrix only')

        self.weights = weights

    def predict(self, x: np.ndarray) -> np.ndarray:
        prod = np.matmul(self.weights.transpose(), x)
        logger.debug(f"Liner Perceptron Predict called for w = {self.weights}, x = {x}, wx = {prod}")
        return prod

    def gradient(self, sample: np.ndarray, label: np.ndarray) -> np.ndarray:
        logger.debug(f"In gradient, prediction - label: {self.predict(sample) - label}")
        return 2 * ((self.predict(sample) - label) @ sample.transpose()).transpose()

class LinearPerceptronTrainer(object):
    def __init__(self):
        pass

    def fit(self, samples: list[np.ndarray], labels: list[np.ndarray]) -> LinearPerceptron:
        eta = 0.01
        max_iterations = 100
        perceptron = LinearPerceptron(np.zeros((len(samples[0]), len(labels[0]))))
        logger.debug(f"Current weights: {perceptron.weights}")
        for sample, label in zip(samples, labels):
            iteration = 0
            while iteration < max_iterations:
                gradient = perceptron.gradient(sample, label)
                if np.allclose(gradient, 0):
                    iteration = max_iterations
                    continue

                logger.debug(f"Error for sample: {sample}, label: {label}, error: {gradient}")
                perceptron.weights -= eta * gradient

        return perceptron

def tests_run(perceptron: LinearPerceptron, tests):
    for vector, classification in tests:
        actual = perceptron.predict(vector)
        if np.allclose(classification, actual):
            print(f"{np.transpose(vector)} was classified correctly")
        else:
            print(classification - perceptron.predict(vector))
            print(f"Vector: {np.transpose(vector)}, Correct: {classification}, Actual: {actual}")

def colvec(*values: float) -> np.ndarray:
    return np.array([values]).transpose()

def tests():
    print(" --- BEGIN Single Neuron Manual Test Section ---")
    perceptron = LinearPerceptron(colvec(2, 3))
    print("weights:\n", perceptron.weights)
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
    expectedweights = colvec(2., 3.)
    print("expected weights:\n", expectedweights)
    print("actual weights:\n", perceptron.weights)
    print(f"Match: {np.allclose(expectedweights, perceptron.weights)}")
    print("\n --- BEGIN Single Neuron Trained Test Section ---")
    tests = [
            (colvec(1, 0), colvec(2.)),
            (colvec(0, 2), colvec(6.)),
        ]
    tests_run(perceptron, tests)
    print("\n --- BEGIN Manual Test Section ---")
    perceptron = LinearPerceptron(np.array([[2, -1], [3, 1]]))
    print("weights:\n", perceptron.weights)
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
    expectedweights = np.array([[2, -1], [3, 1]])
    print("expected weights:\n", expectedweights)
    print("actual weights:\n", perceptron.weights)
    print(f"Match: {np.allclose(expectedweights, perceptron.weights)}")
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
