import sys
sys.path.append('../code/')
import dabam
import matplotlib.pyplot as plt
import numpy as np
import math

dm = dabam.dabam()
#*******************************************
localFileRoot='Fraunhofer-IWS'
dm.set_input_localFileRoot(localFileRoot)
dm.load()
#a=dm.rawdata.copy()
#x=[ele[0] for ele in a]
#y=[ele[1] for ele in a]
#plt.plot(x,y)
##plt.axis([-50,50,0,500])
#print(1e6*dm.zSlopesUndetrended)
#*******************************************
plt.plot(1e3*dm.y,1e6*dm.zSlopes,label=localFileRoot)
plt.xlabel("coordinate along the mirror/mm")
plt.ylabel("slope/$\mu$rad")
plt.legend()
plt.title('detrended slope profile for elliptical mirror')
plt.axis([-50,50,-50,50])
plt.show()
print(dm.zSlopes.std(ddof=1))#standard deviation(ddof=1-->defree od freedom=n-1)
print(np.sqrt(np.mean(np.square(dm.zSlopes))))#rms
#*******************************************
self=dm
print(self.f.size)
plt.loglog(self.f,self.psdHeights,'.b-',label=localFileRoot)
y = self.f**(self.powerlaw["hgt_pendent"])*10**self.powerlaw["hgt_shift"]
i0 = self.powerlaw["index_from"]
i1 = self.powerlaw["index_to"]
#    plt.loglog(self.f,y)
#    plt.loglog(self.f[i0:i1],y[i0:i1])
beta = -self.powerlaw["hgt_pendent"]
plt.title("PSD of heights profile (beta=%.2f,Df=%.2f)"%(beta,(5-beta)/2))
plt.xlabel("f [m^-1]")
plt.ylabel("PSD [m^3]")
plt.legend()
plt.show()
#*******************************************
#dm.set_input_entryNumber(3)
#dm.set_input_nbinS(500)
#dm.load()
#plt.plot(1e3*dm.y,1e9*dm.zSlopes)

#plt.plot(dm.histoSlopes['x'],dm.histoSlopes['y1'])
#print(dm.histoSlopes['x'].size)

##################################################

#plt.plot(a_h,a_v)
#sy = a_h
#sz1 = numpy.gradient(a_v,(sy[1]-sy[0]))*648000/math.pi
#sz1 = [math.atan(i)*648000/math.pi for i in numpy.gradient(a_v,(sy[1]-sy[0]))]
#print(sz1)