def identity_matrix(n):
    matrix=[]
    count=0
    for i in range(n):
        matrix.append([0 for x in range(n)])
    for row in matrix:
        row[count]=1
        count+=1
    return matrix

print(identity_matrix(5))