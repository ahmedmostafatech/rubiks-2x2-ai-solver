# Rubik's 2x2 AI Solver

> EELU Artificial Intelligence Project, Fall 2026-2027
> Course instructor: Dr. Mahmoud Bassiouni

A 2x2 Rubik's Cube (Pocket Cube) game and solver built around classic **search algorithms**. Play the cube yourself, scramble it, or let the AI solve it with different algorithms and compare how they perform.

---

## 1. Project Idea

The 2x2 cube has **3,674,160** reachable states, which is small enough to run every search algorithm on the same problem and compare them fairly, but still a real challenge (a solution can need up to 11 moves in the half-turn metric).

**Features**

- Scramble the cube with a chosen number of moves
- Play manually with the keyboard
- Solve mode: pick an algorithm and watch the solution step by step
- Hint: show the next best move
- Move counter, timer, undo/redo, time-attack mode and a leaderboard
- Benchmark: compare all algorithms (time, nodes expanded, solution length)

---

## 2. Algorithms Used

| Algorithm | Type | Optimal? | Notes |
|---|---|---|---|
| BFS | Uninformed | Yes | Baseline, slow on deep scrambles |
| Bidirectional BFS | Uninformed | Yes | Searches from the scramble and from the solved state until they meet |
| IDA* | Informed | Yes | Low memory, uses pattern-database heuristics |
| Greedy Best-First | Informed | No | Fast but may give long solutions or fail |

**Heuristic (IDA\*)**: `h(s) = max(h_orientation, h_permutation)`. Each part solves a relaxed version of the problem, so it never overestimates the real cost (admissible), and the max of admissible heuristics is also admissible.

**Greedy heuristic**: number of corner cubies that are not in their correct place.

---

## 3. State Representation

The cube is stored as 8 corner cubies, each with a **permutation** (which cubie is in which slot) and an **orientation** (0, 1 or 2). One cubie is kept fixed so only three faces (U, R, F) are needed. Moves: `U, U2, U', R, R2, R', F, F2, F'` (9 moves).

---

## 4. Project Structure and Ownership

```
rubiks-2x2-ai-solver/
├── README.md
├── requirements.txt
├── src/
│   ├── cube.py              # State + moves + scramble           (Member 1)
│   ├── solvers/
│   │   ├── bfs.py                                                 (Member 1)
│   │   ├── bidirectional.py                                       (Member 1)
│   │   ├── heuristics.py    # Pattern databases                   (Member 1)
│   │   ├── ida_star.py                                            (Member 1)
│   │   └── greedy.py                                              (Member 3)
│   ├── game/
│   │   └── features.py      # Timer, counter, undo/redo, leaderboard (Member 3)
│   ├── gui/
│   │   └── main.py          # Pygame interface                    (Member 2)
│   └── benchmark.py         # Runs all solvers, writes CSV        (Member 3)
├── tests/                   # Unit tests                          (Member 3)
├── data/
│   └── leaderboard.txt
└── docs/                    # Screenshots, charts, final PDF
```

---

## 5. Team and Roles

| Member | Role | Responsibilities |
|---|---|---|
| Member 1: Ahmed | Lead Developer / Algorithms | State and moves, BFS, Bidirectional BFS, Pattern DBs, IDA*, final integration |
| Member 2: _name_ | GUI Developer | Pygame interface, animations, keyboard controls, connecting the solvers to the UI |
| Member 3: _name_ | Game Features and Testing | Greedy solver, timer/counter/undo/leaderboard, unit tests, benchmark script |

Each member writes the documentation section for their own part.

---

## 6. Shared Interface (agreed by all members)

Everyone codes against these names, so we can work in parallel.

| Item | Definition |
|---|---|
| State | A pair `(cp, co)`: corner permutation and corner orientation |
| `SOLVED` | The solved state |
| `MOVES` | Dictionary of the 9 move names to their move tables |
| `apply(state, move)` | Returns the new state after a move |
| `inv(move)` | Returns the inverse move name |
| `scramble(n)` | Returns `(state, list_of_moves)` |
| Solver call | `solve(state)` returns `(moves_list, nodes_expanded)` |
| Facelets (GUI) | A function that converts a state to 24 sticker colors for drawing |

---

## 7. How to Run

```bash
git clone https://github.com/<username>/rubiks-2x2-ai-solver.git
cd rubiks-2x2-ai-solver
pip install -r requirements.txt
python src/gui/main.py
```

Run the tests:

```bash
python -m unittest discover tests
```

Run the benchmark:

```bash
python src/benchmark.py
```

---

## 8. Libraries

- Python 3.10+
- Pygame (GUI)
- _(add any other library here as soon as it is used)_

---

## 9. Input / Output Samples

_To be filled after the solvers are ready._

| Scramble | Algorithm | Solution | Length | Nodes | Time |
|---|---|---|---|---|---|
| ... | BFS | ... | ... | ... | ... |

---

## 10. Testing Results

_To be filled by Member 3 after running the benchmark._

---

## 11. Team Workflow

- `main` always contains working code; nobody pushes to it directly
- Each member works on their own branch: `member1-algorithms`, `member2-gui`, `member3-features`
- Merge into `main` with a Pull Request, reviewed by at least one other member
- Weekly meeting to review progress
- Internal deadline: 3-4 days before the official deadline

---

## 12. Academic Integrity

All code and documentation are written by the team. External libraries are listed in section 8. Each member's role is listed in section 5.
