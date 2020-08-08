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

    # config for player 1
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


# gets players input and updates the board
def player_move():
    playermove = input("make a move\n")
    valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:
        if playermove in valid:
            playermove = int(playermove) - 1
        elif playermove in range(9):
            if board.board[playermove] == " ":
                board.board[playermove] = "X"
                return
        else:
            playermove = int(input("make a valid move\n")) - 1


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

    # removes choices from marbles and dumps to json files
    def punish(self, reward):
        self.update()
        for i in range(reward):
            for j in cpu.usedMarbles:
                if len(self.marbles[j]) > 0:
                    self.marbles[j].remove(cpu.usedMarbles[j])
                else:
                    break
        self.dump()

    # adds marbles and dumps to json file
    def reward(self, reward):
        self.update()
        for i in range(reward):
            for j in cpu.usedMarbles:
                self.marbles[j].append(cpu.usedMarbles[j])
        self.dump()

    def endgame(self, reward):
        if reward > 0:
            self.reward(reward)
        elif reward < 0:
            self.punish(reward)


# class for cpu object
class CPU:
    def __init__(self):
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

            board.board[choice] = "O"
            board.demanipulate()
        else:
            print("M.E.N.A.C.E. has resigned")
            board.winner = "X"


# main loop
while True:
    # (re)initializes classes for use in main loop
    db = DB()
    board = BoardTools.Board(db.gamestates, db.marbles)
    cpu = CPU()
    print("resetting")

    # configuration for who goes first ( 0 = cpu 1 = player
    player = player1

    # game loop
    while True:
        # switches between player's and cpu's turn
        if player == 0:
            cpu.move()
            player = 1
        elif player == 1:
            print_board()
            player_move()
            player = 0

        board.check_win()

        # executes endgame functions based on a winner or a draw
        if board.winner == "O":
            print("you lost")
            db.endgame(win)
            break
        elif board.winner == "X":
            db.endgame(loss)
            print("you won")
            break
        elif " " not in board.board:
            db.endgame(draw)
            db.dump()
            print("draw")
            break

    # deletes board and cpu objects to clear data
    del board
    del cpu
