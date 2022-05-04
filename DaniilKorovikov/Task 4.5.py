def get_digits(num):
    """
    Function returns a tuple of a given integer's digits
    """
    t = [int(i) for i in str(num)]
    return tuple(t)

print(get_digits(87178291199))
