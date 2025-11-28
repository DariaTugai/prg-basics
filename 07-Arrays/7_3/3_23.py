text='An apple a day keeps the doctor away'
def x(text):
    count=0
    for i in text.split(' '):
        count+=1
    return count
print(x(text))
def g(text):
    g=text.split(' ')
    gg=[]
    for i in g:
        gg.append(i)
    return sorted(gg,key=len,reverse=True)
print(g(text))
def m(text):
    l=text.split(' ')
    lg=[]
    for i in l:
        lg.append(i)
    return sorted(lg)
print(m(text))