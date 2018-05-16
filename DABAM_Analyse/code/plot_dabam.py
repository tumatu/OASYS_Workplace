
#from matplotlib import pylab as plt
import matplotlib.pyplot as plt
import dabam
import numpy
import seaborn as sns
import pandas as pd
import json
from io import StringIO
do_plots = 1


#create DABAM objects to load experimental and two simulated profiles

#dm = [dabam.dabam(),dabam.dabam(),dabam.dabam()]

#
# load input from DABAM
#
dm = dabam.dabam()
#[dm[i-1].set_input_entryNumber(i) for i in range(1,57)]
#[dm[i-1].load() for i in range(1,57)]
#for i in range(1,57):
#plane_entry=[i for i in range(1,57) if dm[i-1].metadata['SURFACE_SHAPE']=="plane"]
#self.metadata['SURFACE_SHAPE']
plane_entry=[]
cylindrical_entry=[]
elliptical_entry=[]
spherical_entry=[]
toroidal_entry=[]
surface_set=set()
#df=pd.DataFrame()
#for i in range(1,57):
#    dm.set_input_entryNumber(i)
#    fileaddress='../data/'+(dm.file_metadata())
#    print(fileaddress)
#    metafile=open(fileaddress, mode='r') 
#    data = json.load(metafile)
#    #print((data))
#    if i==1:
#        df=pd.DataFrame.from_dict(data,orient='index')
#        #df.transpose()
#    else:
#        dft=pd.DataFrame.from_dict(data,orient='index')
#        #dft.transpose()
#        df.join(dft,lsuffix='_caller', rsuffix='_other')
#    #df = pd.DataFrame(data)
#    #data = pd.read_json(metafile,orient='index')
##df.transpose()
#print(df)

print(dabam.dabam_summary(nmax=56,latex=2))
#dm.set_input_entryNumber(1)
#dm.load()
dm.set_input_entryNumber(15)
dm.set_input_silent(False)
dm.load()

for i in range(1,57):
    dm.set_input_entryNumber(i)
    dm.set_input_silent(True)
    dm._load_file_metadata()
    #print(dm.info_profiles())
    surface_set.add(dm.metadata['SURFACE_SHAPE'])
    if dm.metadata['SURFACE_SHAPE'].lower()=="plane":
        plane_entry.append(i)
    elif dm.metadata['SURFACE_SHAPE'].lower()=="cylindrical":
        cylindrical_entry.append(i)
    elif "elliptical" in dm.metadata['SURFACE_SHAPE'].lower():
        elliptical_entry.append(i)
    elif dm.metadata['SURFACE_SHAPE'].lower()=="spherical":
        spherical_entry.append(i)
    elif "toroid" in dm.metadata['SURFACE_SHAPE'].lower():
        toroidal_entry.append(i)
print(len(plane_entry)+len(cylindrical_entry)+len(elliptical_entry)+len(spherical_entry)+len(toroidal_entry))
        
print(surface_set)
print('plane_entry:',plane_entry)
print('cylindrical_entry:',cylindrical_entry)
print('elliptical_entry:',elliptical_entry)
print('spherical_entry:',spherical_entry)
print('toroidal_entry:',toroidal_entry)

#dm = dabam.dabam()
########################################################################
plane_entry_sub=[2,10,11,12,23,24,25]
#figure0
print('Undetrended height profile for plane mirror')
for dabam_entry in plane_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    plt.plot(1e3*dm.y,1e9*dm.zHeightsUndetrended,label=dabam_entry)
plt.xlabel("coordinate along the mirror/mm")
plt.ylabel("heights profile Z/nm")
plt.legend()
plt.title('Undetrended height profile for plane mirror')
plt.show()
#figure1
print('detrended height profile for plane mirror')
for dabam_entry in plane_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    plt.plot(1e3*dm.y,1e9*dm.zHeights,label=dabam_entry)
plt.xlabel("coordinate along the mirror/mm")
plt.ylabel("heights profile Z/nm")
plt.legend()
plt.title('detrended height profile for plane mirror')
plt.show()

print('Undetrended slope profile for plane mirror')
#figure1.5
for dabam_entry in plane_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    plt.plot(1e3*dm.y,1e6*dm.zSlopesUndetrended,label=dabam_entry)
    #print('size',dm.y.size)
plt.xlabel("coordinate along the mirror/mm")
plt.ylabel("slope/$\mu$rad")
plt.legend()
plt.title('Undetrended slope profile for plane mirror')
plt.show()

