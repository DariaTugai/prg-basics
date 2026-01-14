
arr=[3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
arr2=list(filter(lambda x:x>2.0,arr))
mean=0
for i in arr2:
    mean+=i
meean=mean/len(arr2)
print(meean)