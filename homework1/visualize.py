import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from homework1.pre_processing import data_array
import pickle

with open('sim_array.pkl', 'rb') as f:
    sim_array = pickle.load(f)


def fill_fre(array):
    d = dict()
    for n in array:
        if n != '?':
            if d.get(n):
                d[n] += 1
            else:
                d[n] = 1
    d['0'] = 0
    m = '0'
    for key in d:
        if d[key] > d[m]:
            m = key
    return float(m)


def fill_sim(array, index):
    res_array = []

    def __help(w, i, count=1):
        l = list(sim_array[w, :])
        sort_l = list(sorted(l))
        loc = l.index(sort_l[count])
        if data_array[loc, i] != '?':
            return float(data_array[loc, i])
        else:
            return __help(w, i, count + 1)
    for n, d in enumerate(list(array)):
        if d == '?':
            res_array.append(__help(n, index))
        else:
            res_array.append(float(d))
    return res_array


def visualize_data(array, name, show=False, save=False, model='0', addition=None):
    fig = plt.figure(figsize=[12, 4])
    sub1 = fig.add_subplot(131)
    plt.title('Histogram')
    sub2 = fig.add_subplot(132)
    plt.title('Q-Q')
    sub3 = fig.add_subplot(133)
    plt.title('Box')
    if model == '1':
        data_filled = [float(data) if data != '?' else addition for data in array]
    elif model == '2':
        data_filled = fill_sim(array, addition)
    else:
        data_filled = [float(data) for data in array if data != '?']
    sub1.hist(data_filled, normed=True)
    sub3.boxplot(data_filled)
    sm.qqplot(np.array(data_filled), ax=sub2, line='s')
    if show:
        plt.show()
    if save:
        fig.savefig('./image/'+name+'.jpg')


if __name__ == '__main__':
    for i in [4, 5, 6, 16, 19, 20, 22]:
        visualize_data(data_array[:, i-1], str(i), save=True)
        visualize_data(data_array[:, i-1], 'filled_sim_'+str(i), model='2', save=True, addition=i)
        visualize_data(data_array[:, i-1], 'filled_fre_'+str(i), model='1', save=True, addition=fill_fre(data_array[:, i-1]))