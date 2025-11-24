def f(code):
    isok=(int(code[0])+int(code[1])+int(code[2]))%7==int(code[3])
    return isok
print(f('1982'))