#!/usr/bin/env python

# This script is to investigate the
# range of the so-called global correlation coefficient.
# First I have to generate a random positive semidefinite
# matrix to simulate a covariance matrix.
# Then the inverse and hence the value of the
# global correlation coefficient are calculated.

import numpy as np


def make_psd_matrix(n):
    '''
    Make an nxn positive semidefinite random matrix by
    generating a random nxm matrix and right multiplying
    its transpose.
    '''

    # If m < n, then the resulting matrix will be rank-deficient and thus
    # have a large condition number. This happens half of the times.
    m = np.random.randint(1,2*n)
    A = np.random.uniform(-10,10,(n,m))
    B = np.dot(A,A.transpose())

    return B

# format numpy output
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)

# calculate properties
a = make_psd_matrix(5)
a_pinv = np.linalg.pinv(a)
diag_mults = np.array([a[i,i]*a_pinv[i,i] for i in range(a.shape[0])])
np.array_repr(diag_mults, precision=6)

# print results
print('\npositive semidefinite matrix V')
print(a)
print('\ncondition number of V\n{:.4}'.format(np.linalg.cond(a)))
print('\nV_ii*(V^-1)_ii\n', diag_mults)