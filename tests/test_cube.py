"""
test_cube.py  --  unit tests
Owner: Member 3

These tests already pass with the stub code, so you can see how unittest works.
The real, meaningful tests are the ones marked with @unittest.skip. Remove the
skip line once Member 1 pushes the real cube.py.

Run from the project root:   python -m unittest discover -s tests
"""
import unittest

from src.cube import SOLVED, MOVE_NAMES, inv, apply, scramble, is_solved, get_facelets
from src.solvers import SOLVERS


class TestBasics(unittest.TestCase):
    def test_solved_state_has_8_corners(self):
        cp, co = SOLVED
        self.assertEqual(len(cp), 8)
        self.assertEqual(len(co), 8)

    def test_there_are_9_moves(self):
        self.assertEqual(len(MOVE_NAMES), 9)

    def test_inverse_of_inverse_is_the_same_move(self):
        for m in MOVE_NAMES:
            self.assertEqual(inv(inv(m)), m)

    def test_scramble_returns_the_requested_number_of_moves(self):
        state, moves = scramble(7)
        self.assertEqual(len(moves), 7)

    def test_facelets_gives_24_stickers(self):
        self.assertEqual(len(get_facelets(SOLVED)), 24)

    def test_every_solver_returns_a_list_and_a_node_count(self):
        state, _ = scramble(5)
        for name, solve in SOLVERS.items():
            moves, nodes = solve(state)
            self.assertIsInstance(moves, list, name)
            self.assertIsInstance(nodes, int, name)


class TestRealCube(unittest.TestCase):
    """Enable these once the real cube.py is in."""

    @unittest.skip("enable after the real cube.py is pushed")
    def test_four_turns_come_back_to_start(self):
        for m in ["U", "R", "F"]:
            s = SOLVED
            for _ in range(4):
                s = apply(s, m)
            self.assertEqual(s, SOLVED, m)

    @unittest.skip("enable after the real cube.py is pushed")
    def test_move_then_its_inverse_is_identity(self):
        for m in MOVE_NAMES:
            self.assertEqual(apply(apply(SOLVED, m), inv(m)), SOLVED, m)

    @unittest.skip("enable after the real solvers are pushed")
    def test_every_solver_actually_solves_the_cube(self):
        state, _ = scramble(6)
        for name, solve in SOLVERS.items():
            moves, _ = solve(state)
            s = state
            for m in moves:
                s = apply(s, m)
            self.assertTrue(is_solved(s), name)


if __name__ == "__main__":
    unittest.main()
