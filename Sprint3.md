# Tasks

j/h : Jour / Homme (une colomne du tableau final)

BD : base de données

Dev : développeur / utilisateur dans la BD

Lien vers le Trello : https://trello.com/b/ONLkJXed

On considère qu'une tâche est "DONE" lorsque le composant associé est fonctionnel et que les tests associés qui valident l'US correspondante sont valides.

## Tâches du Sprint 3 :

| Id | Composant | Description | Coût (en jour/homme) | Issue(s) associée(s) |
| --- | --- | --- | --- | --- |
| T1 | issueManagement.py | Écriture de plusieurs fonctions permettant l'ajout, la modification et la suppression d'une Issue dans la BD. | 1 | #5 |
| T2 | devManagement.html | Création d'une page affichant une liste de Dev présents sur le projet. À côté de chaque Dev se trouvera un bouton "Supprimer" retirant le Dev du projet. On trouvera aussi sur la page une barre de recherche dans laquelle l'utilisateur pourra taper l'Identifiant d'un Dev. Une liste de Dev correspondant à cet Identifiant sera alors affichée en dessous de la barre de recherche. À côté de chaque Dev se trouvera un bouton "Ajouter" ajoutant le Dev au projet. | 0.5 | #4 |
| T3 | devManagement.py | Écriture de plusieurs fonctions permettant l'ajout, la modification et la suppression d'un Dev par rapport à un projet spécifique dans la BD et la recherche d'un Dev dans la BD (à partir de son Identifiant utilisateur). | 1 | #4 |
| T4 | sprints.html | Création d'une page affichant sur la gauche une liste des sprints du projet. Cliquer sur un sprint affichera au centre de la page la liste des tâches de ce sprint. Un tableau d'estimation des coûts en jour / homme apparaît en fin de page. | 1 | #6, #7, #8 |
| T5 | sprints.py | Écriture de plusieurs fonctions permettant l'ajout et la suppression  d'un sprint dans la BD. | 0.5 | #6 |
| T6 | tasks.html | Création d'une page affichant la liste des tâches d'un sprint ainsi que leurs informations (Composant, Description, Coût en j/h, Status). A côté de chaque tâche se trouvera trois boutons (Ajout, Modification, Suppression). En bas de page se trouvera un tableau interactif permettant de visualiser et modifier les status des tâches. | 1 | #7, #10 |
| T7 | tasks.py | Écriture de plusieurs fonctions permettant l'ajout, la modification et la suppression d'une tâche dans la BD. Une fonction devra aussi renvoyer les données d'une tâche (Id, Composant, Description, Coût en jour / homme). | 1 | #7 |
| T8 | tests.html | Création d'une page affichant une liste de scénarii de tests. Sous chaque scénario se trouvera les résultats du test (Validation, Date). | 0.5 | #12, #13, #14 |
| T9 | tests.py | Écriture de plusieurs fonctions permettant l'ajout, la modification et la suppression d'un scénario de test dans la BD ainsi que l'ajout, la modification et la suppression de résultat associé à un test (Validation, Date) dans la BD.| 1 | #12, #13, #14 |
| T10 | planning.html | Création d'une page affichant le planning des Dev pour le projet. | 1 | #9 |
| T11 | code.html | Création d'une page affichant la nomenclature du code. | 0.5 | #15 |
| T12 | code.py | Ecriture de plusieurs fonctions permettant d'écrire et de récupérer la nomenclature du code dans la BD. | 0.5 | #15 |
| T13 | documentation.html | Création d'une page affichant la nomenclature de la documentation. | 0.5 | #16 |
| T14 | documentation.py | Ecriture de plusieurs fonctions permettant d'écrire et de récupérer la nomenclature de la documentation dans la BD | 0.5 | #16 |
| T15 | release.html | Création d'une page affichant la liste des releases du projet. Un bouton "Ajouter" permet d'ajouter une release au projet. | 0.5 | #17 |
| T16 | release.py | Ecriture de plusieurs fonctions permettant d'ajouter et de récupérer la liste des releases dans la BD. | 0.5 | #17 |
