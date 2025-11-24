def f(name):
    name =name.split(' ')
    acronym=''
    for i in name:
        acronym+=i[0]
    return acronym
print(f("Internet of Things"))