# 3.1 Store names, then print a greeting for each name in the list.

names = ['natalya', 'pyotr', 'nadezhda', 'ludmyla']

print("Hi, " + names[0].title() + ".")
print("Hi, " + names[1].title() + ".")
print("Hi, " + names[2].title() + ".")
print("Hi, " + names[3].title() + ".")

# 3.2 Same, plus message. Message should be the same
# I will store the second part of the message in a variable.

greeting = ", how are you these days?"

print("Dear " + names[0].title() + greeting)
print("Dear " + names[1].title() + greeting)
print("Dear " + names[2].title() + greeting)
print("Dear " + names[3].title() + greeting)

# List with favourite modes of transportation

sentence = "I would like to own a "
vehicles = ['bike', 'airplane', 'spaceship']

print(sentence + vehicles[0] + ".")
print(sentence + vehicles[1] + ".")
print(sentence + vehicles[2] + ".")


