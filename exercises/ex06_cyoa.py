"""EX06 Choose your own adventure!"""

__author__ = "730521406"

import random

player: str = ""
points: int = 0 
STAR: str = "\U00002B50"

def main() -> None:
    """This function contains our main body of code."""

    global points
    global player
    
    greet()
    print(f"{STAR} Hello {player}! {STAR}\n, I can give you the following options:\n1) I love the Chipmunks!\n2) I am only here for money.\n3) I would like to end the quiz. {STAR}")
    answer: int = int(input(f"{STAR} Please select your answer using the number it is associated with(1, 2, or 3) {STAR} "))
    while (answer != 1):
        if answer in [2, 3]:
            break
        answer: int = int(input("Sorry, please pick one of the options provided above(1, 2, or 3)"))

    if answer == 1:
        shirt_question()
        icecream_question() 
        exit()
    if answer == 2:
        shirt_question()
        points = money_question(points)
        icecream_question()
        print("You thought you were gonna be a chimpunk, but you just like money!\nYou're Uncle Ian")
        exit()
    if answer == 3:
        print(f"ByeBye!\nAchievement Points: {points}")
        exit()

def greet() -> None:
    """This function greets the user."""
    global player
    print("Which Chipmunk are you?\nWelcome to the game!\nif you were in the movie, \n\"Alvin and the Chipmunks\", who would you be?")
    player = input("Before we get started,\nwhat is your name? ")

def shirt_question() -> None:
    "This function asks the player their favorite color."
    global points
    print(f"{STAR} {player}, quick! {STAR}")
    print(f"{STAR} If you had to wear one color for the rest your life, which one would it be? {STAR}\n1) Red\n2) Blue\n3) Green")
    fav_color: int = int(input(f"{STAR} Please select your answer using the number it is associated with(1, 2, or 3) {STAR} "))
    while (fav_color != 1):
        if fav_color in [2, 3]:
            break
        fav_color: int = int(input("Sorry, please pick one of the options provided above(1, 2, or 3)"))
    
    if fav_color == 1:
        points += 5
    if fav_color == 2:
        points += 3
    if fav_color == 3:
        points +=  7
        
def money_question(points_earned: int) -> int:
    "A little joke for the game."
    print(f"{STAR} Next question! {STAR}\nYou currently have {points_earned} bucks!")
    more_money: str = input("If you would like more money, please print \"yes\" ")
    if more_money == "yes" or "Yes":
        print(f"Silly {player}, you don't get any!")
        points_earned -= 3
        return points_earned

def icecream_question() -> None:
    "This function asks the player their favorite ice-cream flavor."
    global points
    print(f"{STAR} {player}! {STAR}")
    print(f"{STAR} The chipmunks love ice cream! What is your favorite flavor? {STAR}\n1) Rocky Road\n2) Cotton Candy\n3) Mint Chocolate Chip")
    fav_color: int = int(input(f"{STAR} Please select your answer using the number it is associated with(1, 2, or 3) {STAR} "))
    while (fav_color != 1):
        if fav_color in [2, 3]:
            break
        fav_color: int = int(input("Sorry, please pick one of the options provided above(1, 2, or 3)"))
    
    if fav_color == 1:
        points += 5
    if fav_color == 2:
        points += 3
    if fav_color == 3:
        points +=  7

    print(f"{player}, all signs are pointing to you being {who_are_you()}")
    go_on: int = int(input("Would you like to:\n1) stop here\n2) keep going\n"))
    if go_on == 1:
        final_answer()

def who_are_you() -> str:
    """Returns what Chipmunk the player is."""
    global points 
    result: str = ""
    if points in [10, 7]:
        result = "Alvin"
        return result
    if points in [6, 3]:
        result = "Simon"
        return result
    if points in [14, 11]:
        result = "Theodore" 
        return result
    if points not in [3, 6, 7, 10, 11, 14]:
        poss_list: list[str] = ["Alvin", "Simon", "Theodore"]
        idx: int = random.randint(1,3)
        result = poss_list(idx)
        return result
    

def final_answer() -> None:
    """Give the final result."""
    global points
    print(f"{STAR} You have finished the quiz {player}! {STAR}")
    print(f"With a total of . . . {points} points . . .\n . . . you are . . .\n{who_are_you()}")
    exit()

if __name__ == "__main__":
    main()

