# -*- coding: utf-8 -*-

from brian2 import *
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#Make sure you are working in the good directory
VPY_1=loadtxt('../../Data/PY_v_disconnected_02.txt')
VPY_2=loadtxt('../../Data/PY_v_disconnected_07.txt')
runtime=10
N=100
#see file "propagation_speeds.ods
gPYPY=[0.12,0.13,0.14,0.15,0.16]
speed_gPYPY=[140.058830623526,217.821159932437,257.209284928657,295.81064194477295,314.53219726645415]
std_gPYPY=[92.063885282553,118.561802997673,136.616568606629,84.49404861794169,123.67190859817416]

gPYIN=[0.02,0.03,0.04,0.05,0.06,0.07,0.08]
speed_gPYIN=[418.946549551418,337.888173205426,298.894122048514,316.857506963284,259.261546250333,243.948460767159,216.836170113911]
std_gPYIN=[143.770337191745,112.911177154143,129.743217746648,171.336013907523,103.000087226226,137.406408723269,114.57633281407]

#Top pannel
fig = plt.figure(figsize=(15, 12))
gs = gridspec.GridSpec(2, 2, width_ratios=[20, 0.5], height_ratios=[1, 1], wspace=0.05, hspace=0.3)
ax1 = plt.subplot(gs[0, 0])
im1 = ax1.imshow(VPY_1, aspect='auto', cmap='YlGnBu', vmax=-60, vmin=-75, 
                 extent=[0, runtime, N-1, 0], interpolation='bicubic')
ax1.set_title('Conductance PY-IN = 0.02$\mu$S', size=30, loc='left')
ax1.set_ylabel('Neuron index', size=30, labelpad=30)
ax1.set_xlim(0.1, 5.1)
ax1.yaxis.set_major_locator(MultipleLocator(base=25))
ax1.tick_params(axis='both', which='major', labelsize=25, width=2)
ax2 = plt.subplot(gs[1, 0])
im2 = ax2.imshow(VPY_2, aspect='auto', cmap='YlGnBu', vmax=-60, vmin=-75, 
                 extent=[0, runtime, N-1, 0], interpolation='bicubic')
ax2.set_title('Conductance PY-IN = 0.07$\mu$S', size=30, loc='left')
ax2.set_xlabel('Time (s)', size=30, labelpad=10)
ax2.set_ylabel('Neuron index', size=30, labelpad=30)
ax2.set_xlim(0.1, 5.1)
ax2.yaxis.set_major_locator(MultipleLocator(base=25))
ax2.tick_params(axis='both', which='major', labelsize=25, width=2)
cbar_ax = plt.subplot(gs[:, 1])
cbar = fig.colorbar(im1, cax=cbar_ax, orientation='vertical')
cbar.set_label('Membrane potential (mV)', size=30, labelpad=30)
cbar.ax.tick_params(labelsize=25, width=2)
#plt.savefig('Figure12cmap.png', dpi=300,bbox_inches='tight')
plt.show()

#Bottom pannel
plt.figure(figsize=(15, 6))
ax1 = plt.subplot(121)
ax1.errorbar(gPYPY, speed_gPYPY, std_gPYPY, marker='^', color="black")
ax1.set_xlabel('Conductance PY-PY $(μS)$', size=30, labelpad=20)
ax1.set_ylabel('Velocity (cell/s)', size=30, labelpad=20)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(True)
ax1.spines['left'].set_visible(True)
ax1.tick_params(axis='both', which='major', labelsize=30, width=2)
ax2 = plt.subplot(122)
ax2.errorbar(gPYIN, speed_gPYIN, std_gPYIN, marker='^', color="black")
ax2.set_xlabel('Conductance PY-IN $(μS)$', size=30, labelpad=20)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(True)
ax2.spines['left'].set_visible(True)
ax2.tick_params(axis='both', which='major', labelsize=30, width=2)
plt.savefig('Figure12velocity.png', dpi=300, bbox_inches='tight')
plt.show()