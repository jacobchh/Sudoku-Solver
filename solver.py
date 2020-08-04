import numpy as np

board = np.zeros(shape=(9, 9))
count = 0


def solve():
    global count
    count += 1
    if count % 1000 == 0:
        print('\rCurrent number of computations made:', count, end='')
    freePos = find()
    if freePos is None:
        return True
    i = freePos[0]
    j = freePos[1]
    for w in range(1, 10):
        if possible(w, freePos):
            board[i][j] = w

            if solve():
                return True

            board[i][j] = 0

    return False


def find():
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return [i, j]
    return None


def possible(value, position):
    # position = (i, j) tuple
    i = position[0]
    j = position[1]

    # checks row and column for repeat value
    if (value in board[:, j]) or (value in board[i]):
        return False

    # reset to i,j - top left square
    i = (i // 3) * 3
    j = (j // 3) * 3

    # check all squares in square
    for n in range(i, i + 3):
        for m in range(j, j + 3):
            if board[n][m] == value:
                return False
    return True


def change(position):
    # position = (i, j) tuple
    i = position[0]
    j = position[1]
    for w in range(1, 10):
        if w not in board[:, j] and w not in board[i]:
            board[i][j] = w
            return True
    return False


def initialize():
    print("Please enter the values on the board starting from left to right, top to bottom, 0 for blank")
    integerChunk = input("Numbers: ")
    pos = 0
    for i in range(9):
        for j in range(9):
            board[i][j] = int(integerChunk[pos])
            pos += 1


def displayBoard():
    for i in range(3):
        for j in range(9):
            if board[i][j] == 0:
                print("  ", end="")
            else:
                print("%d " % board[i][j], end="")
            if (j == 2) or (j == 5):
                print("| ", end="")
            if j == 8:
                print("")
    print("- - - - - - - - - - -")
    for i in range(3, 6):
        for j in range(9):
            if board[i][j] == 0:
                print("  ", end="")
            else:
                print("%d " % board[i][j], end="")
            if (j == 2) or (j == 5):
                print("| ", end="")
            if j == 8:
                print("")
    print("- - - - - - - - - - -")
    for i in range(6, 9):
        for j in range(9):
            if board[i][j] == 0:
                print("  ", end="")
            else:
                print("%d " % board[i][j], end="")
            if (j == 2) or (j == 5):
                print("| ", end="")
            if j == 8:
                print("")


def main():
    initialize()
    print("Is this the correct board? Press enter to continue or 'q' to exit program.")
    displayBoard()
    response = input()
    if response == "q":
        exit()
    print("---------------SOLVING---------------\n")
    solve()
    print("\r\rSOLUTION")
    displayBoard()
    print("\nTotal number of computations:", count)


if __name__ == "__main__":
    main()

