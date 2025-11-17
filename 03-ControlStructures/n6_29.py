N=int(input('Enter how many prime numbers you want:  '))
prime_numbers_count=0
prime_numbers=""
x=1
while prime_numbers_count<N:
    for i in range(1,):
        factors_count=0
        factor=1
        while factors_count!=3:
            if i%factor==0:
                factors_count+=1
                factor+=1
            else:
                factor+=1
        if factors_count==2:
            prime_numbers=prime_numbers+" "+ f'{i}'
            prime_numbers_count+=1
print(prime_numbers)
