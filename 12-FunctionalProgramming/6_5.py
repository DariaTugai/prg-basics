arr=[x for x in range(1,21)]
tr=list(filter(lambda x:x%2==0 and x%3==0,arr))
print(tr)

# arr=[x for x in range(1,21) if x%2==0 and x%3==0]
# print(arr)