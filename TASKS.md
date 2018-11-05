# Tasks

j/h : Jour / Homme (une colomne du tableau final)
BD : base de données
Dev : développeur

Tâches du Sprint 1 :

Installation du serveur                      1 j/h
Installation de Docker                       0.5 j/h  

On prévoit d'écrire toutes les interfaces des fichiers en deux réunions des membres du projet (durée prévue d'1 j/h).

database.py                                  1 j/h
  Installation de la BD.

connexion.html                               0.5 j/h
  Interface de connexion avec :
    - Deux champs :
      - Identifiant
      - Mot de passe
    - Deux boutons :
      - Inscription
      - Connexion

userManagement.py                            1 j/h
  Une fonction permet d'ajouter/modifier/supprimer un utilisateur à la BD.
  Une fonction permet de vérifier si un utilisateur est présent dans la BD.
  Une fonction permet de récupérer les projets liés à un utilisateur.


(Noms de fonctions à déplacer dans l'interface)
  addUser
  deleteUser
  modifyUser
  checkUser
  getUserWorkspace


nav.html                                     0.5 j/h
  Après s'être connecté un bouton "Accueil" et un bouton "Déconnection" apparaîssent dans une barre de navigation.
  Après avoir choisi un projet, une barre de navigation apparait avec deux onglets :
    - Issue
    - Gestion

index.html                                   0.5 j/h
  (importe nav.html)
  Affiche une liste de tous les projets affiliés au Dev connecté, un bouton "Ajouter un projet" qui ouvre une pop-up avec un formulaire à remplir (nom du projet)
  Cliquer sur un projet amène à la page issues.html.

projectManagement.py                         0.5 j/h
  Une fonction permet d'ajouter/modifier/supprimer un projet à la BD.
  Une fonction permet de récuperer toutes les informations liées à un projet (Issues, Développeurs).


(Noms de fonctions à déplacer dans l'interface)
  addProject
  modifyProject
  deleteProject
  getProjectWorkspace


issues.html                                  0.5 j/h
  (importe nav.html)
  Affiche le "Backlog" du projet, chaque issue possède un bouton "Supprimer" et "Modifier".
  Un bouton permet de rajouter une Issue.

issuesManagement.py                          0.5 j/h
  Une fonction permet d'ajouter/modifier/supprimer une issue à la BD pour un projet.


(Noms de fonctions à déplacer dans l'interface)
  addIssue
  modifyIssue
  deleteIssue


devManagement.html                           0.5 j/h
  (importe nav.html)
  Une liste de Dev déjà présents sur le projet.
  Une barre de recherche et un bouton permet d'ajouter un Dev au projet.
  Un bouton permet de supprimer un Dev du projet.

devManagement.py                             1 j/h
  Une fonction permet d'ajouter/supprimer un Dev a la BD pour un projet.
  Une fonction permet de chercher un Dev dans la BD.


(Noms de fonctions à ajouter dans l'interface)
  addDev
  deleteDev
  searchDev
