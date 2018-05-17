#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 10:48:34 2018

@author: hongjie
"""
#simple calculation for psd function of generated surface from OASYS
import matplotlib.pyplot as plt

#import sys
#sys.path.insert(0, '../DABAM_Analyse/code/')
#import dabam
import srxraylib.metrology.dabam

#import numpy
#import seaborn as sns
#import pandas as pd
#import json
#from io import StringIO

localFile='mirror_srw_psd_format'

do_plots = 1

dabam_entry=6
dm = dabam.dabam()
#dm.set_input_entryNumber(dabam_entry)
dm.set_input_localFileRoot(localFile)
dm.metadata={'FILE_FORMAT':2,'FILE_HEADER_LINES':1,'X1_FACTOR':1e-3,'Y1_FACTOR':1e-3,'SURFACE_SHAPE':"plane",'FACILITY':"none",'PLOT_TITLE_X1':"x(mm)",'PLOT_TITLE_Y1':"height",'CALC_SLOPE_RMS':None,'CALC_SLOPE_RMS_FACTOR':None}#,"ELLIPSE_DESIGN_P": 4.5,  "ELLIPSE_DESIGN_Q": 0.49914,  "ELLIPSE_DESIGN_THETA": 3.499e-3}
#dm.load()
dm._load_file_data()
dm._calc_detrended_profiles()
dm._calc_psd()
plt.plot(1e3*dm.y,1e9*dm.zHeightsUndetrended,label=dabam_entry)
plt.show()
#plt.plot(1e3*dm.y,1e9*dm.zHeights,label=dabam_entry)
#plt.show()
#
plt.plot(1e3*dm.y,1e6*dm.zSlopes,label=dabam_entry)
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
plt.axis([0,1e4,1e-33,1e-12])
#plt.title('psd_h profile for plane mirror')
plt.show()

print(dm.info_profiles())