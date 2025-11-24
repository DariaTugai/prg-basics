def input_string(a):
    return a
def input_integer(a):
    return(int(a))
def input_real(a):
    return(float(a))
def input_boolean(a):
    tf=''
    if a=='True' or a=="y":
        tf=True
    else:
        tf=False
    return tf