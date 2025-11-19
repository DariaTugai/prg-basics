def amount_to_pay(amount):
    PLN5=0
    PLN2=0
    PLN1=0
    if amount%5>=0:
        PLN5=(amount-amount%5)//5
        amount=amount%5
    if amount%2>=0:
        PLN2=(amount-amount%2)//2
        amount=amount%2
    if amount%1>=0:
        PLN1=(amount-amount%1)//1
        amount=amount%1
    return PLN5, PLN2, PLN1

print(amount_to_pay(27))