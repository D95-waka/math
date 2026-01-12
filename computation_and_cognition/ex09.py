#!/usr/bin/env python3

from itertools import groupby
import numpy as np

def max_p(c):
    c = map(lambda x: x[0], filter(lambda x: len(x[1]) == 1, map(lambda x: (x[0], list(x[1])), groupby(c))))
    print(len(list(c)))
    return max(c)

if __name__ == "__main__":
    M = 20
    choices = np.array(range(M)) + 1
    N = 300
    eta = 0.001
    w = np.ones((M))
    while True:
        p = (1 / sum(w)) * w
        c = np.random.choice(choices, size = N, p = p)
        print(c)
        R = np.zeros_like(w)
        R[max_p(c) - 1] += 1
        print(R)
        break
