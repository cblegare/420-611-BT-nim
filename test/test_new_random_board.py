from random import randint

import pytest
from nim import new_random_board


def test_number_of_piles_negative():
    negative_integer = -4

    with pytest.raises(ValueError):
        new_random_board(negative_integer)


def test_number_of_piles_random():
    random_integer = randint(1, 10)

    assert len(new_random_board(random_integer)) == random_integer


def test_number_of_piles_provided():
    # TODO: (3 points)
    #   Implémenter test_number_of_piles_provided
    ...


def test_number_of_piles_not_provided():
    assert new_random_board()
