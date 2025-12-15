#!/usr/bin/env python3

import logging

logger = logging.getLogger(__name__)

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

