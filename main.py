from tkinter import *

table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
tour = ["X", "O"]
finished = False
tourValid = False
compt = 0

"""Création de la fenêtre"""

window = Tk()
window.title('TicTacToe')
window.geometry('500x500')
window.minsize(500, 500)


def insertIntoTable(x, y):
    """
    place the letter on the board
    :param x: the x coord
    :param y: the y coord
    :return true/false: return if the letter fits in the table
    """
    global compt
    if table[x][y] == " ":
        table[x][y] = tour[compt]
        printTable(x, y)
        if checkWin(table, tour[compt]):
            victoire(tour[compt])
        elif checkLose(table):
            defaite()
        else:
            compt = (compt + 1) % 2
            label_tour.config(text="Tour de " + tour[compt])


def printTable(x=-1, y=-1):
    """
    Edit de pressed button
    """
    if x == 0:
        if y == 0:
            btn0.config(state=DISABLED, text=tour[compt])
        if y == 1:
            btn1.config(state=DISABLED, text=tour[compt])
        if y == 2:
            btn2.config(state=DISABLED, text=tour[compt])
    if x == 1:
        if y == 0:
            btn3.config(state=DISABLED, text=tour[compt])
        if y == 1:
            btn4.config(state=DISABLED, text=tour[compt])
        if y == 2:
            btn5.config(state=DISABLED, text=tour[compt])
    if x == 2:
        if y == 0:
            btn6.config(state=DISABLED, text=tour[compt])
        if y == 1:
            btn7.config(state=DISABLED, text=tour[compt])
        if y == 2:
            btn8.config(state=DISABLED, text=tour[compt])
    if x == -1 and y == -1:
        btn0.config(state=ACTIVE, text='')
        btn1.config(state=ACTIVE, text='')
        btn2.config(state=ACTIVE, text='')
        btn3.config(state=ACTIVE, text='')
        btn4.config(state=ACTIVE, text='')
        btn5.config(state=ACTIVE, text='')
        btn6.config(state=ACTIVE, text='')
        btn7.config(state=ACTIVE, text='')
        btn8.config(state=ACTIVE, text='')
        label_tour.config(text='Tour de '+tour[compt])


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
            return True
        if table[i][0] == player and table[i][1] == player and table[i][2] == player:
            return True
    if table[0][0] == player and table[1][1] == player and table[2][2] == player:
        return True
    if table[0][2] == player and table[1][1] == player and table[2][0] == player:
        return True
    return False


def victoire(winner):
    btn0.config(state=DISABLED)
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    label_tour.config(text='VICTOIRE DE ' + winner)


def checkLose(table):
    if ' ' not in table[0] and ' ' not in table[1] and ' ' not in table[2]:
        return True
    return False


def defaite():
    label_tour.config(text='Defaite')


def Restart():
    global table
    global compt
    table = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    compt = (compt + 1) % 2
    printTable()


def But0pressed():
    insertIntoTable(0, 0)


def But1pressed():
    insertIntoTable(0, 1)


def But2pressed():
    insertIntoTable(0, 2)


def But3pressed():
    insertIntoTable(1, 0)


def But4pressed():
    insertIntoTable(1, 1)


def But5pressed():
    insertIntoTable(1, 2)


def But6pressed():
    insertIntoTable(2, 0)


def But7pressed():
    insertIntoTable(2, 1)


def But8pressed():
    insertIntoTable(2, 2)


titleFrame = Frame(window, bg='#654321')
label_tour = Label(titleFrame, text='Tour de ' + tour[compt])
label_tour.pack()
titleFrame.pack()

playFrame = Frame(window)
btn0 = Button(playFrame, text="", font=('Arial', 25), padx=4, pady=4, height=1, width=3, command=But0pressed)
btn0.grid(row=0, column=0)
btn1 = Button(playFrame, text="", font=('Arial', 25), padx=4, pady=4, height=1, width=3, command=But1pressed)
btn1.grid(row=0, column=1)
btn2 = Button(playFrame, text="", font=('Arial', 25), padx=4, pady=4, height=1, width=3, command=But2pressed)
btn2.grid(row=0, column=2)
btn3 = Button(playFrame, text="", font=('Arial', 25), padx=4, pady=4, height=1, width=3, command=But3pressed)
btn3.grid(row=1, column=0)
btn4 = Button(playFrame, text="", font=('Arial', 25), padx=4, pady=4, height=1, width=3, command=But4pressed)
btn4.grid(row=1, column=1)
btn5 = Button(playFrame, text="", font=('Arial', 25), padx=4, pady=4, height=1, width=3, command=But5pressed)
btn5.grid(row=1, column=2)
btn6 = Button(playFrame, text="", font=('Arial', 25), padx=4, pady=4, height=1, width=3, command=But6pressed)
btn6.grid(row=2, column=0)
btn7 = Button(playFrame, text="", font=('Arial', 25), padx=4, pady=4, height=1, width=3, command=But7pressed)
btn7.grid(row=2, column=1)
btn8 = Button(playFrame, text="", font=('Arial', 25), padx=4, pady=4, height=1, width=3, command=But8pressed)
btn8.grid(row=2, column=2)
playFrame.pack(expand=YES)

RestartFrame = Frame(window)
btnRestart = Button(RestartFrame, text="Restart", font=('Arial', 12), padx=4, pady=4, height=1, width=5,
                    command=Restart)
btnRestart.pack()
RestartFrame.pack()

window.mainloop()
