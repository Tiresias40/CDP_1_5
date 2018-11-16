# Tasks

j/h : Jour / Homme (une colomne du tableau final)

BD : base de données

Dev : développeur / utilisateur dans la BD

lien vers le Trello : https://trello.com/b/ONLkJXed

## Tâches du Sprint 1 :

| Id | Composant | Description | Coût (en jour/homme) |
| --- | --- | --- | --- |
| T1 | nav.html | Création d'une barre de navigation (importée sur les pages index.html, issues.html, devManagement.html) comportant, dans un premier temps, un bouton "Accueil" amenant à la page index.html, un bouton "Déconnexion" amenant à la page connexion.html. Dans un second temps, une fois un projet sélectionné dans l'application, apparaîtront un onglet "Issues" amenant à la page issues.html et un onglet "Gestion" amenant à la page devManagement.html. | 0.5 |
| T2 | index.html | Création d'une page affichant une liste de tous les projets du Dev connecté. On trouvera sur la page un bouton "Ajouter un projet" ouvrant un formulaire (sous la forme d'une fenêtre) dont l'unique champ à remplir sera "Nom du projet". Cliquer sur un projet amène à la page issues.html en chargeant les données de ce projet dans l'application. | 0.5 |
| T3 | projectManagement.py | Écriture de plusieurs fonctions permettant l'ajout, la modification et la suppression d'un projet dans la BD et la récupération de toutes les informations (Issues, Dev) liées à un projet (à partir de son Nom et/ou Id). | 1 |
| T4 | issues.html | Création d'une page affichant le Backlog (liste d'Issues) du projet. Chaque Issue (Id, Description, Priorité, Difficulté, Sprint) aura deux boutons associés, "Modifier" permettant la modification de n'importe lequel de ces champs et "Supprimer" permettant de supprimer l'Issue du Backlog. En fin de liste se trouvera un bouton "Ajouter une issue" ouvrant un formulaire (sous la forme d'une fenêtre) où l'utilisateur remplira les champs caractéristiques d'une Issue. | 0.5 |
| T5 | issueManagement.py | Écriture de plusieurs fonctions permettant l'ajout, la modification et la suppression d'une Issue dans la BD. | 1 |
| T6 | devManagement.html | Création d'une page affichant une liste de Dev présents sur le projet. À côté de chaque Dev se trouvera un bouton "Supprimer" retirant le Dev du projet. On trouvera aussi sur la page une barre de recherche dans laquelle l'utilisateur pourra taper l'Identifiant d'un Dev. Une liste de Dev correspondant à cet Identifiant sera alors affichée en dessous de la barre de recherche. À côté de chaque Dev se trouvera un bouton "Ajouter" ajoutant le Dev au projet. | 0.5 |
| T7 | devManagement.py | Écriture de plusieurs fonctions permettant l'ajout, la modification et la suppression d'un Dev par rapport à un projet spécifique dans la BD et la recherche d'un Dev dans la BD (à partir de son Identifiant utilisateur). | 1 |
| T8 | sprints.html | Création d'une page affichant sur la gauche une liste des sprints du projet. Cliquer sur un sprint affichera au centre de la page la liste des tâches de ce sprint. | 0.5 |
| T9 | sprints.py | Écriture de plusieurs fonctions permettant l'ajout et la suppression  d'un sprint dans la BD. | 0.5 |
| T10 | tasks.py | Écriture de plusieurs fonctions permettant l'ajout, la modification et la suppression d'une tâche dans la BD. Une fonction devra aussi renvoyer les données d'une tâche (Id, Composant, Description, Coût en jour / homme). | 1 |
| T11 | tests.html | Création d'une page affichant une liste de scénarii de tests. Sous chaque scénario se trouvera les résultats du test (Validation, Date). | 0.5 |
| T12 | tests.py | Écriture de plusieurs fonctions permettant l'ajout, la modification et la suppression d'un scénario de test dans la BD ainsi que l'ajout, la modification et la suppression de résultat associé à un test (Validation, Date) dans la BD.| 1 |
