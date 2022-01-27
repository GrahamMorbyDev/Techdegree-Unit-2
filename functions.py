# Define a function
def print_name():
    print('Graham Morby')

# Send a value to a function


def print_movie(movie):
    print(movie)


# Use a function
print_movie('Die hard')


# Return a value from a function
def two_plus_two():
    val = 2 + 2
    return val


sum = two_plus_two()
print(sum)


# Taking arguements
def subtract_two(num1, num2):
    val = num1 - num2
    return val


print(subtract_two(67, 31))


# Arguments to a tuple with packing
def packer(*args):
    print(args)


packer('My', 'name', 'is', 'graham')


# Unpacking 
def unpacker():
    return(1, 2, 3)

var1, var2, var3 = unpacker()

print(var1)
print(var2)
print(var3)

first, last = input('Enter your full name: \n').split(' ')

print(first)
print(last)