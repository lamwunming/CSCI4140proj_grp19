#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt, mpld3

N = 4
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

yvals = [0.29, 0.13, 0.2, 0.29]
rects1 = ax.bar(ind+width*0.5, yvals, width, color='r')
kvals = [0.24, 0.10, 0.14, 0.31]
rects3 = ax.bar(ind+width*1.5, kvals, width, color='b')

ax.set_ylabel('Probability of Bankruptcy')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Algorithm 1', 'Algorithm 2', 'Algorithm 3', 'Algorithm 4') )
ax.legend((rects1[0], rects3[0]), ('AAPL', 'GOOG') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, float(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects3)

# plt.show()
mpld3.show()
