"""
    Fichier : database_tools.py
    Auteur : OM 2021.03.03
    Connection à la base de données.
    Nécessite un fichier de configuration externe : Config_App.yml
    Nécessite un fichier DUMP en MySql de la BD : /database/NOM_PRENOM_INFO1X_SUJET_104_2021.sql
"""
import os
import re
import pymysql
from pymysql.constants import CLIENT
import yaml
import sqlparse
from erreurs.exceptions import *


class Toolsbd:
    """
        Auteur : OM 2021.03.03
        Nom classe : Toolsbd
        Classe pour définir quelques outils en rapport avec la base de données.
    """

    def __init__(self):
        """
            Quand on instancie la classe "Toolsbd()" il interprète le code __init__
            Les paramètres sont définis dans le fichier de configuration "Config_App.yml"
        """

        self.name_fichier_dump_sql_bd = "../database/NOM_PRENOM_INFO1X_SUJET_104_2021.sql"
        self.name_fichier_config_application = "../Config_App.yml"
        self.connexion_bd = None

    def extract_name_bd_from_dump_file(self):
        """
            Auteur : OM 2021.03.09
            Nom : extract_name_bd_from_dump_file(self)
            But : Extrait la chaîne de caractère du nom de la base de donnée contenu dans le fichier :
                    "NOM_PRENOM_INFO1X_SUJET_104_2021.sql"
                    à la ligne de commande "USE NOM_PRENOM_INFO1X_SUJET_104_2021;"
        """
        try:

            if os.path.exists(self.name_fichier_dump_sql_bd):
                fichier_dump_sql_bd = open(self.name_fichier_dump_sql_bd, "r", encoding="utf8")
                lignes_fichier_dump = fichier_dump_sql_bd.read()
                extract_nom_bd = re.search(r'USE(.*?);', lignes_fichier_dump).group(1)

                # Extrait le nom de la BD après suppression des espaces autour de la chaîne de caractères.
                extract_nom_bd = extract_nom_bd.strip()
                print("extract_nom_bd ", extract_nom_bd)
                fichier_dump_sql_bd.close()
            else:
                print(f"Le fichier DUMP n'existe pas !!!")
        except Exception as ErreurExtractNameBD:
            raise ErreurExtractNameBD("Problème avec l'extraction du nom de la BD")

        return extract_nom_bd

    def test_load_config_file(self):
        """
            Auteur : OM 2021.03.09
            Nom : test_load_config_file(self)
            Avertit des problèmes éventuels sur le fichier "Config_App.yml"
            Son emplacement, son nom et son ouverture.
        """
        try:
            if os.path.exists(self.name_fichier_config_application):
                fichier_cfg = open(self.name_fichier_config_application, "r")
                config = yaml.load(fichier_cfg, Loader=yaml.FullLoader)

                host = config["database"]["host"]
                user = config["database"]["user"]
                password = config["database"]["password"]

                fichier_cfg.close()
            else:
                raise ErreurFichierConfig(f"Erreur fichier de config. Config_App.yml (nom, emplacement, etc)")

        except IOError as erreur_fichier_cfg:
            print(f"Erreur fichier de config. Config_App.yml (nom, répertoire, chemin)  "
                  f"{erreur_fichier_cfg.args[0]}, "
                  f"{erreur_fichier_cfg}")
            raise
        except KeyError as erreur_config_key:
            print(f"Erreur dans le fichier config. (host, password, user, mabd)  "
                  f"{erreur_config_key.args[0]}, "
                  f"{erreur_config_key}")
            raise
        except Exception as erreur_particuliere:
            print(f"Erreur particulière __init__ Toolsbd : "
                  f"{erreur_particuliere.args[0]}, "
                  f"{erreur_particuliere}")
            raise
        else:
            print("Variables initialisation OK !")

        return host, user, password

    def test_cmd_CRD_file_dump_sql(self):
        """
            Auteur : OM 2021.03.09
            Nom : test_cmd_CRD_file_dump_sql(self)
            Tester si il y a des problèmes éventuels sur le fichier : "NOM_PRENOM_INFO1X_SUJET_104_2021.sql"
            Son emplacement, son nom, son ouverture et s'il contient les commandes MySql suivantes :
            DROP DATABASE IF EXIST nom_bd; CREATE DATABASE IF NOT EXISTS nom_bd; USE nom_bd;
            (Commandes obligatoires pour le MODULE 104, afin de garantir la dernière version de la BD)
        """
        try:
            if os.path.exists(self.name_fichier_dump_sql_bd):
                fichier_dump_sql_bd = open(self.name_fichier_dump_sql_bd, "r", encoding="utf8")
                lignes_fichier_dump = fichier_dump_sql_bd.read()
                """
                    Si le fichier DUMP en SQL "../database/NOM_PRENOM_INFO1X_SUJET_104_2021.sql" existe, 
                    on l'ouvre et il est "découpé" dans une LISTE ligne par ligne.
                    Dans une boucle FOR chaque élément de l liste (ligne du fichier) est "executée" sur le Serveur MySql
                    On valide la transaction par un "commit".
                    On ferme ce qui est ouvert (fichier, curseur de la BD, connection à la BD)
                """

                lignes_fichier_sql = sqlparse.split(lignes_fichier_dump)
                print(" lignes_sql ", lignes_fichier_sql, "....", type(lignes_fichier_sql))

                sql_cmd_drop_bd = lignes_fichier_dump.find("DROP DATABASE IF EXIST")
                sql_cmd_create_bd = lignes_fichier_dump.find("CREATE DATABASE IF NOT EXISTS")
                sql_cmd_use_bd = lignes_fichier_dump.find("USE")

                """
                    Pour CE projet et uniquement dans des projets (d'école) ou l'on doit reconstruire la BD.
                    Ne jamais oublier qu'il faut les 3 instructions dans le fichier DUMP en SQL
                    DROP DATABASE IF EXIST nom_bd; CREATE DATABASE IF NOT EXISTS nom_bd; USE nom_bd;
                """
                if sql_cmd_drop_bd == -1:
                    raise ErreurFichierSqlDump("Fichier DUMP : Il manque une commande \"DROP DATABASE IF EXIST\"")
                elif sql_cmd_create_bd == -1:
                    raise ErreurFichierSqlDump(
                        "Fichier DUMP : Il manque une commande \"CREATE DATABASE IF NOT EXISTS\"")
                elif sql_cmd_use_bd == -1:
                    raise ErreurFichierSqlDump("Fichier DUMP : Il manque une commande \"USE\"")
                else:
                    fichier_dump_sql_bd.close()
                    print(f"Les instructions DROP; CREATE ; USE sont ok dans le fichier DUMP en SQL")
            else:
                print(f"Problème avec le Fichier DUMP SQL")

        except Exception as erreur_fichier_sql_dump:
            print(f"Mauvais paramètres dans (Config_App.yml) "
                  f"{erreur_fichier_sql_dump.args[0]}, "
                  f"{erreur_fichier_sql_dump}")
            raise ErreurFichierSqlDump("Problème avec le Fichier DUMP SQL !!! (nom, emplacement, etc)")

        return lignes_fichier_sql

    def load_dump_sql_bd_init(self):
        """
            Auteur : OM 2021.03.09
            Nom : load_dump_sql_bd_init(self)
            Méthode pour charger le fichier DUMP en SQL dans le serveur MySql.

            autocommit=False ==> Oblige le programmeur à ordonner la confirmation (commit) de la transaction dans la BD.

            1) Récupérer les paramètres de la configuration dans le fichier "Config_App.yml"
            2) Se connecter à la BD
            3) Tester si les instructions MySql
                DROP DATABASE IF EXIST nom_bd; CREATE DATABASE IF NOT EXISTS nom_bd; USE nom_bd;
            4) Parcourir les lignes du fichier DUMP en MySql et les exécuter dans le serveur MySql.
        """
        try:
            try:
                host_mabd, user_mabd, password_mabd = self.test_load_config_file()
                conn_bd_dump = pymysql.connect(
                    host=host_mabd,
                    user=user_mabd,
                    password=password_mabd,
                    autocommit=False)

                lignes_fichier_sql = self.test_cmd_CRD_file_dump_sql()

                if lignes_fichier_sql:
                    for ligne in lignes_fichier_sql:
                        nb_row_sql = conn_bd_dump.cursor().execute(ligne)
                        print("lignes sql executées  ", nb_row_sql)
                    conn_bd_dump.commit()
                else:
                    raise ErreurFichierSqlDump("Fichier DUMP SQL vide, C'EST étrange !!!")

            except AttributeError as erreur_attr:
                print(f"Mauvais paramètres dans (Config_App.yml) "
                      f"{erreur_attr.args[0]}, "
                      f"{erreur_attr}")
                raise
            except pymysql.OperationalError as erreur_connection:
                print(f"Erreur de configu. dans la connection de la BD "
                      f"{erreur_connection.args[0]}, "
                      f"{erreur_connection}")
                raise
            except Exception as erreur_load_dump:
                print(f"Erreur particulière load_dump_sql_bd_init "
                      f"{erreur_load_dump.args[0]}, "
                      f"{erreur_load_dump}")
                raise
            else:
                conn_bd_dump.close()
                print("Fichier DUMP SQL chargé dans le serveur MySql")
        except (Exception,
                ConnectionRefusedError,
                AttributeError,
                pymysql.err.OperationalError,
                pymysql.err.DatabaseError) as erreur_load_dump_file:
            print(f"Erreur particulière load_dump_sql_bd_init "
                  f"{erreur_load_dump_file.args[0]}, "
                  f"{erreur_load_dump_file}")
            raise ErreurFichierSqlDump("Problème avec le Fichier DUMP SQL !!!")

    def connect_database(self):
        """
            Auteur : OM 2021.03.09
            Nom : connect_database(self)
            Se connecter à la BD avec les paramètres de connection suivants :
                1) Dans le fichier : Config_App.yml
                2) Extrait la chaîne de caractère du nom de la base de donnée dans le fichier :
                    "NOM_PRENOM_INFO1X_SUJET_104_2021.sql"
                    dans la commande "USE NOM_PRENOM_INFO1X_SUJET_104_2021;"

            client_flag=CLIENT.MULTI_STATEMENTS ==> Indispensable pour pouvoir passer plusieurs
            requêtes en une seule fois.

            autocommit=False ==> Oblige le programmeur à ordonner la confirmation (commit) de la transaction dans la BD.

            cursorclass=pymysql.cursors.DictCursor ==> Retourne les données de la BD sous la forme d'un DICTIONNAIRE

            1) Récupérer le nom de la BD dans le fichier DUMP en MySql "NOM_PRENOM_INFO1X_SUJET_104_2021.sql"
            2) Récupérer les paramètres de la configuration dans le fichier "Config_App.yml"
            3) Se connecter à la BD
        """
        try:
            nom_ma_bd = self.extract_name_bd_from_dump_file()
            host_mabd, user_mabd, password_mabd = self.test_load_config_file()

            self.connexion_bd = pymysql.connect(
                host=host_mabd,
                user=user_mabd,
                password=password_mabd,
                database=nom_ma_bd,
                client_flag=CLIENT.MULTI_STATEMENTS,
                autocommit=False,
                cursorclass=pymysql.cursors.DictCursor)

        except (Exception,
                ConnectionRefusedError,
                pymysql.err.OperationalError,
                pymysql.err.DatabaseError) as erreur_connect_database:

            print(f"Erreur particulière connect_database "
                  f"{erreur_connect_database.args[0]}, "
                  f"{erreur_connect_database}")
            raise ErreurConnectionBD("Problème avec la méthode connect_database !!!")

        return self.connexion_bd
