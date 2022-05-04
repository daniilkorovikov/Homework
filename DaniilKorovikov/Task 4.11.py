def combine_dicts(*args):
    res = {}
    for dct in args:
        for key, value in dct.items():
            res[key] = res.get(key, 0) + value
    return res

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))
# {'a': 300, 'b': 200, 'c': 300}


print(combine_dicts(dict_1, dict_2, dict_3))
#  {'a': 600, 'b': 200, 'c': 300, 'd': 100}