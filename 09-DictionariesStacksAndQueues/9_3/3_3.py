import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   opening=queue.LifoQueue()
   closing=queue.LifoQueue()
   for i in expression:
      if i=='[' or i=='{' or i=='(':
         opening.put(i)
      elif i==']':
         closing.put('[')
      elif i=='}':
         closing.put('{')
      elif i==')':
         closing.put('(')

   return opening==(closing)
print(brackets_ok(expression1))

# if brackets_ok(expression1):
#    print(...)
# else
#    ...

# if brackets_ok(expression2):
# ...
# ...