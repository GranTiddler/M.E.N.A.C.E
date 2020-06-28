import random
import json


# a list of all possible game states
metalist = [
    [" ", " ", " ", " ", " ", " ", " ", " ", " "],
    ["O", "X", " ", " ", " ", " ", " ", " ", " "],
    ["O", " ", " ", " ", "X", " ", " ", " ", " "],
    ["X", "O", " ", " ", " ", " ", " ", " ", " "],
    [" ", "O", " ", " ", "X", " ", " ", " ", " "],
    ["X", " ", "O", " ", " ", " ", " ", " ", " "],
    [" ", "X", "O", " ", " ", " ", " ", " ", " "],

    ["X", " ", " ", " ", "O", " ", " ", " ", " "],
    [" ", "X", " ", " ", "O", " ", " ", " ", " "],
    ["X", " ", " ", " ", " ", "O", " ", " ", " "],
    [" ", "X", " ", " ", " ", " ", " ", "O", " "],
    ["X", " ", " ", " ", " ", " ", " ", " ", "O"],
    ["O", "O", " ", " ", "X", "X", " ", " ", " "],
    ["O", "O", " ", " ", "X", " ", " ", "X", " "],
    ["O", "O", " ", " ", " ", "X", " ", "X", " "],

    ["O", "X", "O", "X", " ", " ", " ", " ", " "],
    ["O", "X", "O", " ", "X", " ", " ", " ", " "],
    ["X", "O", "O", " ", "X", " ", " ", " ", " "],
    ["X", "O", "O", " ", " ", "X", " ", " ", " "],
    ["X", "O", "O", " ", " ", " ", "X", " ", " "],
    ["O", "X", "O", " ", " ", " ", " ", "X", " "],
    ["O", " ", "O", " ", "X", " ", " ", "X", " "],
    ["X", "O", "O", " ", " ", " ", " ", "X", " "],

    ["X", "O", "O", " ", " ", " ", " ", " ", "X"],
    ["X", "X", "O", "O", " ", " ", " ", " ", " "],
    ["X", "O", "X", "O", " ", " ", " ", " ", " "],
    ["O", "X", " ", "O", "X", " ", " ", " ", " "],
    ["X", "O", " ", "O", "X", " ", " ", " ", " "],
    ["O", "X", " ", "O", " ", "X", " ", " ", " "],
    ["X", "O", " ", "O", " ", "X", " ", " ", " "],
    ["O", "X", " ", "O", " ", " ", " ", "X", " "],
]
"""
# initialize 2 lists, 1 to act as a buffer to be added to the other list, of which each index corrosponds to the index of the matching gamestate in metalist
marbles = []
bufferList = []
# adds 4 copies of each empty index to the buffer list and appends that to the marbles list
for x in metalist:
    for y in range(0, 9):
        if x[y] == " ":
            for z in range(4):
                bufferList += str(y)
    marbles += ""
    marbles.append(bufferList)
"""


# switches between true and false
def switch(flopPosition):
    if flopPosition == 0:
        return 1
    elif flopPosition == 1:
        return 2
    elif flopPosition == 2:
        return 0



# mirrors the game board to check if it fits
def flopH(lisp, lisp2):
    lisp2 = [lisp[2], lisp[1], lisp[0], lisp[5], lisp[4], lisp[3], lisp[8], lisp[7], lisp[6]]
    return lisp2

def flopY(lisp, lisp2):
    lisp2 = [lisp[6], lisp[7], lisp[8], lisp[3], lisp[4], lisp[5], lisp[0], lisp[1], lisp[2]]
    return lisp2

# rotates the game board to check if it fits
def rotate(lisp, lisp2):
    lisp2 = [lisp[6], lisp[3],lisp[0], lisp[7], lisp[4], lisp[1], lisp[8], lisp[5], lisp[2]]
    return (lisp2)



# manipulates the game board to find which game state it fits
def findState(metalist, gamestate, flopState):
    for i in range (0, 13):
        if gamestate in metalist:
            return metalist.index(gamestate)
        elif flopState == 0:
            gamestate = flopY(gamestate, [])
            flopState = switch(flopState)
            continue
        elif flopState == 1:
            gamestate = flopH(gamestate, [])
            flopState = switch(flopState)
            continue
        elif flopState == 2:
            gamestate = rotate(gamestate, [])
            flopState = switch(flopState)
            continue



