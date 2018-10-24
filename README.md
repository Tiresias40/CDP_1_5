# Backlog

Application Web-UI avec base de données (SQL). Html-CSS-javascript (Bootstrap). Serveur python (Flask). \\[|]/

Le backlog couvre 2 rôles : Chef de projet (CP) & Développeur (Dev)

| Id | Description | Priorité | Difficulté | Dépendances |
| --- | --- | --- | --- | --- |
| 1 | En tant que Dev / CP, je souhaite me connecter / déconnecter afin d'accéder à l'outil. | | | |
| 2 | En tant que CP, je souhaite ajouter / modifier / supprimer une issue afin de gérer le backlog. | | | |
| 3 | En tant que Dev, je souhaite visualiser le backlog afin de connaître les issues de mon projet. | | | |
| 4 | En tant que Dev, je souhaite exporter le backlog afin d'y accéder hors ligne. | | | |
| 5 | En tant que CP, je souhaite ajouter / modifier / supprimer un composant afin de concevoir l'architecture de mon projet. | | | |
| 6 | En tant que Dev, je souhaite visualiser la liste des composants afin de connaître leurs détails. | | | |
| 7 | En tant que Dev, je souhaite exporter la liste des composants afin d'y accéder hors ligne. | | | |
| 8 | En tant que CP, je souhaite créer / modifier le tableau d'estimation du coût en jour/homme des tâches afin d'organiser mon projet. | | | |
| 9 | En tant que CP, je souhaite ajouter une dépendance à une tâche afin de générer automatiquement le graphe de dépendances des tâches. | | | |
| 10 | En tant que CP, je souhaite créer un diagramme de Pert à partir du graphe de dépendances des tâches afin de prévoir les deadlines de mon projet et d'estimer le nombre de développeurs nécessaires. | | | |
| 11 | En tant que CP, je souhaite construire / modifier un planning afin d'assigner les tâches aux développeurs. | | | |
| 12 | En tant que Dev, je souhaite visualiser le planning afin de connaître mes tâches. | | | |
| 13 | En tant que Dev, je souhaite exporter le planning afin d'y accéder hors ligne. | | | |
| 14 | En tant que CP, je souhaite écrire des scénarios de tests afin de vérifier si le projet correspond aux issues. | | | |
| 15 | En tant que Dev, je souhaite consulter les scénarios de tests afin de les implémenter. | | | |
| 16 | En tant que Dev, je souhaite importer le résultat d'un test associé à un scénario afin de garder une trace de ce résultat. | | | |
| 17 | En tant que CP, je souhaite pouvoir suivre les résultats des scénarios de tests afin de savoir s'ils sont passés ou non. | | | |
| 18 | En tant que CP, je souhaite écrire une nomenclature du code afin d'assurer un code propre dans le projet. | | | |
| 19 | En tant que Dev, je souhaite visualiser la nomenclature du code afin de coder selon les normes établies par le CP. | | | |
| 20 | En tant que CP, je souhaite ajouter les résultats d'un linter afin de suivre la propreté du code fichier par fichier. | | | |
| 21 | En tant que Dev, je souhaite accéder aux résultats d'un linter pour un fichier afin de le corriger et le rendre pur. | | | |
| 22 | En tant que CP, je souhaite écrire une nomenclature de la documentation afin d'assurer une documentation propre dans le projet. | | | |
| 23 | En tant que Dev, je souhaite visualiser la nomenclature de la documentation afin de documenter selon les normes établies par le CP. | | | |
| 24 | En tant que CP, je souhaite ajouter de la documentation concernant l'environnement du projet afin de donner toutes les informations nécessaires à mes développeurs. | | | |
| 25 | En tant que Dev, je souhaite visualiser la documentation concernant l'environnement du projet afin de le mener à bien. | | | |
| 26 | En tant que CP, je souhaite ajouter une release à la liste de celles-ci afin de garder une trace de mes progrès. | | | |
| 27 | En tant que Dev, je souhaite visualiser la liste des releases afin de voir l'historique de notre projet. | | | |

# Annexes

### Issue :
* Id
* Description
* Priorité
* Difficulté
* Dépendances

### Backlog :
* Liste d'issues

### Composant :
* Id
* Nom du fichier
* Description
* Dépendances avec les autres composants

### Tâches :
* Définition de l'interface d'un composant
* Réalisation d'un composant
* Ecriture d'un scénario de test d'une issue
* Exécution d'un scénario de test d'une issue

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
* Issues / Tâches implémentées