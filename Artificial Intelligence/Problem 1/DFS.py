from copy import deepcopy


def writeOutput(i, matrix):
    with open('outputDFS.txt', 'a') as f:
        f.write(f"OUTPUT:{i}\n")
        for row in matrix:
            f.write(f"{''.join(row).replace('#', '0')}\n")
        f.write('\n')


def printAnswer(matrix):
    for row in matrix:
        print(*row)
    print()


def readInput():
    matrix = []
    with open(INPUT, 'r') as f:
        N = int(f.readline().strip())
        P = int(f.readline().strip())
        for _ in range(N):
            matrix.append(list(f.readline().strip().replace('0', '#')))
    return N, P, matrix


def nQueens(N, P, BOARD):

    def modifyBoard(matrix, R, C):
        temp = deepcopy(matrix)

        def modifyVertical(r, c):
            i = r
            while i > -1 and temp[i][c] != '2':
                temp[i][c] = '0'
                i -= 1

            i = r
            while i < N and temp[i][c] != '2':
                temp[i][c] = '0'
                i += 1

        def modifyHorizontal(r, c):
            j = c
            while j < N and temp[r][j] != '2':
                temp[r][j] = '0'
                j += 1

        def modifyUpperDiagonal(r, c):
            i, j = r, c
            while i > -1 and j < N and temp[i][j] != '2':
                temp[i][j] = '0'
                i -= 1
                j += 1

        def modifyLowerDiagonal(r, c):
            i, j = r, c
            while i < N and j < N and temp[i][j] != '2':
                temp[i][j] = '0'
                i += 1
                j += 1

        modifyVertical(R, C)
        modifyHorizontal(R, C)
        modifyUpperDiagonal(R, C)
        modifyLowerDiagonal(R, C)

        temp[R][C] = '1'
        return temp

    def getValidRows(matrix, c):
        rows = []
        for i in range(N):
            if matrix[i][c] == '#':
                rows.append(i)
        return rows

    def getChildren(matrix, c):
        children = []
        rows = getValidRows(matrix, c)
        for r in rows:
            children.append(modifyBoard(matrix, r, c))
        return children

    def checkColumn(matrix, c):
        for i in range(N):
            if matrix[i][c] == '#':
                return True
        return False

    stack = [(deepcopy(BOARD), 0, 0)]
    while stack:
        currBoard, col, p = stack.pop()
        if col < N:
            nextBoard = getChildren(currBoard, col)
            for nb in nextBoard:
                if p == P-1:
                    return nb
                else:
                    if checkColumn(nb, col):
                        stack.append((nb, col, p+1))
                    stack.append((nb, col+1, p+1))
    return []


if __name__ == "__main__":

    for i in range(1, 7):
        INPUT = f'Input/input{i}.txt'
        N, P, MATRIX = readInput()
        finalBoard = nQueens(N, P, MATRIX)
        writeOutput(i, finalBoard)