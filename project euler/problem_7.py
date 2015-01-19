MAX = int(1e8)
def check_prime(num, prime_list):
    for number in prime_list:
        if num%number==0:
            return False
    return True

def st_prime(num):
    prime_list = [2]
    poistion=1
    for i in xrange(3, MAX, 2):
        flag = check_prime(i, prime_list)
        if flag:
            flag = False
            prime_list.append(i)
            poistion+=1
            if poistion==num:
                return i
        else:
            pass
    print MAX, "is not big enough"



print st_prime(10001)

