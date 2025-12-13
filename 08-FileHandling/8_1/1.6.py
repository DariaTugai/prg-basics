###
# Reads the entire contents of a file
#
for line in sorted(open('08-FileHandling/countries.txt','r').read().split('\n')):print(line)

file_lines = open('08-FileHandling/countries.txt','r').read().splitlines()
print(hash(type(file_lines)))
