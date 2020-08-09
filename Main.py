import BoardTools
import json
import random


# sets up configurations
with open("config.json", 'r') as config:
    config = json.load(config)

    # configurations for learning rates
    win = config["win"]
    draw = config["draw"]
    loss = config["loss"]

    player1 = config["player1"]
    # deletes config
    del config


# prints game board to the terminal
def print_board():
    print(f"""
      {board.board[0]}  |  {board.board[1]}  |  {board.board[2]}    
    _____|_____|____
      {board.board[3]}  |  {board.board[4]}  |  {board.board[5]}   
    _____|_____|____
      {board.board[6]}  |  {board.board[7]}  |  {board.board[8]}  
         |     |
    """)


# handles json file interactions
class DB:
    # gets data from json files
    def __init__(self):
        with open("gamestates.json", 'r') as G:
            self.gamestates = json.load(G)

        with open("marbles.json", 'r') as M:
            self.marbles = json.load(M)

    # updates data to be consistant with BoardTools.py
    def update(self):
        self.gamestates = board.gamestates
        self.marbles = board.marbles

    # dumps data to json files for future use
    def dump(self):
        self.update()
        with open("marbles.json", "w") as M:
            json.dump(self.marbles, M, indent=1)

        with open("gamestates.json", "w") as G:
            json.dump(self.gamestates, G, indent=1)


# initializes agent class
class Agent:
    def __init__(self, letter, name):
        self.letter = letter
        self.name = name

    def update_board(self, index):
        board.board[index] = self.letter

    def endgame(self, reward):
        pass


# class for cpu object
class CPU(Agent):
    def __init__(self, name, letter="O"):
        super().__init__(letter, name)
        self.gamestates = board.gamestates
        self.marbles = board.marbles
        self.usedMarbles = dict()

    # updates information about marbles and gamestates
    def update(self):
        db.update()
        self.gamestates = db.gamestates
        self.marbles = db.marbles

    # chooses a random move based off marbles list
    def move(self):
        gamestate = board.get_gamestate()
        self.update()

        # verifies that it has choices or resigns
        if self.marbles[gamestate]:
            choice = random.choice(self.marbles[gamestate])
            self.usedMarbles[gamestate] = choice

            self.update_board(choice)
            board.demanipulate()
        else:
            print("M.E.N.A.C.E. has resigned")
            board.winner = "X"

    # handles endgame
    def endgame(self, reward):
        db.update()
        if reward > 0:
            for i in range(reward):
                for j in self.usedMarbles:
                    self.marbles[j].append(self.usedMarbles[j])
        elif reward < 0:
            for i in range(reward):
                for j in self.usedMarbles:
                    if len(self.marbles[j]) > 0:
                        self.marbles[j].remove(self.usedMarbles[j])
                    else:
                        break
        db.dump()


# class for player object
class Player(Agent):
    def __init__(self, name, letter="X"):
        super().__init__(letter, name)

    # gets players input and updates the board
    def move(self):
        playermove = input("make a move\n")
        valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while True:
            if playermove in valid:
                playermove = int(playermove) - 1
            elif playermove in range(9):
                if board.board[playermove] == " ":
                    self.update_board(playermove)
                    return

                else:
                    playermove = int(input("make a valid move\n")) - 1
                    continue


# initializes db
db = DB()


# print instructions and waits 2 seconds
print("""
board positions:
      0  |  1  |  2    
    _____|_____|____
      3  |  4  |  5   
    _____|_____|____
      6  |  7  |  8  
         |     |
""")

wins = [0, 0]
# main loop
while True:
    # (re)initializes classes for use in main loop
    board = BoardTools.Board(db.gamestates, db.marbles)
    p1 = CPU("CPU", "O")
    p2 = Player("Player", "X")

    # configuration for who goes first ( 0 = cpu 1 = player
    player = player1

    # game loop
    while True:
        # switches between player's and cpu's turn
        print_board()
        if player == 0:
            p1.move()
            player = 1
        elif player == 1:
            p2.move()
            player = 0

        board.check_win()

        # executes endgame functions based on a winner or a draw
        if board.winner == p1.letter:
            print(f"{p1.name} won")
            p1.endgame(win)
            wins[0] += 1
            break
        elif board.winner == p2.letter:
            print(f"{p2.name} won")
            p2.endgame(loss)
            wins[1] += 1
            break
        elif " " not in board.board:
            p1.endgame(draw)
            p2.endgame(draw)
            db.dump()
            break

    # deletes board and cpu objects to clear data
    del board
    del p1
    del p2
