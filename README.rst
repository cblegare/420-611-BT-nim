Travail pratique: Nim
=====================

Dans le jeu de Nim, deux joueurs s'affrontent pour vider tour-à-tour des
tas d'objets. 
À chaque tour, un joueur retire un nombre quelconque d'objets d'un tas. 
Le joueur qui prend le dernier objet des tas a perdu.

Nous utiliserons le *Q-Learning* pour entraîner un agent à jouer au Nim.
Rappelez-vous que dans le Q-learning, nous essayons d'apprendre une valeur 
de récompense (un nombre) pour chaque paire `(état, action)`. 
Une action qui fait perdre la partie aura une récompense de -1, 
une action qui gagne la partie aura une récompense de 1, 
et une action qui fait que la séquence continue a une 
récompense immédiate de 0, mais aura également une récompense future.


Rappelez-vous que la formule clé pour le Q-learning est ci-dessous.
Chaque fois que nous sommes dans un état `s` et que nous prenons une action `a`, nous
pouvons mettre à jour la valeur Q `Q(s, a)` selon

.. math::

    Q(s, a) \leftarrow Q(s, a) + \alpha \cdot (Q_{new} - Q_{old})
