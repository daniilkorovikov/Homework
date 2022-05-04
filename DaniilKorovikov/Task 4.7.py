def foo(a):
    res = [1]*len(a)
    ind = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if j != ind:
                res[i] *= a[j]
        ind += 1
    return res

print(foo([1, 2, 3, 4, 5]))
print( foo([3, 2, 1]))