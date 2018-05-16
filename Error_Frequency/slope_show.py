import matplotlib.pyplot as plt
import math
import numpy as np
with open('waviness_c5_0.5arcsec.dat') as f1:
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
    slope_error=ele1[1::]
plt.plot(np.linspace(ymin, ymax, num=200),ele1[1::])
plt.show()