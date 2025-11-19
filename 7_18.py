def f(sentence):
    new=''
    for i in sentence:
        if i!=' ':
            new+=i
    return new
print(f("integrated development environment"))