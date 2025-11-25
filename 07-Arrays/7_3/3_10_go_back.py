arr1=[4,36,12,28,9,44,5]
arr2=[5,1,36]
arr3=[]
for i in arr1:
    if i not in arr2:
        arr3.append(i)
print(arr3)