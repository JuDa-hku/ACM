dic = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 100:7}
def number_to_count(number):
    if (number<=20):
        return dic[number]
    if(20<number<100):
        tmp = dic[10*(number/10)]+dic[number%10]
        return tmp
    if(number>=100):
        tmp = dic[number/100]+dic[100]
        if(number%100!=0):
            ## need an "and"
            return tmp+number_to_count(number%100)+3
        else:
            return tmp
print number_to_count(342)
print number_to_count(115)
print number_to_count(4)
print number_to_count(14)
result = 0
for i in xrange(1,1000):
    result += number_to_count(i)
print result
    
    
    
