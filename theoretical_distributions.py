#!/usr/bin/python

# Hello world python program

#print "Hello World!";
#import pyfits
import numpy as np
# Pyplot is a module within the matplotlib library for plotting
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
import os
#import Parameters.py
import numpy.random;
#Generate 1000 random integer numbers which are between 1 and 9999(included).

rc('text',usetex=True)

# Change all fonts to 'Computer Modern'
#rc('font',**{'family':'serif','serif':['Computer Modern']})



#DataIn1 = np.loadtxt('timeseries_forward_process.dat')
#F_V_i, F_s_i, F_C_i, F_V_f, F_s_f, F_C_f, F_nuc_time, F_W = np.loadtxt('timeseries_forward_process.dat', unpack=True, usecols=[0,1,2,3,4,5,6,7])


#print "after read in";
# //////////////////////////////////


# //////////////////////////////////
plt.figure(1)
plt.subplots_adjust(hspace=.3,wspace=.3)

#  subplots_adjust(left=None, bottom=None, right=None, top=None,
#                    wspace=None, hspace=None)
x=randn(1000)
plt.suptitle('')

plt.subplot(111)

plt.title('histogram')
plt.ylabel('pdf')
plt.xlabel('x')

plt.hist(x,bins=100)

legend(loc='lower left',prop={'size':12})
 
#print "after subplot(221)";

# Save the figure in a separate file
plt.savefig('histo_work.png')
