#!/usr/bin/env python3

import logging
import matplotlib.pyplot as plt
import random

logger = logging.getLogger(__name__)

rewards = {
    ('H', 0): 0,
    ('H', 1): 1,
    ('O', 0): 2,
    ('O', 1): 0
}

def R(s, a):
    r = rewards[(s, a)]
    if a == 0:
        return s, r

    if s == 'O':
        return 'H', r

    return random.choices(['H', 'O'], weights = (2, 8))[0], r

if __name__ == "__main__":
    logging.basicConfig(
            level = logging.INFO,
            handlers = [
                logging.StreamHandler()
                ]
            )

    # Question 2.4:
    v_prev = { 'H': -600.0, 'O': 600.0 }
    V = { 'H': 0.0, 'O': 0.0 }
    gamma = 0.5
    r = lambda s, a: {
            ('H', 0): 0,
            ('H', 1): 1,
            ('O', 0): 2,
            ('O', 1): 0
        }[(s, a)]
    p = lambda s2, s, a: {
            ('H', 'H', 0): 1,
            ('H', 'O', 0): 0,
            ('O', 'H', 0): 0,
            ('O', 'O', 0): 1,
            ('H', 'H', 1): 0.2,
            ('H', 'O', 1): 0.8,
            ('O', 'H', 1): 1,
            ('O', 'O', 1): 0,
        }[(s2, s, a)]
    for _ in range(5000):
        v_new = { 'H': 0.0, 'O': 0.0 }
        for s in V.keys():
            v_new[s] = max(r(s, a) + gamma * sum(p(s2, s, a) * V[s2] for s2 in V.keys()) for a in range(2))

        V, v_prev = v_new, V

    print(V)

    # Question 2.5
    V = { 'H': 0.0, 'O': 0.0 }
    eta = 0.01
    T = 3000
    s = 'H'
    data_VH = []
    data_VO = []
    for i in range(T):
        data_VH.append(V['H'])
        data_VO.append(V['O'])
        a = random.choice([0, 1])
        sn, r = R(s, a)
        V[s] += eta * (r + gamma * V[sn] - V[s])
        s = sn

    print(V)
    fig, ax = plt.subplots(layout='constrained')
    ax.set_title("TD-Learning of V")
    ax.plot(range(T), data_VO, alpha = 0.6, label = 'V(O)', color = 'blue')
    ax.plot(range(T), data_VH, alpha = 0.6, label = 'V(H)', color = 'red')
    plt.axhline(4, color = 'blue', linestyle = 'dashed', label = 'V*(O)')
    plt.axhline(2.88, color = 'red', linestyle = 'dashed', label = 'V*(H)')
    plt.xlabel('Iteration number')
    plt.ylabel('value')
    plt.legend()
    plt.savefig('bin/out6_1.jpg')

    # Question 2.6
    Q = {
        ('H', 0): 0.0,
        ('H', 1): 0.0,
        ('O', 0): 0.0,
        ('O', 1): 0.0
    }
    eta = 0.01
    T = 5000
    s = 'H'
    data_VH = []
    data_VO = []
    for i in range(T):
        data_VH.append(max(Q[('H', b)] for b in [0, 1]))
        data_VO.append(max(Q[('O', b)] for b in [0, 1]))
        a = random.choice([0, 1])
        sn, r = R(s, a)
        Qn = max(Q[(sn, b)] for b in [0, 1])
        Q[(s, a)] += eta * (r + gamma * Qn - Q[(s, a)])
        s = sn

    print(Q)
    fig, ax = plt.subplots(layout='constrained')
    ax.set_title("Q-Learning of V")
    ax.plot(range(T), data_VO, alpha = 0.6, label = 'V(O)', color = 'blue')
    ax.plot(range(T), data_VH, alpha = 0.6, label = 'V(H)', color = 'red')
    plt.axhline(4, color = 'blue', linestyle = 'dashed', label = 'V*(O)')
    plt.axhline(2.88, color = 'red', linestyle = 'dashed', label = 'V*(H)')
    plt.legend()
    plt.xlabel('Iteration number')
    plt.ylabel('value')
    plt.savefig('bin/out6_2.jpg')
