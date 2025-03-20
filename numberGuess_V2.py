"""
Chapter 9 example (page 242-245)
Program: numberGuess_V2.py
3/17/2025

**NOTE: the module breezypythongui.py MUST be in the same directory of this file for the app to run properly

GUI based version of the number guessing fame from Chapter 3
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
import random
# Other imports can go here

# Class Header (class name will change from project to project)
class GuessingGame(EasyFrame):
    
    # Definition of our classes constructor method
    def __init__(self):
        """Comment specific to project"""
        # CALL to the EasyFrame class constructor from breezypythongui.py
        EasyFrame.__init__(self, title = "Guessing Game 2.0", width = 285, height = 160, resizable = False, background = "mediumorchid1")
        # Other components are added here
        # Initialize the instance variables for this class
        self.myNumber = random.randint(1, 100)
        self.count = 0

        # Create and add widgets to the window
        self.hintLabel = self.addLabel(text= "Guess a number between 1 and 100", row= 0, column= 0, sticky= "NSEW", columnspan= 2, background = "mediumorchid1")
        self.addLabel(text= "Your Guess:", row=1, column=0, background = "mediumorchid1", sticky="E")
        self.guessField = self.addIntegerField(value = 0, row= 1, column= 1, sticky= "W")
        self.nextButton = self.addButton(text= "Next", row = 2, column= 0, command= self.nextGuess)
        self.newButton = self.addButton(text= "New Game", row= 2, column= 1, command = self.newGame)

        

    # Definition of the nextGuess() method which handles the Next Button Click
    def nextGuess(self):
        """Process the user's next guess."""
        self.count += 1
        guess = self.guessField.getNumber()
        # Logic that determines the game's outcome
        if guess == self.myNumber:
            self.hintLabel["text"] = "You've guessed it in " + str(self.count) + " attempt(s)!"
            self.nextButton["state"] = "disabled"
        elif guess < self.myNumber:
            self.hintLabel["text"] = "Sorry, your guess was too low!"
        else:
            self.hintLabel["text"] = "Whoops! Your guess was too high!"
    
    # Definition of the newGame() method which handles the New Game button click
    def newGame(self):
        """Resets the data and GUI to their original states."""
        self.myNumber = random.randint(1, 100)
        self.count = 0
        self.hintLabel["text"] = "Guess a number between 1 and 100"
        self.guessField.setNumber(0)
        self.nextButton["state"] = "normal"



# End of class block

# Global definition of the main() function
def main():
    """Instantiate an object from the class into mainloop()"""
    GuessingGame().mainloop()

# Global call to main() for program entry
if __name__ == "__main__":
    main()