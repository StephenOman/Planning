from abc import ABC, abstractmethod

# Abstract base class for states

class State(ABC):
    def __init__(self, state_vars) -> None:
        """
        The state_vars contain the state variables that you want to
        store to represent the state in your domain.

        These should be represented as key, value pairs in a dictionary
        """
        super().__init__()
        self.state_vars = state_vars

    @abstractmethod
    def is_applicable(self, action) -> bool:
        """
        This method should determine if given a state instance,
        is the action applicable to that state. It should return
        True is the action is applicable, and False otherwise.
        """
        pass

    @abstractmethod
    def apply(self, action):
        """
        This method applies the action to the state instance. 
        Note that it should return a new state instance rather
        than updating the existing one
        """
        pass

    def __eq__(self, o: object) -> bool:
        for var in self.state_vars.keys():
            if var not in o.state_vars.keys():
                return False
            if self.state_vars[var] != o.state_vars[var]:
                return False
        return True