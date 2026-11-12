"""
benchmark.py  --  compares all the solvers and saves the results to a CSV
Owner: Member 3

It runs every solver on the same scrambles, measures time / nodes / solution
length, and writes everything to data/benchmark_results.csv. We'll use that
file for the charts and the testing section of the documentation.

This script already runs with the stub solvers (so you can see how it works).
The numbers will only mean something once the real solvers are in.

Run it from the project root:   python -m src.benchmark
"""
import csv
import time

from src.cube import scramble, is_solved, apply
from src.solvers import SOLVERS

DEPTHS = [3, 5, 7]          # how many scramble moves (TODO: add 9 and 11 later)
SCRAMBLES_PER_DEPTH = 5     # TODO: raise to 20 when the solvers are fast enough
OUTPUT_FILE = "data/benchmark_results.csv"


def run_benchmark():
    rows = []
    for depth in DEPTHS:
        for i in range(SCRAMBLES_PER_DEPTH):
            state, _ = scramble(depth)
            for name, solve in SOLVERS.items():
                start = time.time()
                moves, nodes = solve(state)
                seconds = time.time() - start

                # Check the solution really solves the cube.
                # (With the stub cube this check can't mean much yet.)
                check = state
                for m in moves:
                    check = apply(check, m)

                rows.append({
                    "depth": depth,
                    "scramble_no": i + 1,
                    "algorithm": name,
                    "solution_length": len(moves),
                    "nodes": nodes,
                    "seconds": round(seconds, 6),
                    "solved_correctly": is_solved(check),
                })

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print(f"Done, {len(rows)} rows saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    run_benchmark()