print('detrended slope profile for plane mirror')
#figure2
for dabam_entry in plane_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    plt.plot(1e3*dm.y,1e6*dm.zSlopes,label=dabam_entry)
    #print('size',dm.y.size)
plt.xlabel("coordinate along the mirror/mm")
plt.ylabel("slope/$\mu$rad")
plt.legend()
plt.title('detrended slope profile for plane mirror')
plt.show()
########################################################################
non_elliptical_entry_sub=[3,5,13,14,16,17,18]
print('Undetrended height profile for non-elliptical mirror(spherical, cylindrical, toroidal)')
#figure3
for dabam_entry in non_elliptical_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    plt.plot(1e3*dm.y,1e9*dm.zHeightsUndetrended,label=dabam_entry)
    #print('size',dm.y.size)
plt.xlabel("coordinate along the mirror/mm")
plt.ylabel("heights profile Z/nm")
plt.legend()
plt.title('Undetrended height profile for non-elliptical mirror')
plt.show()

print('detrended height profile for non-elliptical mirror(spherical, cylindrical, toroidal)')
#figure3.5
for dabam_entry in non_elliptical_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    plt.plot(1e3*dm.y,1e9*dm.zHeights,label=dabam_entry)
    #print('size',dm.y.size)
plt.xlabel("coordinate along the mirror/mm")
plt.ylabel("heights profile Z/nm")
plt.legend()
plt.title('detrended height profile for non-elliptical mirror')
plt.show()

print('Undetrended slope profile for non-elliptical mirror(spherical, cylindrical, toroidal)')
#figure4
for dabam_entry in non_elliptical_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    plt.plot(1e3*dm.y,1e6*dm.zSlopesUndetrended,label=dabam_entry)
    #print('size',dm.y.size)
plt.xlabel("coordinate along the mirror/mm")
plt.ylabel("slope/$\mu$rad")
plt.legend()
plt.title('Undetrended slope profile for non-elliptical mirror')
plt.show()

print('detrended slope profile for non-elliptical mirror(spherical, cylindrical, toroidal)')
#figure4.5
for dabam_entry in non_elliptical_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    plt.plot(1e3*dm.y,1e6*dm.zSlopes,label=dabam_entry)
    #print('size',dm.y.size)
plt.xlabel("coordinate along the mirror/mm")
plt.ylabel("slope/$\mu$rad")
plt.legend()
plt.title('detrended slope profile for non-elliptical mirror')
plt.show()
########################################################################
elliptical_entry_sub=[4,6,19,20,21]
print('Undetrended height profile for elliptical mirror')
#figure5
for dabam_entry in elliptical_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    plt.plot(1e3*dm.y,1e9*dm.zHeightsUndetrended,label=dabam_entry)
    #print('size',dm.y.size)
plt.xlabel("coordinate along the mirror/mm")
plt.ylabel("heights profile Z/nm")
plt.legend()
plt.title('Undetrended height profile for elliptical mirror')
plt.show()

print('detrended height profile for elliptical mirror')
#figure5.5
for dabam_entry in elliptical_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    plt.plot(1e3*dm.y,1e9*dm.zHeights,label=dabam_entry)
    #print('size',dm.y.size)
plt.xlabel("coordinate along the mirror/mm")
plt.ylabel("heights profile Z/nm")
plt.legend()
plt.title('detrended height profile for elliptical mirror')
plt.show()

print('Undetrended slope profile for elliptical mirror')
#figure6
for dabam_entry in elliptical_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    plt.plot(1e3*dm.y,1e6*dm.zSlopesUndetrended,label=dabam_entry)
    #print('size',dm.y.size)
plt.xlabel("coordinate along the mirror/mm")
plt.ylabel("slope/$\mu$rad")
plt.legend()
plt.title('Undetrended slope profile for elliptical mirror')
plt.show()

print('detrended slope profile for elliptical mirror')
#figure6.5
for dabam_entry in elliptical_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    plt.plot(1e3*dm.y,1e6*dm.zSlopes,label=dabam_entry)
    #print('size',dm.y.size)
plt.xlabel("coordinate along the mirror/mm")
plt.ylabel("slope/$\mu$rad")
plt.legend()
plt.title('detrended slope profile for elliptical mirror')
plt.show()
########################################################################
print('psd_h profile for plane mirror')
#figure7
for dabam_entry in plane_entry_sub:
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    self=dm
    plt.loglog(self.f,self.psdHeights,label=dabam_entry)
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
#    print(plt.axis())
    plt.axis([0,1e4,1e-36,1e-14])
    plt.title('psd_h profile for plane mirror')
plt.show()


