sentence = 'I completely agree with you.'
result = list(map(lambda x:len(x)  , sentence[:-1].split()))
print(result)