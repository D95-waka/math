#!/usr/bin/env python3

from pca import *
import logging
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(
            level = logging.INFO,
            handlers = [
                logging.StreamHandler()
            ]
        )

    # Question 0.1
    P = 2000
    s = np.vstack([
        np.array(np.random.normal(0, 1, P)),
        np.array(np.random.normal(0, 4, P))
    ])
    fig, ax = plt.subplots(layout='constrained')
    ax.scatter(s[0], s[1], alpha = 0.6, s = 10)
    ax.quiver(0, 3, color = 'red')
    plt.title('Random points distributed (N(0, 1), N(0, 4))')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('bin/out4_0_1.jpg')

    # Question 1
    csv = [[float(y) for y in x[:-1].split(',')] for x in open('./wine.csv', 'r').readlines()[1:]]
    data = np.array(csv)
    logger.debug(data)

    # Question 2
    patches = [
        mpatches.Patch(color='red', label='Producer 1'),
        mpatches.Patch(color='blue', label='Producer 2'),
        mpatches.Patch(color='green', label='Producer 3')
    ]
    colors = ['red' if x[0] == 1 else 'blue' if x[0] == 2 else 'green' for x in csv]
    fig, ax = plt.subplots(layout='constrained')
    ax.scatter(data[:,1], data[:,2], alpha = 0.6, s = 10, color = colors)
    plt.title('Wine DataSet partitioned by producer')
    plt.xlabel('Property 1')
    plt.ylabel('Property 2')
    plt.legend(handles = patches)
    plt.savefig('bin/out4_2.jpg')

    # Question 3
    data = np.array(data)[:,1:]
    mean = np.mean(data, axis = 0)
    std_dev = np.std(data, axis = 0)
    data = (data - mean) / std_dev
    data = data.T
    pca_factory = PCAFactory()
    pca, C, values, vectors = pca_factory.inner_fit_batch(data, 2)

    # Question 5
    total = sum(values)
    variances = [100 * sum(values[:i + 1]) / total for i in range(len(values))]
    fig, ax = plt.subplots(layout='constrained')
    ax.scatter(range(len(variances)), variances, alpha = 0.6, s = 10)
    plt.title('Calculated variance per number of used dimensions')
    plt.xlabel('Embedded Dimension')
    plt.ylabel('error percentage')
    plt.savefig('bin/out4_5.jpg')

    # Question 6
    projections = np.array([pca.project(p) for p in data.T]).T
    fig, ax = plt.subplots(layout='constrained')
    colors = ['red' if x[0] == 1 else 'blue' if x[0] == 2 else 'green' for x in csv]
    ax.scatter(projections[0], projections[1], alpha = 0.6, s = 10, color = colors)
    plt.title('Embedded space using PCA to dimension 2')
    plt.xlabel('vector 1')
    plt.ylabel('vector 2')
    plt.legend(handles = patches)
    plt.savefig('bin/out4_6.jpg')

    # Question 7
    pca.components = vectors[:, (0,12)]
    projections = np.array([pca.project(p) for p in data.T]).T
    fig, ax = plt.subplots(layout='constrained')
    ax.scatter(projections[0], projections[1], alpha = 0.6, s = 10, color = colors)
    plt.title('Embedded space using first and last vectors calculated for PCA')
    plt.xlabel('vector 1')
    plt.ylabel('vector 13')
    plt.legend(handles = patches)
    plt.savefig('bin/out4_7.jpg')
