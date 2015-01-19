def is_palindro(number):
    num_str = str(number)
    if(num_str==num_str[::-1]):
        return True
    return False
#print is_palindro(123321)

#def biggest_3_digit():
begin = 999
end = 100
result = 0
for i in xrange(begin, end, -1):
    for j in xrange(begin, end, -1):
        tmp = i*j
        if tmp<=result:
            pass
        elif is_palindro(tmp):
            result = tmp
print result
            
        