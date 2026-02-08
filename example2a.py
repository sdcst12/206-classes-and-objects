# rock paper scissors game created with functions and a main block
import random
import time


debug = False
choices = {
    "R" : "Rock",
    "S" : "Scissors",
    "P" : "Paper"
}

def playerChoice(testing):
    choice = ""
    valids = ['R','P','S','X']
    names = { 
        'R' : "Rock",
        'S' : "Scissors",
        'P' : "Paper"
        }

    if testing:
        print("\n")
        return random.choice(valids)
    
    while choice not in valids:
        choice = input("Make your move:\nR rock\nP paper\nS scissors\nX Quit\n>").upper()
        if choice not in valids:
            print("That is not a valid choice\n")
    return choice

def computerChoice():
    return random.choice(['R','P','S'])

def showChoices(player,computer):
    print(f"Player chooses {choices[player]}")
    print(f"Computer chooses {choices[computer]}")

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
    return( {1:"Player wins,",0:"Tie,",-1:"Player Loses,"}[score])

def resultMsg(a,b):
    if a == b:
        return f"Both chose {choices[a]}"
    game = [a,b]
    game.sort()
    #print(game)
    if game == ['P','R']:
        return "Paper covers rock!"
    elif game == ['P','S']:
        return "Scissors cuts paper!"
    elif game == ['R','S']:
        return "Rock crushes scissors!"

if __name__ == "__main__":
    player = ""
    while player != "X":
        player = playerChoice(debug)
        if player != "X":
            computer = computerChoice()
            showChoices(player,computer)
            time.sleep(1)
            print( result( pwins(player,computer)) , end=" ") 
            print( resultMsg(player,computer))
            print("")