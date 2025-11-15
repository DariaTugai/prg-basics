temp=int(input('Enter temperature in Celsius: '))
if temp>35 :
    print('It is extremely hot.')
elif temp>30 and temp<= 35:
    print('It is hot.')
elif temp<=30 and temp>=15:
    print('It is warm.')
elif temp>=0 and temp< 15:
    print('It is cold.')
else:
    print('Warning')