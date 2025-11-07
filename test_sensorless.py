# You write this:
from SensorlessProblem import SensorlessProblem
from Maze import Maze
from astar_search import astar_search

# change maze as needed
maze4 = Maze("maze4.maz")
prob = SensorlessProblem(maze4)
result = astar_search(prob, prob.null_heuristic)
print(result)
