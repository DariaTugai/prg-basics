number=int(input('Enter number of products: '))
price=int(input('Enter price: '))
discount=0.25
amount=''
if number>2:
    amount=number*(price-price*discount)
    print(f'Number of products purchased: {number}\nProduct price: {price}\nAmount to pay: {amount}')
else:
    amount=number*price
    print(f'No discount. \nNumber of products purchased: {number}\nProduct price: {price}\nAmount to pay: {amount}')