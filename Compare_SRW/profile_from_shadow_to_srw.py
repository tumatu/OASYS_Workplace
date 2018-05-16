#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 17:09:12 2018

@author: hongjie
"""
import matplotlib.pyplot as plt
import numpy as np

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
    
#(x_srw,y_srw,z_srw)=get_srw_format_profile('mirror_2d.dat')
#data=[x_srw,y_srw,z_srw]
#plt.plot(x_srw,z_srw[0])
#plt.show()

(x_shadow,y_shadow,z_shadow)=get_shadow_format_profile('mirror_srw-hybrid-ray.dat')
data=[x_shadow,y_shadow,z_shadow]
plt.plot(x_shadow,z_shadow[1])
plt.show()

writesrwfile='mirror_srw2D.dat'

write_srw_format_profile(data,writesrwfile)

(x_srw,y_srw,z_srw)=get_srw_format_profile('mirror_srw2D.dat')
#data=[x_srw,y_srw,z_srw]
plt.plot(x_srw,z_srw[0])
plt.show()