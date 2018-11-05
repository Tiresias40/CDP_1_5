# Tasks

j/h : Jour / Homme (une colomne du tableau final)

BD : base de données

Dev : développeur / utilisateur dans la BD

## Tâches du Sprint 1 :

| Id | Composant | Description | Coût (en jour/homme) |
| --- | --- | --- | --- |
| T1 | Fichiers générés par Flask | Installation du serveur | 1 |
| T2 | Dockerfile | Installation de Docker | 0.5 |
| Titf | Fichiers d'interface .txt | Écriture des interfaces de tous les fichiers du projet | 1 |
| T3 | database.py | Installation de la BD | 1 |
| T4 | connexion.html | Création d'une interface de connexion composée de deux champs (Identifiant, Mot de passe) et deux boutons (Inscription, Connexion) | 0.5 |
| T5 | userManagement.py | Écriture de plusieurs fonctions permettant l'ajout, la modification et la suppression d'un utilisateur dans la BD, la vérification de la présence d'un utilisateur dans la BD (à partir de son Identifiant) et la récupération des projets d'un utilisateur (à partir de son Identifiant) | 1 |
| T6 | nav.html | Création d'une barre de navigation (importée sur les pages index.html, issues.html, devManagement.html) comportant, dans un premier temps, un bouton "Accueil" amenant à la page index.html, un bouton "Déconnexion" amenant à la page connexion.html. Dans un second temps, une fois un projet sélectionné dans l'application, apparaîtront un onglet "Issues" amenant à la page issues.html et un onglet "Gestion" amenant à la page devManagement.html. | 0.5 |
| T7 | index.html | Création d'une page affichant une liste de tous les projets du Dev connecté. On trouvera sur la page un bouton "Ajouter un projet" ouvrant un formulaire (sous la forme d'une fenêtre) dont l'unique champ à remplir sera "Nom du projet". Cliquer sur un projet amène à la page issues.html en chargeant les données de ce projet dans l'application. | 0.5 |
| T8 | projectManagement.py | Écriture de plusieurs fonctions permettant l'ajout, la modification et la suppression d'un projet dans la BD et la récupération de toutes les informations (Issues, Développeurs) liées à un projet (à partir de son Nom et/ou Id). | 0.5 |
| T9 | issues.html | Création d'une page affichant le Backlog (liste d'Issues) du projet. Chaque Issue (Id, Description, Priorité, Difficulté, Sprint) aura deux boutons associés, "Modifier" permettant la modification de n'importe lequel de ces champs et "Supprimer" permettant de supprimer l'Issue du Backlog. En fin de liste se trouvera un bouton "Ajouter une issue" ouvrant un formulaire (sous la forme d'une fenêtre) où l'utilisateur remplira les champs caractéristiques d'une Issue. | 0.5 |
| T10 | issueManagement.py | Écriture de plusieurs fonctions permettant l'ajout, la modification et la suppression d'une Issue dans la BD. | 0.5 |
| T11 | devManagement.html | Création d'une page affichant une liste de Développeurs présents sur le projet. À côté de chaque Dev se trouvera un bouton "Supprimer" retirant le Dev du projet. On trouvera aussi sur la page une barre de recherche dans laquelle l'utilisateur pourra taper l'Identifiant d'un Dev. Une liste de Dev correspondant à cet Identifiant sera alors affichée en dessous de la barre de recherche. À côté de chaque Dev se trouvera un bouton "Ajouter" ajoutant le Dev au projet. | 0.5 |
| T12 | devManagement.py | Écriture de plusieurs fonctions permettant l'ajout, la modification et la suppression d'un Dev par rapport à un projet spécifique dans la BD et la recherche d'un Dev dans la BD (à partir de son Identifiant utilisateur). | 1 |

Ci-dessous des débuts d'interfaces de quelques fichiers (à déplacer) :

userManagement.py :
  addUser
  deleteUser
  modifyUser
  checkUser
  getUserWorkspace

projectManagement.py :
  addProject
  modifyProject
  deleteProject
  getProjectWorkspace

issueManagement.py :
  addIssue
  modifyIssue
  deleteIssue

devManagement.py :
  addDev
  deleteDev
  searchDev
