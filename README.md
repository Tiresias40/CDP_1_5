# Backlog

Application Web-UI avec base de données (SQL). Html-CSS-javascript (Bootstrap). Serveur python (Flask).

Le backlog couvre 2 rôles : Développeur (Dev) & Visiteur (V)

| Id | Description | Priorité | Difficulté | Sprint |
| --- | --- | --- | --- | --- |
| 1 | En tant que V, je souhaite créer un compte sur l'outil afin de participer à des projets. | Moyenne | 2 | 1 |
| 2 | En tant que V, je souhaite me connecter / déconnecter en tant que Dev afin d'accéder à l'outil. | Moyenne | 2 | 1 |
| 3 | En tant que Dev, je souhaite créer un nouveau projet sur l'outil. | Haute | 1 | 2 |
| 4 | En tant que Dev, je souhaite ajouter / supprimer un nouveau Dev au projet. | Moyenne | 1 | 2 |
| 5 | En tant que Dev, je souhaite ajouter / modifier / supprimer une US au backlog du projet correspondant. | Haute | 1 | 2 |
| 6 | En tant que Dev, je souhaite ajouter / supprimer un sprint à un projet. | Haute | 1 | 3 |
| 7 | En tant que Dev, je souhaite ajouter / modifier / supprimer une tâche dans un sprint. | Haute | 1 | 3 |
| 8 | En tant que Dev, je souhaite générer le tableau d'estimation du coût en jour/homme des tâches afin d'organiser mon projet. | Basse | 1 | 3 |
| 9 | En tant que Dev, je souhaite construire / modifier un planning afin d'assigner les tâches aux développeurs. | Basse | 3 | 3 |
| 10 | En tant que Dev, je souhaite accéder à un tableau affichant les status des tâches séparées en trois colonnes (TODO, DOING, DONE). | Basse | 2 | 3 |
| 11 | En tant que Dev, je souhaite accéder au Burn Down Chart afin de visualiser le travail restant. | Basse | 3 | 3 |
| 12 | En tant que Dev, je souhaite écrire des scénarios de tests. | Basse | 1 | 3 |
| 13 | En tant que Dev, je souhaite consulter les scénarios de tests afin de les implémenter. | Basse | 1 | 3 |
| 14 | En tant que Dev, je souhaite ajouter les résultats d'un test associé à un scénario afin de garder une trace de ce résultat. | Basse | 2 | 3 |
| 15 | En tant que Dev, je souhaite écrire une nomenclature du code. | Basse | 1 | 3 |
| 16 | En tant que Dev, je souhaite ajouter de la documentation concernant l'environnement du projet afin de permettre à d'autres développeurs de travailler dessus facilement. | Basse | 1 | 3 |
| 17 | En tant que Dev, je souhaite ajouter une release à la liste de celles-ci afin de garder une trace de mes progrès. | Basse | 2 | 3 |

# Annexes
Les éléments optionnels sont en italique.

### Compte :
* Nom
* Mot de passe
* *Projets (nul à la création)*

### Projet :
* Backlog
* Sprints
* *Tests*
* *Nomenclature Code*
* *Nomenclature Documentation*
* *Documentation sur l'environnement*
* *Releases*

### User Story (US) :
* Id
* Description
* Priorité
* Difficulté
* *Dépendances*

### Backlog :
* Liste d'US

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
* Status (TODO, DOING, DONE)

### Test :
* Scénario de test
* Résultat de test

### Scénario d'un test :
* Liste d'actions que l'utilisateur effectue pour vérifier q'une US est respectée

### Résultat d'un test :
* Id
* Status
* Date
* Version du projet

### Release :
* N° de version
* Date
* US implémentées


# Lancement du projet :
Exécuter l'image docker de la première release sur sa machine
```
docker run -p 5000:5000 leduclouis/cdp1.5:0.2
```
Lancer ensuite un navigateur à l'adresse localhost:5000


# Tests :

Les tests Selenium s'exécutent automatiquement grâce à Travis lorsqu'un commit est fait sur le projet.
Ils sont donc effectués sur la dernière version du projet, sont datés et un code couleur nous indique s'ils sont passés ou non.
Concernant les **test unitaires**, il ne semble pas pertinent de les réaliser pour notre projet. 

# Clean Code :

Nous avons contrôlé la qualité de notre code grâce à sonarcloud,
grace à cet outil nous avons pu corriger les différents bugs de notre code et respecter les conventions de nommages.
L'analyse par sonarcloud est disponible à cette adresse
https://sonarcloud.io/dashboard?id=Tiresias40_CDP_1_5
