def fun(number,even):
    sum_even=0
    sum_odd=0
    for j in str(number):
            i=int(j)
            if i%2==0:
                sum_even=sum_even+i
            else:
                sum_odd=sum_odd+i
    if even==True:
        return sum_even
    if even==False:
         return sum_odd
    
print(fun(319826,False))