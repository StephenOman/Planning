class Action():
    """
    Name = name of the action, e.g. 'N', 'S', 'E', 'W'
    Effect = tuple(y,x), where y = change in location in the
        vertical axis and x = change in the horizontal axis
        location
    """
    def __init__(self, name, effect: tuple) -> None:
        self.name = name
        self.effect = effect

        # TODO: Variable costs for different actions
        self.cost = 1

    """
    gets the expected effect of this action
    on the location (y,x) passed in 
    """
    def get_effect(self, location):
        # Make sure that the agent cannot move off the screen
        vertical = max(0, location[0] + self.effect[0])
        horizontal = max(0, location[1] + self.effect[1])

        # TODO: Check that these are the valid dimensions of the dungeon
        vertical = min(vertical, 20)
        horizontal = min(horizontal, 80)

        # TODO: Check against things you cannot move into, like walls etc
        return (vertical, horizontal)

if __name__ == '__main__':
    actions = [Action('N', (-1, 0)), Action('S', (1, 0)), Action('E', (0, 1)), Action('W', (0, -1))]

    current_state = (10,10)

    print('Loc:', current_state)
    for act in actions:
        print(act.name, act.get_effect(current_state))





