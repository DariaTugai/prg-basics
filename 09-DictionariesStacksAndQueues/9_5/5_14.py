import queue
que=queue.Queue()
ticket=1
for i in range(20):
    que.put(ticket)
    ticket+=1
while not que.empty():
    print(que.get())