import numpy as np

def generate_dynamic_table(capacity, items):
    matrix = np.zeros((capacity + 1, len(items)+1))
    for item in items:
        j = item.index + 1
        for i in range(capacity + 1):
            if item.weight <= i:
                matrix[i][j] = max((matrix[i][j-1], item.value + matrix[i-item.weight][j-1]))
            else: matrix[i][j] = matrix[i][j-1]
    return matrix

def evaluate_matrix(items, capacity, matrix):
    taken = [0]*len(items)
    i = capacity
    value = 0
    for item in reversed(items):
        j = item.index + 1
        if matrix[i][j] != matrix[i][j-1]:
            taken[j-1] = 1
            i = i - item.weight
            value = value + item.value
    return value, taken