print('csd_h profile for plane mirror')
#figure8
for dabam_entry in plane_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    self=dm
    plt.semilogx(self.f,self.csd_heights(),label=dabam_entry)
    plt.title("Cumulative Spectral Density of heights profile")
    plt.xlabel("f [m^-1]")
    plt.ylabel("csd_h")
    #print('size',dm.y.size)
plt.legend()
plt.title('csd_h profile for plane mirror')
plt.show()

print('psd_h profile for non-elliptical mirror(spherical, cylindrical, toroidal)')
#figure9
for dabam_entry in non_elliptical_entry_sub:
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    self=dm
    plt.loglog(self.f,self.psdHeights,label=dabam_entry)
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
#    print(plt.axis())
    plt.axis([0,1e4,1e-36,1e-14])
    plt.title('psd_h profile for non-elliptical mirror')
plt.show()


print('csd_h profile for non-elliptical mirror(spherical, cylindrical, toroidal)')
#figure10
for dabam_entry in non_elliptical_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    self=dm
    plt.semilogx(self.f,self.csd_heights(),label=dabam_entry)
    plt.title("Cumulative Spectral Density of heights profile")
    plt.xlabel("f [m^-1]")
    plt.ylabel("csd_h")
    #print('size',dm.y.size)
plt.legend()
plt.title('csd_h profile for non-elliptical mirror')
plt.show()


print('psd_h profile for elliptical mirror')
#figure9
for dabam_entry in elliptical_entry_sub:
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    self=dm
    plt.loglog(self.f,self.psdHeights,label=dabam_entry)
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
#    print(plt.axis())
    plt.axis([0,1e4,1e-36,1e-14])
    plt.title('psd_h profile for elliptical mirror')
plt.show()


print('csd_h profile for elliptical mirror')
#figure10
for dabam_entry in elliptical_entry_sub:
    #print(dabam_entry)
    #print(dm.inputs["entryNumber"])
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    self=dm
    plt.semilogx(self.f,self.csd_heights(),label=dabam_entry)
    plt.title("Cumulative Spectral Density of heights profile")
    plt.xlabel("f [m^-1]")
    plt.ylabel("csd_h")
    #print('size',dm.y.size)
plt.legend()
plt.title('csd_h profile for elliptical mirror')
plt.show()
#*******************************************
#get the sampling distance
for i in range(1,57):
    dm.set_input_entryNumber(i)
    dm.set_input_silent(True)
    dm.load()
    a = dm.rawdata
    #print(a)
    a[:,0] = a[:,0]*dm.metadata['X1_FACTOR']
    a[:,1] = a[:,1]*dm.metadata['Y1_FACTOR']
    a_h = a[:,0]
    a_v = a[:,1]
#    print(i,a_h[1]-a_h[0])

##################################################for latex

powerlawl=[]
txt=""
txt_cor="Entry & shape & Length[mm] & N & skh & kuh & ch & betah & shifth & sks & kus & slp_err [urad]  & hgt_err [um]\n"
print(len(plane_entry)+len(cylindrical_entry)+len(elliptical_entry)+len(spherical_entry)+len(toroidal_entry))
beta_scatter=[]
shift_scatter=[]
for dabam_entry in range(1,57):
    if dabam_entry in plane_entry:
        shape_no=0
    elif dabam_entry in elliptical_entry:
        shape_no=2
    elif dabam_entry in (cylindrical_entry+spherical_entry+toroidal_entry):
        shape_no=1
#    print(shape_no)
    dm.set_input_entryNumber(dabam_entry)
    dm.load()
    self=dm
    plt.loglog(self.f,self.psdHeights,label=dabam_entry)
    y = self.f**(self.powerlaw["hgt_pendent"])*10**self.powerlaw["hgt_shift"]
    i0 = self.powerlaw["index_from"]
    i1 = self.powerlaw["index_to"]
