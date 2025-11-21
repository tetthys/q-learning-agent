from src.contracts import Action, Agent, QTable, Reward, ActionPolicy, State

def test_agent_can_learn():
    q_table = QTable()

    # stub data
    data = [
        (("state1", "action1"), 0.5),
        (("state1", "action2"), 0.2),
        (("state2", "action1"), 0.8),
    ]

    agent = Agent(q_table, data)

    assert agent is not None


def test_action_policy_can_select():
    action_policy = ActionPolicy()

    q_table = QTable()

    current_state = State()

    action = action_policy.select(q_table, current_state)

    assert isinstance(action, Action)