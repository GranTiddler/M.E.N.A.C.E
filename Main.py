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
    playermove = int(input("make a move\n")) - 1
    while True:
        if board.board[playermove] == " ":
            board.board[playermove] = "X"
            return
        else:
            playermove = int(input("make a valid move\n")) - 1


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

    def punish(self, reward):
        self.update()
        for i in range(reward):
            for j in cpu.usedMarbles:
                if len(self.marbles[j]) > 0:
                    self.marbles[j].remove(cpu.usedMarbles[j])
                else:
                    break
        self.dump()

    def reward(self, reward):
        self.update()
        for i in range(reward):
            for j in cpu.usedMarbles:
                self.marbles[j].append(cpu.usedMarbles[j])
        self.dump()


class CPU:
    def __init__(self):
        self.gamestates = board.gamestates
        self.marbles = board.marbles
        self.usedMarbles = dict()

    def update(self):
        db.update()
        self.gamestates = board.gamestates
        self.marbles = board.marbles

    def move(self):

        gamestate = board.get_gamestate()
        self.update()
        if self.marbles[gamestate]:
            choice = random.choice(self.marbles[gamestate])
            self.usedMarbles[gamestate] = choice

            board.board[choice] = "O"
            board.demanipulate()
        else:
            print("M.E.N.A.C.E. has resigned")
            board.winner = "X"


# configurations for learning
win = 3
draw = 1
loss = 1


while True:
    db = DB()
    board = BoardTools.Board(db.gamestates, db.marbles)
    cpu = CPU()
    print("resetting")
    player = 0

    while True:
        if player == 0:
            cpu.move()
            board.check_win()
            print_board()
            player = 1
        elif player == 1:
            player_move()
            print_board()
            board.check_win()
            player = 0

        if board.winner == "O":
            db.reward(win)
            break
        elif board.winner == "X":
            db.punish(loss)
            break
        elif " " not in board.board:
            db.reward(draw)
            db.dump()
            print("draw")
            break

    print(f"{board.winner} Won")

    del board
    del cpu
