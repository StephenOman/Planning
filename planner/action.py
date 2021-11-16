# Abstract base class for actions

from abc import ABC, abstractmethod

class Action(ABC):
    def __init__(self, name, effects) -> None:
        """
        Each of the actions should have a name to identify it uniquely.
        The effects parameter is a collection of the effects that this
        action will have.
        """
        super().__init__()

        self.name = name
        self.effects = effects

    @abstractmethod
    def get_effect(self, state):
        """
        This method applies the action to the state. In effect, it
        creates a new state with updated state_vars, which are the
        effects
        """
        pass