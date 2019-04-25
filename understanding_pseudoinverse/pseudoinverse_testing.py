#!/usr/bin/env python

import copy
import math
import numpy as np
import random
import statistics

def avg_glob_corr_coef(a,a_inv):
    rhos = []
    a_size = a.shape[0]
    for i in range(a_size):
        mult = a[i,i]*a_inv[i,i]
        if mult < 0 or mult >= 1:
            rhos.append(math.sqrt(1.-1./mult))
    print('\nrho vector\n',rhos)
    if len(rhos) == 0: return 0
    return statistics.mean(rhos)

# fix the random number seed
random.seed(1)

# create a singular symmetric random matrix
N = 5
b = np.random.randint(-50,50+1,size=(N,N))
a = (b + b.T)/2
a[:,1] = 0
a[1,:] = 0
for i in range(a.shape[0]):
    a[i,i] = abs(a[i,i])

# make a copy to play with
# make it non-singular by setting the zero diagonal element nonzero
b = copy.deepcopy(a)
b[1,1] = 0.05

# calculate inverse and pseudoinverse
a_pinv = np.linalg.pinv(a)
b_inv = np.linalg.inv(b)

# configure output format
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

# print results
print('\na\n',a)
print('\npseudoinverse of a\n',a_pinv)
print('\naverage global correlation coefficient of a\n',avg_glob_corr_coef(a,a_pinv))
print('\nb\n',b)
print('\ninverse of b\n',b_inv)
print('\naverage global correlation coefficient of b\n',avg_glob_corr_coef(b,b_inv))