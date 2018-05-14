#! /usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt, mpld3
import cgi
import cgitb
cgitb.enable()
from CSCI4140 import grabnpred

form = cgi.FieldStorage()
code1 = form.getvalue("code")
code2 = form.getvalue("secondCode")

N = 4
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

# 0700.HK : [array([0.83, 0.12]), array([0.85, 0.15]), array([0.88, 0.12]), array([0.98, 0.02])]
# 0939.HK : [array([0.77, 0.23]), array([0.84, 0.16]), array([0.82, 0.18]), array([0.74, 0.26])]
# code1 = "0700.HK"
# code2 = "0939.HK"

# yvals = [0.12, 0.15, 0.12, 0.02]
yvals = grabnpred(code1)
rects1 = ax.bar(ind+width*0.5, yvals, width, color='r')
# kvals = [0.23, 0.16, 0.18, 0.26]
kvals = grabnpred(code2)
rects3 = ax.bar(ind+width*1.5, kvals, width, color='b')


# title = 'Comparison Prediction Result of ' +  code1 + ' and ' + code2
# ax.title(title)
ax.set_ylabel('Probability of Bankruptcy')
ax.set_xticks(ind+width)
ax.set_xticklabels( ('Algorithm 1', 'Algorithm 2', 'Algorithm 3', 'Algorithm 4') )
ax.legend((rects1[0], rects3[0]), (code1, code2) )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, float(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects3)

# plt.show()
mpld3.show()
