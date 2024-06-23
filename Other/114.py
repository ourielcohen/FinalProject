def func(ns):
    s = 0
    for k in range(1,len(ns)):
        s += ns[k]
    return s
    qs = [1,2,3,4,5]
    print(func(qs))
