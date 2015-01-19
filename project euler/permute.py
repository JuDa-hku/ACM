def permu(al, lower=0):
    if lower+1>=len(al):
        print "0"
        yield al
    else:
        for p in permu(al, lower+1):
            print "1"
            yield p
        for i in xrange(lower+1, len(al)):
            al[i], al[lower] = al[lower], al[i]
            for p in permu(al, lower+1):
                print "2"
                yield p
            al[i], al[lower] = al[lower], al[i]

print (permu([1,2,3,4]))



def makeRange(n):
    # return 0,1,2,...,n-1
    i = 0
    while i < n:
        yield i
        i += 1

def yield_try():
    yield 1
    print 'k1'
    yield 2
    print 'k2'