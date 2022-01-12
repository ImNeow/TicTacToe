table = [1, 0, 0], [1, 0, 0], [1, 0, 0]


def insertIntoTable(lettre, x, y):
    table[x][y] = lettre


def printTable(table):

    print("   |     |")
    print(str(table[0][0])+"  |  "+str(table[0][1])+"  |  "+str(table[0][2]))
    print("   |     |")
    print("------------")
    print("   |     |")
    print(str(table[1][0])+"  |  "+str(table[1][1])+"  |  "+str(table[1][2]))
    print("   |     |")
    print("------------")
    print("   |     |")
    print(str(table[2][0])+"  |  "+str(table[2][1])+"  |  "+str(table[2][2]))
    print("   |     |")


def checkWin(table):

    col = 0
    row = 0
    diag = 0
    rdiag = 0
    x = 0
    y = 0
    winner = False
    n = 3
    for i in range(9):
        if table[x][i] == 1:
            col += col
        if table[i][y] == 1:
                row += row
        if table[i][i] == 1:
                diag += diag
        try:
            if table[i][n - i] == 1:
                rdiag += rdiag
        except:
            pass
        print(x, y)
    x += x
    y += y


    print(row, col, diag, rdiag)
    if row == n or col == n or diag == n or rdiag == n:
        winner = True


printTable(table)
checkWin(table)
