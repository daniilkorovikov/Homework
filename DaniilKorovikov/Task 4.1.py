def replace_sym(s: str):
    """
    Function receives a string and replaces all " symbols with ' and vise versa
    """
    d = {'"': "'", "'": '"'}
    return ''.join([d[i] if i in d else i for i in s])

print(replace_sym('hello " word'))