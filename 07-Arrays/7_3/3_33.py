arr=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[14,15,16]]
arr2=[row[:] for row in arr]
for item in arr2:
    z=item[0]
    item[0]=item[2]
    item[2]=z
    print(' '.join(str(x) for x in item))
print('arr1')
for item in arr:
    print(' '.join(str(x) for x in item))


