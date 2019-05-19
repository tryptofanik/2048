from Field import Field
import random
import time


class Board:

    def __init__(self, size):
        self.size = size
        self.fields = self.makeBoard(size)

    def __str__(self):
        out = ""
        for i in range(self.size):
            for j in self.fields[i]:
                out += "{:5s}".format(str(j.getValue()))
            out += "\n"
        return out

    def makeBoard(self, size):
        # create matrix of empty initialized fields objects
        board = [[Field(None) for i in range(size)] for j in range(size)]

        # make some random values on board
        addedRandom = 0
        # fill the board in 1/8
        while addedRandom <= size**2/8:
            x = random.randint(0, size-1)
            y = random.randint(0, size-1)
            if not board[x][y].isOccupied():
                if random.random() < 0.6:
                    board[x][y].setValue(2)
                else:
                    board[x][y].setValue(4)
                addedRandom+=1
        return board

    # this one can be better
    # TODO
    def moveSlice(self, slice, toLeft):
        # slice is a row or column from board
        # toLeft == 1 means agregate values to the left
        if not toLeft:
            slice.reverse()
        newslice = []
        current = None
        for i in range(len(slice)):
            if slice[i].getValue() is None:
                continue
            if current is None and isinstance(slice[i].getValue(), int):
                current = slice[i].getValue()
                continue
            elif slice[i].getValue() == current and isinstance(slice[i].getValue(), int):
                newslice.append(Field(current*2))
                current = None
            elif slice[i].getValue() != current and isinstance(slice[i].getValue(), int):
                newslice.append(Field(current))
                current = slice[i].getValue()

        newslice.append(Field(current))
        for i in range(self.size - len(newslice)):
            newslice.append(Field(None))
        if not toLeft:
            newslice.reverse()
            return newslice
        return newslice

    def moveVertical(self, up):
        for i in range(self.size): # i is column index
            slice = []
            for j in range(self.size):
                slice.append(self.fields[j][i])
            if up:
                newslice = self.moveSlice(slice, 1)
            else:
                newslice = self.moveSlice(slice, 0)
            for j in range(self.size):
                self.fields[j][i] = newslice[j]
        return self.fields

    def moveHorizontal(self, left):
        for i in range(self.size):  # i is row index
            slice = []
            for j in range(self.size):
                slice.append(self.fields[i][j])
            if left:
                newslice = self.moveSlice(slice, 1)
            else:
                newslice = self.moveSlice(slice, 0)
            for j in range(self.size):
                self.fields[i][j] = newslice[j]
        return self.fields

    def moveBoard(self, direct):
        if direct == "w":
            self.fields = self.moveVertical(1)
        elif direct == "s":
            self.fields = self.moveVertical(0)
        elif direct == "a":
            self.fields = self.moveHorizontal(1)
        elif direct == "d":
            self.fields = self.moveHorizontal(0)

    def insert(self):
        flag = False
        t = time.process_time()
        while not flag:
            a = random.randint(0, self.size - 1)
            b = random.randint(0, self.size - 1)
            if not self.fields[a][b].isOccupied():
                flag = True
                if random.random() < 0.6:
                    self.fields[a][b].setValue(2)
                else:
                    self.fields[a][b].setValue(4)
            if time.process_time() - t > 0.001:
                print("Game over :(")
                exit(-1)


