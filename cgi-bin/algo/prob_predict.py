#!/usr/bin/python
import os,sys
import cgi
import cgitb; cgitb.enable()
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt, mpld3
import pylab

objects = ('Algorithm 1', 'Algorithm 2', 'Algorithm 3', 'Algorithm 4')
y_pos = np.arange(len(objects))
willCorrupt = [0.29, 0.13, 0.2, 0.29]

plt.bar(y_pos, willCorrupt, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Probability')
plt.title('Algorithms Prediction Result')

# fig = plt.figure()
# plt.show()
mpld3.show()
# url = "http://localhost:8080/cgi-bin/dashboard.html"

# print ("Status: 302 Found")
# print ("Location: " + url)
# print ("Content-Type: image/png\n")
# save the plot as a png and output directly to webserver
# print ("<html>")
# print ("<head>")
# print ('<meta http-equiv="refresh" content="0;url=' + url + '" />')
# print ("</head>")
# print ("<body>")
# pylab.savefig(sys.stdout, format='png' )
# print ("TEST")
# print ("</body>")
# print ("</html>")
