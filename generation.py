import random

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

# initialize 2 lists, 1 to act as a buffer to be added to the other list, of which each index corrosponds to the index of the matching gamestate in metalist
marbles = []
bufferList = []
# adds 4 copies of each empty index to the buffer list and appends that to the marbles list
for x in metalist:
    for y in range(0, 9):
        if x[y] == " ":
            for z in range(8):
                bufferList += str(y)
    marbles += ""
    marbles.append(bufferList)


# switches between true and false
def switch(flopPosition):
    if flopPosition == 0:
        return 1
    elif flopPosition == 1:
        return 2
    elif flopPosition == 2:
        return 0


# mirrors the game board to check if it fits
def flopH(lisp, lisp2 = []):
    lisp2 = [lisp[2], lisp[1], lisp[0], lisp[5], lisp[4], lisp[3], lisp[8], lisp[7], lisp[6]]
    return lisp2

def flopY(lisp, lisp2 = []):
    lisp2 = [lisp[6], lisp[7], lisp[8], lisp[3], lisp[4], lisp[5], lisp[0], lisp[1], lisp[2]]
    return lisp2

# rotates the game board to check if it fits
def rotate(lisp, lisp2):
    lisp2 = [lisp[6], lisp[3],lisp[0], lisp[7], lisp[4], lisp[1], lisp[8], lisp[5], lisp[2]]
    return (lisp2)



# manipulates the game board to find which game state it fits
def findState(metalist, gamestate, flopState):
    for i in range (0, 12):
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

    print("gamestate not found")


def printBoard(positions):
    print("""
    """ + positions[0] + """  |  """ + positions[1] + """  |  """ + positions[2] + """  
  _____|_____|____
    """ + positions[3] + """  |  """ + positions[4] + """  |  """ + positions[5] + """ 
  _____|_____|____
    """ + positions[6] + """  |  """ + positions[7] + """  |  """ + positions[8] + """
       |     |
  """)


rotatae = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
for i in range(0, 4):
    printBoard(rotatae)
    rotatae = rotate(rotatae, [])

def findState(metalist, gamestate, flopState):
    for i in range(0, 8):
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
        else:
            gamestate = rotate(gamestate, [])
            flopState = switch(flopState)
            printBoard(gamestate)
            continue
    print("gamestate not found")

