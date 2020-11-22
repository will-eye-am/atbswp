my_pets = ['Sally', 'Peach', 'Minnie']

print('Enter a name:')
name = input()

if name not in my_pets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')