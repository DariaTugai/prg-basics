import queue
natnum=int(input('enter a number: '))
binnum=queue.LifoQueue()
while natnum!=0:
    binnum.put(natnum%2)
    natnum=int(natnum/2)
while not binnum.empty():
    print(binnum.get(),end='')