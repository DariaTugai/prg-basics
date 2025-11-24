def f(text):
    s=' '
    for i in range(len(text)):
        if i==len(text)-1:
            s=s+text[i]
        else:
            s=s+text[i]+"-"
    return s
print(f('meow'))
        