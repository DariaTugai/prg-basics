def f(arr):
    arrs=sorted(arr,reverse=True)
    return arrs[1]
print(f([5,4,78,2,34,455]))
def g(arr):
    arrrev=sorted(arr,reverse=True)
    arrs=sorted(arr)

    return arrrev[0]-arrs[0]
print(g([5,4,78,2,34,45]))
def i(arr):
    counter=0
    for x in arr:
        counter+=1
    if counter%2==1:
        return arr[counter//2]
    else:
        return (arr[counter//2]+arr[(counter//2)-1])/2
print(i([5,4,78,7,34,45]))
def m(arr):
    sl=[]
    arrs=min(arr)
    arrl=max(arr)
    sl.append(arrs)
    sl.append(arrl)
    return sl
print(m([5,4,78,7,34,45]))
