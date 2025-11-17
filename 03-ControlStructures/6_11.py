current=int(input("Enter current product price: "))
previous=int(input("Enter previous product price: "))
discount=round(100-((current*100)/previous))
if discount>=10:
    print(f'Buy the product!!\nProduct price reduced by {discount}%')
else:
    print('No.')