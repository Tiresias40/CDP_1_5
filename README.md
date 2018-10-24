Application Web-UI avec base de données (SQL). En html-CSS-javascript (Bootstrap). Serveur python (Flask). \[|]/

2 rôles : Chef de projet (CP) & Développeur (Dev)

0. Préface

    a. En tant que Dev / CP, je souhaite me connecter / déconnecter afin d'accéder à l'outil.

1. Issues

    a. En tant que CP, je souhaite ajouter une issue afin de gérer le backlog.
    b. En tant que CP, je souhaite supprimer une issue afin de gérer le backlog.
    c. En tant que CP, je souhaite modifier une issue afin de gérer le backlog.
    d. En tant que Dev, je souhaite visualiser le backlog afin de connaître les issues de mon projet.
    e. En tant que Dev, je souhaite exporter le backlog afin d'y accéder hors ligne.

2. Tasks

    a. En tant que CP, je souhaite ajouter un composant afin de concevoir l'architecture de mon projet.
    b. En tant que CP, je souhaite supprimer un composant afin de concevoir l'architecture de mon projet.
    c. En tant que CP, je souhaite modifier un composant afin de concevoir l'architecture de mon projet.
    d. En tant que Dev, je souhaite visualiser la liste des composants afin de connaître leurs détails (quand je clique dessus).
    e. En tant que Dev, je souhaite exporter la liste des composants afin d'y accéder hors ligne.

    f. En tant que CP, je souhaite créer / modifier le tableau d'estimation du coût en j/h des tâches afin d'organiser mon projet.
    g. En tant que CP, je souhaite ajouter des dépendances à mes tâches afin de générer automatiquement le graphe de dépendances des tâches.
    h. En tant que CP, je souhaite créer un diagramme de Pert à partir du graphe de dépendances des tâches afin de prévoir les deadlines de mon projet et estimer le nombre de développeurs à affecter au projet. 

    i. En tant que CP, je souhaite construire / modifier un planning afin d'assigner les tâches de mon projet à mes Dev.
    j. En tant que Dev, je souhaite visualiser le planning afin de connaître les tâches qui me sont assignées.
    e. En tant que Dev, je souhaite exporter le planning afin d'y accéder hors ligne.

3. Tests

    a. En tant que CP, je souhaite écrire des scénarios de tests afin de vérifier si le projet correspond aux issues.
    b. En tant que Dev, je souhaite consulter les scénarios de tests afin de les implémenter.
    c. En tant que Dev, je souhaite importer le résultat d'un test associé à un scénario afin de garder une trace de ce résultat.
    d. En tant que CP, je souhaite pouvoir suivre les résultats des scénarios de tests afin de savoir s'ils sont passés ou non.

4. Code

    a. En tant que CP, je souhaite écrire une nomenclature du code afin d'assurer un code propre dans le projet.
    b. En tant que Dev, je souhaite visualiser la nomenclature du code afin de coder selon les normes établies par le CP.

    // c. En tant que CP, je souhaite ajouter les résultats d'un linter afin de suivre la propreté du code fichier par fichier
    // d. En tant que Dev, je souhaite accéder aux résultats d'un linter pour un fichier afin de le corriger et le rendre pur

5. Doc

    a. En tant que CP, je souhaite écrire une nomenclature de la documentation afin d'assurer une documentation propre dans le projet.
    b. En tant que Dev, je souhaite visualiser la nomenclature de la documentation afin de documenter selon les normes établies par le CP.

    // c. En tant que CP, je souhaite ajouter de la documentation pour l'installation de l'environnement du projet
    // d. En tant que Dev, je souhaite visualiser cette documentation

6. Release

    a. En tant que CP, je souhaite ajouter une release à la liste de celles-ci afin de garder une trace de mes progrès.
    b. En tant que Dev, je souhaite visualiser la liste des releases afin de voir l'historique de notre projet.

Annexes :

Issue :
    - Id
    - Description
    - Priorité
    - Difficulté
    - Dépendances

Backlog :
    Liste d'issues

Composant :
    - Id (TA, TB, etc ...)
    - Nom du fichier
    - Description
    - Dépendances avec les autres composants

Tâches :
    - Définition d'interface d'un composant (nommage des fichiers, des variables, etc ...)
    - Réalisation d'un composant
    - Ecriture d'un scénario de test d'une issue (user story)
    - Exécution d'un scénario de test d'une issue (user story)

Scénario d'un test :
    Liste d'actions que l'utilisateur effectue pour respecter une issue

Résultat d'un test :
    - Id
    - Status
    - Date
    - Version du projet

Release :
    - N° de version
    - Date
    - Tâches implémentées