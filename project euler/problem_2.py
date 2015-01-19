import numpy as np
fib_list = np.zeros(1000)
fib_list[0]=1
fib_list[1]=2
def fib(n):
    if fib_list[n]!=0:
        return fib_list[n]
    else:
        fib_list[n] = fib(n-1)+fib(n-2)
        return fib_list[n]
result = 0
for i in xrange(500):
    tmp = fib(i)
    if tmp<4e6 and tmp%2==0:
        print tmp
        result += tmp
print result
    
    