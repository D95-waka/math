#!/usr/bin/env python3

import base64
import bz2
import importlib.machinery
import matplotlib.pyplot as plt
import numpy as np

class SourcelessMemoryLoader(importlib.machinery.SourcelessFileLoader):
    def __init__(self, *args, **kwargs):
        data = b'QlpoOTFBWSZTWfQ9a8sAATP/////vxnUK3qVzn2fSK7n3zhc+OY4ACAABACASHRMIGgAMAGWTayEU9CjTU9PUjyR6jT0T0E0MmgaBkZGRkyZNAxDQPUMgaPSN6g1ENBpojInqbQmjIaaaGgDQZDJoAAAAAZDE9JoNTQptT1QDRjSYRpo2oyGgGIZGQaBgjJkDQ0aNAwge7cUFacsjWB4EGQSQUiZSEjFI4UIO+4nFqHsHkSWIaAQDtJ5ht/RL8OGxIBhjEA9IABomiHr0oQEaBwBwNHNbIxu4gIIhHtu8XLS1gmm+7DmcoZ6uW4d2cP2KBfrFAh1rAILWogVmfMgtaLCy4TJKiM8uosF1yfdeutdorLUWTwGNgebYVVBnEkqDO0pQqutnN0vpB+7cXksuCFCwx+tinP1ykdlFHAqkJsYwjyzNZFtXOox0jxLAt+R1+QFHg9ZL3013Un7wbILNjZKq7G0nA3l4vphRpBxjOI2P9XbjhyzfvpRDpsw2aQ3koJJ2VnGS2OQjIkJW3UFDY0ypW3JV8ophDwB7h8rGvft9zlQ7Puuh/DY7j3bMwcuAXzOmwwTISzE3IEMNRQ/lzrKgqnhMFGEUGULeO03k0mXplk7JQ8dJgoXtNRBNtuKqPLhvEadGLJlvMCO1eqHDEhH83x1Lk7wnw63XQ2zFpWKSdlpBhKHOBsp6sHmkjU1jWJn8rXR/nCSZGwdmtGi57qOAgJV6hCRn5DtdJXyEKGkjiF3JFOFCQ9D1ryw'
        data = base64.b64decode(data)
        data = bz2.decompress(data)
        self._data = data
        super().__init__(*args, **kwargs)

    def get_data(self, path) -> bytes:
        return self._data


if __name__ == "__main__":
    loader = SourcelessMemoryLoader(path="Hamster", fullname="Hamster")
    Hamster = loader.load_module("Hamster")
    my_hamster = Hamster.myHamster

    # Question 1
    ID = 123
    Xg = 1
    delta = 0.01
    Xs = 0
    a = my_hamster(Xs, Xg, ID)
    while my_hamster(Xs, Xg, ID) == a:
        Xs += delta

    print(f"X_s^1 = {Xs}")

    # Question 2
    Xg = Xs
    Xs = 0
    a = my_hamster(Xs, Xg, ID)
    while my_hamster(Xs, Xg, ID) == a:
        Xs += delta

    print(f"X_s^2 = {Xs}")

    # Question 3
    Xg = [1]
    Xs = []
    u = []
    N = 5
    for _ in range(5):
        Xs.append(0)
        a = my_hamster(Xs[-1], Xg[-1], ID)
        while my_hamster(Xs[-1], Xg[-1], ID) == a:
            Xs[-1] += delta

        if Xg[-1] == 1:
            u.append(0.5)
        else:
            u.append(u[-1] * 0.5)

        Xg.append(Xs[-1])

    print(', '.join([f'X_s^{n} = {x}, X_g^{n} = {y}' for (n, x, y) in zip(range(len(Xs)), Xs, Xg)]))

    # Question 4
    fig, ax = plt.subplots(layout='constrained')
    ax.scatter(Xs, u)
    ax.plot(Xs, u)
    plt.title(f'u(X_s) for ID = {ID}')
    plt.xlabel('X_s')
    plt.ylabel('u(X_s)')
    plt.savefig('bin/out8_1.jpg')

    # Question 2.1
    p = np.arange(0.0, 1.0, 0.01)
    alpha = 2
    pi = lambda p: np.exp(- (- np.log(p)) ** alpha)

    fig, ax = plt.subplots(layout='constrained')
    ax.plot(p, pi(p), label = f'alpha = {alpha}')
    alpha = 1
    ax.plot(p, pi(p), label = f'alpha = {alpha}')
    alpha = 1/2
    ax.plot(p, pi(p), label = f'alpha = {alpha}')
    plt.title('pi(x) for various alpha values')
    plt.xlabel('p')
    plt.ylabel('pi(p)')
    plt.legend()
    plt.savefig('bin/out8_2.jpg')

    # Question 2.2
    x = np.arange(0.0, 5.0, 0.05)
    sigma = 2
    u = lambda x: x ** sigma
    fig, ax = plt.subplots(layout='constrained')
    ax.plot(x, u(x), label = f'sigma = {alpha}')
    sigma = 1
    ax.plot(x, u(x), label = f'sigma = {alpha}')
    sigma = 1/2
    ax.plot(x, u(x), label = f'sigma = {alpha}')
    plt.title('u(x) for various sigma values')
    plt.xlabel('x')
    plt.ylabel('u(x)')
    plt.legend()
    plt.savefig('bin/out8_3.jpg')
    plt.show()
