a='*'
x=1
y=1
while x!=6:
    print(a)
    a+="*"
    x+=1
while x!=0:
    print(a[0:(len(a)-y)])
    y+=1
    x-=1
    

        