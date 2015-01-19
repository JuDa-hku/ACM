import prime_list as pl
from numpy import abs
import collections
prime_list = pl.get_prime_list(10000)
max_prime = max(prime_list)
min_prime = -max_prime
minus_prime_list = [-num for num in prime_list]
prime_list.extend(minus_prime_list)
prime_dict = collections.defaultdict(int)
for num in prime_list:
    prime_dict[num] = 1

def max_length(a, b):
    result = 0
    for n in xrange(b):
        tmp = n**2+a*n+b
        assert(tmp < max_prime)
        assert(tmp > min_prime)
        if prime_dict[tmp]==1 :
            result += 1
        else:
            return result
    return result

print max_length(1, 41)
print max_length(-79, 1601)

result = 0
product_max = 0
for a in xrange(-999, 1000):
    for b in xrange(-999, 1000):
        tmp = max_length(a, b)
        if tmp>result:
            result = tmp
            a_fina = a
            b_fina = b
            product_max = abs(a*b)
        elif tmp == result and abs(a*b)>product_max:
            result = tmp
            a_fina = a
            b_fina = b
            product_max = abs(a*b)
