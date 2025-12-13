f = ''.join([line for line in open('08-FileHandling/pets.txt').read().split('\n')])
print(len(f.split(' ')))