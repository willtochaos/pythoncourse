# Use every function introduced in this list once

languages = ['portuguese', 'french', 'english', 'polish', 'hungarian']

print(languages)
print(languages[0])

languages.append('russian')
print(languages)

languages.insert(0, 'swedish')
print(languages)

del languages[0]
print(languages)

languages.pop()
print(languages)

languages.pop(0)
print(languages)

languages.remove('polish')
print(languages)

languages.sort()
print(languages)

languages.sort(reverse=True)
print(languages)

languages = ['hindi', 'zulu', 'japanese', 'chinese', 'quechua']
print(languages)
print(sorted(languages))
print(languages)

languages.reverse()
print(languages)

number = len(languages)
print(number)
