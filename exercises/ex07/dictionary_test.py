"""EX07 List utility test tests!"""

__author__ = "730521406"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count
import pytest

#Test cases for invert
with pytest.raises(KeyError):
    my_dictionary = {'maya': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)

def test_no_string() -> None:
    """Regular test using one entry."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}

def test_many_strings() -> None:
    """Regular test for multiple keys."""
    test_dict: dict[str, str] = {'a': 'z', 'b' : 'y', 'c': 'x'}
    assert invert(test_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_one_string() -> None:
    """Regular test using one entry."""
    test_dict: dict[str, str] = {"birds": "bees"}
    assert invert(test_dict) == {"bees": "birds"}

#Test cases for favorite_color
def test_no_string() -> None:
    """Regular test using one entry."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ''

def test_many_strings() -> None:
    """Regular test for multiple keys."""
    test_dict: dict[str, str] = {'maya': 'red', 'max' : 'red', 'mars': 'blue'}
    assert favorite_color(test_dict) == 'red'


def test_one_string() -> None:
    """Regular test using one entry."""
    test_dict: dict[str, str] = {"maya": "red"}
    assert favorite_color(test_dict) == {"red"}
    
#Test cases for count