import random, sys

print('ROCK, PAPER, SCISSORS')

# Keeping track of wins, losses, and ties
wins = 0
losses = 0
ties = 0

# Game loop
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        player_move = input()

        if player_move == 'q':
            sys.exit()
        if player_move == 'r' or player_move =='p' or player_move =='s':
            break # Program exit
        print('Type of the the following: r, p, s, or q.')

    # Print player choice
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Generate and display computer choice
    random_number = random.randint(1,3)

    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_number == 3:
        computer_move = 's'
        print('SCISSORS')
    
    # Display results and record
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r':
        if computer_move == 's':
            print('You win!')
            wins = wins + 1
        elif computer_move == 'p':
            print('You lose!')
            losses = losses + 1
    elif player_move == 'p':
        if computer_move == 'r':
            print('You win!')
            wins = wins + 1
        elif computer_move == 's':
             print('You lose!')
             losses = losses + 1
    elif player_move == 's':
        if computer_move == 'p':
            print('You win!')
            wins = wins + 1
        elif computer_move == 'r':
            print('You lose!')
            losses = losses + 1