def get_pairs(l):
    if len(l) == 1:
        return
    list_of_tuples = []
    for i in range(len(l)-1):
        list_of_tuples.append((l[i],l[i+1]))
    return list_of_tuples

print(get_pairs([1, 2, 3, 8, 9]))
print(get_pairs(['need', 'to', 'sleep', 'more']))
print(get_pairs([1]))

