# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 18:58:42 2017

@author: CaoTri
"""


#%% Here is a code for automatic import or installation of the missing packages

# Clear the console
import os
os.system('cls')
print("Cleaning the console")

#%% To make better plot than matlibplot 
# source: http://nbviewer.jupyter.org/github/plotly/python-user-guide/blob/master/s6_matplotlylib/s6_matplotlylib.ipynb

# General setting for plotly

# (*) Import plotly package
import plotly  as py  
# (*) To communicate with Plotly's server, sign in with credentials file
py.tools.set_credentials_file(username='malganis35', api_key='rCj7uQvW5DbgQDby831N')

# Check plolty version (if not latest, please upgrade)
print("plotly version")
py.__version__

# (*) Useful Python/Plotly tools
import plotly.tools as tls   

# (*) Graph objects to piece together plots
from plotly.graph_objs import *


#%% import package

# (*) numpy for math functions and arrays
import numpy as np  

import matplotlib.pyplot as plt # (*) import matplotlib

#%% Package all mpl plotting commands inside one function
def plot_mpl_fig():
    
    # Make two time arrays
    t1 = np.arange(0.0, 2.0, 0.1)
    t2 = np.arange(0.0, 2.0, 0.01)

    # N.B. .plot() returns a list of lines.  
    # The "l1, = plot" usage extracts the first element of the list 
    # into l1 using tuple unpacking.  
    # So, l1 is a Line2D instance, not a sequence of lines
    l1, = plt.plot(t2, np.exp(-t2), label='decaying exp.')
    l2, l3 = plt.plot(t2, np.sin(2 * np.pi * t2), '--go', 
                      t1, np.log(1 + t1), '.')
    l4, = plt.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 'rs-.')

    # Add axis labels and title
    plt.xlabel('time')
    plt.ylabel('volts')
    plt.title('Damped oscillation')
    
    return (l1, l2, l3, l4)  # return line objects (for legend, later)

# Plot it!
plot_mpl_fig()

# N.B. get matplotlib figure object and assign a variable to it
mpl_fig1 = plt.gcf()


#%% Convert to plotly

py_fig1 = tls.mpl_to_plotly(mpl_fig1, verbose=True)

print(py_fig1.to_string())

# print(key-value pairs corresponding to the figure's size
for i in ['autosize', 'width', 'height']:
    print(i, py_fig1['layout'][i])
    
py.iplot_mpl(mpl_fig1, filename='s6_damped_oscillation')    