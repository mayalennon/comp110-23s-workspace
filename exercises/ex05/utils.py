"""EX04 List utility test functions!"""

__author__ = "730521406"


def only_evens(num_list: list[int]) -> list[int]:
    """Given a list, returns a lists of only evens from the given list."""
    even_list: list[int] = list()
    for idx in range(0, len(num_list)):
        if ((num_list[idx] % 2 == 0)):
            even_list.append(num_list[idx])
    return even_list


def concat(a_list: list[int], b_list: list[int]) -> list[int]:
    """Give two list, reutrns all elements from from both lists."""
    total_list: list[int] = list()
    for idx in range(0, len(a_list)):
        total_list.append(a_list[idx])
    for index in range(0, len(b_list)):
        total_list.append(b_list[index])
    return total_list


def sub(num_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Gives all the elements in a list from the start index given to but not including the end index."""
    sub_list: list[int] = list()
    if (len(num_list) == 0) or (start_idx >= (len(num_list))) or (0 >= end_idx):
        return sub_list
    if start_idx < 0:
        start_idx = 0
    if end_idx > len(num_list):
        end_idx = len(num_list)
    for idx in range(start_idx, end_idx):
        sub_list.append(num_list[idx])
    return sub_list
