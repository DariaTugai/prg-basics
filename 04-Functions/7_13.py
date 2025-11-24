def f(n):
    str=''
    for i in range(1,n+1):
        str+=f'{i}'
    return str
print(f(100))