# introduction
print("""you should know how to play tic tack toe
you will play as x
you will just enter the co-ordinates in the same way as chess or battle ship as shown below
the ai will go first


    A1 | A2 | A3
  _____|____|____
    B1 | B2 | B3
  _____|____|____
    C1 | C2 | C3
       |    |

you will be playing against a machine learning ai called MENACE(machine educable noughts and crosses engine)
it was one of the earliest machine learnting algorithms and was used to teach a pile of matchboxes full of marbles to play tic tac toe""")

usedMarbles = []

# initializes gameboard
positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


# converts coordinates to indexes
def convert(player):
    player = player.upper()
    if (player == "A1"):
        return 0
    elif (player == "A2"):
        return 1
    elif (player == "A3"):
        return 2
    elif (player == "B1"):
        return 3
    elif (player == "B2"):
        return 4
    elif (player == "B3"):
        return 5
    elif (player == "C1"):
        return 6
    elif (player == "C2"):
        return 7
    elif (player == "C3"):
        return 8
    else:
        return "invalid"


# prints the positions in the board
def printBoard(positions):
    print("""
    """ + positions[0] + """  |  """ + positions[1] + """  |  """ + positions[2] + """  
  _____|_____|____
    """ + positions[3] + """  |  """ + positions[4] + """  |  """ + positions[5] + """ 
  _____|_____|____
    """ + positions[6] + """  |  """ + positions[7] + """  |  """ + positions[8] + """
       |     |
  """)


# checks if either party has won
def checkWin(lisp):
    if lisp[4] == lisp[1] and lisp[4] == lisp[7]:
        return lisp[4]
    elif lisp[4] == lisp[3] and lisp[4] == lisp[5]:
        return lisp[4]
    elif lisp[4] == lisp[2] and lisp[4] == lisp[6]:
        return lisp[4]
    elif lisp[4] == lisp[0] and lisp[4] == lisp[8]:
        return lisp[4]
    elif lisp[0] == lisp[1] and lisp[0] == lisp[2]:
        return lisp[0]
    elif lisp[0] == lisp[3] and lisp[0] == lisp[6]:
        return lisp[0]
    elif lisp[8] == lisp[7] and lisp[8] == lisp[6]:
        return lisp[8]
    elif lisp[8] == lisp[2] and lisp[8] == lisp[5]:
        return lisp[8]
    else:
        return "null"


# loss and win punishment/reward
def finish(winState, marbles, marblesList):
    if winState == "O":
        return marbles[marblesList[0]].append(marblesList[1])

    elif winState == "X":
        return marbles[marblesList[0]].remove(marblesList[1])



# gets players move and makes sure it is valid
def playerMove(lisp, player=""):
    player = convert(input("please enter the coordinates with no spaces\n").upper())
    while True:
        if player == "invalid":
            player = convert(input("Please enter valid coordinates\n").upper())
            continue
        elif lisp[player] == " ":
            lisp[player] = "X"
            lisp = cpu[0]
            printBoard(lisp)
            return lisp
        else:
            player = convert(input("Please enter valid coordinates\n").upper())
            continue


# logic to find the cpus move
def cpuMove(metalist, marbles, positions, findIndex = 0, choice = 0):
    findIndex = findState(metalist, positions, True)
    if len(marbles[findIndex]) > 0:
        choice = random.choice(marbles[findIndex])
        positions[int(choice)] = "O"
        printBoard(positions)
        return [positions, [findIndex, choice]]
    else:
        print("MENACE has resigned the game")
        pass


# main loop of the game


flopState = True
hasWon = "null"

"""with open("marbles.json", 'r') as M:
    marbles = json.load(M.json, M, indent=1)"""

while 1 == 1:
    hasWon = checkWin(positions)
    if hasWon == "X":
        positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        print("You Won")
        flopState = True
        marbles = finish(hasWon,marbles,usedMarbles)
        with open("marbles.json", 'w') as M:
            json.dump(marbles, M, indent=1)

    elif hasWon == "O":
        positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        print("You Won")
        flopState = True
        marbles = finish(hasWon, marbles, usedMarbles)
        with open("marbles.json", 'w') as M:
            json.dump(marbles, M, indent=1)


    if flopState:
        cpu = cpuMove(metalist, marbles, positions)
        positions = cpu[0]
        usedMarbles.append(cpu[1])
        flopState = False
    else:
        positions = playerMove(positions)
        flopState = True






#current issues:
    # - not all gamestates added(causes error in most games past 2 moves)
x
# TODO
    # - complete entry of gamestates/automatic generation(likley not exactly preformante)
        # - Seriously stop procrastinating you bloody moron
    # - tkinter GUI
        # - updating after cpuMove
        # - buttons that actually do LITERALLY ANYTHING
            # - tie into playerMove

