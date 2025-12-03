def transpose_matrix(m):
    general=[]
    newarr=[]
    rows = len(m)
    columns=len(m[0])
    for t in range(columns):
        for z in range(rows):
            newarr.append(m[z][t])
        general.append(newarr)
        newarr=[]
    return general

print(transpose_matrix([[1,2,3],[4,5,6],[7,8,9],[9,0,8]]))
