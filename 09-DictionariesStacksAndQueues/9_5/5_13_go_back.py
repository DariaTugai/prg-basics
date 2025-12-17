# import queue
# stck=queue.LifoQueue()
# while True:
#     num=input('Enter a num ar operator: ')
    
#     if num=='=':
#         while not stck.empty():
#             print(stck.get())
#         break
#     try:
#         stck.put(int(num))
#     except ValueError:
#         stck.put(num)

import queue

stck = queue.LifoQueue()

while True:
    token = input('Enter number/operator (= to finish): ').strip()

    if token == '=':
        result = stck.get()
        print('Result:', result)
        break

    # якщо число
    try:
        value = int(token)
        stck.put(value)
    except ValueError:
        # якщо оператор
        b = stck.get()
        a = stck.get()

        if token == '+':
            stck.put(a + b)
        elif token == '-':
            stck.put(a - b)
        elif token == '*':
            stck.put(a * b)
        elif token == '/':
            stck.put(a / b)
        else:
            print('Unknown operator')