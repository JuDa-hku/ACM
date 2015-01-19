from prime_list import get_prime_list
primeList = get_prime_list(100)

result = {}
def list_all_factor(number, result):
    for i in primeList:
        if number%i==0:
            result[i]=result.get(i, 0) + 1
            list_all_factor(number/i, result)
            break
        else:
            pass
    return result

    
print (list_all_factor(28,result))

def total_div(dict_type):
    result = 1
    for i in dict_type.keys():
        result *= (dict_type[i]+1)
    return result

print total_div(list_all_factor(30, {}))
        

def triangular_number(n):
    return (1+n)*n/2

for i in xrange(1, 100000):
    tmp = triangular_number(i)
    if total_div(list_all_factor(tmp, {}))>500:
        print tmp
        break
    else:
        pass
    