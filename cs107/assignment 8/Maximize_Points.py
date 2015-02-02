from collections import defaultdict
from copy import deepcopy
import numpy as np
import math
##-1 means not consider, 0 means no pebble, 1 means one pebble

def updateState(beforeState, pebblePosition, dim, state):
    afterState = deepcopy(beforeState)
    if state==0:
        afterState[pebblePosition] = 0
        return afterState
    #put pebble case
    row = pebblePosition/dim
    col = pebblePosition%dim
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            newRow = row + i
            newCol = col + j
            tagRow = newRow>=0 and newRow<dim
            tagCol = newCol>=0 and newCol<dim
            if (tagRow and tagCol):
                afterState[newRow*dim+newCol] = 0
    afterState[pebblePosition] = 1
    return afterState
#beforeState = [-1]*25
#afterState = updateState(beforeState, 0, 5, 1)

def checkTranVali(beforeState, afterState):
    for i,j in zip(beforeState, afterState):
        if(i==1 and j==0):
            return False
        if(i==0 and j==1):
            return False
    return True
# beforeState = [-1]*25
# afterState = updateState(beforeState, 0, 5, 1)
# afterState1 = updateState(beforeState, 1, 5, 1)
# print checkTranVali(afterState, afterState1)
# print checkTranVali(beforeState, afterState)

def checkStatVali(stateList):
    for position in xrange(len(stateList)):
        if(not checkOneVali(position, stateList)):
            return False
    return True
        
def checkOneVali(position, stateList):
    assert(position<len(stateList))
    if(stateList[position]==0 or stateList[position]==-1):
        return True
    dim = int(math.sqrt(len(stateList)))
    row = position/dim
    col = position%dim
    assert(stateList[position]==1)
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            newRow = row + i
            newCol = col + j
            tagRow = newRow>=0 and newRow<dim
            tagCol = newCol>=0 and newCol<dim
            tagNotThis = (i!=0) or (j!=0)
            if (tagRow and tagCol and tagNotThis):
                if(stateList[newRow*dim+newCol]==1):
                    return False
    return True
#print checkStatVali(afterState)
print checkOneVali(2,[1,0,1,0,0,0,0,0,0])


                
def checkFull(stateList):
    for state in stateList:
        if (state==-1):
            return False
    return True


def calculateScore(data, dataState):
    for i in dataState:
        assert(i!=-1)
    newData = np.array(data).reshape(len(data)**2)
    return sum(np.array(dataState)*newData)
    

def calculateMax(data, dataState, position, cache):
    bestScore = 0
    dim = len(data)

    if (cache[tuple(dataState)]!=0):
        return cache[tuple(dataState)]
    if (checkFull(dataState) and checkStatVali(dataState)):
        cache[tuple(dataState)] = calculateScore(data, dataState)
        return cache[tuple(dataState)]
    if(not dataState[position]==-1):
        return calculateMax(data, dataState, position+1, cache)
        
    state = 0
    afterState = updateState(dataState, position, dim, state)
    if (checkTranVali(dataState, afterState) and checkStatVali(afterState)):
        score = calculateMax(data, afterState, position+1, cache)
        if score>bestScore:
            bestScore = score
            cache[tuple(afterState)]=bestScore
    
    state = 1
    afterState = updateState(dataState, position, dim, state)
    if (checkTranVali(dataState, afterState) and checkStatVali(afterState)):
        score = calculateMax(data, afterState, position+1, cache)
        if score>bestScore:
            bestScore = score
            cache[tuple(afterState)]=bestScore
    return bestScore

cache = defaultdict(int)
data = [[71,24,95,56,54],[85,50,74,94,28],[92,96,23,71,10],[23,61,31,30,46],[64,33,32,95,89]]
dataState = [-1]*25
print calculateMax(data,dataState, 0, cache)

data = [[78,78,11,55,20,11],[98,54,81,43,39,97],[12,15,79,99,58,10],[13,79,83,65,34,17],
        [85,59,61,12,58,97],[40,63,97,85,66,90]]
dataState = [-1]*36
bestState = []
print calculateMax(data,dataState, 0, cache)


data = [[1,2,3,10],[4,5,6,11],[7,8,9,12],[13,14,15,16]]
dataState = [-1]*16
print calculateMax(data,dataState, 0, cache)    

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
dataState = [-1]*(11**2)
print calculateMax(data,dataState, 0, cache)
