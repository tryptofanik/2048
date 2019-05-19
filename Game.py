#!/usr/bin/env python

# imports
from Board import Board
import random
import sys
import getopt
import readchar

def randomGame(board):
    # initializing counter
    i = 0
    while True:
        i += 1
        # randomly choose direction
        move = ["w", "a", "s", "d"][random.randint(0, 3)]
        print("move no.", i)
        # move board in selected direction
        board.moveBoard(move)
        # insert new value to empty field
        board.insert()
        # print board
        print(board)

def normalGame(board):
    # init counter
    i=0
    while True:
        # read move from the user
        move = readchar.readchar()
        # if user insert 'q' then quit game
        if move == "q":
            exit(2)
        # check if move is possible
        if move not in ["w", "a", "s", "d"]:
            # if not get another move
            continue
        else:
            print("move n0.", i)
            # move board in selected direction
            board.moveBoard(move)
            # insert new value into empty field
            board.insert()
        i+=1
        print(board)


def main(argv):
    description = 'Game.py -h -n <sizeOfBoard> -r\n-h for help\n-n for setting size of a board\n-r for random game\n'

    try:
        opts, args = getopt.getopt(argv,"hn:r")
    except getopt.GetoptError:
        print ('ERROR! Pass correct arguemnts\n',description)
        sys.exit()

    randomgame = False
    size = 4

    for opt, arg in opts:
        if opt == '-h':
            print ('Game.py -n <sizeOfBoard>')
            sys.exit()
        elif opt == "-n":
            size = int(arg)
        elif opt == "-r":
            randomgame=True

    board = Board(size)
    print(board)

    if randomgame:
        randomGame(board)
        exit(0)
    else:
        normalGame(board)



if __name__ == "__main__":
    main(sys.argv[1:])
