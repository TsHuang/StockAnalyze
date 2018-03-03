import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

import matplotlib.pyplot as plt

fig = plt.figure()  
ax = fig.add_subplot(1,1,1)


def PlotDemo1():
 fig  = plt.figure()
 ax = fig.add_subplot(1,1,1)
 ax.plot([1,2,3,4],[2,3,4,5])
 plt.show()