table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def insertIntoTable(lettre, x, y):
    """
    place the letter on the board
    :param lettre: the player's letter
    :param x: the x coord
    :param y: the y coord
    :return true/false: return if the letter fits in the table
    """
    if table[x][y] == " ":
        table[x][y] = lettre
        return True
    return False

def printTable(table):
    """
    Print the table
    :param table: the board
    """
    print("   |     |")
    print(str(table[0][0]) + "  |  " + str(table[0][1]) + "  |  " + str(table[0][2]))
    print("   |     |")
    print("------------")
    print("   |     |")
    print(str(table[1][0]) + "  |  " + str(table[1][1]) + "  |  " + str(table[1][2]))
    print("   |     |")
    print("------------")
    print("   |     |")
    print(str(table[2][0]) + "  |  " + str(table[2][1]) + "  |  " + str(table[2][2]))
    print("   |     |")


def checkWin(table, player):
    """
    Check if there's a win
    :param table: current board
    :param player: player to check
    :return: 0 if no win, winner num if win
    """
    n = 3

    for i in range(n):
        if table[0][i] == player and table[1][i] == player and table[2][i] == player:
            return player
        if table[i][0] == player and table[i][1] == player and table[i][2] == player:
            return player
    if table[0][0] == player and table[1][1] == player and table[2][2] == player:
        return player
    if table[0][2] == player and table[1][1] == player and table[2][0] == player:
        return player
    return 0


i = 0
tour = ["X", "O"]
finished = False
tourValid = False

print("Tour de "+tour[i % 2])
printTable(table)
while not finished:
    num = int(input('Enter Num :'))
    tourValid = insertIntoTable(tour[i % 2], int(num / 3), num % 3)

    if checkWin(table, tour[i % 2]) == tour[i % 2]:
        finished = True

    if tourValid:
        i = i+1
        print("Tour de " + tour[i % 2])
        printTable(table)
    else:
        print("Déja pris ^^")
print("GG")
