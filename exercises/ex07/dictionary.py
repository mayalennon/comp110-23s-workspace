"""EX07 List utility test functions!"""

__author__ = "730521406"

def invert(given: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, returns an inverted dictionary where the keys and values are flipped."""
    invert_dict: dict[str,str] = {}
    for key in given:
        if given[key] in invert_dict:
            raise KeyError("Sorry, I cannot continue!")
        invert_dict[given[key]] = key
        
    return invert_dict

def favorite_color(given: dict[str, str]) -> str:
    """Given a dict, returns the color that appears the most."""
    color_count: dict = {}
    for color in given.values():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    max_color = ""
    max_count = 0
    for color, count in color_count.items():
        if count > max_count:
            max_color = color
            max_count = count

    return max_color


def count(given: list[str]) -> dict[str,int]:
    """Given a list, returns a lists of only evens from the given list."""
    count_dict: dict[str, int] = {}
    for item in given:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
    
    
