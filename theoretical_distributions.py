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

rc('text',usetex=True)

# Change all fonts to 'Computer Modern'
#rc('font',**{'family':'serif','serif':['Computer Modern']})

f=open('Parameters.dat','r')
tau=str(f.readline().rstrip('\n'))
P_ini=str(f.readline().rstrip('\n'))
delta_P=str(f.readline().rstrip('\n'))
f.close()

f=open('statistics.txt','r')
frequency_1=str(f.readline().rstrip('\n'))
frequency_2=str(f.readline().rstrip('\n'))
frequency_3=str(f.readline().rstrip('\n'))
frequency_4=str(f.readline().rstrip('\n'))
f.close()
#DataIn0 = np.loadtxt('Parameters.dat')
#paras = np.loadtxt('Parameters.dat', unpack=True)


#DataIn1 = np.loadtxt('timeseries_forward_process.dat')
F_V_i, F_s_i, F_C_i, F_V_f, F_s_f, F_C_f, F_nuc_time, F_W = np.loadtxt('timeseries_forward_process.dat', unpack=True, usecols=[0,1,2,3,4,5,6,7])

#DataIn2 = np.loadtxt('timeseries_reversed_process.dat')
R_V_i, R_s_i, R_C_i, R_V_f, R_s_f, R_C_f, R_nuc_time, R_W = np.loadtxt('timeseries_reversed_process.dat', unpack=True, usecols=[0,1,2,3,4,5,6,7])
neg_R_W=-R_W

#DataIn1 = np.loadtxt('timeseries_forward_process_backup.dat')
F_V_i_back, F_s_i_back, F_C_i_back, F_V_f_back, F_s_f_back, F_C_f_back, F_nuc_time_back, F_W_back = np.loadtxt('timeseries_forward_process_backup.dat', unpack=True, usecols=[0,1,2,3,4,5,6,7])

#DataIn2 = np.loadtxt('timeseries_reversed_process_backup.dat')
R_V_i_back, R_s_i_back, R_C_i_back, R_V_f_back, R_s_f_back, R_C_f_back, R_nuc_time_back, R_W_back = np.loadtxt('timeseries_reversed_process_backup.dat', unpack=True, usecols=[0,1,2,3,4,5,6,7])
neg_R_W_back=-R_W_back


#print "after read in";
# //////////////////////////////////


# //////////////////////////////////
plt.figure(1)
plt.subplots_adjust(hspace=.3,wspace=.3)

#  subplots_adjust(left=None, bottom=None, right=None, top=None,
#                    wspace=None, hspace=None)

plt.suptitle('$\Delta P$='+str(delta_P)+', $P_{ini}=$'+str(P_ini)+', t='+ str( tau ))

plt.subplot(221)

plt.title('Forward Process')
plt.ylabel('$W_F$')
plt.xlabel('final $\#$ solid particles ')

plt.scatter(F_s_f,F_W,color='red',s=10,label= " statistics "+str(frequency_1))
plt.scatter(F_s_f_back,F_W_back,color='blue',s=2,label=" statistics "+ str(frequency_2))

legend(loc='lower left',prop={'size':12})
 
#print "after subplot(221)";

plt.subplot(222)


plt.title("Histogramm work")
plt.ylabel('$P(W_F)$')
plt.xlabel('$W_F$')
plt.ylim(0.0,0.5)

plt.hist(F_W, bins=100, normed=True, histtype='step',linewidth=2.0,color='red', log=True)
plt.hist(F_W_back, bins=100, normed=True, histtype='step',linewidth=1.0,color='blue', log=True)



#print "after subplot(222)";

plt.subplot(223)

plt.title('Reversed Process')
plt.xlabel('final $\#$ solid particles ')
plt.ylabel('$-W_R$')

plt.scatter(R_s_f,neg_R_W,alpha=.99,s=10, color='red',label= " statistics "+str(frequency_3))
plt.scatter(R_s_f_back,neg_R_W_back,alpha=.99,s=2, color='blue',label= " statistics "+str(frequency_4))
legend(loc='lower left',prop={'size':12})
#print "after subplot(223)";

plt.subplot(224)

