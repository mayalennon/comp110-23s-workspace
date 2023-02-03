"""EX02 One Shot Wordle."""

__author__ = "730521406"

secret_word: str = "python"
secret_word_len: int = len(secret_word)
guess_word: str = input("What is your 6-letter guess? ")

while (len(guess_word) != secret_word_len):
    guess_word = input(f"That was not {secret_word_len} letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

correct_counter: int = 0
idx: int = 0
result_output: str = ""

while (idx < len(guess_word)):
    if (guess_word[idx] == secret_word[idx]):
        correct_counter = correct_counter + 1
        result_output = result_output + GREEN_BOX
    else:
        index: int = 0
        found_letter: bool = False
        while (index < secret_word_len):
            if (guess_word[idx] == secret_word[index]):
                found_letter = True
            index = index + 1
        if (found_letter):
            result_output = result_output + YELLOW_BOX
        else:
            result_output = result_output + WHITE_BOX
    idx = idx + 1

print(result_output)
if (correct_counter == len(guess_word)):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
