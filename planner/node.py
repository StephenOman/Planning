# Base class for the nodes used by the planner

import random

class Node():
    """
    A Node in the planning graph encapsulates a state, the action that
    led to that state and a reference to the parent node. For the root
    node, the initial_state should be set instead.
    """
    def __init__(self, parent, action, initial_state) -> None:
        super().__init__()
        if initial_state:
            self.parent = None
            self.action = None
            self.state = initial_state

            self.plan = []
            self.cost = 0
        elif (parent and action):
            self.parent = parent
            self.action = action
            self.state = parent.state.apply(action)

            self.plan = parent.plan.copy()
            self.plan.append(action)
            self.cost = parent.cost + action.cost

    def get_plan(self):
        pl = []
        for step in self.plan:
            pl.append(step.name)
        return pl

    def satisfies(self, state):
        if self.state == state:
            return True
        else:
            return False


class NodeFactory():
    def __init__(self) -> None:
        self._nodes = {}
        self.head = None

    def produce_head(self, state):
        self.head = Node(initial_state = state)
        #TODO Need to work out a way of generating hash key for the state- 
        #     the location here is specific to a location state and should
        #     not be used for generic states
        node_key = state.location
        self._nodes[node_key] = self.head
        return self.head

    def produce(self, parent, action) -> Node:
        state =  parent.state.apply(action)
        if state.location in self._nodes.keys():
            return self._nodes[state.location]
        else:
            new_node = Node(parent, action)
            node_key = new_node.state.location
            self._nodes[node_key] = new_node
            return new_node

    def expand(self, node: Node, actions):
        """
        for act in actions:
            if node.state.is_applicable(act):
                child = self.produce(node, act)
                node.children.append(child)
        """
        # randomise the order of the actions
        act_list = actions.copy()
        while len(act_list) > 0:
            index = random.randint(0, len(act_list)-1)
            act = act_list.pop(index)
            if node.state.is_applicable(act, map):
                child = self.produce(node, act, map)
                node.children.append(child)