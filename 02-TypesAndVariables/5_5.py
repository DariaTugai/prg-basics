price=float(input('Enter price: '))
discount=float(input('Enter discount %: '))
afterprice=price-price*discount/100
print(f'Product price: {price}')
print(f'Discount: {discount}')
print(f'Price with discount: {afterprice}')
print(f'Reduction: {price-afterprice}')