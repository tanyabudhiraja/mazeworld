from collections import deque
from SearchSolution import SearchSolution
#from FoxProblem import FoxProblem

class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None, move=None, depth = 0):
        #state
        self.state= state
        self.goal_state = (0, 0, 0)
        self.parent= parent
        self.depth = depth

    def get_state(self):
        return self.state
    
    def get_parent(self):
        return self.parent
    
    def get_depth(self):
        return self.depth


#function for how to backchain 
def backchain(node):
    path = [] #empty list to store 
        #start at the end state - node
    while node is not None: #while there is something there as the node
        path.append(node.state) #add the state tuple of the node to the list
        node = node.parent #replace node with its parent now 
    path.reverse() #flip list before returning to get from most shallow to deepest 
    return path 



def bfs_search(search_problem):
    solution = SearchSolution(search_problem, "BFS")
#frontier = new queue
    start = SearchNode(search_problem.start_state) #start state is a search node object
    frontier = deque([start])#add start state to queue 
    visited = {start.state}#storing first state with no parent 
#pack start state into a node
#add node to frontier
#while frontier is not empty:
    while len(frontier) > 0:
        current= frontier[0]
        frontier.popleft() #remove parent from frontier 
        solution.nodes_visited += 1
    #get current_node from the frontier
    #get current_state from current_node
        if search_problem.goal_test(current.state):
            solution.path= backchain(current)
            return solution
                #if current_state is the goal:
                    #backchain from current_node and return solution
        else:
            #for each child of current_state:
                #pack child state into a node, with backpointer to current_node
                #add the node to the frontier
            kids = search_problem.get_successors(current.state)
            for kid in kids: #for all children of the state
                if kid not in visited: #if it hasnt been visited before
                    frontier.append(SearchNode(kid, parent=current))
                    #add searchnode to frontier not just the state
            visited.add(current.state) #add parent to visited

    return solution
                
def dfs_search(search_problem, depth_limit=100, node=None, path=None, solution=None):
    # if no node object given, create a new search from starting state
    if node is None:
        node = SearchNode(search_problem.start_state, parent=None, depth=0)
        path= [node.state] #for path checking
        solution = SearchSolution(search_problem, "DFS")
    solution.nodes_visited+=1

    #check if we are at goal 
    if search_problem.goal_test(node.state):
        solution.path= backchain(node)
        return solution
    #dont go past deepest limit
    
    if node.depth >= depth_limit:
        return None
    
    #for children of node, check if already in path- ignore it if it has alr been visited 
    for kid in search_problem.get_successors(node.state):
        if kid in path:
            continue
        child = SearchNode(kid, parent=node, depth=node.depth + 1)
        path.append(kid) 

        #going into kids subtree
        path2 = dfs_search(search_problem, depth_limit=depth_limit, node=child, path=path, solution=solution)
        if path2 is not None:
            return path2
        path.pop() #backtrack
    return None



#ids= running dfs with deeper and deeper limits
def ids_search(search_problem, depth_limit=100):
    ids_solution = SearchSolution(search_problem, "IDS")
    for i in range(1,depth_limit+1):
        dfs_solution = dfs_search(search_problem, depth_limit=i, node=None, path=None)
        if dfs_solution is None:  #if no solution from dfs go to next iteration
            continue
        ids_solution.nodes_visited += dfs_solution.nodes_visited

    #if there is a solution return it
        if dfs_solution is not None:
            ids_solution.path = dfs_solution.path
            return ids_solution
        
    return ids_solution


