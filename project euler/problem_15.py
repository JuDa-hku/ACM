import numpy as np
from collections import defaultdict
path_number_dict = defaultdict(int)

def calculate_path_number(start):
    path_number = 0
    down_right_dict = {}
    for i,j in [[1,0],[0,1]]:
        next = [start[0]+i, start[1]+j]
        if next[0]>20 or next[1]>20:
            down_right_dict[(i,j)] = 0
        elif next[0]==20 and next[1]==20:
            down_right_dict[(i,j)] = 1
        elif path_number_dict[tuple(next)]!=0:
            down_right_dict[(i,j)] = path_number_dict[tuple(next)]
        else:
            down_right_dict[(i,j)] = calculate_path_number(next)
            path_number_dict[tuple(next)] = down_right_dict[(i,j)]
    return sum(down_right_dict.values())


if __name__ == '__main__':
    print calculate_path_number([0,0])
        


    