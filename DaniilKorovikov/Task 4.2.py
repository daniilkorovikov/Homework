def is_palindrome(s):
    """
    Function checks whether a 's' string is a palindrome or not
    """
    return 'Palindrome' if s == s[::-1] else 'Not palindrome'

print(is_palindrome('aba'))