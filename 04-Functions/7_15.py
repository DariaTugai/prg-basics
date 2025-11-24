<<<<<<< HEAD
def f(detector):
    count=0
    for i in detector:
        if i=='+':
            count+=1
        elif i=='-':
            count-=1
    is3=count>=3
    return is3
=======
def f(detector):
    count=0
    for i in detector:
        if i=='+':
            count+=1
        elif i=='-':
            count-=1
    is3=count>=3
    return is3
>>>>>>> 02a8f2406fd9236bd610261934085dadc20cef97
print(f('+-+++-+++-'))