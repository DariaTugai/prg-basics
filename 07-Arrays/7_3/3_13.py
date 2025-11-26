def occurs(num,arr):
    if num in arr:
        return f'number {num} appears in the array'
    else:
        return f'number {num} doesn\'t appear in the array'
    
print(occurs(23,[2,5,6,2]))