def gcd(num1, num2):
    if num1<num2:
        tmp = num2
        num2 = num1
        num1 = tmp
    if num1%num2==0:
        return num2
    if num2 == 1:
        return 1
    else:
        return gcd(num2, num1%num2)

def gcm(num1, num2):
    return (num1*num2)/gcd(num1, num2)
print gcd(15, 10)
print gcm(15, 10)
    
def smallest_multiple(largest):
    result = largest
    for num in xrange(largest, 0, -1):
        if result%num == 0:
            pass
        else:
            result = gcm(result, num)
    return result
print smallest_multiple(10)
print smallest_multiple(20)