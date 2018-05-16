import matplotlib.pyplot as plt
import numpy as np

srw_source_file=['srw-source-200um-50000npts.txt']

srw_on_slit_file=['srw-on-slit-5um.txt','srw-on-slit-10um.txt','srw-on-slit-50um.txt','srw-on-slit-100um.txt']

srw_slit_file=['srw-slit-5um.txt','srw-slit-10um.txt','srw-slit-50um.txt','srw-slit-100um.txt']

srw_mirror_calib_file=['srw-mirror-5um_calib.txt','srw-mirror-10um_calib.txt','srw-mirror-50um_calib.txt','srw-mirror-100um_calib.txt']

srw_mirror_focus_at_source_file=['srw-mirror-5um_first-focus-at-source.txt','srw-mirror-10um_first-focus-at-source.txt','srw-mirror-50um_first-focus-at-source.txt','srw-mirror-100um_first-focus-at-source.txt']

srw_mirror_with_error1_file=['srw-mirror-5um_with-error1.txt','srw-mirror-10um_with-error1.txt','srw-mirror-50um_with-error1.txt','srw-mirror-100um_with-error1.txt']

legenddict_srw=[r"5$\mu$m slit srw",r"10$\mu$m slit srw",r"50$\mu$m slit srw",r"100$\mu$m slit srw"]

axis_config_on_slit=[[-100,100],[0,0.01],[x*0.001 for x in range(0,11)]]
axis_config_slit=axis_config_on_slit
axis_config_mirror=[[-0.8,0.8],[0,1],[x*0.1 for x in range(0,11)]]
axis_config_mirror_error=[[-0.8,0.8],[0,1],[x*0.1 for x in range(0,11)]]

axis_config=[axis_config_on_slit,axis_config_slit,axis_config_mirror,axis_config_mirror_error]

srw_title=['srw on-slit calculation','srw slit calculation(0.1$\mu$m step)','srw slit & mirror calculation(auto sample step)','srw slit & mirror(error) calculation(auto sample step)']

sampling_step=1
#to use the sampling setting as configured
#2 for data from shadow histgrom widget because of double sampling
#1 for data from 1D wavefront from SRW(&worfy) widgets
#you can also set it larger to undersample the data
simulation_index=3
#0-on slit; 
#1-slit diffraction; 
#2-focusing by mirror; 
#3-focusing by mirror with error
file_gather=[srw_on_slit_file,srw_slit_file,srw_mirror_calib_file,srw_mirror_with_error1_file]

def image_plot(filename):
    with open(filename) as f1:
        lines1 = f1.readlines()
        x = [line.split()[0] for line in lines1]
        y = [line.split()[1] for line in lines1]
        xx=[float(i) for i in x]
        yy=[float(i) for i in y]
    xxx=xx[::sampling_step]#srw widget plot does not double sample
    yyy=yy[::sampling_step]#srw widget plot does not double sample
    return(xxx,yyy)#,ys)

(x_source,y_source)=image_plot(srw_source_file[0])
#print(round(y_source[0]))
print("npts in source :",len(x_source))
delta_sourcelist=[x_source[i+1]-x_source[i] for i in range(0,len(x_source)-1)]
delta_source=round(sum(delta_sourcelist)/len(delta_sourcelist),4)
print("delta_source =",round(sum(delta_sourcelist)/len(delta_sourcelist),4),"micrometer")
source_sum=(sum(y_source))
print('source_sum :',source_sum)
for i in range(4):
    (xxx_noerr,yyy1_noerr)=image_plot(file_gather[simulation_index][i])
    delta_xxxlist=[xxx_noerr[i+1]-xxx_noerr[i] for i in range(0,len(xxx_noerr)-1)]
    delta_xxx=round(sum(delta_xxxlist)/len(delta_xxxlist),4)
    print('delta_xxx :',delta_xxx)
    print(sum(yyy1_noerr))
    plt.plot(xxx_noerr,[i/source_sum/delta_source for i in yyy1_noerr],label=legenddict_srw[i]+"/"+str(round(sum(yyy1_noerr)/source_sum*delta_xxx/delta_source,4)))#since sampling at continuous curve
plt.legend(loc='upper left', shadow=True)
axes = plt.gca()
axes.set_xlim(axis_config[simulation_index][0])
axes.set_ylim(axis_config[simulation_index][1])
plt.yticks(axis_config[simulation_index][2])
plt.xlabel(r"horizontal coordinate/$\mu$m")
plt.ylabel("sampled energy ratio/sampling step")
#plt.title(srw_title[0]+'('+str(delta_xxx)+r'$\mu$m step)')
plt.title(srw_title[simulation_index])
plt.show()