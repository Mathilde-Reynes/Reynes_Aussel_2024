# -*- coding: utf-8 -*-

from brian2 import *
import numpy as np
import matplotlib.pyplot as plt
VPY_s = np.loadtxt('../../Data/PY_v_10.txt')
VPY_d = np.loadtxt('../../Data/PYdend_v_10.txt')
VIN = np.loadtxt('../../Data/IN_v_10.txt')
VIN_d = np.loadtxt('../../Data/INdend_v_10.txt')
VRE = np.loadtxt('../../Data/RE_v_10.txt')
VTC = np.loadtxt('../../Data/TC_v_10.txt')
time=np.arange(0, 10000, 0.02)
time_s=time/1000

###Figure S1 every dt
fig,ax = subplots(4,1, sharex = True,figsize=(19,24))
ax[0].plot(time_s, VPY_s[50],color="tab:blue",linewidth=1.5)
ax[0].set_title('PY', size=30, loc='left')
ax[0].set_ylabel('mV',size=30, labelpad=30)
#ax[0].set_xlim([15000,30000])
ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].spines['bottom'].set_visible(True)
ax[0].spines['left'].set_visible(True)
ax[0].yaxis.set_major_locator(MultipleLocator(base=25))
ax[0].tick_params(axis='both', which='major', labelsize=25, width=2)
#
ax[1].plot(time_s, VIN[15],color="tab:green",linewidth=1.5)
ax[1].set_title('IN', size=30, loc='left')
ax[1].set_ylabel('mV',size=30, labelpad=30)
ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].spines['bottom'].set_visible(True)
ax[1].spines['left'].set_visible(True)
ax[1].yaxis.set_major_locator(MultipleLocator(base=25))
ax[1].tick_params(axis='both', which='major', labelsize=25, width=2)
#
ax[2].plot(time_s, VRE[25],color="tab:red",linewidth=1.5)
ax[2].set_title('RE', size=30, loc='left')
ax[2].set_ylabel('mV',size=30, labelpad=30)
ax[2].spines['top'].set_visible(False)
ax[2].spines['right'].set_visible(False)
ax[2].spines['bottom'].set_visible(True)
ax[2].spines['left'].set_visible(True)
ax[2].yaxis.set_major_locator(MultipleLocator(base=25))
ax[2].tick_params(axis='both', which='major', labelsize=25, width=2)
#
ax[3].plot(time_s, VTC[25],color="tab:orange",linewidth=1.5)
ax[3].set_title('TC', size=30, loc='left')
ax[3].set_ylabel('mV', size=30, labelpad=30)
ax[3].set_xlabel('second', size=30)
ax[3].tick_params(axis='both',labelbottom=True)
ax[3].spines['top'].set_visible(False)
ax[3].spines['right'].set_visible(False)
ax[3].spines['bottom'].set_visible(True)
ax[3].spines['left'].set_visible(True)
ax[3].yaxis.set_major_locator(MultipleLocator(base=25))
ax[3].tick_params(axis='both', which='major', labelsize=25, width=2)
#plt.savefig('Supplementary1A.png', dpi=300, bbox_inches='tight')

