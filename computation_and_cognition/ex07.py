#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import random

# question 1
def D(C, V, t, k):
    d = lambda t0: 1 / (1 + k * t0)
    return -C * d(t) + V * d(t + 1)

# question 3
def get_p(C, V, k) -> float:
    delta = 0.001
    p = delta
    p_c = -1
    c_c = 1
    while p < 1:
        c = abs(p * D(C, V, 0, k) - sum(p * (1 - p) ** n * D(C, V, n, k) for n in range(1, 1000)))
        if c < c_c:
            p_c = p
            c_c = c

        p += delta

    return p_c

if __name__ == "__main__":
    # question 2
    k = 0.5
    C = 60
    V = 100
    N = 30
    for i in range(N):
        value_today = D(C, V, 0, k)
        value_tomorrow = D(C, V, 1, k)
        if value_today > value_tomorrow:
            print(i)
            break

    # question 3b
    p = get_p(C, V, k)

    # question 4
    P = 10000
    data = []
    for i in range(P):
        a = 0
        c = 0
        while a == 0:
            a = random.choices((0, 1), (1 - p, p))[0]
            c += 1

        data.append(c)

    fig, ax = plt.subplots(layout='constrained')
    ax.hist(data)
    plt.title('Histogram of agents choice of doing the exercise after n days')
    plt.xlabel('number of the day the exercise was done')
    plt.ylabel('number of agents did the exercise on given day')
    plt.savefig('bin/out7_1.jpg')

    #question 4
    x = []
    y = []
    for k in np.arange(0.05, 1, 0.01):
        p = get_p(C, V, k)
        x.append(k)
        y.append(p)

    fig, ax = plt.subplots(layout='constrained')
    ax.plot(x, y)
    plt.title('p as a function of k')
    plt.xlabel('k')
    plt.ylabel('p')
    plt.savefig('bin/out7_2.jpg')
