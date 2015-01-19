from string import uppercase
f = open("problem_22_names.txt")
flag = True
tmp = f.readline()
f.close()
name_list = tmp.split(',')
name_list = [name.strip('"') for name in name_list]
name_list.sort()
assert(name_list[937]=='COLIN')
alph_to_score = {alp:score+1 for score ,alp in list(enumerate(uppercase))}

def calculate(name):
    result = 0
    for cha in name:
        result += alph_to_score[cha]
    return result

assert(calculate(name_list[937]) == 53)    
result = 0
for pos, name in enumerate(name_list):
    result += (pos+1)*calculate(name)


    