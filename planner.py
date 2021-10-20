# Base class generic planner

import abc
from plan_node import Node
from state import State
from action import Action

class Planner(abc.ABC):
    def __init__(self, init_state, goal_state, actions) -> None:
        self.init_state = init_state
        self.goal_state = goal_state

        start_node = Node(self.init_state, None)
        self._frontier = [start_node]

        self._expanded = []
        self._children = []
        self._actions = actions
        self._next_node = None
        super().__init__()


    """
    This method is used to select the next child
    node to be processed
    """
    @abc.abstractmethod
    def select(self):
        pass

    """
    This method must generate the child nodes in
    whatever order you want the search tree to be
    executed.
    """
    @abc.abstractmethod
    def expand(self, node):
        pass

    """
    This method should remove nodes that you don't
    want evaluated e.g. to avoid cycles in your 
    search plan.
    """
    @abc.abstractmethod
    def prune(self):
        pass


    def plan(self):
        while len(self._frontier) > 0:
            self._next_node = self.select()                                # (i)
            self._expanded.append(self._next_node)

            if self._next_node.satisfies(self.goal_state):                 # (ii)
                print("Plan found:", self._next_node.get_plan())
                return True
            #else:
            #    print("Rejecting plan:", self._next_node.get_plan())
                
            self._children = self.expand(self._next_node)

            # prune nodes from collections
            self.prune()                                                   # (iii)
            for child in self._children:
                self._frontier.append(child)                               # (iv)
        print("No plan found")
        return False


class Breadth_First_Planner(Planner):
    def __init__(self, init_state, goal_state, actions) -> None:
        super().__init__(init_state, goal_state, actions)

    def select(self):
        return self._frontier.pop(0)

    def expand(self, node):
        node.expand(self._actions)
        return node.children

    def prune(self):
        #if a child node has already been expanded, delete it
        for child in self._children:
            if child in self._expanded:
                self._children.remove(child)


if __name__ == '__main__':
    initial_state = State((10,10))
    goal_state = State((12,9))
    actions = [Action('N', (-1, 0)), Action('S', (1, 0)), Action('E', (0, 1)), Action('W', (0, -1))]

    planner = Breadth_First_Planner(initial_state, goal_state, actions)
    planner.plan()