text='An apple a day keeps the doctor away'
def x(text):
    count=0
    for i in text:
        count+=1
    return count
print(x(text))