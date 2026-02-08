# rock paper scissors game created with functions and a main block
import random
import time


class RPSGame:
    debug = False
    choices = {
        "R" : "Rock",
        "S" : "Scissors",
        "P" : "Paper"
    }
    playerChoice = ""
    computerChoice = ""
    valids = ['R','P','S','X']
    names = { 
            'R' : "Rock",
            'S' : "Scissors",
            'P' : "Paper"
            }

    def getPlayerChoice(self):
        self.playerChoice = ""
        if self.debug:
            print("\n")
            return random.choice(self.valids)
        
        while self.playerChoice not in self.valids:
            self.playerChoice = input("Make your move:\nR rock\nP paper\nS scissors\nX Quit\n>").upper()
            if self.playerChoice not in self.valids:
                print("That is not a valid choice\n")

    def getComputerChoice(self):
        self.computerChoice = random.choice(['R','P','S'])

    def showChoices(self):
        print(f"Player chooses {self.names[self.playerChoice]}")
        print(f"Computer chooses {self.names[self.computerChoice]}")

    def pwins(self):
        score = {
            'R' : 1,
            'P' : 2,
            'S' : 3
        }
        diff = score[self.playerChoice] - score[self.computerChoice]
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

    def result(self,score):
        return( {1:"Player wins,",0:"Tie,",-1:"Player Loses,"}[score])

    def resultMsg(self):
        a = self.playerChoice
        b = self.computerChoice
        # I got lazy here and decided to not change the variable names for a and b
        if a == b:
            return f"Both chose {self.names[a]}"
        game = [a,b]
        game.sort()
        #print(game)
        if game == ['P','R']:
            return "Paper covers rock!"
        elif game == ['P','S']:
            return "Scissors cuts paper!"
        elif game == ['R','S']:
            return "Rock crushes scissors!"

    def __init__(self):
        while self.playerChoice != "X":
            self.getPlayerChoice()
            if self.playerChoice != "X":
                self.getComputerChoice()
                self.showChoices()
                time.sleep(1)
                print( self.result( self.pwins()) , end=" ") 
                print( self.resultMsg())
                print("")


game = RPSGame()