def f(palindrome):
    istrue=palindrome==palindrome[::-1]
    return istrue
print(f('radar'))