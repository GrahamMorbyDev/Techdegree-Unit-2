nums = [1, 2, 3, 4, 5, 6, 7, 8]
nums_partial = nums[0::2]
print(nums_partial)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors_partial = colors[3:6]
print(colors_partial)

student_gpas = [4.0, 2.3, 3.5, 3.7, 3.9, 2.8, 1.5, 4.0]

# Slice a list and return values - requires a start, stop and can take a step
sliced_gpas = student_gpas[2:5]

# Max value in list
max_gpa = max(student_gpas)
# Min value in list
min_gpa = min(student_gpas)
# Length of list
length = len(student_gpas)

print(sliced_gpas)

# Check if exists using IN or NOT IN
docs = 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'
if 'tuple' not in docs:
    print('No')
else:
    print('Yes')

# How many times something exists
print(docs.count('tuple'))

# Find a placement of where it exists
print(docs.index('tuple'))

obj1 = [1, 2, 3, 4, 5]
obj2 = [6, 7, 8, 9, 10]

# Concat
obj1 = obj1 + obj2