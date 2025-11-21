from abc import ABC, abstractmethod
from src.contracts import QTable, ActionPolicy, Element, State, Environment

class Agent(ABC):
    def __init__(
        self, environment: Environment, q_table: QTable, action_policy: ActionPolicy
    ) -> None:
        self.environment = environment
        self.q_table = q_table
        self.action_policy = action_policy

    def learn(self, times: int) -> None:
        for _ in range(times):
            # select an action based on the current state
            action = self.action_policy.select(self.q_table, self.get_current_state())

            # perform the action in environment
            new_state, reward = self.environment.perform(action)

            # TODO use generalized format
            # make an element to update the Q-table
            element = Element()

            # update the Q-table based on the new experience
            self.q_table.update(element)
            pass

    @abstractmethod
    def get_current_state(self) -> State:
        pass
