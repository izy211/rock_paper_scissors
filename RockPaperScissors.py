import random
import sys


print('Lets play rock, paper, scissors!')

#Keep track of stats
wins = 0
losses = 0
ties = 0

while True:
    print(f'Wins {wins} Losses {losses} Ties {ties}')
    while True:
        #Show options menu
        print('\nEnter your move: (r)ock | (p)aper | (s)cissors | (q)uit')
        playerMove = input()
        playerMove = playerMove.lower()
        if playerMove == 'q':
            sys.exit()
        elif playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        else:
            print('An invalid choice was entered. Please choose R, P, S to play or Q to quite (Not Case Sensitivity)')

    #Player selection
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
    
    #Computer selection
    randomChoice = random.randint(1, 3)
    if randomChoice == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomChoice == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomChoice == 3:
        computerMove = 's'
        print('SCISSORS')
    
    #Compare player and computer selections
    if playerMove == computerMove:
        print('Its a tie!\n')
        ties += 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!\n')
        wins += 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!\n')
        wins += 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!\n')
        wins += 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!\n')
        losses += 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!\n')
        losses += 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!\n')
        losses += 1
