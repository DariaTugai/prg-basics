with open('file.txt','w') as file:
    arr=[]
    for i in range(1,101):
        #  file.write(f'{i,i**2,i**3}\n')
        file.write(f'{i},')
        file.write(f'{i**2},')
        file.write(f'{i**3}')
        file.write('\n')
    
    #     arr.append([i,i**2,i**3])
    # print(x for x in)
    
