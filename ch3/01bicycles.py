# Lists

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Acessing elements in a list
# Positions start at 0

print(bicycles[0])

# Using a method

print(bicycles[0].title())

print(bicycles[1])
print(bicycles[3])

# Accessing the last element in a list [-1]

print(bicycles[-1])

# Using individual values from a list

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)
