Maze Pathfinding with A* and Uninformed Search:
---
This is a Python project that solves grid mazes using A* (with pluggable heuristics) and uninformed search
algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), and Iterative Deepening Search (IDS).

It includes two problem variants:
-Mazeworld (multi-robot): coordinate multiple robots through a maze without collisions.
-Sensorless (blind robot): plan over a belief state when the robot’s exact location is unknown.

Project Overview:
---
  - Maze.py – loads .maz files, tracks walls/floors and robot positions
  - MazeworldProblem.py – multi-robot state, legal moves, goal test, Manhattan heuristic, simple animation
  - SensorlessProblem.py – belief-state representation, transitions, and goal test for the blind-robot problem
  - astar_search.py – generic A* search (node, priority queue, backchaining, visited-cost memo)
  - uninformed_search.py – BFS, DFS, and IDS implementations
  - test_mazeworld.py – example runner for Mazeworld (A* with Manhattan heuristic)
  - test_sensorless.py – example runner for Sensorless (A* with null heuristic = uniform-cost)
  - maze*.maz – maze definitions (# walls, . floors, \robot x y starts)

How to Run:
--- 
Clone the repository and run one of the example scripts:

Mazeworld (A* with Manhattan):

- python3 test_mazeworld.py


Sensorless (A* with null heuristic):

- python3 test_sensorless.py

Example output:
----
Mazeworld problem:
attempted with search method Astar with heuristic manhattan_heuristic
number of nodes visited: 123
solution length: 42
path: [(0, x1, y1, x2, y2, ...), (1, ...), ..., (0, goal_x1, goal_y1, ...)]

----
Blind robot problem:
attempted with search method Astar with heuristic null_heuristic
number of nodes visited: 456
solution length: 37
path: [((x,y), (x,y), ...), ((x,y), ...), ..., ((goal_x, goal_y))]

Requirements:
---

Python 3.10 or later
No external libraries required

Purpose:
---

This project was created to practice and compare classic search algorithms on maze problems, including multi-agent coordination and planning under uncertainty. It’s a useful example for learning state-space modeling, heuristic design, and search algorithm implementation in Python.
