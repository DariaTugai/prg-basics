def f(password):
    isok=len(password)>=6
    isokok=True
    for i in password:
        meow=password.count(i)
        if meow>1:
            isokok=False
            break
    if isok and isokok:
        return True
    else:
        return False   
print(f('7152'))