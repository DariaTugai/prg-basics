from functools import reduce
arr= [2,4,6,3,7,5]
arrr=list(filter(lambda x:x%2==0,arr))
sum=reduce(lambda x,y:x+y,arrr)
print(sum)