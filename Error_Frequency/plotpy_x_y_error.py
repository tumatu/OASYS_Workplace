import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import math
import numpy as np
def image_plot(filename):
    with open(filename) as f1:
        lines1 = f1.readlines()
        x = [line.split()[0] for line in lines1]
        y = [line.split()[1] for line in lines1]
        xx=[float(i) for i in x]
        yy=[float(i) for i in y]
    
    xxx=xx[0:-1:2]
    yyy=yy[0:-1:2]
    return(xxx,yyy)
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
    
        ele = (error1[5].split())
        ele1=[float(i) for i in ele]
    #print(len(ele1))
        x_position =ele1[0]
        yaxis=np.linspace(ymin, ymax, num=200)
        slope_error=[i*1e6 for i in ele1[1::]]#nm unit
    return (yaxis,slope_error)
def slope_error_plot_getx(filename):
    with open(filename) as f1:
        error1 = f1.readlines()
        x_point_number=(len(error1))-2 #number of points at x direction
        y_point_number=(len(error1[1].split()))
        
        #print(error1[2])
        
        xmin=float(error1[2].split()[0])
        xmax=float(error1[-1].split()[0])
        print(xmin,xmax)
        elex=[float(error1[i].split()[1]) for i in range(2,len(error1))]
        #print(len(elex))
        ynew = (error1[1].split())
        ynew1=[float(i) for i in ynew]
        ymin=ynew1[0]
        ymax=ynew1[-1]
    
        ele = (error1[5].split())
        ele1=[float(i) for i in ele]
        #print(len(ele1))
        x_position =ele1[0]
        xaxis=[float(i) for i in error1[1].split()]
        #print(len(xaxis))
        yaxis=np.linspace(ymin, ymax, num=200)
        slope_error=[i*1e6 for i in ele1[1::]]#nm unit

        slope_error_x=[i*1e6 for i in elex]#nm unit
    return(xaxis,slope_error_x)

(yaxis1,slope_error1)=slope_error_plot('waviness_c1_0.15arcsec.dat')#to get the y axis
(xxx1,yyy1)=image_plot('hybrid-wo-error_range6um.txt')
intensity_norm_factor=max(yyy1)
print(intensity_norm_factor)
yyy1 = [(j/intensity_norm_factor) for j in yyy1]


(xaxis2,slope_error2)=slope_error_plot_getx('shape-x-err-0.44arcsec.dat')
(xxx2,yyy2)=image_plot('hybrid-w-error-x_side-0.44arcsec.txt')
yyy2 = [(j/intensity_norm_factor) for j in yyy2]

(xaxis3,slope_error3)=slope_error_plot_getx('shape-x-err-1arcsec.dat')
(xxx3,yyy3)=image_plot('hybrid-w-error-x_side-1.10arcsec.txt')
yyy3 = [(j/intensity_norm_factor) for j in yyy3]

(xaxis4,slope_error4)=slope_error_plot_getx('shape-x-err.dat')
(xxx4,yyy4)=image_plot('hybrid-w-error-x_side-2.20arcsec.txt')
yyy4 = [(j/intensity_norm_factor) for j in yyy4]

(yaxis5,slope_error5)=slope_error_plot('shape-y-err-0.41arcsec.dat')
(xxx5,yyy5)=image_plot('hybrid-w-error-y_side-0.41arcsec.txt')
yyy5 = [(j/intensity_norm_factor) for j in yyy5]
print(len(yyy5))

(yaxis6,slope_error6)=slope_error_plot('shape-y-err-1arcsec.dat')
(xxx6,yyy6)=image_plot('hybrid-w-error-y_side-1.03arcsec.txt')
yyy6 = [(j/intensity_norm_factor) for j in yyy6]

(yaxis7,slope_error7)=slope_error_plot('shape-y-err.dat')
(xxx7,yyy7)=image_plot('hybrid-w-error-y_side-2.06arcsec.txt')
yyy7 = [(j/intensity_norm_factor) for j in yyy7]
#plt.plot(xxx9,yyy9)

print(sum(yyy1))#number of rays
axis_label_error1='mirror position/mm'
axis_label_error2='error/nm'
axis_label_inten1='internsity'
axis_label_inten2=r'image position/$\mu$m'

gs = gridspec.GridSpec(2, 7,height_ratios=[1,1])

ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])
ax4 = plt.subplot(gs[3])
ax5 = plt.subplot(gs[4])
ax6 = plt.subplot(gs[5])
ax7 = plt.subplot(gs[6])
ax8 = plt.subplot(gs[7])
ax9 = plt.subplot(gs[8])
ax10 = plt.subplot(gs[9])
ax11 = plt.subplot(gs[10])
ax12 = plt.subplot(gs[11])
ax13 = plt.subplot(gs[12])
ax14 = plt.subplot(gs[13])

p1=plt.subplot(ax1)
p1.set_title("w/o error")
p1p=plt.plot(yaxis1,[0]*len(yaxis1),'r')#,label='hybrid-w-error(c5_0.1arcsec)')
plt.xlabel(axis_label_error1)
plt.ylabel(axis_label_error2)
plt.axis([-20,20,-60,60])

