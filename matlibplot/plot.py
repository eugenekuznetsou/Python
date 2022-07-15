import matplotlib.pyplot as plt

fig, ax = plt.subplots()
line_up, = ax.plot([1, 2, 3], label='Line 2')
line_down, = ax.plot([3, 2, 1], label='Line 1')
ax.legend(handles=[line_up, line_down])
plt.plot([1,2,3,4],[1,30,77,100])
plt.xlabel('numberX')
plt.ylabel('numberY')
plt.show()