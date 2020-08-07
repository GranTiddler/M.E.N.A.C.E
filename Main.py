import BoardTools
import json
import random


def print_board():
    print(f"""
          {board.board[0]}  |  {board.board[1]}  |  {board.board[2]}    
        _____|_____|____
          {board.board[3]}  |  {board.board[4]}  |  {board.board[5]}   
        _____|_____|____
          {board.board[6]}  |  {board.board[7]}  |  {board.board[8]}  
             |     |
        """)


def player_move():
    player = int(input("make a move\n")) - 1
    while True:
        if board.board[player] == " ":
            board.board[player] = "X"
            return
        else:
            player = int(input("make a valid move\n")) - 1


class DB:
    def __init__(self):
        with open("gamestates.json", 'r') as G:
            self.gamestates = json.load(G)

        with open("marbles.json", 'r') as M:
            self.marbles = json.load(M)

    def update(self):
        self.gamestates = board.gamestates
        self.marbles = board.marbles

    def dump(self):
        self.update()
        with open("marbles.json", "w") as M:
            json.dump(self.marbles, M, indent=1)

        with open("gamestates.json", "w") as G:
            json.dump(self.gamestates, G, indent=1)

    def punish(self):
        for i in cpu.usedMarbles:
            self.marbles[i].remove(cpu.usedMarbles[i])
        self.dump()

    def reward(self):
        for i in cpu.usedMarbles:
            self.marbles[i].append(cpu.usedMarbles[i])
            self.dump()


class CPU:
    def __init__(self, gamestates, marbles):
        self.gamestates = gamestates
        self.marbles = marbles
        self.usedMarbles = dict()

    def update(self):
        db.update()
        self.gamestates = board.gamestates
        self.marbles = board.marbles

    def move(self):
        gamestate = board.get_gamestate()
        self.update()
        choice = random.choice(self.marbles[gamestate])
        self.usedMarbles[gamestate] = choice

        board.board[choice] = "O"
        board.demanipulate()


while True:
    db = DB()
    board = BoardTools.Board(db.gamestates, db.marbles)
    cpu = CPU(db.gamestates, db.marbles)
    print("resetting")

    while True:
        cpu.move()
        board.check_win()
        print_board()
        if board.winner == "O":
            db.reward()
            break
        elif " " not in board.board:
            db.dump()
        player_move()
        print_board()
        board.check_win()
        if board.winner == "X":
            db.punish()
            break
        elif " " not in board.board:
            db.dump()

    print(f"{board.winner} Won")

    del board
    del cpu
