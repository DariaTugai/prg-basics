import queue 
def func(semtence):
    stck=queue.LifoQueue()
    result=''
    meow=semtence.split()
    for wor in meow:
        stck.put(wor)
    while not stck.empty():
        result=result+stck.get()+' '
    return result

print(func(' Push each character of the string onto the stack'))



