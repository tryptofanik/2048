#!/usr/bin/python3

from Board import Board
import random
import sys
import getopt
import readchar

def randomGame(board):
    i = 0
    while True:
        i += 1
        move = ["w", "a", "s", "d"][random.randint(0, 3)]
        print("move no.", i)
        board.moveBoard(move)
        board.insert()
        print(board)

def normalGame(board):
    i=0
    while True:
        move = readchar.readchar()
        if move == "q":
            exit(2)
        if move not in ["w", "a", "s", "d"]:
            continue
        else:
            print("move n0.", i)
            board.moveBoard(move)
            board.insert()
        i+=1
        print(board)


def main(argv):
    # reading arguments
    try:
        opts, args = getopt.getopt(argv,"hn:r")
    except getopt.GetoptError:
        print ('ERROR! Pass correct arguemnts\n','Gra.py -h -n <sizeOfBoard> -r\n-h for help\n-r for random game')
        sys.exit(2)
    randomgame=False
    for opt, arg in opts:
        if opt == '-h':
            print ('Gra.py -n <sizeOfBoard>')
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

