name = 'Carol'
age = 3000

# Happy path
#if name == 'Alice':
#    print('Hi, Alice.')
#elif age < 12:
#    print('You are not Alice, kiddo.')
#elif age > 2000:
#    print('Unlike you, Alice is not an undead vampire.')
#elif age > 100:
#    print('You are not Alice, grannie.')

#  Flawed path; wrong elif order outputs incorrect response
# if name == 'Alice':
#     print('Hi, Alice.')
# elif age < 12:
#     print('You are not Alice, kiddo.')
# elif age > 100:
#     print('You are not Alice, grannie.')
# elif age > 2000:
#     print('Unlike you, Alice is not an undead vampire.')

# Using an else statement
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')