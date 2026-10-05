from nim import Action
from nim.ai import QLearning


def test_get_q_value_default() -> None:
    ai = QLearning()
    assert ai.get_q_value((1, 1, 1), Action(0, 1)) == 0.0, (
        "La Q-Value d'une paire inconnue devrait retourner 0"
    )


def test_update_q_value() -> None:
    alpha = 0.5
    gamma = 0.3
    some_state = (1, 1)
    some_action = Action(0, 1)
    old_q = 0.0
    reward = 10.0
    future_rewards = 5.0

    ai = QLearning(alpha=alpha, gamma=gamma)
    ai.update_q_value(some_state, some_action, old_q, reward, future_rewards)

    expected = old_q + alpha * (reward + gamma * future_rewards - old_q)

    assert ai.q[((1, 1), Action(0, 1))] == expected
