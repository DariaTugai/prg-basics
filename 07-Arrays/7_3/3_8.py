arr=[2, 6, 4, 9, 7]
lt=[]
def star(n):
    for i in range(0,len(n)):
        row= '*'*n[i]
        lt.append(f'{n[i]}: {row}')
    return '\n'.join(lt)
print(star(arr))