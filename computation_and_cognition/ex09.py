#!/usr/bin/env python3

from itertools import groupby
import matplotlib.pyplot as plt
import numpy as np

def max_p(c):
    c = sorted(c)
    c = list(map(lambda x: x[0], filter(lambda x: x[1] == 1, map(lambda x, : (x[0], len(list(x[1]))), groupby(c, key=(lambda x: int(x)))))))
    return max(c or [-1])

if __name__ == "__main__":
    M = 20
    choices = np.array(range(M)) + 1
    N = 30
    eta = 0.001
    w = np.ones((M))
    L = 500000
    p5 = []
    p20 = []
    for _ in range(L):
        p = (1 / sum(w)) * w
        p5.append(p[4])
        p20.append(p[19])
        c = np.random.choice(choices, size = N, p = p)
        R = np.zeros_like(w)
        l = max_p(c)
        if l != -1:
            R[l - 1] += 1

        w += - eta * w + eta * R

    p = (1 / sum(w)) * w
    print(w, p)
    L2 = 100000
    k = np.zeros_like(w)
    kn = 0
    for _ in range(L2):
        c = np.random.choice(choices, size = N, p = p)
        l = max_p(c)
        if l == -1:
            kn += 1
        else:
            k[l - 1] += 1

    print(k, kn)

    # Question 1
    fig, ax = plt.subplots(layout='constrained')
    ax.plot(range(L), p5, label='p(n = 5)')
    ax.plot(range(L), p20, label='p(n = 20)')
    plt.title('probabily for several number choices over learning process')
    plt.xlabel('iteration')
    plt.ylabel('probability')
    plt.legend()
    plt.savefig('bin/out9_1.jpg')

    # Question 2
    fig, ax = plt.subplots(layout='constrained')
    ax.bar(range(1, 21), list(k))
    plt.title('histogram of numbers for winning games')
    plt.xlabel('number')
    plt.ylabel('count')
    plt.savefig('bin/out9_2.jpg')
    plt.show()
