
# heun's method

from __future__ import division
import numpy as np
import math
import matplotlib.pyplot as plt

# right hand side of the ODE
def func(x) :
    return x + 1

# initial condition
x0 = 0

# time step
time_step = 0.01

# solve from 0 to time T
T = 10

# list of discretized time (visualization purpose only) 
t = np.linspace(0, T, int(T/time_step) + 1)

# solution
x = np.zeros(len(t)) 

x[0] = x0;

for i in xrange(1, len(t)) :
    k1 = func(x[i - 1])
    #k2 = func()
    x[i] = x[i - 1] + func(x[i - 1]) * time_step
    
plt.figure()

plt.plot(t, x, color='red')
plt.show()
    