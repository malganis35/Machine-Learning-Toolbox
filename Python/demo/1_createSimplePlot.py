# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 20:27:57 2017

@author: CaoTri
"""

#%% import package
print("Loading general packages: start")

import numpy as np  # (*) numpy for math functions and arrays

import matplotlib.pyplot as plt # (*) import matplotlib

print("Loading general packages: end")

#%%
print("Exercice 1 : create a simple plot")

# arange(1,11, dtype=Float)
# range(1,11)
x = np.arange(0,1,0.01)
y = np.sin( 2 * np.pi * x)


plt.figure()
plt.plot(x,y)
plt.show()

plt.plot()
