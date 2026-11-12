"""
greedy.py  --  Greedy Best-First Search
Owner: Member 3

Your algorithm! The idea is super simple:
  - Look at the cube, try every move, and look at the new states.
  - Pick the state that LOOKS closest to solved and continue from there.
"Looks closest" = our own heuristic: how many corner cubies are NOT in the
right place (fewer = better).

Why it's cool for the project: it's fast, but it does NOT guarantee the
shortest solution, and sometimes it gets stuck. We'll show that in the
comparison against BFS / IDA*, and it's a classic oral question:
"why isn't greedy optimal?"

Tips:
  - Use a priority queue (heapq) ordered by the heuristic value.
  - Keep a `visited` set so you don't loop forever.
  - Add a max_nodes limit so the program never hangs.

STUB for now: returns a fixed fake answer. Replace the body, keep the signature.
"""
from src.cube import SOLVED, FAKE_SOLUTION


def misplaced_corners(state):
    """Heuristic: number of corner cubies that are not in their solved slot.

    TODO (Member 3): implement this. It should return 0 for SOLVED.
    STUB: always returns 0.
    """
    return 0


def solve(state, max_nodes=50000):
    """Solve the cube with Greedy Best-First Search.

    Same return format as every solver: (list_of_moves, nodes_expanded)
    If it can't find a solution before max_nodes, return ([], nodes_expanded).
    """
    if state == SOLVED:
        return [], 1
    # STUB: fake solution, and a longer one than the others to show greedy
    # isn't optimal (remove this when you write the real thing)
    return list(FAKE_SOLUTION) + ["F", "F'"], 80
