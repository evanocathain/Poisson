#!/usr/bin/python

import math as m

# Gehrels 1986 paper http://adsabs.harvard.edu/abs/1986ApJ...303..336G
S     = 1.645 # The Gaussian sigma level corresponding to 95% confidence
beta  = 0.031 # Lower limit parameter appropriate for 95% confidence
gamma = -2.50 # Lower limit parameter appropriate for 95% confidence

S     = 1.000 # The Gaussian sigma level corresponding to 84.13% confidence
beta  = 0.0 # Lower limit parameter appropriate for 84.13% confidence
gamma = 0.0 # Actually undefined for 84.13% confidence

for n in range(0,150):
    lower = 0.0
    # Gehrels 1986 equation 9
    upper = (n+1)*(1.0 - (1.0/(9*(n+1.0))) + (S/(3.0*m.sqrt(n+1.0))))**3 
    if ( n>0 ):
        # Gehrels 1986 equation 14
        lower = n*(1.0 - (1.0/(9.0*n)) - (S/(3.0*m.sqrt(n))) + beta*n**gamma)**3 
    print ("%.1f %d %.1f" % (upper, n,lower))
