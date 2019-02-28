# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        # print gameState.getLegalActions(0)
        # print self.evaluationFunction(gameState)
        # for i in range(gameState.getNumAgents()):
        #     if i == 0:
        #
        #     else:
        # gameState.getLegalActions(agentIndex)
        # gameState.generateSuccessor(0, gameState.getLegalActions(0)[1])
        # for i in range(self.depth):
        # max = -100000
        # maxAction = "Stop"
        # for action in gameState.getLegalActions(0):
        #     utility = self.evaluationFunction(gameState.generateSuccessor(0, action))
        #     if utility > max:
        #         max = utility
        #         maxAction = action
        maxValue, maxAction = self.maxValueFunction(gameState, 0, 0)

        # maxValue = -100000
        # maxAction = "Stop"
        # for action in gameState.getLegalActions(0):
        #     newGameState = gameState.generateSuccessor(0, action)
        #     minValue = 1000000
        #     minAction = "Stop"
        #     for minaction in newGameState.getLegalActions(0):
        #         newnewGameState = newGameState.generateSuccessor(0, minaction)
        #         maxmaxValue = -100000
        #         maxmaxAction = "Stop"
        #         for maxaction in newnewGameState.getLegalActions(0):
        #             nGameState = newnewGameState.generateSuccessor(0, maxaction)
        #             value = self.evaluationFunction(nGameState)
        #             if value > maxmaxValue:
        #                 maxmaxValue = value
        #                 maxmaxAction = maxaction
        #
        #         # value = self.evaluationFunction(newnewGameState)
        #         if maxmaxValue < minValue:
        #             minValue = maxmaxValue
        #             minAction = minaction
        #
        #     # value = self.evaluationFunction(newGameState)
        #     # print "value ", value
        #     # print "action ", action
        #     if minValue > maxValue:
        #         maxValue = minValue
        #         maxAction = action
        # print "maxValue ", maxValue
        # print "maxAction ", maxAction

        # print "st"
        # print gameState.generateSuccessor(0, gameState.getLegalActions(0)[0])
        # print gameState.generateSuccessor(0, gameState.getLegalActions(0)[1])
        # print "st"
        # print self.evaluationFunction()
        # print gameState.getNumAgents()
        return maxAction
        util.raiseNotDefined()

    # def maxValue(self, gameState, agent, depth):
    #     maxValue = float("-inf")
    #     for action in gameState.getLegalActions(agent):
    #         successor = gameState.generateSuccessor(agent, action)
    #         maxValue = max(maxValue, )
    #
    #
    #
    # def minValue(self, gameState, agent, depth):
    #
    #
    # def minimax(self, gameState, agent, depth):


    def maxValueFunction(self, gameState, agent, depth):
        if self.depth == depth:
            ans = self.evaluationFunction(gameState)
            # print ans
            return ans, "Help"
        maxValue = float("-inf")
        maxAction = "Help"
        newAgent = agent + 1
        newAgent = newAgent % gameState.getNumAgents()
        for action in gameState.getLegalActions(agent):
            newGameState = gameState.generateSuccessor(agent, action)
            value, tmp = self.minValueFunction(newGameState, newAgent, depth+1)
            if value > maxValue:
                maxValue = value
                maxAction = action
        return maxValue, maxAction

    def minValueFunction(self, gameState, agent, depth):
        # if self.depth == depth:
        #     ans = self.evaluationFunction(gameState)
        #     # print ans
        #     return ans, "Stop"
        minValue = float("inf")
        minAction = "Help"
        newAgent = agent + 1
        newAgent = newAgent % gameState.getNumAgents()
        for action in gameState.getLegalActions(agent):
            newGameState = gameState.generateSuccessor(agent, action)
            if newAgent == 0:
                value, tmp = self.maxValueFunction(newGameState, newAgent, depth)
                if value < minValue:
                    minValue = value
                    minAction = action
            else:
                value, tmp = self.minValueFunction(newGameState, newAgent, depth)
                if value < minValue:
                    minValue = value
                    minAction = action
        return minValue, minAction


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
