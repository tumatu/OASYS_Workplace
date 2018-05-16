import matplotlib.pyplot as plt
import numpy as np

ray_tracing_source_file=['ray-tracing-on-slit-200um-as-source-in-srw.txt']

ray_tracing_on_slit_file=['ray-tracing-on-slit-5um.txt','ray-tracing-on-slit-10um.txt','ray-tracing-on-slit-50um.txt','ray-tracing-on-slit-100um.txt']

ray_tracing_slit_smallsource_file=['ray-tracing-slit-5um_smaller-source.txt','ray-tracing-slit-10um_smaller-source.txt','ray-tracing-slit-50um_smaller-source.txt','ray-tracing-slit-100um_smaller-source.txt']

ray_tracing_mirror_smallsource_file=['ray-tracing-mirror-5um_smaller-source.txt','ray-tracing-mirror-10um_smaller-source.txt','ray-tracing-mirror-50um_smaller-source.txt','ray-tracing-mirror-100um_smaller-source.txt']

ray_tracing_mirror_with_error1_smallsource_file=['ray-tracing-mirror-5um_smaller-source-with-error1.txt','ray-tracing-mirror-10um_smaller-source-with-error1.txt','ray-tracing-mirror-50um_smaller-source-with-error1.txt','ray-tracing-mirror-100um_smaller-source-with-error1.txt']

legenddict_RAY=[r"5$\mu$m slit ray-tracing",r"10$\mu$m slit ray-tracing",r"50$\mu$m slit ray-tracing",r"100$\mu$m slit ray-tracing"]

axis_config_on_slit=[[-100,100],[0,0.01],[x*0.001 for x in range(0,11)]]
axis_config_slit=axis_config_on_slit
axis_config_mirror=[[-0.8,0.8],[0,1],[x*0.1 for x in range(0,11)]]
axis_config_mirror_error=[[-0.8,0.8],[0,2.2],[x*0.2 for x in range(0,11)]]

axis_config=[axis_config_on_slit,axis_config_slit,axis_config_mirror,axis_config_mirror_error]

ray_tracing_title=['shadow(ray-tracing) on-slit calculation','shadow(ray-tracing) slit calculation','shadow(ray-tracing) slit & mirror calculation','shadow(ray-tracing) slit & mirror(error) calculation']
sampling_step=2
#to use the sampling setting as configured
#2 for data from shadow histgrom widget because of double sampling
#1 for data from 1D wavefront from SRW(&worfy) widgets
#you can also set it larger to undersample the data
simulation_index=3
#0-on slit; 
#1-slit diffraction; 
#2-focusing by mirror; 
#3-focusing by mirror with error
file_gather=[ray_tracing_on_slit_file,ray_tracing_slit_smallsource_file,ray_tracing_mirror_smallsource_file,ray_tracing_mirror_with_error1_smallsource_file]


def image_plot(filename):
    with open(filename) as f1:
        lines1 = f1.readlines()
        x = [line.split()[0] for line in lines1]
        y = [line.split()[1] for line in lines1]
        xx=[float(i) for i in x]
        yy=[float(i) for i in y]
    
    xxx=xx[0:-1:sampling_step]
    yyy=yy[0:-1:sampling_step]
    return(xxx,yyy,sum([round(i) for i in yyy]))
(x_source,y_source,source_sum)=image_plot(ray_tracing_source_file[0])
print(source_sum)
for i in range(4):
    (xxx_noerr,yyy1_noerr,yyysum)=image_plot(file_gather[simulation_index][i])
    delta_xxxlist=[xxx_noerr[i+1]-xxx_noerr[i] for i in range(0,len(xxx_noerr)-1)]
    delta_xxx=round(sum(delta_xxxlist)/len(delta_xxxlist),4)
    print('delta_xxx :',delta_xxx)
    plt.plot(xxx_noerr,[j/source_sum/delta_xxx for j in yyy1_noerr],label=legenddict_RAY[i]+'/'+str(round(yyysum/source_sum,4)))
plt.legend(loc='upper left', shadow=True)
axes = plt.gca()
axes.set_xlim(axis_config[simulation_index][0])
axes.set_ylim(axis_config[simulation_index][1])
plt.yticks(axis_config[simulation_index][2])
plt.xlabel(r"horizontal coordinate/$\mu$m")
plt.ylabel("sampled ray ratio/sampling step")
plt.title(ray_tracing_title[simulation_index]+'('+str(delta_xxx)+r'$\mu$m step)')
plt.show()