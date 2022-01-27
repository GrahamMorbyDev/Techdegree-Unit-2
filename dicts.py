
# Import debugger
# import pdb; pdb.set_trace()

course = {'name': 'Graham', 'profession': 'Developer'}

print(course['name'])

# get keys from dict
course.keys()

# Get values from dict
course.values()

# Sort by alphabet
sorted(course.values())

# Update a value in a dict
course['name'] = 'Bob'

# Give a new keyvalue pair to a dict
course['level'] = 'Advanced'

print(course)

# Delete a value from a dict
del(course['level'])

print(course)

# Iterate over a dict
for key, value in course.items():
    print(value)

# packing a dict
def print_student(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_student(name='Graham', job='developer', level='advanced', date=2022)

# Unpacking
teacher = {
  'name':'Ashley',
  'job':'Instructor',
  'topic':'Python'
}

def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)

print_teacher(**teacher)