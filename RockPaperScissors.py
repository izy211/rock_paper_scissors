#!/usr/bin/env python3
import os
import random
import sys


def player_move():
    while True:
        #Show options menu and get user selection
        print('\nEnter your move: (r)ock | (p)aper | (s)cissors | (q)uit')
        playerMove = input()
        playerMove = playerMove.lower()
        if playerMove == 'q':
            sys.exit()
        elif playerMove in ['r', 'p', 's']:
            if playerMove == 'r':
                print('\nROCK\nvs')
            elif playerMove == 'p':
                print('\nPAPER\nvs')
            elif playerMove == 's':
                print('\nSCISSORS\nvs')
            return playerMove
        else:
            print('An invalid choice was entered. Please choose R, P, S to play or Q to quite (Not Case Sensitivity)')


def computer_move():
    #Get random computer selection
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
    return computerMove


def results(playerMove, computerMove):
    #Compare player and computer selections
    print('='*10)
    if playerMove == computerMove:
        print('Its a tie!\n')
        result = 'tie'
    elif playerMove+computerMove in ['pr', 'sp', 'rs']:
        print('You win!\n')
        result = 'win'
    else:
        print('You lose!\n')
        result = 'lose'
    return result


def main():
    os.system('clear')
    
    wins = 0
    losses = 0
    ties = 0
    
    print('Lets play rock, paper, scissors!')
    while True:
        result = results(player_move(), computer_move())
        #Keep track of stats
        if result == 'win':
            wins += 1
        elif result == 'lose':
            losses += 1
        elif result == 'tie':
            ties += 1

        print(f'Wins {wins} Losses {losses} Ties {ties}')

    
if __name__ == '__main__':
    main()
