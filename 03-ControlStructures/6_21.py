amount=int(input('Enter the amount in PLN: '))
amount1=amount
PLN5=0
PLN2=0
PLN1=0
while True:
    if amount >=5:
        PLN5=amount//5
        amount=amount%5
    if amount >=2 and amount<5:
        PLN2=amount//2
        amount=amount%2
    if amount >=1 and amount<2:
        PLN1=amount//1
        amount=amount%1
        break

print(f'The amount of PLN {amount1} in coins:\n5 PLN coins: {PLN5} \n2 PLN coins: {PLN2} \n1 PLN coins: {PLN1}')
    
