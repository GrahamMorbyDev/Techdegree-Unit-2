# help() allows to see what a function does, 
# using a docstring will be printed when running the help function

def does_something(arg):
    """Takes one arguemnt and does something based on type
        If arg is a string, returns arg * 3
        if arg is int or float, returns arg * 3
    """
    if isinstance(arg, (int, float)):
        return arg + 10
    elif isinstance(arg, str):
        return str * 3
    else:
        raise TypeError("does_something only takes ints, floats, and strings")
