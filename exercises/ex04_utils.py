"""ex04_utils, reproducing tried and true abstractions of the past."""

__author__ = "730521406"


def all(num_list: list[int], given_num: int) -> bool:
    """Do all numbers match?"""
    all_nums_match: bool = False
    idx: int = 0

    if (len(num_list) == 0):
        return all_nums_match   
    while (idx < len(num_list)):
        if (num_list[idx] != given_num):
            return all_nums_match
        idx = idx + 1
    all_nums_match = True
    return all_nums_match


def max(num_list: list[int]) -> int:
    """Find the largest int in a list."""
    if len(num_list) == 0:
        raise ValueError("max() arg is an empty List")
    
    idx: int = 0
    max_num: int = num_list[0]

    while (idx < (len(num_list) - 1)):
        if (num_list[idx + 1] >= max_num):
            max_num = num_list[idx + 1]
        idx = idx + 1
    return max_num


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Are to lists equal?"""
    idx: int = 0
    equality: bool = False
    if (len(first_list) == len(second_list)):
        while (idx < len(first_list)):
            if (first_list[idx] != second_list[idx]):
                return equality
            idx = idx + 1
        equality = True
        return equality
    else:
        return equality
