for a in xrange(250, 1000):
    for b in xrange(500-a, a):
        if a*a+b*b == (1000-a-b)**2:
            print a*b*(1000-a-b)
            print a,b