#!/usr/bin/python
import os,sys
import cgi
import cgitb; cgitb.enable()
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt, mpld3
import pylab
from CSCI4140 import grabnpred

form = cgi.FieldStorage()
code = form.getvalue("code")
# 0700.HK : [array([0.83, 0.12]), array([0.85, 0.15]), array([0.88, 0.12]), array([0.98, 0.02])]
# 0939.HK : [array([0.77, 0.23]), array([0.84, 0.16]), array([0.82, 0.18]), array([0.74, 0.26])]
# code = "0700.HK"

result = grabnpred(code)


objects = ('Algorithm 1', 'Algorithm 2', 'Algorithm 3', 'Algorithm 4')
y_pos = np.arange(len(objects))
# willCorrupt = [0.12, 0.15, 0.12, 0.02]

# plt.bar(y_pos, willCorrupt, align='center', alpha=0.5)
plt.bar(y_pos, result, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Probability of Bankruptcy')
plt.title('Algorithms Prediction Result of ' +  code)

# fig = plt.figure()
# plt.show()
mpld3.show()
