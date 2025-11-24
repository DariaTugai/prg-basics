<<<<<<< HEAD
def f(number):
    sum=0
    numbers='0123456789'
    for i in numbers:
        if number.count(i)>1:
            sum+= int(i)*number.count(i)
    return sum
=======
def f(number):
    sum=0
    numbers='0123456789'
    for i in numbers:
        if number.count(i)>1:
            sum+= int(i)*number.count(i)
    return sum
>>>>>>> 02a8f2406fd9236bd610261934085dadc20cef97
print(f('555678'))