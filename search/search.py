# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


done = False
final_action_list = []
visited_states_list = []

def dbs(problem,position, actions_list):
    
    global done, final_action_list, visited_states_list
    #print(position, "position")
    visited_states_list.append(position)
    # END OF RECURSION    
    if done:
        return

    if problem.isGoalState(position):
        done = True
        final_action_list = list(actions_list)

        return
    
    # RECURSION
    else:
        #EXPAND NODES
        expansion = problem.getSuccessors(position)
        for n in expansion:
            if n[0] not in visited_states_list:
                b = [x for x in actions_list]
                b.append(n[1])
                dbs(problem, n[0], b)



def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    global done, final_action_list, visited_states_list
    visited_states_list = []
    s0 = problem.getStartState()
    done = False
    final_action_list = []
    dbs(problem, s0, [])
    done = False
    return final_action_list

    #util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    lista_de_prioridades = util.Queue()
    start_state = problem.getStartState()
    lista_de_prioridades.push(start_state)
    lista_visitados2 = []
    action_list = []
    family_relations = []
    final_state = None

    while (not lista_de_prioridades.isEmpty()):
        #Expansion 
        state_visited = lista_de_prioridades.pop()
        #print(state_visited)

        if problem.isGoalState(state_visited):
            final_state = state_visited
            break
        
        lista_visitados2.append(state_visited)
        expansion = problem.getSuccessors(state_visited)
        
        for son in expansion:
            #print(son[0], son[0] in lista_visitados2)
            if son[0] not in lista_de_prioridades.list:
                if son[0] not in lista_visitados2:
                    family_relations.append((state_visited, son[1], son[0]))
                    lista_de_prioridades.push(son[0])


    answer = []
    aux_state = final_state
    
    #print(family_relations)
    while (aux_state!= start_state):
        aux = None
        for t in family_relations:
            if t[2] == aux_state:
                aux = t
                answer.insert(0,t[1])
                aux_state = t[0]
        #print(aux_state)

    #answer = [x for x in reversed(answer)]

    return answer

    #util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    "*** YOUR CODE HERE ***"
    lista_de_prioridades = []
    start_state = problem.getStartState()
    lista_de_prioridades.append((start_state, 0))
    lista_visitados2 = []
    action_list = []
    family_relations = []
    final_state = None

    while (len(lista_de_prioridades)>0):
        #Expansion 
        #print(lista_de_prioridades)
        state_visited, cost = lista_de_prioridades.pop(0)
        #print(state_visited, cost)
        #print(state_visited)
        if state_visited in lista_visitados2:
            continue

        if problem.isGoalState(state_visited):
            final_state = state_visited
            break
        
        lista_visitados2.append(state_visited)
        expansion = problem.getSuccessors(state_visited)
        #print(expansion)
        for son in expansion:
            #print(son[0], son[0] in lista_visitados2)
                
            
            if son[0] not in lista_visitados2:
                lista_de_prioridades.append((son[0], cost+son[2]))
                family_relations.append((state_visited, son[1], son[0], cost+son[2]))   
                lista_de_prioridades= sorted(lista_de_prioridades ,key =  lambda x:x[1])
    answer = []
    aux_state = final_state
    
    #print(family_relations)
    while (aux_state!= start_state):
        aux = None
        for t in sorted(family_relations, key = lambda x:x[3]):
            if t[2] == aux_state:
                aux = t
                answer.insert(0,t[1])
                aux_state = t[0]
        #print(aux_state)

    #answer = [x for x in reversed(answer)]

    return answer

	

	
	
def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
	
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    " YOUR CODE HERE "
    " YOUR CODE HERE "
    " YOUR CODE HERE "

    lista_de_prioridades = []
    start_state = problem.getStartState()
    lista_de_prioridades.append((start_state, 0))
    lista_visitados2 = []
    action_list = []
    family_relations = []
    final_state = None

    while (len(lista_de_prioridades)>0):
        #Expansion 
        #print(lista_de_prioridades)
        state_visited, cost = lista_de_prioridades.pop(0)
        #print(state_visited, cost)
        #print(state_visited)
        if state_visited in lista_visitados2:
            continue

        if problem.isGoalState(state_visited):
            final_state = state_visited
            break

        lista_visitados2.append(state_visited)
        expansion = problem.getSuccessors(state_visited)
        #print(expansion)
        for son in expansion:
            #print(son[0], son[0] in lista_visitados2)


            if son[0] not in lista_visitados2:
                lista_de_prioridades.append((son[0], cost+son[2]))
                #print("heu",son[0], heuristic(son[0], problem))
                family_relations.append((state_visited, son[1], son[0], cost+son[2]))
                lista_de_prioridades= sorted(lista_de_prioridades ,key =  lambda x:x[1]+ heuristic(x[0], problem))
    answer = []
    aux_state = final_state

    #print(family_relations)
    while (aux_state!= start_state):
        aux = None
        for t in sorted(family_relations, key = lambda x:x[3]):
            if t[2] == aux_state:
                aux = t
                answer.insert(0,t[1])
                aux_state = t[0]
        #print(aux_state)

    #answer = [x for x in reversed(answer)]

    return answer
	

def learningRealTimeAStar(problem, heuristic=nullHeuristic):
    """Execute a number of trials of LRTA* and return the best plan found."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    # MAXTRIALS = ...
    

# Abbreviations 
# *** DO NOT CHANGE THESE ***
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
lrta = learningRealTimeAStar
