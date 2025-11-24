def f(n):
    prime =[]
    y = 2
    pr = True
    while len(prime)<n:
        for x in range(1,y):
            if x!=1 and y%x == 0:
                pr = False
        if pr:
            prime.append(y)
        pr = True
        y+=1
    print(prime)
    return prime[-1]
print(f(3),'here')                
for x in range(1,10):
     print(f(x),'here')                