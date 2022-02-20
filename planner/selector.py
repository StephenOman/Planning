# Selector class
# 
# will select a node from the Frontier, returning the index of the node picked

import abc
import random
import plan_node

class Selector(abc.ABC):

    def __init__(self, heuristic, cost_func) -> None:
        self.heuristic = heuristic
        self.cost_func = cost_func

    @abc.abstractmethod
    def select(frontier) -> None:
        if len(frontier) == 0:
            raise IndexError
        return


# Selector that returns the first node index from the Frontier
class FirstSelector(Selector):
    def __init__(self, heuristic, cost_func) -> None:
        super().__init__(heuristic, cost_func)

    def select(frontier) -> None:
        super().select(frontier)
        return 0


# Selector that returns the last node index from the Frontier
class LastSelector(Selector):
    def __init__(self, heuristic, cost_func) -> None:
        super().__init__(heuristic, cost_func)

    def select(frontier) -> None:
        super().select(frontier)
        return len(frontier) - 1


# Selector that returns a random node index from the Frontier
class RandomSelector(Selector):
    def __init__(self, heuristic, cost_func) -> None:
        super().__init__(heuristic, cost_func)

    def select(frontier) -> None:
        super().select(frontier)
        return random.randint(0, len(frontier) - 1)


# Selector that returns the node that has the shortest
# number of steps in its plan from the Frontier
# TODO if there are multiple options - apply the heuristic
class MiniStepSelector(Selector):
    def __init__(self, heuristic, cost_func) -> None:
        super().__init__(heuristic, cost_func)

    def select(frontier) -> None:
        super().select(frontier)
        steps = len(frontier[0].plan)
        index = 0
        for node_index in range(1,len(frontier)-1):
            nsteps = len(frontier[node_index].plan)
            if nsteps < steps:
                steps = nsteps
                index = node_index
        return index


# Selector that returns the node that has the longest
# number of steps in its plan from the Frontier
# TODO if there are multiple options - apply the heuristic
class MaxiStepSelector(Selector):
    def __init__(self, heuristic, cost_func) -> None:
        super().__init__(heuristic, cost_func)

    def select(frontier) -> None:
        super().select(frontier)
        steps = len(frontier[0].plan)
        index = 0
        for node_index in range(1,len(frontier)-1):
            nsteps = len(frontier[node_index].plan)
            if nsteps > steps:
                steps = nsteps
                index = node_index
        return index


# Selector that returns the node that has the lowest
# cost of it's plan from the Frontier
# TODO if there are multiple options - apply the heuristic
class MiniCostSelector(Selector):
    def __init__(self, heuristic, cost_func) -> None:
        super().__init__(heuristic, cost_func)

    def select(frontier) -> None:
        super().select(frontier)
        cost = len(frontier[0].plan)
        index = 0
        for node_index in range(1,len(frontier)-1):
            ncost = len(frontier[node_index].plan)
            if ncost < cost:
                cost = ncost
                index = node_index
        return index


# Selector that returns the node that has the highest
# cost of it's plan from the Frontier
# TODO if there are multiple options - apply the heuristic
class MaxiCostSelector(Selector):
    def __init__(self, heuristic, cost_func) -> None:
        super().__init__(heuristic, cost_func)

    def select(frontier) -> None:
        super().select(frontier)
        cost = len(frontier[0].plan)
        index = 0
        for node_index in range(1,len(frontier)-1):
            ncost = len(frontier[node_index].plan)
            if ncost > cost:
                cost = ncost
                index = node_index
        return index