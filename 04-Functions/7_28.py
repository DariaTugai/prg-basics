def f(n):
    themost=0

    for i in n:
        num=n.count(i)
        if num>themost:
            themost=i
         