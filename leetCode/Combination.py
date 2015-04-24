import copy
def combination(nums,combi, C, Res):
    if len(combi) == len(nums):
        Res.add(combi)
        return 
    for num in nums:
        if num in C:
            continue
        elif num not in C:
            print C
            C.add(num)
            combination(nums, combi+str(num), C, Res)
            C.remove(num)
            
            

nums = range(5)
combi=''
C = set()
Res = set()
combination(nums, combi, C, Res)

        
        