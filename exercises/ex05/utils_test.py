"""EX04 List utility test tests!"""

__author__ = "730521406"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat
from exercises.ex05.utils import sub


def test_empty() -> None:
    """Empty test for only_evens."""
    assert only_evens([]) == list()


def test_many() -> None:
    """Regular test for only_evens."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(test_list) == [2, 4, 6]


def test_many_with_negative() -> None:
    """Regular test using negatives for only_evens."""
    test_list: list[int] = [-4, -2, 0, 1, 3]
    assert only_evens(test_list) == [-4, -2, 0]


def test_two_empty_parameters() -> None:
    """Empty test for concat function."""
    assert concat([], []) == list()


def test_regular() -> None:
    """Regular test for the concat functon."""
    a_list: list[int] = [1, 2, 3]
    b_list: list[int] = [4, 5, 6]
    assert concat(a_list, b_list) == [1, 2, 3, 4, 5, 6]


def test_same_list() -> None:
    """Test using same list for concat function."""
    a_list: list[int] = [-4, -2, 0, 1, 3]
    b_list: list[int] = a_list
    assert concat(a_list, b_list) == [-4, -2, 0, 1, 3, -4, -2, 0, 1, 3]


def test_empty_list() -> None:
    """Empty test list for sub function."""
    assert sub([], 0, 0) == list()


def test_normal() -> None:
    """Normal test for sub function."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    start_idx: int = 3
    end_idx: int = 5
    assert sub(test_list, start_idx, end_idx) == [4, 5]


def test_negative_idx() -> None:
    """Test using a negative index for sub function."""
    test_list: list[int] = [1, 2, 3, 4, 5, 6]
    start_idx: int = -2
    end_idx: int = 2
    assert sub(test_list, start_idx, end_idx) == [1, 2]