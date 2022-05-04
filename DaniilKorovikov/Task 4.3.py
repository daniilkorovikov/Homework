def same_split(s, sep=' '):
    res = []
    ind = 0
    for i in range(len(s)):
        if s[i] == sep:
            res.append(s[ind:i])
            ind = i + 1
    res.append(s[ind:])
    return res

a = 'Hello World'
print(same_split('Hello.world', sep='H'))
print(a.split("H"))
