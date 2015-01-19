file = open('problem13_data', 'r')
sum = 0
result = dict()
for line in file:
    line = line.rstrip('\n')
    number = int(line[0:12])
    sum += number

# from pandas import DataFrame
# import numpy as np
# dff = DataFrame({'A': np.arange(8), 'B': list('aabbbbcc'), 'C':('ddddaaaa')})

# dd= dff.groupby('B').A.agg([np.sum, np.mean])