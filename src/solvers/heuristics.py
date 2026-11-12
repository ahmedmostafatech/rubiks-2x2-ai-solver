"""
heuristics.py  --  the "smart guess" used by IDA*
Owner: Member 1 (Ahmed)

A heuristic h(state) is a quick estimate of "how many moves are left to solve
this cube". IDA* uses it to skip directions that look hopeless.
To keep the solution optimal, the estimate must NEVER be bigger than the real
number of moves left (we call that "admissible"). Returning 0 is always safe,
it's just not helpful. :)

We'll build two small lookup tables (pattern databases):
  - one that only cares about the orientations (the twists)
  - one that only cares about the permutation (the positions)
and take the bigger of the two.

STUB for now.
"""


def build_pattern_databases():
    """Pre-compute the lookup tables. Called once when the program starts.

    STUB: does nothing yet.
    """
    pass


def h(state):
    """Estimated moves left to solve `state`. Must never over-estimate.

    STUB: returns 0 (safe but useless, IDA* will just act like plain deepening).
    """
    return 0
