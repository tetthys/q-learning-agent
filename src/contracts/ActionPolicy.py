from abc import ABC, abstractmethod
from src.contracts import QTable, State, Action

class ActionPolicy(ABC):
    
    @abstractmethod
    def select(self, q_table: QTable, current_state: State) -> Action:
        pass