# pg 29

# 2.3 Store a person's name in a variable and print a message to that person.
# Solution: concatenate

name = "Nadezhda"

print("Hello, " + name + ", would you like to learn some snaketogue today?")

#2.4 Store name in a variable, then lowercase, uppercase, titlecase.

print(name.upper())
print(name.lower())
print(name.title())

#2.5 Find a quote from a famous author, print it as shown.

print('\n\tvon Clausewitz once said, "War is\n\tthe continuation of politics by other means."')

# 2.6 - Repeat 2.5 but store person's name in a variable, then store message
# in a variable.

famous_person = "von Clausewitz"
message = '\n\t' + famous_person + ' once said, "War is\n\tthe continuation of politics by other means"'
print(message)

name = " \tNatalya \nRomanova "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())
