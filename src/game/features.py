"""
features.py  --  the fun game stuff (counter, timer, undo/redo, leaderboard)
Owner: Member 3

None of this needs the solvers, only the cube. So you can start here on day 1.
Each class is a small box with a few methods. The GUI person (Member 2) will
call these, so keep the method names as they are.

Everything below is a STUB that returns fixed values. Replace the bodies one
by one and keep the names. Start with MoveCounter, it's the easiest.
"""


class MoveCounter:
    """Counts how many moves the player has made."""

    def __init__(self):
        self.count = 0

    def add(self):
        """Call this every time the player makes a move."""
        pass  # TODO: increase self.count

    def reset(self):
        """Back to zero (new game / new scramble)."""
        pass  # TODO


class GameTimer:
    """A stopwatch that starts on the player's first move."""

    def start(self):
        """Start counting (does nothing if it's already running)."""
        pass  # TODO (hint: time.time())

    def stop(self):
        """Stop counting, e.g. when the cube gets solved."""
        pass  # TODO

    def reset(self):
        """Back to zero."""
        pass  # TODO

    def elapsed(self):
        """Seconds passed so far, as a float.

        STUB: always 0.0
        """
        return 0.0


class MoveHistory:
    """Remembers the player's moves so we can undo and redo them.

    Idea: keep two lists, one for 'done' moves and one for 'undone' moves.
    Undo = take the last done move and apply its inverse (see cube.inv).
    A new move after an undo clears the redo list.
    """

    def push(self, move):
        """Record a new move the player just made."""
        pass  # TODO

    def undo(self):
        """Return the move to apply to go back one step, or None if nothing to undo.

        STUB: always None
        """
        return None

    def redo(self):
        """Return the move to re-apply, or None if nothing to redo.

        STUB: always None
        """
        return None

    def can_undo(self):
        return False  # STUB

    def can_redo(self):
        return False  # STUB


class Leaderboard:
    """Saves the best times in a small text file (data/leaderboard.txt)."""

    def __init__(self, path="data/leaderboard.txt"):
        self.path = path

    def add_score(self, name, seconds):
        """Add a result and keep only the best 5. Save to the file."""
        pass  # TODO

    def top(self):
        """Return the best results as a list of (name, seconds), best first.

        STUB: fixed fake list so the GUI can already draw a table.
        """
        return [("Player1", 42.0), ("Player2", 55.5), ("Player3", 61.2)]
