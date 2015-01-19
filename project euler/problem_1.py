def multiple_3_5(upper):
    result = 0
    for i in xrange(upper):
        if i%3==0 or i%5==0:
            result += i
    return result
print multiple_3_5(1000)