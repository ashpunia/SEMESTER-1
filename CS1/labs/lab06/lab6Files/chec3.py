import lab06_util

def print_grid():
    for i in range(0, 9):
        if i == 0:
            print('' + '-' * 25)

        for j in range(0, 9):
            if j % 3 == 0:
                print('|', end=' ')
                print(bd[i][j], end = ' ')
            else:
                print(bd[i][j], end = ' ')
        
            if j == 8:
                print('|')
        
        if i == 2 or i == 5 or i == 8:
            print('-' * 25)

def not_in_row(pos, n):
    for i in range(len(bd[pos[0]])):
        if bd[pos[0]][i] == n and i != pos[1]:
            return False
    return True

def not_in_column(pos, n):
    for i in range(len(bd)):
        if bd[i][pos[1]] == n and i != pos[0]:
            return False
    return True

def not_in_block(pos, n):
    startingPoint = (pos[0] // 3 * 3, pos[1] // 3 * 3)
    for i in range(startingPoint[0], startingPoint[0] + 3):
        for j in range(startingPoint[1], startingPoint[1] + 3):
            if bd[i][j] == n and (pos[0] != i and pos[1] != j):
                return False
    return True

def ok_to_add(pos, n):
    n = int(n)
    if n < 1 or n > 9:
        return False
    n = str(n)
    if (not not_in_row(pos, n)) or (not not_in_column(pos, n)) or (not not_in_block(pos, n)):
        return False
    return True

def is_solved(bd):
    for i in range(len(bd)):
        for n in range(len(bd)):
            if bd[i][n] == '.' or (not ok_to_add((i, n), bd[i][n])):
                return False
    return True

if __name__ == "__main__":

    fileName = input("Enter a file name: ").strip()
    bd = lab06_util.read_sudoku(fileName)
    while not is_solved(bd):
        print_grid()
        posX = int(input("Enter the row position: ").strip())
        posY = int(input("Enter the column position: ").strip())
        value = int(input("Enter the value: ").strip())
        if bd[posX][posY] == '.' and ok_to_add((posX, posY), value):
            bd[posX][posY] = value
        else:
            print("This number cannot be added")
    print("Puzzle solved")