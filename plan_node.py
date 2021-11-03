from typing import List
from state import State
from action import Action

import random

import logging

logger = logging.getLogger(__name__)

class Node:
    def __init__(self, parent, action: Action, map) -> None:
        if parent and action:
            self.parent = parent
            self.plan = parent.plan.copy()
            self.plan.append(action)
            self.state =  parent.state.apply(action, map)
            self.cost = parent.cost + action.cost
        else:
            self.parent = None
            self.plan = []
            self.state = parent
            self.cost = 0

        self.children = []

    def get_plan(self):
        pi = []
        for step in self.plan:
            pi.append(step.name)
        return pi

    def satisfies(self, state: State):
        if state.location == self.state.location:
            return True
        else:
            return False


class NodeFactory():
    def __init__(self) -> None:
        self._nodes = {}
        self.head = None

    def produce_head(self, state):
        self.head = Node(state, None, None)
        node_key = state.location
        self._nodes[node_key] = self.head
        return self.head

    def produce(self, parent, action:Action, map) -> Node:
        state =  parent.state.apply(action, map)
        if state.location in self._nodes.keys():
            return self._nodes[state.location]
        else:
            new_node = Node(parent, action, map)
            node_key = new_node.state.location
            self._nodes[node_key] = new_node
            return new_node

    def expand(self, node: Node, actions: List, map):
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



if __name__ == '__main__':
    actions = [Action('N', (-1, 0)), Action('S', (1, 0)), Action('E', (0, 1)), Action('W', (0, -1))]
    current_state = State((10,10))

    nf = NodeFactory()
    current_state = State((10,10))
    head = nf.produce_head(current_state)
    print("Node location from factory", head.state.location)

    child_node1 = nf.produce(head, actions[0])
    if head == child_node1:
        print("Head and other are the same object")
    else:
        print("Head and other are different")

    child_node2 = nf.produce(child_node1, actions[1])
    if head == child_node2:
        print("Head and other are the same object")
    else:
        print("Head and other are different")

    nf.expand(head, actions)
    for child in head.children:
        print('Child loc', child.state.location, 'with parent location', child.parent.state.location)
        print('Plan to get there', child.get_plan(), 'and plan cost', child.cost)

    print("Negative goal check", head.satisfies(State((0,0))))
    print("Positive goal check", head.satisfies(current_state))