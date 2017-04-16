from homework1.pre_processing import data_array
import numpy as np
from math import sqrt
import pickle


def num_similarity(array, a, b):
    a1 = list(array[a, [4, 5, 6, 16, 19, 20, 22]])
    a2 = list(array[b, [4, 5, 6, 16, 19, 20, 22]])
    i = len(a1) - 1
    while i >= 0:
        if a1[i] == '?' or a2[i] == '?':
            a1.pop(i)
            a2.pop(i)
        else:
            a1[i] = float(a1[i])
            a2[i] = float(a2[i])
        i -= 1
    result = sqrt(sum(np.square(np.array(a1)-np.array(a2))))
    return result


def nom_similarity(array, a, b):
    a1 = list(array[a, [i-1 for i in range(1, 29) if i not in [4, 5, 6, 16, 19, 20, 22]]])
    a2 = list(array[b, [i-1 for i in range(1, 29) if i not in [4, 5, 6, 16, 19, 20, 22]]])
    i = len(a1) - 1
    m = 0
    while i >= 0:
        if a1[i] == '?' or a2[i] == '?':
            a1.pop(i)
            a2.pop(i)
        elif a1[i] == a2[i]:
            m += 1
        i -= 1
    l = len(a1)
    return (l-m)/l


def sim_matrix():
    num_array = np.zeros([368,368])
    nom_array = np.zeros([368,368])
    for i in range(368):
        for j in range(368):
            if i != j:
                num_array[i][j] = num_similarity(data_array, i, j)
                nom_array[i][j] = nom_similarity(data_array, i, j)
    num_array = (num_array - np.ones([368, 368])*num_array.min())/num_array.max()
    sim_array = (num_array + nom_array)/2
    return sim_array


if __name__ == '__main__':
    sim_array = sim_matrix()
    with open('sim_array.pkl', 'wb') as f:
        pickle.dump(sim_array, f)


