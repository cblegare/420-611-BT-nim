from random import randint

import pytest

from nim import new_random_board


def test_num_heaps_negative():
    negative_integer = -4

    with pytest.raises(ValueError):
        new_random_board(negative_integer)


def test_num_heaps_random():
    random_integer = randint(1, 10)

    assert len(new_random_board(random_integer)) == random_integer


def test_num_heaps_provided():
    # TODO: test_num_heaps_provided (3 points)
    #   Implémenter test_num_heaps_provided
    ...


def test_num_heaps_not_provided():
    assert new_random_board()
