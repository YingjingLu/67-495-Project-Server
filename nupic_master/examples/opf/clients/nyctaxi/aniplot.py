import matplotlib.pyplot as plt
import csv
import copy
from matplotlib.animation import FuncAnimation

taxi_list = []
err_list = []
err_index = []
index_list = []


f = open('nycTaxi.csv', 'r')

fig, ax = plt.subplots()
plt.plot(index_list, taxi_list,'k', err_index, err_list, 'bo')

csv_reader = csv.reader(f, delimiter = ',')
csv_reader.__next__()

def animate(i):
    plt.plot(index_list, taxi_list,'k', err_index, err_list, 'bo')

for i, record in enumerate(csv_reader, start = 1):
    index_list.append(i)
    taxi_list.append(float(record[1]))
    taxi2_list.append(float(record[1]) + start)
    start += INCREMENT

f.close()


f=open('anomaly_scores.csv', 'r')
csv_reader = csv.reader(f, delimiter = ',')
csv_reader.__next__()
for record in csv_reader:
    err_list.append(float(record[-3]))
    err_index.append(int(record[-1]))



err2_list = []
err2_index = []

f=open('anomaly_scores_with_increment.csv', 'r')
csv_reader = csv.reader(f, delimiter = ',')
csv_reader.__next__()
for record in csv_reader:
    err2_list.append(float(record[-3]))
    err2_index.append(int(record[-1]))

plt.figure(1)
plt.subplot(211)
plt.plot(index_list, taxi_list,'k', err_index, err_list, 'bo')

plt.subplot(212)
plt.plot(index_list, taxi2_list,'k', err2_index, err2_list, 'bo')
plt.show()


