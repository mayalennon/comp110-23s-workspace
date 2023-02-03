"""Asks user for a number, goes until they get it right"""

SECRET: int = 4
guess: int = int(input("Guess a number! "))
playing: bool = True
i: int = 0


while playing:
    if i == 3:
        print("One more guess!")
        playing = False
    if guess == SECRET:
        print("Yay! You got it right")
        playing = False
    else:
        print("Wrong number. :(")
        if guess % 2 == 1: #guess is odd
            print("Your guess is odd, the answer is even.")
        if guess > SECRET:
            print("Your guess is too high!")
        else: #guess < SECRET
            print("Your guess is too low. ")
        print(f"You have {4-i} guesses left")
        guess = int(input("Make another guess! "))
        i = i + 1
