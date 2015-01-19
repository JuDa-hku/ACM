"""
check all numbers which can be expressed as permutation of '0123456789' and
maintain a count for it.
"""
# list_9 = [str(i) for i in xrange(1,10)]
# list_10 = [str(i) for i in xrange(10)]

# def check_number(number):
#     number_list = [char for char in str(number)]
#     number_list.sort()
#     if len(number_list) == 9:
#         return number_list == list_9
#     if len(number_list) == 10:
#         return number_lis == list_10
#     return False

# min_test = 123456789
# max_test = 9876543210
# count = 0
# end_count = int(1e6)
# for number in xrange(min_test, max_test+1):
#     if check_number(number):
#         count +=1
#     if count%1000 == 0:
#         print "check progress %d", count
#     if count == end_count:
#         print number
#         break



def permu(string, result=[]):
    result = []
    if len(string) == 1:
        result.append(string)
        return result
    else:
        for i in xrange(len(string)):
            if i == 0:
                tmp = permu(string[1:])
            if i == len(string)-1:
                tmp = permu(string[:i])
            else:
                tmp = permu(string[0:i]+string[i+1:])
            for ele in tmp:
                result.append(string[i]+ele)
    return result

print permu('1')            
print permu('123456')            
        