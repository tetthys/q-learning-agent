from abc import ABC, abstractmethod
from src.contracts import State

class Action(ABC):
    
    @abstractmethod
    def perform(self) -> State:
        pass