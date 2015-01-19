from collections import defaultdict

def cal_dig(n):
    reminder_dict = defaultdict(int)
    reminder_count = 1
    reminder_start = 10%n
    while True:
        if reminder_start == 0:
            break
            return 0
        if(reminder_dict[reminder_start]==0):
            reminder_dict[reminder_start] = reminder_count
            reminder_count += 1
            reminder_start = reminder_start*10%n
        if(reminder_dict[reminder_start]!=0):
            length = reminder_count-reminder_dict[reminder_start]
            return length

print cal_dig(3)
print cal_dig(7)
print cal_dig(6)
        
length = 0        
for number in xrange(1000,1,-1):
    if number<length:
        break
    tmp = cal_dig(number)
    if (tmp>length):
        length = tmp
        result = number
print "the number %d with length:%d" %(result, length)









