"""
bidirectional.py  --  Bidirectional BFS
Owner: Member 1 (Ahmed)

Same idea as BFS, but we search from BOTH ends at the same time: from the
scrambled cube going forward, and from the solved cube going backward.
When the two searches meet in the middle, we join the paths. Each side only
goes half the depth, so it's way faster, and the solution is still the shortest.

STUB for now: returns a fixed fake answer.
"""
from src.cube import SOLVED, FAKE_SOLUTION


def solve(state):
    """Solve the cube with Bidirectional BFS.

    Same return format as every solver: (list_of_moves, nodes_expanded)
    """
    if state == SOLVED:
        return [], 1
    # STUB: fake solution and a fake node count (smaller than BFS on purpose)
    return list(FAKE_SOLUTION), 300
