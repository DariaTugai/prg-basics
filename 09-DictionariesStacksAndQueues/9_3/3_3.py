import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    opening=queue.LifoQueue()
    for i in expression:
        if i=='[':
            opening.put('A')
        elif i=='{':
            opening.put('B')
        elif i=='(':
            opening.put('C')
        elif i==']':
            if opening.get()!='A':
                return False
        elif i=='}':
            if opening.get()!='B':
                return False
        elif i==')':
            if opening.get()!='C':
                return False
    return True
  
print(brackets_ok(expression1))
print(brackets_ok(expression2))
