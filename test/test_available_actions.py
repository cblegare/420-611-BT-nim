from nim import available_actions


def test_empty_board_falsy():
    empty_board = ()

    assert not available_actions(empty_board)


def test_empty_board_empty():
    empty_board = ()
    assert len(available_actions(empty_board)) == 0


def test_documented_example():
    assert {(0, 1), (1, 1), (0, 2)} == set(available_actions([2, 1, 0, 0]))


# TODO: test_available_actions (10 points)
#   Ajouter des tests pour les cas-limites de available_actions
