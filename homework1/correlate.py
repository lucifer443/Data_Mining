from homework1.pre_processing import data_array
import numpy as np
from math import sqrt


def correlation(array, a, b):
    a1 = list(array[:, a])
    a2 = list(array[:, b])
    i = len(a1)-1
    while i >= 0:
        if a1[i] == '?' or a2[i] == '?':
            a1.pop(i)
            a2.pop(i)
        else:
            a1[i] = float(a1[i])
            a2[i] = float(a2[i])
        i -= 1
    sum_a1 = sum(a1)
    sum_a2 = sum(a2)
    l = len(a1)
    result = (np.dot(a1, a2) - sum_a1 * sum_a2/l)/sqrt((np.dot(a1, a1) - sum_a1**2/l)*(np.dot(a2, a2) - sum_a2**2/l))
    return result

if __name__ == '__main__':
    cor_array = np.zeros([7, 7])
    num_index = [4, 5, 6, 16, 19, 20, 22]
    for i in range(7):
        for j in range(7):
            cor_array[i][j] = correlation(data_array, num_index[i]-1, num_index[j]-1)
    print(cor_array)
