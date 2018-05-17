#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 17:09:12 2018

@author: hongjie
"""
import matplotlib.pyplot as plt
import numpy as np
import srxraylib.metrology.dabam

def get_shadow_format_profile(filename):
    with open(filename) as f1:
        lines1 = f1.readlines()
        y_n=int(lines1[0].split()[0])
        x_n=int(lines1[0].split()[1])
#        print(x_n,y_n)
        x=lines1[1].split()
        y=[0 for i in range(y_n)]
        z=[[] for k in range(y_n)]
        for i in range(2,2+y_n):
            y[i-2]=lines1[i].split()[0]
            z[i-2]=lines1[i].split()[1::]
        
        xx=[float(i) for i in x]
        yy=[float(i) for i in y]
        zz=[[float(j) for j in i] for i in z]
    if (x_n!=len(xx))or(y_n!=len(y)):
        print('error in format of shadow profile')
        return False
    #xxx=xx[::1]#srw widget plot does not double sample
    #yyy=yy[::1]#srw widget plot does not double sample
    return(xx,yy,zz)#,ys)

def get_srw_format_profile(filename):
    with open(filename) as f1:
        lines1 = f1.readlines()
        x_n=len(lines1[1::])
        y_n=len(lines1[0].split())-1
        #print(x_n,y_n)
        x=[line.split()[0] for line in lines1[1::]]
        y=lines1[0].split()[1::]
        z=[[] for k in range(y_n)]
        for k in range(y_n):
            z[k]=[line.split()[k+1] for line in lines1[1::]]
        xx=[float(i) for i in x]
        yy=[float(i) for i in y]
        zz=[[float(j) for j in i] for i in z]
    if (x_n!=len(xx))or(y_n!=len(y)):
        print('error in format of shadow profile')
        return False
#    xxx=xx[::1]#srw widget plot does not double sample
#    yyy=yy[::1]#srw widget plot does not double sample
    return(xx,yy,zz)#,ys)
    
def write_srw_format_profile(data,filename):
    [xx,yy,zz]=data
    write_srwfile = open(filename, 'w')
    write_srwfile.write("0\t")
    for k in range(len(yy)-1):
        write_srwfile.write("%s\t" %yy[k])
    write_srwfile.write("%s\n"%yy[-1])
    for i in range(len(xx)):
        write_srwfile.write("%s\t" %xx[i])
        for j in range(len(yy)-1):
            write_srwfile.write("%s\t" %zz[j][i])
        write_srwfile.write("%s\n"%zz[-1][i])
        
    #return(xx,yy,zz)#,ys)
def write_psd_analysis_format_profile(data,filename):
    [xx,yy,zz]=data
    write_srwfile = open(filename, 'w')
    write_srwfile.write("x(mm)\theight(mm)\n")
    for i in range(len(xx)):
        write_srwfile.write("%s\t" %xx[i])
        #for j in range(len(yy)-1):
        write_srwfile.write("%s\n" %zz[0][i])
#        write_srwfile.write("%s\n"%zz[-1][i])
        
#(x_srw,y_srw,z_srw)=get_srw_format_profile('mirror_2d.dat')
#data=[x_srw,y_srw,z_srw]
#plt.plot(x_srw,z_srw[0])
#plt.show()
shadowfile='mirror.dat'
(x_shadow,y_shadow,z_shadow)=get_shadow_format_profile(shadowfile)#('mirror_srw-hybrid-ray.dat')
data=[x_shadow,y_shadow,z_shadow]
plt.plot(x_shadow,z_shadow[1])
plt.show()


writesrwfile='mirror_srw2D.dat'
#writepsdfile='mirror_srw_psd_format.dat'
write_srw_format_profile(data,writesrwfile)
#write_psd_analysis_format_profile(data,writepsdfile)

(x_srw,y_srw,z_srw)=get_srw_format_profile(writesrwfile)
#data=[x_srw,y_srw,z_srw]
plt.plot(x_srw,z_srw[0])
plt.show()
 

####################PSD calculation of new generated profile#########################
dm = dabam.dabam()
dm.load_external_profile([(1e-3)*i for i in x_srw],[(1e-3)*i for i in z_srw[0]],type='heights')
plt.plot(1e3*dm.y,1e9*dm.zHeightsUndetrended)
plt.show()
plt.plot(1e3*dm.y,1e9*dm.zHeights)
plt.show()

plt.loglog(dm.f,dm.psdHeights,label=dabam_entry)
y = dm.f**(dm.powerlaw["hgt_pendent"])*10**dm.powerlaw["hgt_shift"]
i0 = dm.powerlaw["index_from"]
i1 = dm.powerlaw["index_to"]
plt.loglog(dm.f,y)
plt.loglog(dm.f[i0:i1],y[i0:i1])
beta = -dm.powerlaw["hgt_pendent"]
plt.title("PSD of heights profile (beta=%.2f,Df=%.2f)"%(beta,(5-beta)/2))
plt.xlabel("f [m^-1]")
plt.ylabel("PSD [m^3]")
#plt.legend()
#    print(plt.axis())
#plt.axis([0,1e4,1e-33,1e-12])
#plt.title('psd_h profile for plane mirror')
plt.show()