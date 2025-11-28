arr=[[-38, 19], [5,40],[-7,11],[29,16]]
mn=0
mx=0
for i,x in arr:
    
    if i<mn:
        mn=i
    elif x<mn:
        mn=x
    if i>mx:
        mx=i
    elif x>mx:
        mx=x
for row in range(len(arr)):
    for iten in range(len(arr[0])):
        if arr[row][iten]==mn:
            mnrow=row+1
            mnite=iten+1
        if arr[row][iten]==mx:
            mxrow=row+1
            mxite=iten+1
print(f'Min number is {mn} row: {mnrow} column: {mnite}. Max number is {mx} row: {mxrow} column: {mxite}')
