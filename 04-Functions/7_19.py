def f(number):
    sum=0
    numbers='0123456789'
    for i in numbers:
        if number.count(i)>1:
            sum+= int(i)*number.count(i)
    return sum
print(f('555678'))