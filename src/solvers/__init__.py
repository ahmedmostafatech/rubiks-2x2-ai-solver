"""
solvers package  --  one place that lists ALL the solvers.

The GUI dropdown and the benchmark both read this dictionary, so when you add
or finish a solver you don't have to touch their code. Every solver here has
the same shape:  solve(state) -> (list_of_moves, nodes_expanded)
"""
from . import bfs, bidirectional, ida_star, greedy

SOLVERS = {
    "BFS": bfs.solve,
    "Bidirectional BFS": bidirectional.solve,
    "IDA*": ida_star.solve,
    "Greedy": greedy.solve,
}
