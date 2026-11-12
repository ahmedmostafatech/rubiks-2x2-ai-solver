"""
ida_star.py  --  IDA* (Iterative Deepening A*)
Owner: Member 1 (Ahmed)

IDA* is like DFS but with a limit on (moves so far + heuristic estimate).
If it fails, it raises the limit a little and tries again. It uses very little
memory compared to A*, and with an admissible heuristic the solution is optimal.

STUB for now: returns a fixed fake answer.
"""
from src.cube import SOLVED, FAKE_SOLUTION


def solve(state):
    """Solve the cube with IDA*.

    Same return format as every solver: (list_of_moves, nodes_expanded)
    """
    if state == SOLVED:
        return [], 1
    # STUB: fake solution and a fake node count
    return list(FAKE_SOLUTION), 150
