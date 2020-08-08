import json

# initializes a number of starting values for the marbles
marblesNum = 4

# imports list of gamestates
with open("gamestates.json", 'r') as G:
    gamestates = json.load(G)

# initializes an empty list for the marbles lists to be added into
marbles = []

# verifies the user wants to continue and resets the training data
if input("Do you want to reset M.E.N.A.C.E's training?\n") == "yes":

    # loops through all encountered game states and adds a list of marbles corrosponding to it
    for i in gamestates:
        marbles.append([])

        # loops through each space of the game board and if empty it adds the specified number of marbles for that space
        for j in range(9):
            if i[j] == " ":
                for k in range(marblesNum):
                    marbles[-1].append(j)

    # dumps the new marbles information back into the marbles json file
    with open("marbles.json", "w") as M:
        json.dump(marbles, M, indent=1)
    print("reset complete")
