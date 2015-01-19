import numpy as np
list_res =  str(np.math.factorial(100)).split()
print sum([int(a) for a in list_res[0]])
