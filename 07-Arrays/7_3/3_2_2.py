arr=[15, 8, 31, 47, 2, 19]
# arr2=arr[::-1]
# print(arr2)

arr2=[]
j=1
for i in arr:
    newelement=arr[len(arr)-j]
    j+=1
    arr2.append(newelement)
print(arr2)