"""
Module: lab14_tester

Test cases for Lab 14 (Crittres)

DO NOT MODIFY THIS FILE IN ANY WAY!

Author: Sat Garcia (sat@sandiego.edu)
"""

from unittest.mock import Mock, MagicMock, mock_open, patch, call
from lab14_critters import *
import io

def run_tests():

    try:
        # test all of the sloth's methods
        test_sloth_init()
        test_sloth_str()
        test_sloth_get_color()
        test_sloth_eat()
        test_sloth_fight()
        test_sloth_get_move()

        # test all of the cat's methods
        test_cat_init()
        test_cat_str()
        test_cat_get_color()
        test_cat_eat()
        test_cat_fight()
        test_cat_get_move()

        print("Congratulations: All tests PASSED!")

    except AssertionError as e:
        print("\tTest FAILED:", e)



def test_sloth_init():
    print("\nTesting Sloth's __init__ method")
    b = Sloth((5, 3), 2)

    assert 'x' in b.__dict__ and 'y' in b.__dict__, \
        "x and y instance variables not set. Did you call the parent's constructor?"

    assert b.x == 5 and b.y == 3, \
        "Sloth's x and y not set correctly. Did you call the super constructor?"

    print("\tTest of Sloth.__init__ PASSED")

def test_sloth_str():
    print("\nTesting Sloth's __str__ method")
    b = Sloth((0, 0), 2)

    # test __str__ 10 times to make sure it doesn't vary
    for _ in range(10):
        assert str(b) == "S", \
            "Sloth should always return 'S' from __str__"

    print("\tTest of Sloth.__str__ PASSED")

def test_sloth_get_color():
    print("\nTesting Sloth's get_color method")

    b = Sloth((0, 0), 2)
    sloth_color = b.get_color()
    assert sloth_color != "brown" and sloth_color != "black", "Sloth should be any color except black or brown"

    print("\tTest of Sloth.get_color PASSED")

def test_sloth_eat():
    print("\nTesting Sloth's eat method")
    b = Sloth((0, 0), 2)

    # test 10 times to make sure it doesn't vary
    for _ in range(10):
        assert b.eat() == True, "Sloth should always eat"

    print("\tTest of Sloth.eat PASSED")

def test_sloth_fight():
    print("\nTesting Sloth's fight method")
    b = Sloth((0, 0), 2)

    # test 5 times against various opponents to make sure it doesn't vary
    for _ in range(5):
        for opponent in ["C", "?"]:
            assert b.fight(opponent) == Attack.SCRATCH, "Sloth should always SCRATCH"

    print("\tTest of Sloth.fight PASSED")

def test_sloth_get_move():
    print("\nTesting Sloth's get_move method")
    b = Sloth((0, 0), 3)

    neighbors = {Direction.NORTH: None,
                 Direction.EAST: None,
                 Direction.SOUTH: None,
                 Direction.WEST: None}

    print("\tTesting movement of new Sloth with speed 3 for 10 turns.")

    expected_moves = [Direction.EAST, Direction.CENTER, Direction.CENTER] * 3
    expected_moves.append(Direction.EAST)

    actual_moves = [b.get_move(neighbors) for _ in range(10)]

    assert actual_moves == expected_moves, \
        "Expected first 10 moves: %s\nActual first 10 moves: %s" % (expected_moves, actual_moves)

    print("\tTesting movement of new Sloth with speed 2 for 10 turns.")
    b = Sloth((0, 0), 2)

    expected_moves = [Direction.EAST, Direction.CENTER] * 5

    actual_moves = [b.get_move(neighbors) for _ in range(10)]

    assert actual_moves == expected_moves, \
        "Expected first 10 moves: %s\nActual first 10 moves: %s" % (expected_moves, actual_moves)

    print("\tTest of Sloth.get_move PASSED")


def test_cat_init():
    print("\nTesting ScaredCat's __init__ method")
    l = ScaredCat((5, 3))

    assert 'x' in l.__dict__ and 'y' in l.__dict__, \
        "x and y instance variables not set. Did you call the parent's constructor?"

    assert l.x == 5 and l.y == 3, \
        "x and y not set correctly. Did you call the parent's constructor?"

    print("\tTest of ScaredCat.__init__ PASSED")

def test_cat_str():
    print("\nTesting ScaredCat's __str__ method")
    l = ScaredCat((0, 0))

    # test __str__ 10 times to make sure it doesn't vary
    for _ in range(10):
        assert str(l) == "!", \
            "ScaredCat should always return '!' from __str__"

    print("\tTest of ScaredCat.__str__ PASSED")

def test_cat_get_color():
    print("\nTesting ScaredCat's get_color method")

    l = ScaredCat((0, 0))

    expected_color = "red"

    # test 10 times to make sure it doesn't vary
    for _ in range(10):
        assert l.get_color() == expected_color, \
            "ScaredCat always return 'red' from get_color"

    print("\tTest of ScaredCat.get_color PASSED")

def test_cat_eat():
    print("\nTesting ScaredCat's eat method")
    l = ScaredCat((0, 0))

    # test 10 times to make sure it doesn't vary
    for _ in range(10):
        assert l.eat() == False, "ScaredCat should never eat (i.e. always return False)"

    print("\tTest of ScaredCat.eat PASSED")

def test_cat_fight():
    print("\nTesting ScaredCat's fight method")
    l = ScaredCat((0, 0))


    # test 10 times to make sure it doesn't vary
    for _ in range(10):
        assert l.fight("M") == Attack.FORFEIT, "ScaredCat should always FORFEIT."

    print("\tTest of ScaredCat.fight PASSED")

def get_neighbors(open_dir):
    # Returns neighbors dictionary, with all neighbors set to "M" except the
    # direction specified by open_dir, which will be None. If open_dir is
    # None, then all neighbors will be "M"

    neighbors = {Direction.NORTH: "M",
                 Direction.EAST: "M",
                 Direction.SOUTH: "M",
                 Direction.WEST: "M"}

    if open_dir is not None:
        neighbors[open_dir] = None

    return neighbors


def test_cat_get_move():
    print("\nTesting ScaredCat's get_move method")
    l = ScaredCat((0, 0))

    expected_moves = [Direction.NORTH, Direction.EAST, Direction.SOUTH,
                      Direction.WEST, Direction.CENTER]

    print("\tTesting when all directions except one have a critter")
    for (i, d) in enumerate([Direction.NORTH, Direction.EAST, Direction.SOUTH,
                        Direction.WEST]):
        neighbors = get_neighbors(d)
        actual_move = l.get_move(neighbors)
        expected_move = expected_moves[i]
        assert actual_move == expected_move, f"Expected: {expected_move}, Actual: {actual_move}"


    print("\tTesting when two directions (EAST and SOUTH) have no critters.")
    neighbors = {Direction.NORTH: "M",
                 Direction.EAST: None,
                 Direction.SOUTH: None,
                 Direction.WEST: "M"}
    actual_move = l.get_move(neighbors)
    assert actual_move == Direction.EAST, f"Expected to go first open dir (EAST), but went {actual_move}"

    print("\tTesting when there are critters in every direction")
    neighbors = get_neighbors(None)

    actual_move = l.get_move(neighbors)
    assert actual_move == Direction.CENTER, f"Expected to not move (CENTER), but went {actual_move}"
    print("\tTest of ScaredCat.get_move PASSED")



if __name__ == "__main__":
    run_tests()
