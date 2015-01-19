keyList = []
import numpy as np
for a in xrange(2, 101):
    for b in xrange(2, 101):
        keyList.append([a,b])
def factor_comp(k1):
    for a in xrange(2, 11):
        for b in xrange(2, 8):
            if a**b>k1:
                pass
            if a**b == k1:
                return [a, b]
    return [k1, 1]
result = []
for k1, k2 in keyList:
    [fac1, fac2] = factor_comp(k1)
    if [fac1, fac2*k2] not in result:
        result.append([fac1, fac2*k2])
print len(result)

    