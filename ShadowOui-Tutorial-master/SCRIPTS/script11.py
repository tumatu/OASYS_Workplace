import Shadow
import numpy as np

print(dir(in_object_1))
x = in_object_1._beam.getshonecol(1)
z = in_object_1._beam.getshonecol(3)
f = in_object_1._beam.getshonecol(10)

print(x)

bad1 = np.where(x <= 0)
bad2 = np.where(z <= 0)

f[bad1] = -100
f[bad2] = -1100


in_object_1._beam.rays[:,9] = f

out_object = in_object_1



