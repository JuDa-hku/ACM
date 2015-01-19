from collections import defaultdict
def calculate_next(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

max_number = int(1e6)
length_dict = defaultdict(int)
length_dict[1] = 1

def find_length(number):
    if length_dict[number]:
        return length_dict[number]
    else:
        next_number = calculate_next(number)
        tmp_length = find_length(next_number)
        length_dict[number] = tmp_length + 1
        return tmp_length+1

def find_longest():
    max_length = 0
    result = 0
    for i in xrange(3,max_number):
        if i%10000 == 0:
            print i
        tmp_length = find_length(i)
        if tmp_length > max_length:
            result = i
            max_length = tmp_length
    return result, max_length


if __name__ == '__main__':
    print find_longest()
    

