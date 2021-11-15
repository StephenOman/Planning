import glyphs

import logging

logger = logging.getLogger(__name__)

class Action():
    """
    Name = name of the action, e.g. 'N', 'S', 'E', 'W'
    Effect = tuple(y,x), where y = change in location in the
        vertical axis and x = change in the horizontal axis
        location
    """
    def __init__(self, name, effect: tuple, step) -> None:
        self.name = name
        self.effect = effect
        self.step = step

        # TODO: Variable costs for different actions
        self.cost = 1

    """
    gets the expected effect of this action
    on the location (y,x) passed in 
    """
    def get_effect(self, location, map):
        # Make sure that the agent cannot move off the top or left
        vertical = max(0, location[0] + self.effect[0])
        horizontal = max(0, location[1] + self.effect[1])

        # Stop from moving off the bottom or right
        vertical = min(vertical, 20)
        horizontal = min(horizontal, 78)

        # Check against things you cannot move into, like walls etc
        glyph = map[vertical][horizontal]
        if glyph in glyphs.WALLS or glyph == glyphs.UNKNOWN or glyph == glyphs.EMPTY:
            return location

        return (vertical, horizontal)





