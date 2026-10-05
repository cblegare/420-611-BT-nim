from typing import Literal

from nim import Action, Board, Probability, QValue

type Algorithm = Literal["greedy", "epsilon-greedy"]


class QLearning:
    def __init__(
        self,
        epsilon: Probability = 0.1,
        alpha: Probability = 0.0,
        gamma: Probability = 0.0,
    ):
        r"""Initialise l'IA.

        Une IA nouvellement initialisée possède
        un dictionnaire d'apprentissage Q vide,
        un taux d'apprentissage (alpha)
        et un taux d'exploration (epsilon).

        Args:
            epsilon:
                Le taux d'exploration.

                TODO: (3 points)
                    Identifier une valeur par défaut
                    et documenter le paramêtre alpha de manière à expliquer
                    le sens du paramêtre et le choix de sa valeur.
            alpha:
                Le facteur d'apprentissage.

                TODO: (3 points)
                    Identifier une valeur par défaut
                    et documenter le paramêtre alpha de manière à expliquer
                    le sens du paramêtre et le choix de sa valeur.
            gamma:
                Le facteur d'actualisation.

                Dans le Q-learning, γ (:math:`\gamma`) multiplie l'estimation
                de la valeur future optimale.
                L'importance accordée à la récompense suivante est définie
                par le paramètre gamma.

                Gamma est un nombre réel compris entre 0 et 1
                (:math:`0 \leq \gamma \leq 1`).
                Si l'on fixe gamma à zéro, l'agent ignore totalement les
                récompenses futures ;
                de tels agents ne prennent en compte que les récompenses
                immédiates.
                En revanche, si l'on fixe gamma à 1,
                l'algorithme recherche des récompenses élevées à long terme.

                TODO: (1 point)
                    Identifier une valeur par défaut


        Le dictionnaire d'apprentissage Q associe les paires (état, action) à
        une valeur-Q.

        """
        self.q: dict[tuple[Board, Action], QValue] = {}
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma

    def update(
        self, old_state: Board, action: Action, new_state: Board, reward: QValue
    ) -> None:
        """Met à jour le modèle Q-learning.

        Args:
            old_state:
                L'état avant l'action.
            action:
                L'action entreprise.
            new_state:
                L'état résultant de l'action.
            reward:
                La récompense obtenue.

        """
        old = self.get_q_value(old_state, action)
        best_future = self.best_future_reward(new_state)
        self.update_q_value(old_state, action, old, reward, best_future)

    def get_q_value(self, state: Board, action: Action) -> QValue:
        """Retourne la valeur-Q pour un état et une action donnés.

        Si aucune valeur-Q n'existe encore dans `self.q`, retourne 0.
        """
        # TODO: (10 points)
        #   Tester et implémenter get_q_value

    def update_q_value(
        self,
        state: Board,
        action: Action,
        old_q: QValue,
        reward: QValue,
        future_rewards: QValue,
    ) -> None:
        r"""Met à jour le Q-value.

        Args:
            state:
                L'état actuellement mis à jour.
            action:
                L'action qui met à jour l'état.
            old_q:
                L'ancienne valeur-Q pour cette paire état-action.
            reward:
                La récompense actuelle.
            future_rewards:
                L'estimation des récompenses futures.

        Utilise la formule:

        .. math::

            Q(S, A) <- Q_{old} + \alpha \cdot (Q_{new} - Q_{old})

        telle que :math:`Q_{old}` est l'ancienne Q-Value, :math:`\alpha` est le
        taux d'apprentissage, et :math:`Q_{new}` est la somme de la récompense
        actuelle et l'estimation des récompenses futures pondérée par le
        facteur d'actualisation.

        """
        # TODO: (10 points)
        #   Tester et implémenter update_q_value
        raise NotImplementedError

    def best_future_reward(self, state: Board) -> QValue:
        """Estime la meilleure récompense future étant donné un état `state`.

        Considère toutes les paires `(état, action)` possibles disponibles
        dans cet état et retourne le maximum de toutes leurs valeurs-Q.
        Utilise 0 comme valeur-Q si une paire n'a pas de valeur-Q dans
        `self.q`.
        S'il n'y a aucune action disponible dans l'état, retourne 0.

        """
        # TODO: (10 points)
        #   Tester et implémenter best_future_reward
        raise NotImplementedError

    def choose_action(self, state: Board, train: bool = True) -> Action:
        """Étant donné un état, retourne une action à entreprendre.

        Si `train` est `False`, retourne la meilleure action disponible dans cet
        état (celle ayant la plus haute valeur-Q, en utilisant 0 pour les paires
        sans valeur-Q).

        Si `train` est `True`, choisit une action disponible aléatoire avec la
        probabilité `self.epsilon`, sinon choisit la meilleure action
        disponible.

        Si plusieurs actions ont la même valeur-Q, n'importe laquelle d'entre
        elles est une valeur de retour acceptable.

        """
        # TODO: (10 points)
        #   Tester et implémenter choose_action
        raise NotImplementedError
