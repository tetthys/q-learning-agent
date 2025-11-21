from src.contracts import Action, Agent, QTable, Reward, ActionPolicy, State, Environment

def test_agent_can_learn():
    q_table = QTable()

    environment_data = []

    environment = Environment(environment_data)

    action_policy = ActionPolicy()

    agent = Agent(environment, q_table, action_policy)

    agent.learn(10)

    assert agent is not None


def test_action_policy_can_select():
    action_policy = ActionPolicy()

    q_table = QTable()

    current_state = State()

    action = action_policy.select(q_table, current_state)

    assert isinstance(action, Action)