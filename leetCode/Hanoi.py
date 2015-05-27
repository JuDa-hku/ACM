def Hanoi(nums, start, through, end, res):
    if len(nums) == 1:
        res.append(str(nums[0])+'from'+str(start)+'to'+str(end))
        return
    tmp = nums[-1]
    Hanoi(nums[:-1], start, end, through, res)
    res.append(str(tmp)+'from'+str(start)+'to'+str(end))
    Hanoi(nums[:-1], through, start, end, res)

nums = [1,2,3]
res = []
start, through, end = 1,2,3
Hanoi(nums, start, through, end, res)


