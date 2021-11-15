from abc import ABC, abstractmethod

# Abstract base class for states

class State(ABC):
    def __init__(self, state_vars):
        """
        The state_vars contain the state variables that you want to
        store to represent the state in your domain.

        These should be represented as key, value pairs in a dictionary
        """
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