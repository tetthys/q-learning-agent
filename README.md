# q-learning-agent

파이썬으로 정의한 Q-Learning 에이전트에 대한 읽기 쉽고 사용하는 것도 쉬운 개념적인 추상 인터페이스입니다. 오픈 소스이며 PR은 언제든지 환영합니다!

# 테스트 방법

## Windows (WSL2)

```bash
bash ./run/test.sh
```

## Mac

```bash
docker compose build test-runner
```

```bash
docker compose run --rm test-runner
```

# 패키지 사용 방법

## 먼저 Q 테이블 객체를 생성합니다.

```python
q_table = QTable()
```

## 그 다음 에이전트와 직접적으로 상호작용하는 환경 객체를 생성합니다.

```python
environment_data = [
    # It could really be anything.
]
environment = Environment(environment_data)
```

## Q-Learning 알고리즘이 액션을 선택하는 데에 필요한 정책이 필요하기에 정책 객체를 생성합니다.

```python
action_policy = ActionPolicy()
```

## 최종적으로 에이전트 객체를 Q 테이블 객체, 환경 객체, 정책 객체와 조합하여 생성한 후, 학습 횟수를 지정하면 됩니다.

```python
agent = Agent(environment, q_table, action_policy)
agent.learn(10)
```