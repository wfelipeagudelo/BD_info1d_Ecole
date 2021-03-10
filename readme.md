Module 104 "Premiers CRI"s" en Python"
---


## Travail de l’élève
### Constater le fonctionnement du projet de OM de la 707. (Films)

* Se connecter au MOODLE de l’EPSIC, afin de lire les consignes.
* Démarrer le serveur MySql (uwamp ou xamp ou mamp, etc)
* Récupérer le projet stocké sur Gitlab avec l’IDE PyCharm.
  * Explications sur le MOODLE de l’EPSIC (Module 104).

* Dans PyCharm ouvrir le répertoire "zzzdemos", puis ouvrir le fichier "1_ImportationDumpSql.py".  
  Ensuite avec le bouton de droite de la souris cliquer sur "run" de ce fichier "1_ImportationDumpSql.py".
  * En cas d'erreurs : ouvrir le fichier à la racine du projet (Config_App.yml), contrôler les indications de connexion pour la bd.   


### Constater le fonctionnement de l'affichage des erreurs

* Pour comprendre comment traiter les erreurs... il faut les provoquer..
* Tenter de filtrer et de "lever" (to raise), les erreurs les plus évidentes lors de l’utilisation du projet.  
  Il doit y avoir un affichage d’erreurs (personnalisé) dans les cas suivants :
1. Pas de serveur MySql.
    - Uwamp n’est pas démarré
2. Fichier de configuration (Config_App.yml)
    - Faux nom.
    - Faux répertoire.
    - Absent.
3. Fichier DUMP (NOM_PRENOM_INFO1X_SUJET_104_2021.sql)
    - Faux nom.
    - Faux répertoire.
    - Absent.
    - Fichier vide.
    - Supprimer la commande  
      DROP DATABASE IF EXISTS NOM_PRENOM_INFO1X_SUJET_104_2021;
    - Supprimer la commande  
      CREATE DATABASE IF NOT EXISTS NOM_PRENOM_INFO1X_SUJET_104_2021;
    - Supprimer la commande  
      USE NOM_PRENOM_INFO1X_SUJET_104_2021;
    - Dans le fichier DUMP en SQL "créer" des erreurs MySql, effacer des caractères de n’importe quelle commande SQL
    
### Projet de l'élève

* Changer le nom du projet en respectant la norme NOM_PRENOM... etc.
* Remplacer le fichier DUMP par votre fichier exporté en SQL depuis PhpMyAdmin.
* Changer la variable du nom du fichier DUMP.
* Tenter de faire un "RUN" du fichier "zzzdemos/1_ImportationDumpSql.py"
    * Si au premier "run" vous n'avez pas d'erreurs.... il s'agit de la chance du débutant, rassurez-vous cela ne vas pas durer !!!
* Ouvrir le fichier "zzzdemos/2_ConnectionBd.py"..., faire un premier "RUN"... pour voir qu’il y a des erreurs...ah enfin !!!
    * Il faut remplacer MA requête par la vôtre !!! Il faut une requête sur une de vos tables.
    * Pour construire VOTRE requête à "COLLER" entre les guillemets, il faut utiliser PhpMyAdmin.
  

* Ecrire la documentation des fichiers Python avec des "docstrings"
    * Les "docstrings" sont les textes entre 3 guillemets (en vert dans PyCharm), chaque élève doit décrire les actions et les paramètres de leur projet personnel.

* Toute la documentation "extérieure" aux fichiers en Python, doit soit trouver dans le fichier "readme.md" (Format Markdown https://www.markdownguide.org/basic-syntax/).


### Ce que l'élève doit envoyer.
* Un fichier texte (respect des normes pour le nom du fichier) sur le MOODLE de l'EPSIC. Dans ce fichier il doit y avoir le lien où est stocké son projet (Gitlab ou Github) 