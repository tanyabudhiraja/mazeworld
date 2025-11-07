from Maze import Maze
from time import sleep

class MazeworldProblem:

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal_locations = goal_locations
        self.num_robo = len(self.maze.robotloc) // 2   
        self.start_state = (0, *self.maze.robotloc)

    def __str__(self):
        string =  "Mazeworld problem: "
        return string

    def is_goal(self, state):
        return tuple(state[1:]) == self.goal_locations


    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))
    
    def null_heuristic(self,state):
        return 0
    
    def manhattan_heuristic(self, state):
        robots = state[1:]
        h=0 
        for num in range(0,len(robots),2):
            x,y= robots[num], robots[num+1]
            goal_x, goal_y = self.goal_locations[num], self.goal_locations[num + 1]
            h += abs(x - goal_x) + abs(y - goal_y)
        return h 

    def get_transition_cost(self,state1,state2):
        if state1==state2:
            return 0
        else:
            return 1
    
    def goal_test(self, state):
        return self.is_goal(state)

    def get_successors(self, state):

        self.maze.robotloc=state[1:]
        if self.num_robo == 1: #there is no wait if only one robot,
            #it kept getting stuck in a loop when there was 1 robot
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
        else:
            moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
        children = []
        turn = state[0]  
        robots = list(state[1:])  #everything except first number is coordinates 

        # 1st position
        robot_x = robots[2 * turn]
        robot_y = robots[2 * turn + 1]

        #for each move in mves get all possible moves 
        for dx, dy in moves:
            new_x = robot_x + dx #transition with moves 
            new_y = robot_y + dy

            #make sure rules are followed 

            if (dx==0 and dy==0) or (self.maze.is_floor(new_x, new_y) and not self.maze.has_robot(new_x, new_y)):
                
                new_robots = robots.copy()
                new_robots[2 * turn] = new_x
                new_robots[2 * turn + 1] = new_y

                #move turn to next robot 
                next_turn = (turn + 1) % (len(self.maze.robotloc) // 2)

                #next state
                new_state = (next_turn,) + tuple(new_robots)

                #add to list 
                children.append(new_state)
            else:
                continue
        return children


if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))
