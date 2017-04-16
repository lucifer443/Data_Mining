import numpy as np
import json
from pre_processing import *


# 处理标称量
def nominal_attribute(array, index):
    attribute = dict()
    for data in array[:, index]:
        if data == '?':
            continue
        if not attribute.get(data):
            attribute[data] = 1
        else:
            attribute[data] += 1
    return attribute


# 求中位数
def median(array):
    l = len(array)
    m = int(l / 2)-1
    if not l % 2:
        med = (array[m] + array[m+1])/2
    else:
        med = array[m+1]
    return med


# 处理数值量
def numeric_attribute(array, index):
    data_list = []
    info = {'missing_value': 0, 'max': 0, 'min': 0, 'mean': 0,
            'quartile': (0, 0), 'median': 0}
    for data in array[:, index]:
        if data == '?':
            info['missing_value'] += 1
            continue
        data_list.append(float(data))
    data_list.sort()
    l = len(data_list)
    m = int(l/2+0.5)-1
    info['max'] = data_list[-1]
    info['min'] = data_list[0]
    info['mean'] = sum(data_list)/len(data_list)
    info['median'] = median(data_list)
    if not l % 2:
        info['quartile'] = median(data_list[:m+1]), median(data_list[m+1:])
    else:
        info['quartile'] = median(data_list[:m+1]), median(data_list[m:])
    return info


if __name__ == '__main__':
    data_processed = {}.fromkeys(range(1, 29))
    numeric = [4, 5, 6, 16, 19, 20, 22]
    for key in data_processed:
        if key in numeric:
            data_processed[key] = numeric_attribute(data_array, key-1)
        else:
            data_processed[key] = nominal_attribute(data_array, key-1)
    with open('data_summary.json', 'w') as f:
        json.dump(data_processed, f)