p2=plt.subplot(ax2,sharey=p3)
p2.set_title("x_0.44arcsec")
p2p=plt.plot(xaxis2,slope_error2,'g')#,label='c5_0.3arcsec-error')
plt.xlabel(axis_label_error1)
#plt.ylabel(axis_label_error2)
plt.axis([-20,20,-60,60])

p3=plt.subplot(ax3)
p3.set_title("x_1.10arcsec")
p3p=plt.plot(xaxis3,slope_error3,'b')#,label='c5_0.5arcsec-error')
plt.xlabel(axis_label_error1)
#plt.ylabel(axis_label_error2)
plt.axis([-20,20,-60,60])

p4=plt.subplot(ax4)
p4.set_title("x_2.20arcsec")
p4p=plt.plot(xaxis4,slope_error4,'c')#,label='hybrid-w-error(c5_0.15arcsec)')
plt.xlabel(axis_label_error1)
#plt.ylabel(axis_label_error2)
plt.axis([-20,20,-60,60])

p5=plt.subplot(ax5,sharey=p4)
p5.set_title("y_0.41arcsec")
p5p=plt.plot(yaxis5,slope_error5,'m')#,label='hybrid-w-error(c5_0.15arcsec)')
plt.xlabel(axis_label_error1)
#plt.ylabel(axis_label_error2)
plt.axis([-20,20,-60,60])

p6=plt.subplot(ax6,sharey=p4)
p6.set_title("y_1.03arcsec")
p6p=plt.plot(yaxis6,slope_error6,'y')#,label='hybrid-w-error(c5_0.15arcsec)')
plt.xlabel(axis_label_error1)
#plt.ylabel(axis_label_error2)
plt.axis([-20,20,-60,60])

p7=plt.subplot(ax7)
p7.set_title("y_2.06arcsec")
p7p=plt.plot(yaxis7,slope_error7,'k')#,label='c5_0.5arcsec-error')
plt.xlabel(axis_label_error1)
#plt.ylabel(axis_label_error2)
#plt.axis([-6,6,0,1])
plt.axis([-20,20,-60,60])

p8=plt.subplot(ax8)
#p4.set_title("hybrid-w-error(c5_0.15arcsec)")
p8p=plt.plot(xxx1,yyy1,'r')#,label='hybrid-w-error(c5_0.15arcsec)')
plt.ylabel(axis_label_inten1)
plt.xlabel(axis_label_inten2)
plt.axis([-6,6,0,1])

p9=plt.subplot(ax9,sharey=p4)
#p4.set_title("hybrid-w-error(c5_0.15arcsec)")
p9p=plt.plot(xxx2,yyy2,'g')#,label='hybrid-w-error(c5_0.15arcsec)')
#plt.ylabel(axis_label_inten1)
plt.xlabel(axis_label_inten2)
plt.axis([-6,6,0,1])

p10=plt.subplot(ax10,sharey=p4)
#p4.set_title("hybrid-w-error(c5_0.15arcsec)")
p10p=plt.plot(xxx3,yyy3,'b')#,label='hybrid-w-error(c5_0.15arcsec)')
#plt.ylabel(axis_label_inten1)
plt.xlabel(axis_label_inten2)
plt.axis([-6,6,0,1])

p11=plt.subplot(ax11,sharey=p4)
#p4.set_title("hybrid-w-error(c5_0.15arcsec)")
p11p=plt.plot(xxx4,yyy4,'c')#,label='hybrid-w-error(c5_0.15arcsec)')
#plt.ylabel(axis_label_inten1)
plt.xlabel(axis_label_inten2)
plt.axis([-6,6,0,1])

p12=plt.subplot(ax12,sharey=p4)
#p4.set_title("hybrid-w-error(c5_0.15arcsec)")
p12p=plt.plot(xxx5,yyy5,'m')#,label='hybrid-w-error(c5_0.15arcsec)')
#plt.ylabel(axis_label_inten1)
plt.xlabel(axis_label_inten2)
plt.axis([-6,6,0,1])

p13=plt.subplot(ax13,sharey=p4)
#p4.set_title("hybrid-w-error(c5_0.15arcsec)")
p13p=plt.plot(xxx6,yyy6,'y')#,label='hybrid-w-error(c5_0.15arcsec)')
#plt.ylabel(axis_label_inten1)
plt.xlabel(axis_label_inten2)
plt.axis([-6,6,0,1])

p14=plt.subplot(ax14,sharey=p4)
#p4.set_title("hybrid-w-error(c5_0.15arcsec)")
p14p=plt.plot(xxx7,yyy7,'k')#,label='hybrid-w-error(c5_0.15arcsec)')
#plt.ylabel(axis_label_inten1)
plt.xlabel(axis_label_inten2)
plt.axis([-6,6,0,1])
#plt.tight_layout()
plt.subplots_adjust(hspace=0.4,wspace=0.6)
plt.show()