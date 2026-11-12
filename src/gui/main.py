"""
main.py  --  the game window (Pygame)
Owner: Member 2

This is a starting skeleton so you can see a window with the cube drawn as a
2D "net" (the cube unfolded like a cross) straight away:

          [U]
      [L] [F] [R] [B]
          [D]

Right now it only shows the solved colors, because get_facelets() is a stub.
Everything else (buttons, keyboard, animation, solver dropdown) is yours.
Make it look good, you're the UI guy. :)

Run it from the project root:   python -m src.gui.main
"""
import pygame

from src.cube import SOLVED, scramble, apply, get_facelets, FACE_ORDER
from src.solvers import SOLVERS
from src.game.features import MoveCounter, GameTimer, MoveHistory

# ---------------------------------------------------------------------------
# Settings (feel free to change the colors, they're just a first try)
# ---------------------------------------------------------------------------
WINDOW_SIZE = (900, 650)
BACKGROUND = (20, 22, 30)
STICKER_SIZE = 48
GAP = 4

# Sticker letter -> real color. (W=white, R=red, G=green, Y=yellow, O=orange, B=blue)
COLORS = {
    "W": (240, 240, 240),
    "R": (200, 40, 40),
    "G": (40, 160, 70),
    "Y": (240, 210, 40),
    "O": (240, 130, 30),
    "B": (40, 90, 200),
}

# Where each face goes in the cross, measured in "sticker units".
# (column, row) of the top-left sticker of that face.
FACE_POSITION = {
    "U": (2, 0),
    "L": (0, 2),
    "F": (2, 2),
    "R": (4, 2),
    "B": (6, 2),
    "D": (2, 4),
}

# Keyboard -> move. Hold SHIFT for the reverse move (R'). TODO: half turns?
KEY_TO_MOVE = {
    pygame.K_u: "U",
    pygame.K_r: "R",
    pygame.K_f: "F",
}


def draw_cube(screen, state, origin=(120, 80)):
    """Draw the 24 stickers of the cube on the screen."""
    facelets = get_facelets(state)
    for face_index, face in enumerate(FACE_ORDER):
        col0, row0 = FACE_POSITION[face]
        for pos in range(4):
            col = col0 + pos % 2
            row = row0 + pos // 2
            x = origin[0] + col * (STICKER_SIZE + GAP)
            y = origin[1] + row * (STICKER_SIZE + GAP)
            color = COLORS[facelets[face_index * 4 + pos]]
            pygame.draw.rect(screen, color, (x, y, STICKER_SIZE, STICKER_SIZE),
                             border_radius=6)


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Rubik's 2x2 AI Solver")
    clock = pygame.time.Clock()

    # The game's state lives here. We start solved; TODO: a Scramble button.
    state = SOLVED
    counter, timer, history = MoveCounter(), GameTimer(), MoveHistory()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # TODO: keyboard moves. Idea: look up the key in KEY_TO_MOVE, add
            # "'" if shift is held, then call apply(state, move) and update the
            # counter / timer / history.

            # TODO: buttons (Scramble, Solve, Hint, Undo, Redo) and a dropdown
            # built from SOLVERS.keys().

            # TODO: animation. When the solver returns a list of moves, apply
            # them one by one with a small delay so the player can follow.

        screen.fill(BACKGROUND)
        draw_cube(screen, state)
        # TODO: draw the counter, the timer and the info panel
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
