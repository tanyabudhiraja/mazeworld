from SearchSolution import SearchSolution
from heapq import heappush, heappop

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object
    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        self.state = state          
        self.parent = parent      
        self.h = heuristic
        self.path = []
        #setup g val -> how far you have come so far
        if parent is None:
            self.g = 0
        else:
            self.g = parent.g + transition_cost

    def priority(self):
        f = self.g + self.h
        return f 

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        #how to compare 2 nodes
        return self.priority() < other.priority()
    

# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent
    result.reverse()
    return result

        
def astar_search(search_problem, heuristic_fn):
# frontier = new priority queue (ordered by path cost)
# pack start_state into a node
# add node to frontier
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = []
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

# explored = new set (for memoizing)
# add start_state to explored

    visited_cost = {}
    visited_cost[start_node.state] = 0
# while frontier is not empty:
    # you write the rest:
    while pqueue:
# get current_node from the frontier # chooses lowest-cost node
# get current_state from current_node
        current = heappop(pqueue)
        solution.nodes_visited += 1
    

# if current_state is the goal:
        if search_problem.is_goal(current.state):
            solution.path= backchain(current)
            return solution
# backchain from current_node and return solution

        else:
            #for each child of current_state:
                #pack child state into a node, with backpointer to current_node
                #add the node to the frontier
            kids = search_problem.get_successors(current.state)
            # for each child of current_state:
            # if child not in explored:
            # add child to explored

            for kid in kids: #for all children of the state
                transition_cost=search_problem.get_transition_cost(current.state,kid)
                if kid in visited_cost and current.g + transition_cost > visited_cost[kid]:
                    continue
                visited_cost[kid] = current.g + transition_cost
                heappush(pqueue, AstarNode(kid, heuristic_fn(kid), parent=current, transition_cost= transition_cost ))
    return solution

# pack child state into a node, with backpointer to current_node
# add the node to the frontier
# else if child is in frontier with higher path cost
# replace that frontier node with child node
# return failure






            