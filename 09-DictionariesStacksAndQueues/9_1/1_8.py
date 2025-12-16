price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
total1=0
for x,y in price_list.items():
    print(x,'-',y)
    total1+=y
print(f'Total sum (first): {round(total1,2)}')

price_list_2={x:y for x,y in price_list.items()}
total2=0
for w,z in price_list_2.items():
    price_list_2[w]=round(z-0.1*z,2)

for w,z in price_list_2.items():
    print(w,'-',z)
    total2+=z
print(f'Total sum (second): {round(total2,2)}')

