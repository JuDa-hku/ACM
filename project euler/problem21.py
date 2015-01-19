from prime_list import get_prime_list
from collections import defaultdict
import numpy as np
prime_list = get_prime_list(2000)
dict_result = defaultdict(int)
#dict_result[1] = 1


def proper_divisor(number):
    if number == 1:
        return None
    for prime in prime_list:
        if prime==number:
            dict_result[prime] +=1
            return None
        if number%prime==0:
            dict_result[prime] += 1
            print number
            proper_divisor(number/prime)
            return None
            
def proper_divisor_calculate(number):
    result = 1
    for i in xrange(2,number):
        if number%i == 0:
            result += i
    return result

def check_amicable(number1):
    number2 = proper_divisor_calculate(number1)
    if proper_divisor_calculate(number2) == number1 and number2!=number1:
        print number1, number2
        return True
    return False
result = 0
for number in xrange(3, 10000):
    if check_amicable(number):
        result += number
    
