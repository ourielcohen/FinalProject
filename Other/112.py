def func(n):
    s=0
    for c in str(n):
        s+=int(c)
    return s
a=1234
print(func(a)**func(a))