#!/usr/bin/env python

from sympy import *
import sys


#===============================================================================
# Circle plotting function from
# https://stackoverflow.com/questions/9081553/python-scatter-plot-size-and-style-of-the-marker/24567352#24567352
def circles(x, y, s, c='b', vmin=None, vmax=None, **kwargs):
  """
  Make a scatter of circles plot of x vs y, where x and y are sequence 
  like objects of the same lengths. The size of circles are in data scale.

  Parameters
  ----------
  x,y : scalar or array_like, shape (n, )
      Input data
  s : scalar or array_like, shape (n, ) 
      Radius of circle in data unit.
  c : color or sequence of color, optional, default : 'b'
      `c` can be a single color format string, or a sequence of color
      specifications of length `N`, or a sequence of `N` numbers to be
      mapped to colors using the `cmap` and `norm` specified via kwargs.
      Note that `c` should not be a single numeric RGB or RGBA sequence 
      because that is indistinguishable from an array of values
      to be colormapped. (If you insist, use `color` instead.)  
      `c` can be a 2-D array in which the rows are RGB or RGBA, however. 
  vmin, vmax : scalar, optional, default: None
      `vmin` and `vmax` are used in conjunction with `norm` to normalize
      luminance data.  If either are `None`, the min and max of the
      color array is used.
  kwargs : `~matplotlib.collections.Collection` properties
      Eg. alpha, edgecolor(ec), facecolor(fc), linewidth(lw), linestyle(ls), 
      norm, cmap, transform, etc.

  Returns
  -------
  paths : `~matplotlib.collections.PathCollection`

  Examples
  --------
  a = np.arange(11)
  circles(a, a, a*0.2, c=a, alpha=0.5, edgecolor='none')
  plt.colorbar()

  License
  --------
  This code is under [The BSD 3-Clause License]
  (http://opensource.org/licenses/BSD-3-Clause)
  """
  import numpy as np
  import matplotlib.pyplot as plt
  from matplotlib.patches import Circle
  from matplotlib.collections import PatchCollection

  if np.isscalar(c):
    kwargs.setdefault('color', c)
    c = None
  if 'fc' in kwargs: kwargs.setdefault('facecolor', kwargs.pop('fc'))
  if 'ec' in kwargs: kwargs.setdefault('edgecolor', kwargs.pop('ec'))
  if 'ls' in kwargs: kwargs.setdefault('linestyle', kwargs.pop('ls'))
  if 'lw' in kwargs: kwargs.setdefault('linewidth', kwargs.pop('lw'))

  patches = [Circle((x_, y_), s_) for x_, y_, s_ in np.broadcast(x, y, s)]
  collection = PatchCollection(patches, **kwargs)
  if c is not None:
    collection.set_array(np.asarray(c))
    collection.set_clim(vmin, vmax)

  ax = plt.gca()
  ax.add_collection(collection)
  ax.autoscale_view()
  if c is not None:
    plt.sci(collection)
  return collection
#===============================================================================



def RepresentsFloat(s):
  try: 
    float(s)
    return True
  except ValueError:
    return False

if len(sys.argv) != 4:
  print 'Number of command line arguments is not 3. Exit...'
  quit()

if not (RepresentsFloat(sys.argv[1]) and RepresentsFloat(sys.argv[2]) and RepresentsFloat(sys.argv[3])):
  print 'There are arguments not representing numbers. Exit...'
  quit()

#===============================================================================
# end of preparation

A = float(sys.argv[1])
B = float(sys.argv[2])
C = float(sys.argv[3])
R = sqrt((B+C)/(A+B))

x = Symbol('x')
y = Symbol('y')

eq1 = sin(x) - R*sin(y)
eq2 = x - sin(x)*cos(x) +  R**2*y - R**2*sin(y)*cos(y) - (B*pi)/(A+B)

solutions = nsolve((eq1, eq2), (x,y), (1,1))
theta = solutions[0]
phi = solutions[1]
# let d be the distance between the two centers of the two circles
d = (cos(x) + R*cos(y)).subs([(x, theta), (y, phi)])
print 'Distance between centers:', d
print 'Angles:', solutions

#===============================================================================
# Plot results
#===============================================================================
from pylab import *
figure(figsize=(8,8))
ax=subplot(aspect='equal')

# Circles
# Use a shrinking factor since the function is in data unit.
shrinkage = 1./(1+d+R)
circles(shrinkage, .5, shrinkage, alpha=0.2, edgecolor='none')
circles(shrinkage*(1+d), .5, shrinkage*R, alpha=0.2, edgecolor='none', c='r')

axis('off')
show()
