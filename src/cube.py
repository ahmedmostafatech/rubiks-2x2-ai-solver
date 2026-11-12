"""
cube.py  --  the cube itself (state + moves + scramble)
Owner: Member 1 (Ahmed)

This is the file EVERYONE imports from, so the names in here are our "contract".
Right now most functions are STUBS (fake versions) so you can start coding
without waiting for me. Anything marked "# STUB" will be replaced by the real
thing, but the names and the return types will NOT change.

Quick rule: if you need something from the cube and it's not here, tell me
instead of writing your own version.
"""

# ---------------------------------------------------------------------------
# 1) The state
# ---------------------------------------------------------------------------
# A state is a pair (cp, co):
#   cp = corner permutation -> which cubie sits in each of the 8 slots
#   co = corner orientation -> how twisted each cubie is (0, 1 or 2)
# We keep one cubie fixed in place, so we only ever need the U, R and F faces.
# The slots are numbered: URF=0, UFL=1, ULB=2, UBR=3, DFR=4, DLF=5, DBL=6, DRB=7
SOLVED = (tuple(range(8)), (0,) * 8)

# A fake scrambled state so the GUI has something different from SOLVED to show.
# (Just a made-up one, it's not a "real" scramble.)
_FAKE_SCRAMBLED = ((1, 0, 2, 3, 4, 5, 6, 7), (1, 2, 0, 0, 0, 0, 0, 0))


# ---------------------------------------------------------------------------
# 2) The moves
# ---------------------------------------------------------------------------
# 9 moves in total: a quarter turn, a half turn (2) and a reverse turn (')
# for each of the three faces. Example: R = right face clockwise, R' = back.
MOVE_NAMES = ["U", "U2", "U'", "R", "R2", "R'", "F", "F2", "F'"]

# MOVES maps a move name to its table (how it shuffles the cubies).
# STUB: the real tables come from me. For now they're empty on purpose.
MOVES = {name: None for name in MOVE_NAMES}

# A fixed fake solution. Every stub solver returns this, so the GUI can
# practice animating "a solution" before the real solvers exist.
FAKE_SOLUTION = ["R", "U", "R'", "U'"]


def inv(move):
    """Return the opposite move: R -> R', R' -> R, R2 -> R2.

    This one is already REAL (it's easy), so you can use it right away.
    """
    if move.endswith("'"):
        return move[0]
    if move.endswith("2"):
        return move
    return move + "'"


def apply(state, move):
    """Apply one move (like "R" or "U2") and return the NEW state.

    It must never change the state you pass in, it always gives back a new one.
    STUB: right now it returns the same state, so nothing visually changes.
    """
    return state


def is_solved(state):
    """True if the cube is solved. Already REAL."""
    return state == SOLVED


# ---------------------------------------------------------------------------
# 3) Scramble
# ---------------------------------------------------------------------------
def scramble(n):
    """Mix the cube with n random moves.

    Returns a pair: (state, list_of_moves_used)
    STUB: ignores randomness, returns the same fake state and a fixed list
    of n moves, so your tests are predictable.
    """
    fake_sequence = ["R", "U", "F", "R'", "U2", "F'", "R2", "U'", "F2"]
    moves = [fake_sequence[i % len(fake_sequence)] for i in range(n)]
    return _FAKE_SCRAMBLED, moves


# ---------------------------------------------------------------------------
# 4) Drawing helper (this one is mainly for the GUI person)
# ---------------------------------------------------------------------------
# Colors by face letter: U=white, R=red, F=green, D=yellow, L=orange, B=blue
FACE_ORDER = ["U", "R", "F", "D", "L", "B"]
COLOR_OF_FACE = {"U": "W", "R": "R", "F": "G", "D": "Y", "L": "O", "B": "B"}


def get_facelets(state):
    """Turn a state into 24 sticker colors, ready to draw.

    Returns a list of 24 letters. Every face has 4 stickers, in this order:
    U, R, F, D, L, B  ->  so sticker number = face_index * 4 + position (0..3).
    Position goes row by row inside the face:  0 1
                                               2 3
    Letters: W=white, R=red, G=green, Y=yellow, O=orange, B=blue.

    STUB: always returns the solved colors, whatever the state is.
    """
    colors = []
    for face in FACE_ORDER:
        colors += [COLOR_OF_FACE[face]] * 4
    return colors
