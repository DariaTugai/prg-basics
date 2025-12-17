paragraph = "cat dog mouse cat rat cat mouse"
paragraph=paragraph.split()
diction={}
for x in paragraph:
    if not x in diction:
        diction[x]=1
    else:
        diction[x]+=1
print(diction)


# words=dict(x for x in paragraph)
# print(words)