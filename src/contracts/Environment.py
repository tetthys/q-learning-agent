# 범용 Environment 인터페이스

from abc import ABC, abstractmethod
from src.contracts import Action, State, Reward
from typing import Tuple, Mapping, Any

class Environment(ABC):

    def __init__(self, data: Mapping[str, Any]) -> None:
        self.data = data

    @abstractmethod
    def perform(self, action: Action) -> Tuple[State, Reward]:
        pass