num=int(input('Enter a number: '))
if num>0:
    sgn= "positive"
elif num<0:
    sgn='negative'
else: 
    sgn= '0'
print(f'Number {num} is {sgn}.')