plt.title("Histogramm work")
plt.ylabel('$P(-W_R)$')
plt.xlabel('$-W_R$')
#plt.set_yscale('log')
plt.hist(neg_R_W, bins=100, normed=True, histtype='step',linewidth=2.0, color='red', log=True)
plt.hist(neg_R_W_back, bins=100, normed=True, histtype='step',linewidth=1.0, color='blue', log=True)

#print "after subplot(224)";

# Save the figure in a separate file
plt.savefig('histo_work.png')

plt.figure(2)

plt.suptitle('Nucleation time distribution $\Delta P$='+str(delta_P)+', $P_{ini}=$'+str(P_ini)+', t='+ str( tau ))
plt.subplot(121)
plt.hist(F_nuc_time, bins=100, normed=True, histtype='step',linewidth=2.0,color='red', log=True,label= " statistics "+str(frequency_1))
plt.title("Forward Process")

plt.hist(F_nuc_time_back, bins=100, normed=True, histtype='step',linewidth=1.0,color='blue', log=True,label= " statistics "+str(frequency_2))
plt.ylabel('$P(t)$')
plt.xlabel('$t$')
legend(loc='lower left',prop={'size':12})

plt.subplot(122)
plt.hist(R_nuc_time, bins=100, normed=True, histtype='step',linewidth=2.0,color='red', log=True,label= " statistics "+str(frequency_3))
plt.title("Reversed Process")

plt.hist(R_nuc_time_back, bins=100, normed=True, histtype='step',linewidth=1.0,color='blue', log=True,label= " statistics "+str(frequency_4))
plt.ylabel('$P(t)$')
plt.xlabel('$t$')
legend(loc='lower left',prop={'size':12})
plt.savefig('histo_nuctimes.png')


plt.figure(3)

plt.suptitle('Crystalline Particles distribution $\Delta P$='+str(delta_P)+', $P_{ini}=$'+str(P_ini)+', t='+ str( tau ))
plt.subplot(121)
plt.hist(F_s_f, bins=100, normed=True, histtype='step',linewidth=2.0,color='red', log=True,label= " statistics "+str(frequency_1))
plt.title("Forward Process")

plt.hist(F_s_f_back, bins=100, normed=True, histtype='step',linewidth=1.0,color='blue', log=True,label= " statistics "+str(frequency_2))
plt.ylabel('probability')
plt.xlabel('final number of solid paricles')
legend(loc='lower left',prop={'size':12})

plt.subplot(122)
plt.hist(R_s_f, bins=100, normed=True, histtype='step',linewidth=2.0,color='red', log=True,label= " statistics "+str(frequency_3))
plt.title("Reversed Process")

plt.hist(R_s_f_back, bins=100, normed=True, histtype='step',linewidth=1.0,color='blue', log=True,label= " statistics "+str(frequency_4))
plt.ylabel('probability')
plt.xlabel('final number of solid paricles')
legend(loc='lower left',prop={'size':12})
plt.savefig('histo_solid_particles.png')



plt.figure(4)

plt.suptitle('$\Delta P$='+str(delta_P)+', $P_{ini}=$'+str(P_ini)+', t='+ str( tau ))

plt.ylabel('P(Work)')
plt.xlabel('Work')

plt.hist(F_W, bins=100, normed=True, histtype='step',linewidth=2.0,color='red', log=True,label= " statistics "+str(frequency_1))
plt.hist(F_W_back, bins=100, normed=True, histtype='step',linewidth=1.0,color='blue', log=True)

plt.hist(neg_R_W, bins=100, normed=True, histtype='step',linewidth=2.0, color='red', log=True,label= " statistics "+str(frequency_3))
plt.hist(neg_R_W_back, bins=100, normed=True, histtype='step',linewidth=1.0, color='blue', log=True)
legend(loc='lower left',prop={'size':12})
plt.savefig('histo_work_distribution.png')

# Draw the plot to the screen
#plt.show()
#for t in zip(bx[ix], by[iy], bz[iz], H[ix,iy,iz]):
#    print t
#W2=W-1000;
#DataOut = np.column_stack((W,W2))
#np.savetxt('python_output_2.dat', DataOut)

#np.savetxt('python_output.dat', (W,W2));

#pyfits.info("timeseries_forward_process.dat")
#f = open('timeseries_forward_process.dat', 'r');
#for line in f:
#        print line,
