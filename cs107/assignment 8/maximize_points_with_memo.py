import copy
from collections import defaultdict
def key(currRow, currCol, stateList):
    return str(currRow)+'-'+str(currCol)+'-'+str(stateList)
    
def calculateSubBoard(dataBoard, currRow, currCol, stateList, cache):
    if cache.has_key(key(currRow, currCol, stateList)):
        return cache[key(currRow,currCol, stateList)]
    if currCol>=len(dataBoard):
        currCol = 0
        currRow += 1
    if currRow==len(dataBoard):
        return 0
    stateListWithout = copy.copy(stateList)
    stateListWithout.pop(0)
    stateListWithout.append(True)
    scoreWithout = calculateSubBoard(dataBoard, currRow, currCol+1, stateListWithout, cache)
    bestScore = scoreWithout
    if(stateList[0]):
        stateListWith = copy.copy(stateList)
        stateListWith.pop(0)
        stateListWith[-1] = False
        if currCol == 0:
            stateListWith[0] = False
        if currCol>0 and currCol<len(dataBoard)-1:
            stateListWith[0] = False
            stateListWith[-2] = False
        if currCol==len(dataBoard)-1:
            stateListWith[-2] = False
        stateListWith.append(currCol==(len(dataBoard)-1))
        scoreWith = dataBoard[currRow][currCol] + calculateSubBoard(dataBoard, currRow, currCol+1, stateListWith, cache)
        if scoreWith>bestScore:
            bestScore = scoreWith
    cache[key(currRow, currCol, stateList)] = bestScore
    return bestScore

def calculateMax(dataBoard):
    cache = defaultdict(int)
    dataState = map(lambda x: True, xrange(0,len(dataBoard)+1))
    return calculateSubBoard(dataBoard,0,0,dataState, cache)






data = [[71,24,95,56,54],[85,50,74,94,28],[92,96,23,71,10],[23,61,31,30,46],[64,33,32,95,89]]

print calculateMax(data)

data = [[78,78,11,55,20,11],[98,54,81,43,39,97],[12,15,79,99,58,10],[13,79,83,65,34,17],
        [85,59,61,12,58,97],[40,63,97,85,66,90]]
print calculateMax(data)

data = [[1,2,3,10],[4,5,6,11],[7,8,9,12],[13,14,15,16]]
print calculateMax(data)

data = [[33,49,78,79,30,16,34,88,54,39,26],
        [80,21,32,71,89,63,39,52,90,14,89],
        [49,66,33,19,45,61,31,29,84,98,58],
        [36,53,35,33,88,90,19,23,76,23,76],
        [77,27,25,42,70,36,35,91,17,79,43],
        [33,85,33,59,47,46,63,75,98,96,55],
        [75,88,10,57,85,71,34,10,59,84,45],
        [29,34,43,46,75,28,47,63,48,16,19],
        [62,57,91,85,89,70,80,30,19,38,14],
        [61,35,36,20,38,18,89,64,63,88,83],
        [45,46,89,53,83,59,48,45,87,98,21],
        ]
print calculateMax(data)



        
        
        
