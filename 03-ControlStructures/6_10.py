age=int(input('Enter dog\'s age: '))
age_converted=''
if age<=2 and age>0:
    age_converted=age*10.5/2
    print(f'Dog\'s age is equal to {age_converted} human years.')
elif age>2:
    age_converted=10.5 + ((age-2)*4)
    print(f'Dog\'s age is equal to {age_converted} human years.')
else:
    print('Error.')