arr=[2.5,4.4,56.4,7.9,3.2,45.1134]
num=float(input('Enter a number: '))
ilosc=0
for i in arr:
    if i>num:
        ilosc+=1
print(ilosc)