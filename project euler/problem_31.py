money_list = [1, 2, 5, 10, 20, 50, 100]
total = 200
result = {}
number = 0
def change(total, money_list):
    global result
    global number
    max_value = max(money_list)
    max_number = total/max_value
    if(max_value==1 or total==0):
        number += 1
        result[max_value] = max_number
        print result
        result = {}
        return
    else:
        for i in xrange(max_number+1):
            result[max_value] = i
            change(total-i*max_value, money_list[0:len(money_list)-1])
    return number
print change(total, money_list)