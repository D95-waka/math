#!/usr/bin/env python3

import logging
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
        actual = binary_perceptron.predict(vector)
        if np.array_equal(classification, actual):
            print(f"{np.transpose(vector)} was classified correctly")
        else:
            print(f"Vector: {np.transpose(vector)}, Correct: {classification}, Actual: {binary_perceptron.predict(vector)}")

if __name__ == "__main__":
    logging.basicConfig(
            level = logging.DEBUG,
            handlers = [
                logging.StreamHandler()
            ]
        )
    logging.getLogger().addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)
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
