import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import Data
df = pd.read_csv('./IFSVR_data/data_1206_1.out')
#print(df)

# Draw Plot
plt.figure(figsize=(16,10), dpi= 80)
plt.plot('startTm', 'sec', data=df, color='tab:green')
# Decoration
#plt.ylim(50, 750)
#xtick_location = df.index.tolist()[::8]
#xtick_labels = [x[-8:] for x in df.date.tolist()[:14]]
plt.xticks(rotation='vertical', fontsize=5, horizontalalignment='center', alpha=.7)
plt.yticks(fontsize=12, alpha=.7)
plt.title("IFSVR timeouts", fontsize=22)
plt.grid(axis='both', alpha=.3)

# Remove borders
plt.gca().spines["top"].set_alpha(0.0)    
plt.gca().spines["bottom"].set_alpha(0.3)
plt.gca().spines["right"].set_alpha(0.0)    
plt.gca().spines["left"].set_alpha(0.3)   
plt.show()


#f = open('./IFSVR_data/sort_bbl1_data_1206.out', 'r')		# читаем файл в f
#sepFile = np.array([elem.strip().split(' ') for elem in f])	# каждый элемент файла помещаем в двуменый массив 
#x = (sepFile[:,1])	# x будет один из элементов каждого подмассива
#y = (sepFile[:,0])	# y будет другой из элементов каждого подмассива

#sns.relplot(x="time", y="count", sort=False, kind="line", data=sepFile);
