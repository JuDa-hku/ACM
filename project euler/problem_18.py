from collections import defaultdict
file = open('./problem18_data')
np_array = []
while True:
    line = file.readline()
    if line == '\n':
        break
    line_number = line.split()
    line_number = [int(ele) for ele in line_number]
    np_array.append(line_number)
# define a dict to store the result
#test case
#np_array = [[3],[7,4],[2,4,6],[8,5,9,3]]
nrow = len(np_array)
max_i_j = defaultdict(int)
    
def calculate_max(x, y):
    if x == nrow-1:
        max_i_j[(x,y)] = np_array[x][y]
        return np_array[x][y]
    if max_i_j[(x,y)] != 0:
        return max_i_j[(x,y)]
    sub_left = calculate_max(x+1, y)
    sub_right = calculate_max(x+1, y+1)
    if sub_left>=sub_right:
        ##remember the result
        max_i_j[(x,y)] = sub_left + np_array[x][y]
    else:
        max_i_j[(x,y)] = sub_right + np_array[x][y]
    return max_i_j[(x,y)]

print calculate_max(0,0)