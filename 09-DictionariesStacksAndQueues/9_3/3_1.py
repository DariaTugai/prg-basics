import queue
table=queue.LifoQueue()
table.put(2)
table.put(3)
table.put(7)
table.put(4)
table.put(1)
table.put(9)
table.put(8)
l=table.get()
p=table.get()
sum=l+p
print(sum)
sum2=0
while not table.empty():
    sum2+=table.get()
print(sum2)