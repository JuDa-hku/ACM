import numpy as np
from prime_list import get_prime_list

primeList = get_prime_list(1000)
squareList = np.array(range(1, 100))**2

"""
Guess the number should be small than 1e5, and check. The number should be composite number.
"""
MAX = int(1e5)

def check_one_number(number):
    global primeList, squareList
    if number in primeList:
        return True
    for j in primeList:
        if j>number:
            break
        if (number-j)/2.0 in squareList:
            return True
    return False

for i in xrange(3, MAX, 2):
    if not check_one_number(i):
        print i
        
    