###Figure S1 not every dt
fig,ax = subplots(4,1, sharex = True,figsize=(19,24))
ax[0].plot(time_s[::50], VPY_s[50][::50],color="tab:blue",linewidth=1.5)
ax[0].set_title('PY', size=30, loc='left')
ax[0].set_ylabel('mV',size=30, labelpad=30)
#ax[0].set_xlim([15000,30000])
ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].spines['bottom'].set_visible(True)
ax[0].spines['left'].set_visible(True)
ax[0].yaxis.set_major_locator(MultipleLocator(base=25))
ax[0].tick_params(axis='both', which='major', labelsize=25, width=2)
#
ax[1].plot(time_s[::50], VIN[15][::50],color="tab:green",linewidth=1.5)
ax[1].set_title('IN', size=30, loc='left')
ax[1].set_ylabel('mV',size=30, labelpad=30)
ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].spines['bottom'].set_visible(True)
ax[1].spines['left'].set_visible(True)
ax[1].yaxis.set_major_locator(MultipleLocator(base=25))
ax[1].tick_params(axis='both', which='major', labelsize=25, width=2)
#
ax[2].plot(time_s[::50], VRE[25][::50],color="tab:red",linewidth=1.5)
ax[2].set_title('RE', size=30, loc='left')
ax[2].set_ylabel('mV',size=30, labelpad=30)
ax[2].spines['top'].set_visible(False)
ax[2].spines['right'].set_visible(False)
ax[2].spines['bottom'].set_visible(True)
ax[2].spines['left'].set_visible(True)
ax[2].yaxis.set_major_locator(MultipleLocator(base=25))
ax[2].tick_params(axis='both', which='major', labelsize=25, width=2)
#
ax[3].plot(time_s[::50], VTC[25][::50],color="tab:orange",linewidth=1.5)
ax[3].set_title('TC', size=30, loc='left')
ax[3].set_ylabel('mV', size=30, labelpad=30)
ax[3].set_xlabel('second', size=30)
ax[3].tick_params(axis='both',labelbottom=True)
ax[3].spines['top'].set_visible(False)
ax[3].spines['right'].set_visible(False)
ax[3].spines['bottom'].set_visible(True)
ax[3].spines['left'].set_visible(True)
ax[3].yaxis.set_major_locator(MultipleLocator(base=25))
ax[3].tick_params(axis='both', which='major', labelsize=25, width=2)
#plt.savefig('Supplementary1B.png', dpi=300, bbox_inches='tight')

###Figure S2
fig,ax = subplots(4,1, sharex = True,figsize=(19,24))
ax[0].plot(time_s, VPY_s[50],color="tab:blue",linewidth=1.5)
ax[0].set_title('PY axosomatic compartment', size=30, loc='left')
ax[0].set_ylabel('mV',size=30, labelpad=30)
#ax[0].set_xlim([15000,30000])
ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].spines['bottom'].set_visible(True)
ax[0].spines['left'].set_visible(True)
ax[0].set_ylim(-80, 50) 
ax[0].yaxis.set_major_locator(MultipleLocator(base=25))
ax[0].tick_params(axis='both', which='major', labelsize=25, width=2)
#
ax[1].plot(time_s, VPY_d[50],color="tab:blue",linewidth=1.5)
ax[1].set_title('PY dendritic compartment', size=30, loc='left')
ax[1].set_ylabel('mV',size=30, labelpad=30)
ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].spines['bottom'].set_visible(True)
ax[1].spines['left'].set_visible(True)
ax[1].set_ylim(-80, 50) 
ax[1].yaxis.set_major_locator(MultipleLocator(base=25))
ax[1].tick_params(axis='both', which='major', labelsize=25, width=2)
#
ax[2].plot(time_s, VIN[15],color="tab:green",linewidth=1.5)
ax[2].set_title('IN axosomatic compartment', size=30, loc='left')
ax[2].set_ylabel('mV',size=30, labelpad=30)
ax[2].spines['top'].set_visible(False)
ax[2].spines['right'].set_visible(False)
ax[2].spines['bottom'].set_visible(True)
ax[2].spines['left'].set_visible(True)
ax[2].set_ylim(-100, 50) 
ax[2].yaxis.set_major_locator(MultipleLocator(base=25))
ax[2].tick_params(axis='both', which='major', labelsize=25, width=2)
#
ax[3].plot(time_s, VIN_d[15],color="tab:green",linewidth=1.5)
ax[3].set_title('IN dendritic compartment', size=30, loc='left')
ax[3].set_ylabel('mV', size=30, labelpad=30)
ax[3].set_xlabel('second', size=30)
ax[3].tick_params(axis='both',labelbottom=True)
ax[3].spines['top'].set_visible(False)
ax[3].spines['right'].set_visible(False)
ax[3].spines['bottom'].set_visible(True)
ax[3].spines['left'].set_visible(True)
ax[3].set_ylim(-100, 50) 
ax[3].yaxis.set_major_locator(MultipleLocator(base=25))
ax[3].tick_params(axis='both', which='major', labelsize=25, width=2)
fig.tight_layout()
#plt.savefig('Supplementary2.png', dpi=300, bbox_inches='tight')