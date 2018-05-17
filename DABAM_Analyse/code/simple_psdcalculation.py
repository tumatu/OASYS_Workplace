#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:48:34 2018

@author: hongjie
"""
#simple calculation for psd function of generated surface from OASYS


import matplotlib.pyplot as plt
import dabam
#import numpy
#import seaborn as sns
#import pandas as pd
#import json
#from io import StringIO
do_plots = 1

dabam_entry=15
dm = dabam.dabam()
dm.set_input_entryNumber(dabam_entry)
dm.load()
#plt.plot(1e3*dm.y,1e9*dm.zHeightsUndetrended,label=dabam_entry)
#plt.show()
#plt.plot(1e3*dm.y,1e9*dm.zHeights,label=dabam_entry)
#plt.show()
#
#plt.plot(1e3*dm.y,1e6*dm.zSlopes,label=dabam_entry)
#plt.show()

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
plt.axis([0,1e4,1e-33,1e-12])
#plt.title('psd_h profile for plane mirror')
plt.show()