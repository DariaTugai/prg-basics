arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
j=1
st=2
for i in range(len(arr[0])):
    arr[0][i]=j
    j+=1
# while st<6:
#     for j in range(len(arr[0])):
#         arr[1][j]=arr[0][j]*st
#     st+=1
# print(arr)
while st<6:
    for f in range(len(arr)):
        for j in range(len(arr[0])):
            arr[f+1][j]=arr[f][j]*st
        st+=1
print(arr)