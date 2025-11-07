from Maze import Maze
from time import sleep

class SensorlessProblem:
    def __init__(self, maze: Maze):
        self.maze = maze
        floors = []
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                if self.maze.is_floor(x, y):
                    floors.append((x, y))
        
        self.start_state = tuple(sorted(floors))

    def __str__(self):
        string =  "Blind robot problem: "
        return string

    def is_goal(self, state):
        return len(state) == 1
    
    def goal_test(self, state):
        return self.is_goal(state)    
    
    def null_heuristic(self, state):
        return 0
    
    def get_transition_cost(self, state1, state2):
        return 1


    def get_successors(self, state):
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)] #only one robot, no wait
        children = []

        for dx, dy in moves:
            belief = set()
            for (x, y) in state: #every possible location in current belief 
                new_x, new_y = x + dx, y + dy #move
                if self.maze.is_floor(new_x, new_y): #if valid
                    belief.add((new_x, new_y)) #add
                else:
                    belief.add((x, y)) #dont move 
            children.append(tuple(sorted(belief))) #all possible new positions
        return children
        

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
