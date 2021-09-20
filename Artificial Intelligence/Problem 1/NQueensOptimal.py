from copy import deepcopy


def printAnswer(matrix):
    for row in matrix:
        print(*row)


def nQueens(N):
    matrix = [['0' for _ in range(N)] for _ in range(N)]

    def modifyBoard(matrix, r, c):
        temp = deepcopy(matrix)
        for i in range(N):
            for j in range(N):
                if temp[i][j] == '0' and (i==r or j==c or (i+j)==(r+c) or (i-j)==(r-c)):
                    temp[i][j] = '#'
        temp[r][c] = '1'
        return temp

    def getValidRows(matrix, c):
        rows = []
        if c > N:
            return rows
        for i in range(N):
            if matrix[i][c] == '0':
                rows.append(i)
        return rows

    def getChildren(matrix, c):
        children = []
        rows = getValidRows(matrix, c)
        for r in rows:
            children.append(modifyBoard(matrix, r, c))
        return children

    queue = [(deepcopy(matrix), 0)]
    while(queue):
        currBoard, col = queue.pop(0)
        nextBoard = getChildren(currBoard, col)
        for nb in nextBoard:
            if col+1 == N:
                return nb
            else:
                queue.append((nb, col+1))
    return []


if __name__ == "__main__":

    for N in range(1, 10):
        finalBoard = nQueens(N)
        printAnswer(finalBoard)
        print()