#    plt.loglog(self.f,y)
#    plt.loglog(self.f[i0:i1],y[i0:i1])
    beta = -self.powerlaw["hgt_pendent"]
    shift=-self.powerlaw["hgt_shift"]
    beta_scatter.append(beta)
    shift_scatter.append(shift)
    plt.title("PSD of heights profile")
    # (beta=%.2f,Df=%.2f)"%(beta,(5-beta)/2))
    plt.xlabel("f [m^-1]")
    plt.ylabel("PSD [m^3]")
    powerlawl.append([self.powerlaw["hgt_pendent"],self.powerlaw["hgt_shift"]])
    latex=('%d & %s & %d & %d & %.2f & %.2f & %d & %.2f & %.2f & %.2f & %.2f\\\\'%(   \
                self.get_input_value("entryNumber"),   \
                self.metadata['SURFACE_SHAPE'], \
                int(1e3*(self.y[-1]-self.y[0])),   \
                self.y.size, \
                self.momentsHeights[2], \
                self.momentsHeights[3],\
                ((dabam.autocorrelationfunction(self.y,self.zHeights))[2])*1e3, \
                -self.powerlaw["hgt_pendent"], \
                self.powerlaw["hgt_shift"], \
                self.momentsSlopes[2], \
                self.momentsSlopes[3],\
                ))
    forcorrelation=('%d & %d & %d & %d & %.2f & %.2f & %d & %.2f & %.2f & %.2f & %.2f & %.2f & %.2f'%(   \
                self.get_input_value("entryNumber"),   \
                shape_no,  \
                #self.metadata['SURFACE_SHAPE'], \
                int(1e3*(self.y[-1]-self.y[0])),   \
                self.y.size, \
                self.momentsHeights[2], \
                self.momentsHeights[3],\
                ((dabam.autocorrelationfunction(self.y,self.zHeights))[2])*1e3, \
                -self.powerlaw["hgt_pendent"], \
                self.powerlaw["hgt_shift"], \
                self.momentsSlopes[2], \
                self.momentsSlopes[3],\
                1e6*self.zSlopes.std(ddof=1),      \
                1e9*self.zHeights.std(ddof=1),   
                ))
    txt+=latex+"\n"
    txt_cor+=forcorrelation+'\n'
plt.show()
#print(powerlawl,txt)
#print(type(dm.zSlopes))
##################################################
for i in range(1,57):
    dm.set_input_entryNumber(i)
    dm.load()
    autocorr1=(dabam.autocorrelationfunction(dm.y,dm.zHeights)[0])
    autocorr2=(dabam.autocorrelationfunction(dm.y,dm.zHeights)[1])
    plt.plot(autocorr1[:-1]/(dm.y[-1]-dm.y[0]),autocorr2)
plt.xlabel("normalized mirror length")
plt.ylabel("autocorrelation")
plt.title("autocorrelation on normalized mirror length for height profile")
plt.show()
##################################################
print(txt_cor.split('\n')[1:3])
txt_cor_del_outlier=[]
txt_cor_del_outlier=txt_cor.split('\n')[0:22]+txt_cor.split('\n')[23:57]
txt_cor_del_outlier_str='\n'.join(txt_cor_del_outlier)
TESTDATA = StringIO(txt_cor_del_outlier_str)
df = pd.read_csv(TESTDATA, sep="&")
#df.head()
#df=df[:4][2:]
def plot_correlation_map( df ):
    corr = df.corr()
    _ , ax = plt.subplots( figsize =( 12 , 10 ) )
    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )
    _ = sns.heatmap(
        corr, 
        cmap = cmap,
        square=True, 
        cbar_kws={ 'shrink' : .9 }, 
        ax=ax, 
        annot = True, 
        annot_kws = { 'fontsize' : 12 }
    )
plot_correlation_map(df)
##################################################
plt.scatter(beta_scatter,shift_scatter)
plt.xlabel("abs($\\beta$)")
plt.ylabel("abs(shift)")
plt.title("scatter plot for beta and shift in power law")
plt.show()
##################################################
zSlopes_scatter=[]
zHeights_scatter=[]
for i in range(1,57):
    dm.set_input_entryNumber(i)
    dm.load()
    zSlopes_scatter.append(1e6*dm.zSlopes.std(ddof=1))
    zHeights_scatter.append(1e9*dm.zHeights.std(ddof=1))
plt.scatter(zSlopes_scatter,zHeights_scatter)
plt.xlabel("zSlopes_scatter")
plt.ylabel("zHeights_scatter")
plt.title("scatter plot for slope and height")
plt.show()
##################################################
#    plt.legend()
#    plt.title('psd_h profile for non-elliptical mirror')
#plt.show()
#dabam_entry = 12

#dm = dabam.dabam()
#dm.set_input_entryNumber(dabam_entry)
#dm.load()
#dm.set_input_plot("heights")
#dm.plot()
#dm.set_input_plot("slopes")
#dm.plot()
#if do_plots:
#sns.set_style()
#sns.distplot(dm.zHeights)
#plt.plot(dm.zHeights)
#plt.plot(dm.zHeightsUndetrended)
#Plotting options are: heights slopes psd_h psd_s csd_h csd_s acf_h acf_s
#
# define inputs for fractal and Gaussian simulated profiles
#
