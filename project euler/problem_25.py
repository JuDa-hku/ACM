def fib():
    f1,f2 = 1,1
    while True:
        f3 = f1 + f2
        yield f3
        f1, f2 = f2, f3
count = 2
for fib_number in fib():
    count += 1
    if len(str(fib_number)) >= 1000:
        print count
        break
    
        