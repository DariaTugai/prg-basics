def transpose_matrix(m):
    newarr=[]
    rows=0
    columns=0
    row1=0
    col1=0
    for row in m:
        rows+=1
    for i in m[0]:
        columns+=1
    while True:
        for z in range(rows):
            newarr.append(m[row1][0])
            row1+=1
            col1+=1
            if row1==rows:
                    break 
    return newarr

print(transpose_matrix([[1,2,3],[4,5,6],[7,8,9]]))
