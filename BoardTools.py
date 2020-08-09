import copy


# mirrors board across the Y axis
def mirror_y(board):
    board = [board[2], board[1], board[0], board[5], board[4], board[3], board[8], board[7], board[6]]
    return board


# mirrors board across the X axis
def mirror_x(board):
    board = [board[6], board[7], board[8], board[3], board[4], board[5], board[0], board[1], board[2]]
    return board


# rotates the game board 90 degrees clockwise
def rotate(board):
    board = [board[6], board[3], board[0], board[7], board[4], board[1], board[8], board[5], board[2]]
    return board


# rotates the game board 90 degrees counter-clockwise
def counter_rotate(board):
    board = [board[2], board[5], board[8], board[1], board[4], board[7], board[0], board[3], board[6]]
    return board


# board class for logic and data storage
class Board:
    def __init__(self, gamestates, marbles):
        self.rotation = None
        self.gamestates = gamestates
        self.marbles = marbles
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.winner = False

    # finds the rotation of the board compared to the list and returns the index of the board
    def find_rotation(self):
        manipulationstate = 0
        timesrun = 0
        self.rotation = [0, 0, 0]
        while True:
            # returns index of board if it is in the list of gamestates
            if self.board in self.gamestates:
                return self.gamestates.index(self.board)

            # manipulates the board up to 12 times and after the 12th time adds the gamestate to the list of gamestates
            if timesrun >= 12:
                print("gamestate not found in gamestates list - adding")
                self.rotation = [0, 0, 0]

                self.marbles.append([])
                var = copy.copy(self.board)
                self.gamestates.append(var)
                del var

                for i in range(9):
                    if self.gamestates[-1][i] == " ":
                        for j in range(4):
                            self.marbles[-1].append(i)
                print("gamestate added")

                return self.gamestates.index(self.board)

            elif manipulationstate == 0:
                self.rotation[0] += 1
                self.board = rotate(self.board)
                manipulationstate = 1
                timesrun += 1

            elif manipulationstate == 1:
                self.rotation[1] += 1
                self.board = mirror_x(self.board)
                manipulationstate = 2
                timesrun += 1

            elif manipulationstate == 2:
                self.rotation[2] += 1
                self.board = mirror_y(self.board)
                manipulationstate = 0
                timesrun += 1

    # finds the inndex of the current gamestate and returns it
    def get_gamestate(self):
        if not self.rotation:
            return self.find_rotation()

        self.manipulate()

        if self.board in self.gamestates:
            return self.gamestates.index(self.board)
        else:
            self.demanipulate()
            self.rotation = [0, 0, 0]
            return self.find_rotation()

    # manipulates the code into the cpu's/gamestate list's orientation
    def manipulate(self):
        if self.rotation != [0, 0, 0]:
            if self.rotation[0] != 0:
                for i in range(self.rotation[0]):
                    self.board = rotate(self.board)
                    del i

            if self.rotation[1] != 0:
                for i in range(self.rotation[1]):
                    self.board = mirror_x(self.board)
                    del i

            if self.rotation[2] != 0:
                for i in range(self.rotation[2]):
                    self.board = mirror_y(self.board)
                    del i

    # manipulates code back to the player's orientation
    def demanipulate(self):
        if self.rotation[2] != 0:
            for i in range(self.rotation[2]):
                self.board = mirror_y(self.board)
                del i

        if self.rotation[1] != 0:
            for i in range(self.rotation[1]):
                self.board = mirror_x(self.board)
                del i

        if self.rotation[0] != 0:
            for i in range(self.rotation[0]):
                self.board = counter_rotate(self.board)
                del i

    # checks if the game has been won yet
    def check_win(self):
        # horizontal
        if self.board[0] == self.board[1] and self.board[1] == self.board[2] and self.board[2] != " ":
            self. winner = self.board[2]
        elif self.board[3] == self.board[4] and self.board[4] == self.board[5] and self.board[5] != " ":
            self. winner = self.board[5]
        elif self.board[6] == self.board[7] and self.board[7] == self.board[8] and self.board[8] != " ":
            self. winner = self.board[8]

        # vertical
        elif self.board[0] == self.board[3] and self.board[3] == self.board[6] and self.board[3] != " ":
            self. winner = self.board[3]
        elif self.board[1] == self.board[4] and self.board[4] == self.board[7] and self.board[4] != " ":
            self. winner = self.board[4]
        elif self.board[2] == self.board[5] and self.board[5] == self.board[8] and self.board[5] != " ":
            self. winner = self.board[0]

        # diagonal
        elif self.board[0] == self.board[4] and self.board[4] == self.board[8] and self.board[4] != " ":
            self. winner = self.board[4]
        elif self.board[2] == self.board[4] and self.board[4] == self.board[6] and self.board[4] != " ":
            self. winner = self.board[4]
        else:
            self.winner = False
