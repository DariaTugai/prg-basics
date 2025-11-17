decimal=int(input('Enter a decimal number: '))
binary=''
while decimal!=0:
    binary=f'{binary}'+ f'{decimal%2}'
    decimal//=2
print(f'Your number is {binary[::-1]}')
    
