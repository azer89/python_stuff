'''
This code is rewritten from http://www.nervouscomputer.com/hfs/pdf/introtns/Getting-to-know-Python.pdf
'''

from __future__ import division
import numpy as np
import math
import matplotlib.pyplot as plt



# right hand side of the ODE
def func(x) :
    return x + 1

# initial condition
y0 = 0

# time step
time_step = 0.01

# solve from 0 to time T
T = 10

# list of discretized time (visualization purpose only) 
x = np.linspace(0, T, int(T/time_step) + 1)

# solution
y = np.zeros(len(t)) 

y[0] = y0;

for i in xrange(1, len(t)) :
    y[i] = y[i - 1] + func(y[i - 1]) * time_step
    
plt.figure()

plt.plot(x, y, color='red')
plt.show()
    

