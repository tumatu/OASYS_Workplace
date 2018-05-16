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


(yaxis1,slope_error1)=slope_error_plot('waviness_c1_0.15arcsec.dat')#to get the y axis
(xxx1,yyy1)=image_plot('hybrid-wo-error_range6um.txt')
intensity_norm_factor=max(yyy1)
print(intensity_norm_factor)
yyy1 = [(j/intensity_norm_factor) for j in yyy1]

(yaxis2,slope_error2)=slope_error_plot('waviness_c1_0.15arcsec.dat')
(xxx2,yyy2)=image_plot('hybrid-w-error(c1_0.15arcsec)_range6um.txt')
yyy2 = [(j/intensity_norm_factor) for j in yyy2]

(yaxis3,slope_error3)=slope_error_plot('waviness_c3_0.35arcsec.dat')
(xxx3,yyy3)=image_plot('hybrid-w-error(c3_0.35arcsec)_range6um.txt')
yyy3 = [(j/intensity_norm_factor) for j in yyy3]

(yaxis4,slope_error4)=slope_error_plot('waviness_c5_0.55arcsec.dat')
(xxx4,yyy4)=image_plot('hybrid-w-error(c5_0.55arcsec)_range6um.txt')
yyy4 = [(j/intensity_norm_factor) for j in yyy4]

#plt.plot(xxx9,yyy9)

print(sum(yyy1))#number of rays
axis_label_error1='mirror position/mm'
axis_label_error2='error/nm'
axis_label_inten1='internsity'
axis_label_inten2=r'image position($\mu$m)'
axis_range_err = [-20,20,-5,5]
axis_range_inten = [-3,3,0,1]


gs = gridspec.GridSpec(4, 2,height_ratios=[1,2,1,2])

ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])
ax4 = plt.subplot(gs[3])
ax5 = plt.subplot(gs[4])
ax6 = plt.subplot(gs[5])
ax7 = plt.subplot(gs[6])
ax8 = plt.subplot(gs[7])

p1=plt.subplot(ax1)
p1.set_title("hybrid-w/o-error")
p1p=plt.plot(yaxis1,[0]*len(yaxis1),'r',label='hybrid-w/o-error')
plt.xlabel(axis_label_error1)
plt.ylabel(axis_label_error2)
plt.axis(axis_range_err)
#plt.axis([-20,20,-5,5])
p2=plt.subplot(ax2,sharey=p1)
p2.set_title("hybrid-w-error(c1_0.15arcsec)")
p2p=plt.plot(yaxis2,slope_error2,'g',label='c1_0.15arcsec-error')
plt.xlabel(axis_label_error1)
plt.ylabel(axis_label_error2)
plt.axis(axis_range_err)

p3=plt.subplot(ax3)
#p3.set_title("hybrid-w/o-error")
p3p=plt.plot(xxx1,yyy1,'r',label='hybrid-w/o-error')
plt.ylabel(axis_label_inten1)
plt.xlabel(axis_label_inten2)
plt.axis(axis_range_inten)

p4=plt.subplot(ax4,sharey=p3)
#p4.set_title("hybrid-w-error(c1_0.15arcsec)")
p4p=plt.plot(xxx2,yyy2,'g',label='hybrid-w-error(c1_0.15arcsec)')
plt.ylabel(axis_label_inten1)
plt.xlabel(axis_label_inten2)
plt.axis(axis_range_inten)

p5=plt.subplot(ax5,sharey=p1)
p5.set_title("hybrid-w-error(c3_0.35arcsec)")
p5p=plt.plot(yaxis3,slope_error3,'b',label='c3_0.35arcsec-error')
plt.xlabel(axis_label_error1)
plt.ylabel(axis_label_error2)
plt.axis(axis_range_err)

p6=plt.subplot(ax6,sharey=p1)
p6.set_title("hybrid-w-error(c5_0.55arcsec)")
p6p=plt.plot(yaxis4,slope_error4,'y',label='c5_0.55arcsec-error')
plt.xlabel(axis_label_error1)
plt.ylabel(axis_label_error2)
plt.axis(axis_range_err)

p7=plt.subplot(ax7,sharey=p3)
#p7.set_title("hybrid-w-error(c3_0.35arcsec)")
p7p=plt.plot(xxx3,yyy3,'b',label='hybrid-w-error(c3_0.3arcsec)')
plt.ylabel(axis_label_inten1)
plt.xlabel(axis_label_inten2)
plt.axis(axis_range_inten)

p8=plt.subplot(ax8,sharey=p3)
#p8.set_title("hybrid-w-error(c5_0.55arcsec)")
p8p=plt.plot(xxx4,yyy4,'y',label='hybrid-w-error(c5_0.5arcsec)')
#plt.legend(loc='upper right', shadow=True)
plt.ylabel(axis_label_inten1)
plt.xlabel(axis_label_inten2)
plt.axis(axis_range_inten)
#plt.tight_layout()
plt.subplots_adjust(hspace=0.8,wspace=0.5)
plt.show()