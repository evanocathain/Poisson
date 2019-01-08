#!/usr/bin/puthon

import numpy as np
import scipy.misc as s
import scipy.stats as stats
import math as m
import matplotlib.pyplot as plt

prob = lambda k, l: l**k*m.exp(-l)/s.factorial(k)
p4 = np.zeros(50)
p15 = np.zeros(50)
for i in range(0,50):
    p4[i]  = prob(i*1.0,4)
    p15[i] = prob(i*1.0,15*0.7)

ks = stats.ks_2samp(p4,p15)
print ks
plt.plot(p4)
plt.plot(p15)
plt.show()
