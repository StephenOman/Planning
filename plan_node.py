from typing import List
from state import State
from action import Action

class Node:
    def __init__(self, parent, action: Action) -> None:
        if parent and action:
            self.parent = parent
            self.plan = parent.plan.copy()
            self.plan.append(action)
            self.state =  parent.state.apply(action)
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

    def expand(self, actions):
          for act in actions:
              if self.state.is_applicable(act):
                  #ToDo need to be a bit clever here
                  #   don't create a new node if one
                  #   already exists with this state
                  child = Node(self, act)
                  self.children.append(child)

    def satisfies(self, state: State):
        if state.location == self.state.location:
            return True
        else:
            return False



if __name__ == '__main__':
    actions = [Action('N', (-1, 0)), Action('S', (1, 0)), Action('E', (0, 1)), Action('W', (0, -1))]
    current_state = State((10,10))
    start = Node(current_state, None)

    start.expand(actions)

    for child in start.children:
        print('Child loc', child.state.location, 'with parent location', child.parent.state.location)
        print('Plan to get there', child.get_plan(), 'and plan cost', child.cost)

    print("Negative goal check", start.satisfies(State((0,0))))
    print("Positive goal check", start.satisfies(current_state))

    print('Plan B :)')
    current_state = State((0,0))
    start = Node(current_state, None)

    start.expand(actions)

    for child in start.children:
        print('Child loc', child.state.location, 'with parent location', child.parent.state.location)
        print('Plan to get there', child.get_plan(), 'and plan cost', child.cost)