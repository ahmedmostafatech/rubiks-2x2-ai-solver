"""
bfs.py  --  Breadth-First Search
Owner: Member 1 (Ahmed)

BFS explores the cube level by level: all states 1 move away, then 2 moves
away, and so on. That's why it always finds the SHORTEST solution, but it can
get slow because the number of states grows really fast.

STUB for now: returns a fixed fake answer.
"""
from src.cube import SOLVED, FAKE_SOLUTION


def solve(state):
    """Solve the cube with BFS.

    Returns a pair: (list_of_moves, nodes_expanded)
      - list_of_moves: for example ["R", "U", "R'"]. Empty list if already solved.
      - nodes_expanded: how many states the search looked at (for the benchmark).
    """
    if state == SOLVED:
        return [], 1
    # STUB: fake solution and a fake node count
    return list(FAKE_SOLUTION), 1000
