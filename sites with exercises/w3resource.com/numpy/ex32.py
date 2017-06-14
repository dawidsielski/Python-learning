import numpy as np
a = np.arange(1,10,.5)

print(a)
np.savetxt('file.out', a, delimiter=',')