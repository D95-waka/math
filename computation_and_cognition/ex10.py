#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import random
import math
from scipy.optimize import curve_fit
from scipy import special
from matplotlib.ticker import FuncFormatter

def myNivdak(id, stimType, S_target, vNL=None) -> bool:
    if stimType == 0:
        vNL = None

    S_standard = 5.5
    deltaS = S_target - S_standard
    nType = id % 4 + 1
    sigH = 0.1
    sigV = -30.0
    if vNL == 0:
        sigV = 0.01
    elif vNL == 1:
        sigV = 0.05
    elif vNL == 2:
        sigV = 0.1
    elif vNL == 3:
        sigV = 0.2

    sig = -30.0
    if stimType == 0:
        sig = sigH
    elif stimType == 1:
        sig = sigV
    elif stimType == 2:
        if nType == 1:
            sig = sigH
        elif nType == 2:
            sig = sigV
        elif nType == 3:
            sig = min([sigH, sigV])
        elif nType == 4:
            sig = sigH * sigV / math.sqrt(sigH ** 2 + sigV ** 2)

    mu = deltaS
    p = 1 - 0.5 * math.erfc((0 + mu) / (sig * math.sqrt(2)))
    r = random.random()
    response = r <= p
    return response

if __name__ == "__main__":
    # Question 1.2.1
    x = np.arange(-0.5, 1.5, 0.001)
    p = 0.4
    fig, ax = plt.subplots(layout='constrained')
    sigma = 1
    ax.plot(x, (p * np.exp(- (x - 1)**2 / (2 * sigma**2)) + (1 - p) * np.exp(- x**2 / (2 * sigma**2))) / (2 * np.pi * sigma**2)**0.5, label = f'sigma = {sigma}')
    sigma = 0.1
    ax.plot(x, (p * np.exp(- (x - 1)**2 / (2 * sigma**2)) + (1 - p) * np.exp(- x**2 / (2 * sigma**2))) / (2 * np.pi * sigma**2)**0.5, label = f'sigma = {sigma}')
    plt.title('f(x)')
    plt.xlabel('x')
    plt.ylabel('f')
    plt.legend()
    plt.savefig('bin/out10_1.jpg')

    # Question 2
    ID = 3
    St = 4.5
    delta = 0.05
    N = 1000
    data = []
    while St <= 6.5:
        curr = [0.0] * 5
        for _ in range(N):
            curr[0] += int(myNivdak(ID, 0, St))
            for i in range(4):
                curr[1 + i] += int(myNivdak(ID, 1, St, vNL=i))

        for i in range(len(curr)):
            curr[i] /= N

        data.append([St - 5.5] + curr)
        St += delta

    data = np.array(data)
    fig, ax = plt.subplots(layout='constrained')
    ax.plot(data[:,0], data[:,1], label='touch')
    for i in range(4):
        ax.plot(data[:,0], data[:,2 + i], label = f'vision, {i}')

    plt.title('estimated selection probabilites when tested case using single senses')
    plt.xlabel('delta S')
    plt.ylabel('p')
    plt.legend()
    plt.savefig('bin/out10_2.jpg')

    # Question 2.2
    def fit(x, y):
        def func_to_fit(x, sigma):
            return 0.5 *special.erfc((-1/(math.sqrt(2)*sigma))*x)

        sigma, _ = curve_fit(func_to_fit, x, y)
        y_fitted = []
        for i in x:
            y_fitted.append(func_to_fit(i,sigma))

        return y_fitted, np.round(sigma[0], decimals=3)

    fig, ax = plt.subplots(layout='constrained')
    sigmas = []
    data2, sigma2 = fit(data[:, 0], data[:, 1])
    ax.plot(data[:, 0], data2, label=f'touch, sigma={sigma2}')
    for i in range(4):
        data2, sigma = fit(data[:, 0], data[:, 2 + i])
        sigmas.append([i, sigma])
        ax.plot(data[:,0], data2, label = f'vision, {i}, sigma={sigma}')

    plt.legend()
    plt.title('estimated noise when tested case using single senses')
    plt.xlabel('delta S')
    plt.ylabel('p')
    plt.savefig('bin/out10_3.jpg')

    # Question 3
    data = []
    St = 4.5
    while St <= 6.5:
        curr = [0.0] * 4
        for _ in range(N):
            for i in range(4):
                curr[i] += int(myNivdak(ID, 2, St, vNL=i))

        for i in range(len(curr)):
            curr[i] /= N

        data.append([St - 5.5] + curr)
        St += delta

    data = np.array(data)
    fig, ax = plt.subplots(layout='constrained')
    for i in range(4):
        ax.plot(data[:, 0], data[:, 1 + i], label = f'both, {i}')

    plt.title('probability of selection when using both senses')
    plt.xlabel('delta S')
    plt.ylabel('p')
    plt.legend()
    plt.savefig('bin/out10_4.jpg')

    fig, ax = plt.subplots(layout='constrained')
    for i in range(4):
        data2, sigma = fit(data[:, 0], data[:, 1 + i])
        sigmas[i].append(sigma)
        ax.plot(data[:,0], data2, label = f'both, {i}, sigma={sigma}')

    plt.legend()
    plt.title('estimated noise when tested case using both senses')
    plt.xlabel('delta S')
    plt.ylabel('p')
    plt.savefig('bin/out10_5.jpg')

    # Question last
    sigmas = np.array(sigmas)
    fig, ax = plt.subplots(layout='constrained')
    ax.scatter(sigmas[:,0], sigmas[:,1], label = 'vision')
    ax.scatter(sigmas[:,0], sigmas[:,2], label = 'both')
    ax.axhline(sigma2, linestyle='dashed', label = 'touch')
    plt.legend()
    def floored_percent(x_val, _):
        val = math.floor(200 * x_val / 3)
        return f"{val}%"

    ax.xaxis.set_major_formatter(FuncFormatter(floored_percent))
    plt.title('correlation of estimated noise proportion')
    plt.xlabel('visual noise level')
    plt.ylabel('proportional value to sigma')
    plt.savefig('bin/out10_6.jpg')
    plt.show()
