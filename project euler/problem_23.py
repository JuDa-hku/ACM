import number_class as nc
abundant_number_list = []
for i in xrange(12, 28124):
    if i<nc.nb(i).div_sum():
        abundant_number_list.append(i)
#print abundant_number_list

def check_consit_abundant(number):
    for i in abundant_number_list:
        if i>=number:
            break
        elif (number-i) in abundant_number_list:
            return True
    return False

#print check_consit_abundant(24)
#print check_consit_abundant(25)    
consit_abundant_list = []
for i in xrange(24, 28124):
    if i%1000 == 0:
        print "check %d now", i
    if check_consit_abundant(i):
        consit_abundant_list.append(i)
print consit_abundant_list

sum(xrange(28124))-sum(consit_abundant_list)