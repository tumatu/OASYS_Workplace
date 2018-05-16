import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.interpolate import spline
with open('ray-tracing-wo-error.txt') as f1:
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


with open('hybrid-wo-error_range6um.txt') as f2:
    lines2 = f2.readlines()
    x2 = [line.split()[0] for line in lines2]
    y2 = [line.split()[1] for line in lines2]
    xx2=[float(i) for i in x2]
    yy2=[float(i) for i in y2]
    
    xxx2=xx2[0:-1:2]
    yyy2=yy2[0:-1:2]

print(sum([float(j) for j in y1]))
plt.plot(xxx1,yyy1,label='pure ray-tracing w/o error\nFWHM=0.15um')
plt.plot(xxx2,yyy2,label='hybrid w/o error\nFWHM=0.24um')
plt.legend(loc='upper right', shadow=True)
plt.ylabel('number of rays')
plt.xlabel(r'image position/$\mu$m')
plt.show()