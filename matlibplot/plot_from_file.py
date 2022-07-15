import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import string

f = open('./IFSVR_data/sort_bbl1_data_1207.out', 'r')		# читаем файл в f
sepFile = np.array([elem.strip().split(' ') for elem in f])	# каждый элемент файла помещаем в двуменый массив 
x = (sepFile[:,1])	# x будет один из элементов каждого подмассива
y = (sepFile[:,0])	# y будет другой из элементов каждого подмассива

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid(True, linestyle='dotted', color='black')
ax.tick_params(labelcolor='black', labelsize='x-small', width=1)
plt.xlabel('Time')
plt.ylabel('Count')
plt.title('IFSVR GET_MESSAGE_ID BBL1 above 0.5s')
plt.gcf().autofmt_xdate()
plt.show()
