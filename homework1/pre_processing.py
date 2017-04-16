import numpy as np
with open('data.txt') as f:
    data = [item.split() for item in f.read().split('\n')][:368]
data_array = np.array(data)

#for i in data_array[:, 4]:
    #print(i)
