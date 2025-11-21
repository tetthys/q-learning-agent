# 추상 Q-Table 인터페이스

from abc import ABC, abstractmethod
from src.contracts import Element

class QTable(ABC):
    
    @abstractmethod
    def update(self, element: Element) -> None:
        pass