import numpy as np


def calculate(l: list):
    if len(l) != 9:
        raise ValueError('List must contain nine numbers.')
    m = np.array(l).reshape((3, 3))

    calculations = {
        'mean': [list(np.mean(m, axis=0)), list(m.mean(axis=1)), m.mean()],
        'variance': [list(np.var(m, axis=0)), list(np.var(m, axis=1)), np.var(m)],
        'standard deviation': [list(np.std(m, axis=0)), list(np.std(m, axis=1)), np.std(m)],
        'max': [list(m.max(axis=0)), list(m.max(axis=1)), m.max()],
        'min': [list(m.min(axis=0)), list(m.min(axis=1)), m.min()],
        'sum': [list(m.sum(axis=0)), list(m.sum(axis=1)), m.sum()]
    }

    return calculations


# print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
