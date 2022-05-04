def split_by_index(s, indexes):
    """
    Function splits the 's' string by indexes specified in indexes. Wrong indexes will be ignored
    """
    ind_2 = [i for i in indexes if i <= len(s)]
    res = []
    start = 0
    for index in ind_2:
        res.append(s[start:index])
        start = index
    res.append(s[start:])
    return res


print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("no luck", [42]))


