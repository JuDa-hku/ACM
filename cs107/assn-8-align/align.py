#!/usr/bin/env python

import random # for seed, random
import sys    # for stdout
from collections import defaultdict

# Computes the score of the optimal alignment of two DNA strands.
def findOptimalAlignment(strand1, strand2, cache):
    #if the key is there, return directly
    if((tuple(strand1),tuple(strand2)) in cache.keys()):
        return cache[(tuple(strand1), tuple(strand2))]
    
	# if one of the two strands is empty, then there is only
	# one possible alignment, and of course it's optimal
    if len(strand1) == 0:
        bestDict={'strand1':[' ']*len(strand2), 'strand2':strand2, 'score':[-2]*len(strand2)}
        cache[(tuple)(strand1), (tuple)(strand2)] = bestDict
        return bestDict
    if len(strand2) == 0:
        bestDict={'strand2':[' ']*len(strand1), 'strand1':strand1, 'score':len(strand1)*[-2]}
        cache[(tuple)(strand1), (tuple)(strand2)] = bestDict
        return bestDict

    bestWithDict = findOptimalAlignment(strand1[1:], strand2[1:], cache)
    bestDict=defaultdict(int)
    bestDict['strand1'] = [strand1[0]]
    bestDict['strand1'].extend(bestWithDict['strand1'])
    bestDict['strand2'] = [strand2[0]]
    bestDict['strand2'].extend(bestWithDict['strand2'])
    bestDict['score'] = [-1]
    bestDict['score'].extend(bestWithDict['score'])

	# There's the scenario where the two leading bases of
	# each strand are forced to align, regardless of whether or not
	# they actually match.
    if strand1[0] == strand2[0]:
        bestDict['score'][0] = 1
        cache[(tuple)(strand1), (tuple)(strand2)] = bestDict
        return bestDict # no benefit from making other recursive calls

	# It's possible that the leading base of strand1 best
	# matches not the leading base of strand2, but the one after it.
    bestWithoutDict = findOptimalAlignment(strand1, strand2[1:], cache)
    bestStrand1ToSpaceDict = {'strand1':[strand1[0]], 'strand2':[' '], 'score':[-2]}
    bestStrand1ToSpaceDict['strand1'].extend(bestWithoutDict['strand1'])
    bestStrand1ToSpaceDict['strand2'].extend(bestWithoutDict['strand2'])
    bestStrand1ToSpaceDict['score'].extend(bestWithoutDict['score'])
    if sum(bestWithoutDict['score'])-2 > sum(bestDict['score']):
        bestDict = bestStrand1ToSpaceDict

	# opposite scenario
    bestWithoutDict = findOptimalAlignment(strand1[1:], strand2, cache)
    bestStrand2ToSpaceDict = {'strand1':[' '], 'strand2':[strand2[0]], 'score':[-2]}
    bestStrand2ToSpaceDict['strand1'].extend(bestWithoutDict['strand1'])
    bestStrand2ToSpaceDict['strand2'].extend(bestWithoutDict['strand2'])
    bestStrand2ToSpaceDict['score'].extend(bestWithoutDict['score'])
    if sum(bestStrand2ToSpaceDict['score']) > sum(bestDict['score']):
        bestDict = bestStrand2ToSpaceDict
    cache[(tuple)(strand1), (tuple)(strand2)] = bestDict
    return bestDict

# Utility function that generates a random DNA string of
# a random length drawn from the range [minlength, maxlength]
def generateRandomDNAStrand(minlength, maxlength):
	assert minlength > 0, \
	       "Minimum length passed to generateRandomDNAStrand" \
	       "must be a positive number" # these \'s allow mult-line statements
	assert maxlength >= minlength, \
	       "Maximum length passed to generateRandomDNAStrand must be at " \
	       "as large as the specified minimum length"
	strand = ""
	length = random.choice(xrange(minlength, maxlength + 1))
	bases = ['A', 'T', 'G', 'C']
	for i in xrange(0, length):
		strand += random.choice(bases)
	return strand

# Method that just prints out the supplied alignment score.
# This is more of a placeholder for what will ultimately
# print out not only the score but the alignment as well.

def printAlignment(bestDict, out = sys.stdout):
    out.write("\n Optimal score is "+str(sum(bestDict['score']))+"\n")
    out.write('+\t'+''.join(str(i)  if i>0 else s.join(' ') for i in bestDict['score'])+"\n")
    out.write(' \t'+''.join(char for char in bestDict['strand1'])+"\n")
    out.write(' \t'+''.join(char for char in bestDict['strand2'])+"\n")
    out.write('-\t'+''.join(str(-i)  if i<0 else s.join(' ') for i in bestDict['score'])+"\n")



# Unit test main in place to do little more than
# exercise the above algorithm.  As written, it
# generates two fairly short DNA strands and
# determines the optimal alignment score.
#
# As you change the implementation of findOptimalAlignment
# to use memoization, you should change the 8s to 40s and
# the 10s to 60s and still see everything execute very
# quickly.
 
def main():
    while (True):
        sys.stdout.write("Generate random DNA strands? ")
        answer = sys.stdin.readline()
        if answer == "no\n":
            break
        strand1 = generateRandomDNAStrand(8, 60)
        strand2 = generateRandomDNAStrand(8, 60)
        strand1 = "TGTACCCGCCGATCCCCGACTAAAAACTCTGGGTATTGGGGTGTACTTCCACCAA"
        strand2 = "CGACTCACAACATTCGGATAGAGAAAGCCGTTAGACAGGGCTTAGTGAGACATT"
        sys.stdout.write("Aligning these two strands: " + strand1 + "\n")
        sys.stdout.write("                            " + strand2 + "\n")
        cache = defaultdict()
        alignment = findOptimalAlignment(strand1, strand2, cache)
        printAlignment(alignment)
		
if __name__ == "__main__":
    main()

