import string

def intersection_of_strings(*args):
    res = set(args[0])
    for arg in args:
        res.intersection_update(arg)
    return res

def sum_of_strings(*args):
    res = set()
    for arg in args:
        res.update(set(arg))
    return res

def at_least_two(*args):
    res = set()
    for i, word1 in enumerate(args):
        for j, word2 in enumerate(args):
            if i != j:
                res.update(set(word1) & set(word2))
    return res

def not_used_chars(*args):
    res = set()
    all_chars = set(string.ascii_lowercase)
    res = all_chars - sum_of_strings(*args)
    return res

print(intersection_of_strings("hello", "world", "python"))
print(sum_of_strings("hello", "world", "python"))
print(at_least_two("hello", "world", "python"))
print(not_used_chars("hello", "world", "python"))

