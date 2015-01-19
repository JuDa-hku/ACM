


def get_prime_list(largest_number):
    prime_list = range(0,largest_number)
    bool_list = [True]*len(prime_list)
    for i in prime_list[2:]:
        if bool_list[i]:
            for j in xrange(2, int(largest_number/i)+1):
                if i*j<len(prime_list):
                    bool_list[i*j] = False
    return [prime_list, bool_list]

num =100
num = 2e6
prime_list, bool_list = get_prime_list(int(num))

index = [i for i in xrange(int(num)) if bool_list[i]]
sum(index[2:])