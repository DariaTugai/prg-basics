hours=int(input('Enter the number of hours: '))
if hours>=1 and hours<=2:
    print('Total fee is 5 PLN')
elif hours>=3 and hours<=6:
    print('Total fee is 15 PLN')
elif hours>6:
    print('Total fee is 20 PLN')
else:
    print('Wrong number.')

