arr=[
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
i=0
for row in arr:
    row[i]=1
    i+=1
    print(' '.join(str(j) for j in row))
#print(' '.join(str(j) for j in row)) str separately for each symbol. 
#.just works with strings only.