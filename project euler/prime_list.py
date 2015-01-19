MAX = int(1e6)


def check_prime(i, prime_list):
    if i<max(prime_list):
        print "The number", i, "you want to check be should in the prime list"
    for j in prime_list:
        if i%j == 0:
            return False
    return True

def get_prime_list(number_of_prime):
    global MAX
    index = 1
    prime_list = [2]
    for i in xrange(3, MAX, 2):
        if check_prime(i, prime_list):
            prime_list.append(i)
            index +=1
            if index == number_of_prime:
                return prime_list
    if index<number_of_prime:
        MAX *= 10
        return get_prime_list(number_of_prime)
#print get_prime_list(1000)


#prime_list = get_prime_list(60000)