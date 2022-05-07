# Task 1, Find a way to call inner_function without moving it from inside of enclosed_function.
a = "I am global variable!"


def enclosing_funcion():

    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)

    inner_function()

enclosing_funcion()

# Task 2.1. Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope.

def enclosing_funcion_1():

    a = "I am variable from enclosed function!"


    def inner_function():
        global a
        print(a)

    inner_function()

enclosing_funcion_1()

# Task 2.2. Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function.

def enclosing_funcion_2():

    a = "I am variable from enclosed function!"


    def inner_function():
        nonlocal a
        print(a)

    inner_function()

enclosing_funcion_2()
