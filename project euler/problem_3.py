def largest_prime(n):
    result = 1
    for i in xrange(2,n+1):
        if n%i==0:
            result = max(result, i, largest_prime(n/i))
            return result

print largest_prime(600851475143)
            