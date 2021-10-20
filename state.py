from action import Action

class State():
    def __init__(self, location) -> None:
        self.location = location

    def is_applicable(self, act: Action):
        new_loc = act.get_effect(self.location)

        # check the agent would be able to move
        if new_loc == self.location:
            return False
        else:
            return True

    def apply(self, act: Action):
        return State(act.get_effect(self.location))


if __name__ == '__main__':
    current_state = State((10,10))
    actions = [Action('N', (-1, 0)), Action('S', (1, 0)), Action('E', (0, 1)), Action('W', (0, -1))]

    print('Loc:', current_state.location)
    for act in actions:
        print('Move', act.name, current_state.is_applicable(act))

    current_state = State((0,0))
    print('Loc:', current_state.location)
    for act in actions:
        print('Can move', act.name, current_state.is_applicable(act))


    current_state = State((10,10))
    print('Loc:', current_state.location)
    for act in actions:
        current_state = current_state.apply(act)
        print('Loc:', current_state.location)