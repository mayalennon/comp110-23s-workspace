"""EX03 Wordle!"""

__author__ = "730521406"

def contains_char(guess_word: str, char: str) -> bool:
    """Finding if is a letter is in the word"""
    assert len(char) == 1
    idx: int = 0
    found: bool = False

    while (idx < len(guess_word)):
        if (guess_word[idx] == char):
            found = True
        idx =idx + 1
    
    return found

def emojified(guess: str, secret_word: str) -> str:
    """using emojis to represent letter placements"""
    assert len(guess) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C" 
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    idx: int = 0
    result_output: str = ""

    while (idx < len(guess)):
        if (guess[idx] == secret_word[idx]):
            result_output = result_output + GREEN_BOX
        else:
            if contains_char(secret_word,guess[idx]): 
                result_output = result_output + YELLOW_BOX
            if True != contains_char(secret_word,guess[idx]):
                result_output = result_output + WHITE_BOX
        idx = idx + 1

    return result_output

def input_guess(expected_length: int) -> str:
    
    guess_word: str = input(f"Enter a {expected_length} character word: ")

    while (expected_length) != len(guess_word):
        guess_word = input(f"That wasn't {expected_length} chars! Try again: ")
    
    return guess_word

def main() -> None:
    secret_word: str = "codes"
    guess_word: str = ""
    turn: int = 1
    """The entrypoint of the game and main game loop"""
    """Keep track of the number of turns, if they have the word right, control the flow"""

    while(turn <= 6):
        print(f"=== Turn {turn}/6 ===")
        guess_word = input_guess(len(secret_word))
        print(emojified(guess_word,secret_word))
        if(guess_word == secret_word):
            print(f"You won in {turn}/6 turns!")
            return
        if(turn == 6):
            print("x/6 - Sorry, try again tomorrow!")
        turn = turn + 1
    return

if __name__ == "__main__":
    main()