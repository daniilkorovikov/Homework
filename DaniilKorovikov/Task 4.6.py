def get_longest_word(s):
    """
    Function returns the longest word in the given string.
    The word can contain any symbols except whitespaces ( , \n, \t and so on).
    If there are multiple longest words in the string with a same length function returns the word that occures first
    """
    l = s.split()
    max = l[0]
    for word in l:
        if len(word) > len(max):
            max = word
    return max

print(get_longest_word('Python is simple and effective!'))
print(get_longest_word('Any pythonista like namespaces a lot.'))