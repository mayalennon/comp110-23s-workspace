"""Practice Writing Functions!"""

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if(len(my_words)> letter_idx):
        letter: str = my_words[letter_idx]
        return(letter)
    return("Too high of an index")
    



print(mimic_letter("Hello",3))
print(mimic_letter("Hello",5))

