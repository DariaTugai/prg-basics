def f(n):
    x=0
    y=1
    for i in range(n-1):
        x,y=y,x+y
    return x
print(f(6))

#0,1,1,2,3,5,8