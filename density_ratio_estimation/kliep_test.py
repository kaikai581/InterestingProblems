#!/usr/bin/env python

from scipy.stats import norm
from pykliep import DensityRatioEstimator
import matplotlib.pyplot as plt
import numpy as np

def true_density_ratio(x):
    return norm.pdf(x, 1, 1./8) / norm.pdf(x, 1, 1./2)

np.random.seed(0)

x = norm.rvs(size = 1500, loc = 1, scale = 1./8)
x = x.reshape(len(x),1)
y = norm.rvs(size = 1500, loc = 1, scale = 1./2)
y = y.reshape(len(y),1)
print(x.shape, y.shape)
# density ration estimation
kliep = DensityRatioEstimator()
# first argument denominator, second numerator
kliep.fit(y, x)

x = np.linspace(-1, 3, 400)
plt.plot(x, true_density_ratio(x), "r-", lw=5, alpha=0.6, label="w(x)")
plt.plot(x, kliep.predict(x.reshape(len(x),1)), "k-", lw=2, label="w-hat(x)")
plt.legend(loc="best", frameon=False)
plt.xlabel("x")
plt.ylabel("Density Ratio")
plt.show()