def binary_number(number):
    isok=number.isdigit() 
    isokok=True
    for i in number:
        if i!='1' or i!='0':
            isokok=False
            break
    return isok and isokok
print(binary_number('1910010'))