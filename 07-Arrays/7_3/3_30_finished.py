arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
number_first_row=1
second_row=1
multiply_by=2
for i in range(len(arr[0])):
    arr[0][i]=number_first_row
    number_first_row+=1
while second_row<5:
    for z in range(len(arr[second_row])):
        arr[second_row][z]=(arr[0][z])*multiply_by
    second_row+=1
    multiply_by+=1

for row in arr:
    print(' '.join(str(x) for x in row))