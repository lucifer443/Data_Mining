import requests
url_data = 'http://archive.ics.uci.edu/ml/machine-learning-databases/horse-colic/horse-colic.data'
url_test = 'http://archive.ics.uci.edu/ml/machine-learning-databases/horse-colic/horse-colic.test'
data = requests.get(url_data).text
test = requests.get(url_test).text
with open('data.txt', 'w') as f:
    f.write(data)
    f.write(test)