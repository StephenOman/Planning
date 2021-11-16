# Base class generic planner

import abc
from plan_node import NodeFactory
from state import State
from action import Action

import logging
logger = logging.getLogger(__name__)

class Planner(abc.ABC):
    def __init__(self, init_state, goal_state, actions) -> None:
        self.init_state = init_state
        self.goal_state = goal_state

        self.nf = NodeFactory()
        start_node = self.nf.produce_head(self.init_state)
        self._frontier = [start_node]

        self._expanded = []
        self._children = []
        self._actions = actions
        self._next_node = None
        self.goal_node = None
        super().__init__()


    """
    This method is used to select the next child
    node to be processed
    """
    @abc.abstractmethod
    def select(self):
        pass

    """
    This method must generate the child nodes
    """
    @abc.abstractmethod
    def expand(self, node):
        self.nf.expand(node, self._actions)
        return node.children

    """
    This method should remove nodes that you don't
    want evaluated e.g. to avoid cycles in your 
    search plan.
    """
    @abc.abstractmethod
    def prune(self):
        #if a child node has already been expanded, delete it
        for child in self._children:
            if child in self._expanded:
                self._children.remove(child)

        #if a node in the frontier has already been expanded in
        #another part of the tree, delete it
        for next in self._frontier:
            if next in self._expanded:
                self._frontier.remove(next)


    def plan(self, map):
        while len(self._frontier) > 0:
            self._next_node = self.select()                                # (i)

            # Ignore nodes already expanded
            if self._next_node not in self._expanded:
                self._expanded.append(self._next_node)

                if self._next_node.satisfies(self.goal_state):                 # (ii)
                    logger.debug("Plan found:" + str(self._next_node.get_plan()))
                    self.goal_node = self._next_node
                    return True
                #else:
                #    print("Rejecting plan:", self._next_node.get_plan())
                    
                self._children = self.expand(self._next_node, map)

                # prune nodes from collections
                self.prune()                                                   # (iii)
                for child in self._children:
                    self._frontier.append(child)                               # (iv)

                logger.debug("Completed node " + str(self._next_node) + " with location " + str(self._next_node.state.location))

        logger.debug("No plan found")
        return False


class Breadth_First_Planner(Planner):
    def __init__(self, init_state, goal_state, actions) -> None:
        super().__init__(init_state, goal_state, actions)

    def select(self):
        return self._frontier.pop(0)

    def expand(self, node, map):
        self.nf.expand(node, self._actions, map)
        return node.children

    # uses the standard pruning mechanism
    def prune(self):
        return super().prune()


class Depth_First_Planner(Planner):
    def __init__(self, init_state, goal_state, actions) -> None:
        super().__init__(init_state, goal_state, actions)

    def select(self):
        return self._frontier.pop(len(self._frontier)-1)

    def expand(self, node, map):
        return super().expand(node, map)

    # uses the standard pruning mechanism
    def prune(self):
        return super().prune()