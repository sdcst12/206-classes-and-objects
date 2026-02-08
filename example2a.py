# rock paper scissors game created with functions and a main block
import random
import time


debug = False

def playerChoice(testing):
    choice = ""
    valids = ['R','P','S']
    names = { 
        'R' : "Rock",
        'S' : "Scissors",
        'P' : "Paper"
        }

    if testing:
        return random.choice(valids)
    
    while choice not in valids:
        choice = input("Make your move:\nR rock\nP paper\nS scissors\n>")
        if choice not in valids:
            print("That is not a valid choice\n")
    print("\n")
    return choice

def computerChoice():
    return random.choice(['R','P','S'])

def pwins(p,c):
    score = {
        'R' : 1,
        'P' : 2,
        'S' : 3
    }
    diff = score[p] - score[c]
    if diff == 0:
        return 0
    if diff in [-2,1]:
        return 1
    else:
        return -1
    """
    R P -1 L
    R S -2 W
    P R 1 W
    P S -1 L
    S P 1 W
    S R 2 L
    """

def result(score):
    return( {1:"Player wins!",0:"Tie!",-1:"Player Loses"}[score])

def resultMsg(a,b):
    if a == b:
        return f"Both chose {a}"
    game = [a,b]
    game.sort()
    #print(game)
    if game == ['P','R']:
        return "Paper covers rock"
    elif game == ['P','S']:
        return "Scissors cuts paper!"
    elif game == ['R','S']:
        return "Rock crushers scissors!"

if __name__ == "__main__":
    while True:
        player = playerChoice(debug)
        computer = computerChoice()
        time.sleep(1)

        print( result( pwins(player,computer)))
        print( resultMsg(player,computer))
        print("")