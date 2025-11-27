
def rand_elem(array):
    import random
    return array[random.randint(0,len(array)-1)]
print(rand_elem([3,4,6,7,8,9]))