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
    from game import Directions
    n = Directions.NORTH
    s = Directions.SOUTH
    e = Directions.EAST
    w = Directions.WEST

    # Method 1
    # ans = []
    # found = False
    # visited = []
    # currentStatePos = problem.getStartState()
    # ans, found = nextNode(problem, currentStatePos, visited)
    # ans.reverse()

    ans = []
    visitedCoords = set()
    nodesToVisit = util.Stack()

    nodesToVisit.push((problem.getStartState(), []))
    print "start depthFirstSearch"
    while not nodesToVisit.isEmpty():
        # print "Nodes to visit: " + nodesToVisit.self
        currentNode = nodesToVisit.pop()
        # print "Current Node: %s" % (currentNode,)
        visitedCoords.add(currentNode[0])
        if problem.isGoalState(currentNode[0]):
            ans = currentNode[1]
            # print "Goal state"
            # print "Path "
            # print ans
            break
        else:
            for node in problem.getSuccessors(currentNode[0]):
                if node[0] not in visitedCoords:
                    # print "New Node: %s" % (node,)
                    # print currentNode[1]
                    # print currentNode[1]
                    route = currentNode[1][:]
                    # print route
                    route.append(node[1])
                    # print route
                    # print "Route " + str(route)
                    # print route
                    nodesToVisit.push((node[0], route))


    # print ans, found
    print "END"
    print ans
    return ans
    # return  [s, s, w, s, w, w, s, w]
    util.raiseNotDefined()

# def expandNode( problem, pos, route, visited):
#     # is it the goal,
#     if problem.isGoalState(pos):
#         return route, True
#     else:
#         toVisit.push(problem.getSuccessors(pos))
#         # print toVisit
#     return [], False


def nextNode(problem, currentStatePos, visited):
    ans = []
    if problem.isGoalState(currentStatePos):
        return ans, True
    else:
        visited.append(currentStatePos)
        # print "Visited list: ", visited
        # print "Current location: ", currentStatePos
        # print problem.getSuccessors(currentStatePos)

        for node in problem.getSuccessors(currentStatePos):
            found = False
            for pos in visited:
                if node[0] == pos:
                    # print "help", node[0], pos
                    found = True
                    break
            if found:
                continue
            currentState = node
            ans, isGoal = nextNode(problem, currentState[0], visited)
            # print "Answer: ", ans
            # print type(ans)
            # print currentState
            if isGoal:
                # print "test", currentState[1]
                ans.append(currentState[1])
                # print ans
                return ans, True
    return ans, False
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    ans = []
    visitedCoords = set()
    nodesToVisit = util.Queue()

    nodesToVisit.push((problem.getStartState(), []))
    # print "Start breadthFirstSearch"
    while not nodesToVisit.isEmpty():
        currentNode = nodesToVisit.pop()
        if currentNode[0] in visitedCoords:
            continue
        visitedCoords.add(currentNode[0])
        if problem.isGoalState(currentNode[0]):
            ans = currentNode[1]
            break
        else:
            for node in problem.getSuccessors(currentNode[0]):
                if node[0] not in visitedCoords:
                    route = currentNode[1][:]
                    route.append(node[1])
                    nodesToVisit.push((node[0], route))
    return ans
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    ans = []
    visitedCoords = set()
    nodesToVisit = util.PriorityQueue()
    print problem.getStartState()
    nodesToVisit.push((problem.getStartState(), [], 0), 0 )
    # print "Start uniformCostSearch"
    while not nodesToVisit.isEmpty():
        currentNode = nodesToVisit.pop()
        if currentNode[0] in visitedCoords:
            continue
        visitedCoords.add(currentNode[0])
        if problem.isGoalState(currentNode[0]):
            ans = currentNode[1]
            break
        else:
            for node in problem.getSuccessors(currentNode[0]):
                if node[0] not in visitedCoords:
                    route = currentNode[1][:]
                    route.append(node[1])
                    cost = currentNode[2] + node[2]
                    print cost
                    nodesToVisit.push((node[0], route, cost), cost)
    return ans
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
