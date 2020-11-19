# This program says "Hello" and asks for my name

print('Hello, world!')

print('What is your name?') # asks for name
my_name = input()

print('It is good to meet you, ' + my_name)
print('The length of you name is: ')
print(len(my_name))

print('What is your age?') # asks for age
my_age = input()
print('You will be ' + str(int(my_age) + 1) + ' in a year.')