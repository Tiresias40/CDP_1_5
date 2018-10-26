# Backlog

Application Web-UI avec base de données (SQL). Html-CSS-javascript (Bootstrap). Serveur python (Flask).

Le backlog couvre 2 rôles : Développeur (Dev) & Visiteur (V)

| Id | Description | Priorité | Difficulté | Sprint |
| --- | --- | --- | --- | --- |
| 1 | En tant que V, je souhaite créer un compte sur l'outil afin de participer à des projets. | | 2 | 1 |
| 2 | En tant que V, je souhaite me connecter / déconnecter en tant que Dev afin d'accéder à l'outil. | | 2 | 1 |
| 3 | En tant que Dev, je souhaite créer un nouveau projet sur l'outil. | | 1 | 1 |
| 4 | En tant que Dev, je souhaite ajouter / supprimer un nouveau Dev au projet. | | 1 | 1 |
| 5 | En tant que Dev, je souhaite ajouter / modifier / supprimer une issue au backlog du projet correspondant. | | 1 | 1 |
| 6 | En tant que Dev, je souhaite ajouter / supprimer un sprint à un projet. | | 1 | 2 |
| 7 | En tant que Dev, je souhaite ajouter / modifier / supprimer une tâche dans un sprint. | | 1 | 2 |
| 8 | En tant que Dev, je souhaite générer le tableau d'estimation du coût en jour/homme des tâches afin d'organiser mon projet. | | 1 | 2 |
| 9 | En tant que Dev, je souhaite construire / modifier un planning afin d'assigner les tâches aux développeurs. | | 3 | 3 |
| 10 | En tant que Dev, je souhaite écrire des scénarios de tests afin de vérifier si le projet correspond aux issues. | | 1 | 2 |
| 11 | En tant que Dev, je souhaite consulter les scénarios de tests afin de les implémenter. | | 1 | 2 |
| 12 | En tant que Dev, je souhaite importer le résultat d'un test associé à un scénario afin de garder une trace de ce résultat. | | 2 | 3 |
| 13 | En tant que Dev, je souhaite écrire une nomenclature du code. | | 1 | 3 |
| 14 | En tant que Dev, je souhaite écrire une nomenclature de la documentation. | | 1 | 3 |
| 15 | En tant que Dev, je souhaite ajouter de la documentation concernant l'environnement du projet afin de permettre à d'autres développeurs de travailler dessus facilement. | | 1 | 3 |
| 16 | En tant que Dev, je souhaite ajouter une release à la liste de celles-ci afin de garder une trace de mes progrès. | | 2 | 3 |

# Annexes
Les éléments optionnels sur les différentes notions sont en italic.

### Compte :
* Nom
* Mot de passe
* *Projets (nul à la création)*

### Projet :
* Backlog
* Sprints
* Tests
* Nomenclature Code
* Nomenclature Documentation
* *Documentation sur l'environnement*
* Releases

### Issue :
* Id
* Description
* Priorité
* Difficulté
* *Dépendances*

### Backlog :
* Liste d'issues

### Sprint :
* Id
* *Date de début (à renseigner lors de la création du premier sprint)*
* *Date de fin*
* Liste de tâches

### Tâche :
* Id
* Nom du composant associé
* Description
* Coût en jour / homme
* Status (A faire, En cours, Fait)

### Test :
* Scénario de test
* Résultat de test

### Scénario d'un test :
* Liste d'actions que l'utilisateur effectue pour vérifier q'une issue est respectée

### Résultat d'un test :
* Id
* Status
* Date
* Version du projet

### Release :
* N° de version
* Date
* Issues implémentées
