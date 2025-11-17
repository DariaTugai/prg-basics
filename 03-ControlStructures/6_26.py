x=0
PIN='0805'
entered=(input("Enter the PIN code: "))
while True:
    if entered==PIN:
        print('Correct.')
        break
    elif x==2:
        print('Incorrect... Sorry, your payment card has been blocked.')
        break
    else:
        print('Incorrect...Try again.')
        x+=1
        entered=(input("Enter the PIN code: "))