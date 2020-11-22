def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    else:
        number = 3 * number + 1
        print(number)
        return number

print('Enter a number:')
chosen_number = int(input())

while chosen_number != 1:
    chosen_number = collatz(chosen_number)