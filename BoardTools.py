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


class Board:
    def __init__(self, gamestates, marbles):
        self.rotation = None
        self.gamestates = gamestates
        self.marbles = marbles
        self.usedMarbles = dict()
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.winner = False

    def find_rotation(self):
        manipulationstate = 0
        timesrun = 0
        self.rotation = [0, 0, 0]
        while True:
            if self.board in self.gamestates:
                print(f"Found rotation:{self.rotation}")
                return self.gamestates.index(self.board)

            if timesrun >= 12:
                self.rotation = [0, 0, 0]
                self.gamestates.append(self.board)
                print("gamestate not found in gamestates list - adding")

                self.marbles.append([])

                for i in range(9):
                    if self.gamestates[-1][i] == " ":
                        for j in range(4):
                            self.marbles[-1].append(i)

                print(self.board)
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

    def get_gamestate(self):
        if not self.rotation:
            return self.find_rotation()

        self.manipulate()

        if self.board in self.gamestates:
            print("Found gamestate")

            return self.gamestates.index(self.board)
        else:
            self.demanipulate()
            print("did not find gamestate - rotation value incorrect")
            self.rotation = [0, 0, 0]
            return self.find_rotation()

    def manipulate(self):
        if self.rotation != [0, 0, 0]:
            if self.rotation[0] != 0:
                for i in range(4 % self.rotation[0]):
                    self.board = rotate(self.board)
                    del i

            if self.rotation[1] != 0:
                for i in range(4 % self.rotation[1] + 1):
                    self.board = mirror_x(self.board)
                    del i

            if self.rotation[2] != 0:
                for i in range(4 % self.rotation[2] + 1):
                    self.board = mirror_y(self.board)
                    del i

    def demanipulate(self):
        if self.rotation[0] != 0:
            for i in range(4 % self.rotation[0] + 1):
                self.board = counter_rotate(self.board)
                del i

        if self.rotation[1] != 0:
            for i in range(4 % self.rotation[1] + 1):
                self.board = mirror_x(self.board)
                del i

        if self.rotation[2] != 0:
            for i in range(4 % self.rotation[2] + 1):
                self.board = mirror_y(self.board)
                del i

    def check_win(self):
        if self.board[4] == self.board[1] and self.board[4] == self.board[7 and self.board[4] != " "]:
            self. winner = self.board[4]
        elif self.board[4] == self.board[3] and self.board[4] == self.board[5] and self.board[4] != " ":
            self. winner = self.board[4]
        elif self.board[4] == self.board[2] and self.board[4] == self.board[6] and self.board[4] != " ":
            self. winner = self.board[4]
        elif self.board[4] == self.board[0] and self.board[4] == self.board[8] and self.board[4] != " ":
            self. winner = self.board[4]
        elif self.board[0] == self.board[1] and self.board[0] == self.board[2] and self.board[0] != " ":
            self. winner = self.board[0]
        elif self.board[0] == self.board[3] and self.board[0] == self.board[6] and self.board[0] != " ":
            self. winner = self.board[0]
        elif self.board[8] == self.board[7] and self.board[8] == self.board[6] and self.board[8] != " ":
            self. winner = self.board[8]
        elif self.board[8] == self.board[2] and self.board[8] == self.board[5] and self.board[8] != " ":
            self. winner = self.board[8]
        else:
            self.winner = False
