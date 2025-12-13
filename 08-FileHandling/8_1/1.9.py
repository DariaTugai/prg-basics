empl_file = open('08-FileHandling/it_company.csv').read().split('\n')[1:]
print(empl_file[0])

empl_lst = []

for empl_info in empl_file:
    if empl_info.split(',')[2] == 'Software Engineer':
        empl_lst.append(f"First name - {empl_info.split(',')[1]}, Last name - {empl_info.split(',')[0]}")
for name in empl_lst:print(name)
print(len(empl_lst))