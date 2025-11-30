#!/usr/bin/env python3

import logging
import numpy as np

logger = logging.getLogger(__name__)

class PCA(object):
    def __init__(self, components: np.ndarray):
        if components.ndim != 2:
            raise Exception('Supports weight matrix only')

        self.components = components

    def project(self, x: np.ndarray) -> np.ndarray:
        prod = self.components.transpose() @ x
        logger.debug(f"PCA Projection called for w = {self.components}, x = {x}, wx = {prod}")
        return prod

    def restore(self, x: np.ndarray) -> np.ndarray:
        prod = x.T @ self.components.T
        logger.debug(f"PCA Restoration called for w = {self.components}, x = {x}, wx = {prod}")
        return prod.T

    def gradient(self, x: np.ndarray) -> np.ndarray:
        y = self.project(x)
        return y @ (x - y @ self.components)

class PCAFactory(object):
    def __init__(self):
        pass

    def fit_batch(self, samples: np.ndarray, dim: int) -> PCA:
        return self.inner_fit_batch(samples, dim)[0]

    def inner_fit_batch(self, samples: np.ndarray, dim: int) -> tuple[PCA, np.ndarray, np.ndarray, np.ndarray]:
        '''
        Args:
            samples (np.ndarray): M x N matrix such that each column is a sample vector of size 1 x N
            dim (int): Dimension of embedded space, <= N
        '''
        logger.debug(f"Starting batch fit for {len(samples)}")
        C = samples @ samples.T
        values, vectors = np.linalg.eig(C)
        sorted_indices = np.argsort(values)[::-1]
        values_sorted = values[sorted_indices]
        vectors_sorted = vectors[:,sorted_indices]
        pca_components = vectors_sorted[:, :dim]
        return PCA(pca_components), C, values_sorted, vectors_sorted

def tests_run(pca: PCA, tests):
    for vector, classification in tests:
        actual = pca.restore(pca.project(vector))
        if np.allclose(classification, actual, atol = 0.001):
            print(f"{np.transpose(vector)} was classified correctly")
        else:
            print(f"Vector: {vector.T}, Correct: {classification.T}, Actual: {actual.T}")

def colvec(*values: float) -> np.ndarray:
    return np.array([values]).transpose()

def tests():
    print(" --- BEGIN Single Neuron Manual Test Section ---")
    pca = PCA(colvec(1, 0))
    print("components:\n", pca.components)
    tests = [
            (colvec(1, 0), colvec(1, 0)),
            (colvec(2, 2), colvec(2, 0)),
            (colvec(-2, 2), colvec(-2, 0)),
            (colvec(1, -1), colvec(1, 0)) ]
    tests_run(pca, tests)
    print("\n --- BEGIN Single Neuron Train Section ---")
    trainer = PCAFactory()
    P = 100
    vecs = np.vstack([
        np.random.rand(1, P) / 2 - 1 / 4,
        np.random.rand(1, P) + np.random.randint(-5, 5, (1, P))
    ])
    pca = trainer.fit_batch(vecs, 1)
    expectedweights = colvec(0., -1.)
    print("expected weights:\n", expectedweights)
    print("actual weights:\n", pca.components)
    print(f"Match: {np.allclose(expectedweights, pca.components, atol = 0.01)}")
    print("\n --- BEGIN Manual Test Section ---")
    pca = PCA(np.array([[1, 0, 0], [0, 1, 0]]).T)
    print("weights:\n", pca.components)
    tests = [
            (colvec(1, 1, 1), colvec(1, 1, 0)),
            (colvec(2, 1, 0), colvec(2, 1, 0)),
            (colvec(-1, 2, 10), colvec(-1, 2, 0)),
        ]
    tests_run(pca, tests)
    print("\n --- BEGIN Train Section ---")
    P = 100
    vecs = np.vstack([
        np.random.rand(1, P) / 2 - 1 / 4 + np.random.randint(-2, 2, (1, P)),
        np.random.rand(1, P) + np.random.randint(-20, 20, (1, P)),
        np.zeros((1, P))
    ])
    pca = trainer.fit_batch(vecs, 2)
    expectedweights = np.array([[0, -1], [-1, 0], [0, 0]])
    print("expected weights:\n", expectedweights)
    print("actual weights:\n", pca.components)
    print(f"Match: {np.allclose(expectedweights, pca.components, atol = 0.01)}")
    print("\n --- BEGIN Trained Test Section ---")
    tests = [
            (colvec(1, 1, 1), colvec(1, 1, 0)),
            (colvec(-1, -1, -1), colvec(-1, -1, 0)),
            (colvec(-3, 2, 100), colvec(-3, 2, 0)), ]
    tests_run(pca, tests)

if __name__ == "__main__":
    logging.basicConfig(
            level = logging.DEBUG,
            handlers = [
                logging.StreamHandler()
            ]
        )

    tests()
