def f(detector):
    count=0
    for i in detector:
        if i=='+':
            count+=1
        elif i=='-':
            count-=1
    is3=count>=3
    return is3
print(f('+-+++-+++-'))