arr=[-15, 8, -31, 47, -2, 19]
mx=0
mn=0
for i in arr:
    if mx<i:
        mx=i
    if mn>i:
        mn=i

print(mx,mn)
