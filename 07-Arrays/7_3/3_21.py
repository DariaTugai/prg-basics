arr1=[3,5,7]
arr2=[3,7,8,9]
for i in arr1:
    if arr2.count(i)==0:
        isok='no'
        break
    else:
        isok='yes'
print(isok)


