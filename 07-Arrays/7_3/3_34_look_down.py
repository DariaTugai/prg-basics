def identity_matrix(n):
    matrix=[]
    count=0
    for i in range(n):
        matrix.append([0 for x in range(n)])
    for row in matrix:
        row[count]=1
        count+=1
    print(matrix)
    return '\n'.join([' '.join([str(x) for x in row]) for row in matrix])
print(identity_matrix(5))

#'\n'.join([' '.join([str(x) for x in row]) for row in matrix])