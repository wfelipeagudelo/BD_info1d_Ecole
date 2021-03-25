Module 104 "Hurlements en Python et FLASK"
---

mes couilles qui sont belles

## Remarque :
* En classe j'ai montré comment faire le fichier ".env" avec les variables d'environnement. Ce fichier dans les projets en production ne doit pas se trouver dans le cloud (Gitlab).
* Pour ce début de projet et pour me simplifier la correction des 80 projets. Je l'ai laissé dans le git, ainsi vous n'avez rien à faire de particulier, pour que la démo fonctionne.
  * Avec votre version de votre projet vous serez obligé de le modifier. (Nom de la BD par exemple)



## Travail de l’élève (avant de faire RUN du "1_run_server_flask.py")
* Dans PyCharm ouvrir le répertoire "zzzdemos", puis ouvrir le fichier "1_ImportationDumpSql.py".  
  Ensuite, avec le bouton de droite de la souris cliquer sur "run" de ce fichier "1_ImportationDumpSql.py".
  * En cas d'erreurs : ouvrir le fichier ".env" à la racine du projet, contrôler les indications de connexion pour la bd.
* Puis dans le répertoire racine du projet, ouvrir le fichier "1_run_server_flask.py" et faire un "run".

### Constater l'affichage du contenu de la table "t_genre"

* Démarrer le serveur MySql (uwamp ou xamp ou mamp, etc)
* Récupérer le projet stocké sur Gitlab avec l’IDE PyCharm.
  * Explications sur le MOODLE de l’EPSIC (Module 104).


### Pour cette démo

* Il y a un template CSS, stocké en local dans un répertoire (static) IMPOSE par FLASK.
* On réalise UNIQUEMENT (choix de OM de la 707) l'action READ du CRUD (Create Read Update Delete) sur la table "t_genre".
* Il faut tester le système de gestion des erreurs selon la liste du premier exercice.

### VOTRE travail pour cet exercice :

* Placer votre fichier DUMP au bon endroit comme pour le premier exercice.
  * N'oubliez pas les 3 commandes DROP;CREATE;USE
* Dans le fichier ".env" changez le nom de la BD par le nom de votre BD (NAME_BD_MYSQL="_____NOM_DE_VOTRE_BD")
* L'importer grâce au fichier zzzdemos/1_ImportationDumpSql.py
* Adapter les changements pour qu'UNE seule table de votre projet s'affiche.
* Niveau sup. : Adapter les changements pour que toutes les tables principales de votre projet s'affichent (pas les tables intermédiaires)

### Votre projet sur Gitlab
* Quel que soit l'état de votre exercice. Vous devez le mettre à ma disposition sur Gitlab comme le premier exercice.
* Faites peu de choses, mais il faut les faire.
* Il faut maîtriser un petit peu le "PUSH" sur git
* Faites des essais, lisez le petit tuto sur votre DISCORD
* Un truc simple : avant d’ouvrir PyCharm
  * Effacer le répertoire ".git" et ".idea" de votre projet.
  * Sur le site Gitlab faites un "NEW PROJECT", il vous montre toutes les commandes indispensables, copiez-les dans le bloc-note.
  * Ouvrir le terminal de PyCharm envoyez les commandes générées par Gitlab.
* S’il y a des problèmes techniques, nous en parlons la prochaine fois.

### Nous sommes en avance en comparaison de l'année précédente, donc pas de panique.

## Quelques liens utiles pour les ... (mot étrange !)
https://www.armandphilippot.com/dotenv-variables-environnement/
https://stackoverflow.com/questions/23554872/why-does-pycharm-propose-to-change-method-to-static
