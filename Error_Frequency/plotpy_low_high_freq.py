import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.interpolate import spline
import matplotlib.gridspec as gridspec
slope_error_file=['wav1opt_n10_small.dat','wav1opt_n10.dat','wav1opt_n50_small.dat','wav1opt_n50.dat','wav1opt_n50_big.dat']
ray_tracing_file=['ray-tracing-w-error-low-freq-0.15arcsec.txt','ray-tracing-w-error-low-freq-0.43arcsec.txt','ray-tracing-w-error-high-freq-0.19arc.txt','ray-tracing-w-error-high-freq-0.45arc.txt','ray-tracing-w-error-high-freq-1.28arc.txt']
hybrid_file=['hybrid-w-error-low-freq-0.15arcsec.txt','hybrid-w-error-low-freq-0.43arcsec.txt','hybrid-w-error-high-freq-0.19arcsec.txt','hybrid-w-error-high-freq-0.45arcsec.txt','hybrid-w-error-high-freq-1.28arcsec.txt']
title1=["low freq error(n=[0,10],0.15arcsec)","high freq error(n=[0,10],0.43arcsec)","high freq error(n=[11,50],0.19arcsec)","high freq error(n=[11,50],0.45arcsec)","high freq error(n=[11,50],1.28arcsec)"]

file_no=4

def slope_error_plot(filename):
    with open(filename) as f1:
        error1 = f1.readlines()
        x_point_number=(len(error1))-2 #number of points at x direction
        y_point_number=(len(error1[1].split()))
    
        xmin=error1[2].split()[0]
        xmax=error1[-1].split()[0]
    
        ynew = (error1[1].split())
        ynew1=[float(i) for i in ynew]
        ymin=ynew1[0]
        ymax=ynew1[-1]
    
        ele = (error1[4].split())
        ele1=[float(i) for i in ele]
    #print(len(ele1))
        x_position =ele1[0]
        yaxis=np.linspace(ymin, ymax, num=200)
        slope_error=[i*1e6 for i in ele1[1::]]#nm unit
    return (yaxis,slope_error)
(yaxis1,slope_error1)=slope_error_plot(slope_error_file[file_no])

(xxx_noerr,yyy1_noerr)=image_plot('hybrid-wo-error_range6um.txt')
intensity_norm_factor=max(yyy1_noerr)

with open(ray_tracing_file[file_no]) as f1:
    lines1 = f1.readlines()
    x1 = [line.split()[0] for line in lines1]
    y1 = [line.split()[1] for line in lines1]
    xx1=[float(i) for i in x1]
    yy1=[float(i) for i in y1]
    
    xxx1=xx1[0:-1:2]
    yyy1=yy1[0:-1:2]
    #plt.plot(xxx1,yyy1)
    
    x1_a = np.array(xx1)
    y1_a = np.array(yy1)
    xnew = np.linspace(x1_a.min(),x1_a.max(),300) 
    power_smooth = spline(x1_a,y1_a,xnew)

    #plt.plot(xnew,power_smooth)
yyy1 = [(j/intensity_norm_factor) for j in yyy1]

with open(hybrid_file[file_no]) as f2:
    lines2 = f2.readlines()
    x2 = [line.split()[0] for line in lines2]
    y2 = [line.split()[1] for line in lines2]
    xx2=[float(i) for i in x2]
    yy2=[float(i) for i in y2]
    
    xxx2=xx2[0:-1:2]
    yyy2=yy2[0:-1:2]
    
yyy2 = [(j/intensity_norm_factor) for j in yyy2]

gs = gridspec.GridSpec(2, 1,height_ratios=[1,2])

ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])

axis_label_error1='mirror position/mm'
axis_label_error2='error/nm'

p1=plt.subplot(ax1)
p1.set_title(title1[file_no])
p1p=plt.plot(yaxis1,slope_error1,'r')#,label='hybrid-w-error(0.45arcsec)')
plt.xlabel(axis_label_error1)
plt.ylabel(axis_label_error2)
#plt.axis([-20,20,-15,15])

p2=plt.subplot(ax2)
print(sum(yy2[0:-1:2]))
plt.plot(xxx1,yyy1,label='pure ray-tracing w error')
plt.plot(xxx2,yyy2,label='hybrid w error')
plt.legend(loc='upper right', shadow=True)
plt.title('ray-tracing_vs_hybrid_w_error')
plt.ylabel('internsity')
plt.xlabel(r'image position/$\mu$m')
plt.axis([-3,3,0,1])
plt.subplots_adjust(hspace=0.6)
plt.show()