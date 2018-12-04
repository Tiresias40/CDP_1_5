# Tasks

j/h : Jour / Homme (une colomne du tableau final)

BD : base de données

Dev : développeur / utilisateur dans la BD

Lien vers le Trello : https://trello.com/b/ONLkJXed

On considère qu'une tâche est "DONE" lorsque le composant associé est fonctionnel et que les tests associés qui valident l'US correspondante sont valides.

## Tâches du Sprint 2 :

| Id | Composant | Description | Coût (en jour/homme) | Issue(s) associée(s) |
| --- | --- | --- | --- | --- |
| T1 | nav.html | Création d'une barre de navigation (importée sur les pages index.html, issues.html, devManagement.html) comportant, dans un premier temps, un bouton "Accueil" amenant à la page index.html, un bouton "Déconnexion" amenant à la page connexion.html. Dans un second temps, une fois un projet sélectionné dans l'application, apparaîtront un onglet "Issues" amenant à la page issues.html et un onglet "Gestion" amenant à la page devManagement.html. | 0.5 | X |
| T2 | projectManagement.html | Création d'une page affichant une liste de tous les projets du Dev connecté. On trouvera sur la page un bouton "Ajouter un projet" ouvrant un formulaire (sous la forme d'une fenêtre) dont l'unique champ à remplir sera "Nom du projet". Cliquer sur un projet amène à la page issues.html en chargeant les données de ce projet dans l'application. | 0.5 | #3 |
| T3 | projectManagement.py | Écriture de plusieurs fonctions permettant l'ajout, la modification et la suppression d'un projet dans la BD et la récupération de toutes les informations (Issues, Dev) liées à un projet (à partir de son Nom et/ou Id). | 1 | #3 |
| T4 | issues.html | Création d'une page affichant le Backlog (liste d'Issues) du projet. Chaque Issue (Id, Description, Priorité, Difficulté, Sprint) aura deux boutons associés, "Modifier" permettant la modification de n'importe lequel de ces champs et "Supprimer" permettant de supprimer l'Issue du Backlog. En fin de liste se trouvera un bouton "Ajouter une issue" ouvrant un formulaire (sous la forme d'une fenêtre) où l'utilisateur remplira les champs caractéristiques d'une Issue. | 0.5 | #5 |
