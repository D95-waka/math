#!/usr/bin/env python3

import logging
import numpy as np
from typing import Callable
logger = logging.getLogger(__name__)

class BinaryPerceptron(object):
    def __init__(self, weights: np.ndarray, predicate: Callable[[np.ndarray], np.ndarray] = lambda prod: np.array([int(i[0] >= 1) for i in prod])):
        if weights.ndim != 2:
            raise Exception('Supports weight matrix only')

        self._weights = weights
        self.predicate = predicate

    def predict(self, x: np.ndarray) -> np.ndarray:
        logger.debug(f"Predict init with: x.dim: {x.ndim}, x.shape: {x.shape}, weights.shape: {self._weights.shape}")
        prod = self._weights.T @ x
        logger.debug(f"Predict called with: x: {x}, prod: {prod}")
        return self.predicate(prod)

    def update(self, example: np.ndarray, example_prediction: np.ndarray) -> bool:
        current_prediction = self.predict(example)
        if np.array_equal(current_prediction, example_prediction):
            return True

        a = np.diag(np.transpose(example_prediction - current_prediction)[0])
        b = np.tile(example, (1, len(example_prediction)))
        added_value = np.matmul(b, a)
        self._weights += added_value
        return False

class BinaryPerceptronTrainer(object):
    def __init__(self):
        pass

    def fit(self, examples: list[np.ndarray], example_predictions: list[np.ndarray]):
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
            print(f"Vector: {np.transpose(vector)}, Correct: {classification}, Actual: {actual}")

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

if __name__ == "__main__":
    logging.basicConfig(
            level = logging.INFO,
            handlers = [
                logging.StreamHandler()
            ]
        )

    tests()
