"""
    Fichier : gestion_tel_personne_crud.py
    Auteur : OM 2021.05.01
    Gestions des "routes" FLASK et des données pour l'association entre les films et les ingredient.
"""
import sys

import pymysql
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from APP_FILMS import obj_mon_application
from APP_FILMS.database.connect_db_context_manager import MaBaseDeDonnee
from APP_FILMS.erreurs.exceptions import *
from APP_FILMS.erreurs.msg_erreurs import *

"""
    Nom : tel_personne_afficher
    Définition d'une "route" /tel_personne_afficher
    
    But : Afficher les films avec les ingredient associés pour chaque film.
    
    Paramètres : id_genre_sel = 0 >> tous les films.
                 id_genre_sel = "n" affiche le film dont l'id est "n"
                 
"""


@obj_mon_application.route("/tel_personne_afficher/<int:id_telephone>", methods=['GET', 'POST'])
def tel_personne_afficher(id_telephone):
    if request.method == "GET":
        try:
            try:
                # Renvoie une erreur si la connexion est perdue.
                MaBaseDeDonnee().connexion_bd.ping(False)
            except Exception as Exception_init_films_genres_afficher:
                code, msg = Exception_init_films_genres_afficher.args
                flash(f"{error_codes.get(code, msg)} ", "danger")
                flash(f"Exception _init_films_genres_afficher problème de connexion BD : {sys.exc_info()[0]} "
                      f"{Exception_init_films_genres_afficher.args[0]} , "
                      f"{Exception_init_films_genres_afficher}", "danger")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {msg_erreurs.args[0]}")

            with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:

                strsql_ingredient_film_afficher_data = """SELECT id_telephone, num_telephone, GROUP_CONCAT(prenom_pers, " ",nom_pers) as NomPers FROM t_pers_telephone
                                                            RIGHT JOIN t_personne ON t_personne.id_personne = t_pers_telephone.fk_personne
                                                            RIGHT JOIN t_telephone ON t_telephone.id_telephone = t_pers_telephone.fk_telephone
                                                            GROUP BY id_telephone"""
                if id_telephone == 0:
                    # le paramètre 0 permet d'afficher tous les telephones
                    # Sinon le paramètre représente la valeur de l'id du telephone
                    mc_afficher.execute(strsql_ingredient_film_afficher_data)
                else:
                    # Constitution d'un dictionnaire pour associer l'id du telephone sélectionné avec un nom de variable
                    valeur_id_film_selected_dictionnaire = {"value_id_film_selected": id_telephone}
                    # En MySql l'instruction HAVING fonctionne comme un WHERE... mais doit être associée à un GROUP BY
                    # L'opérateur += permet de concaténer une nouvelle valeur à la valeur de gauche préalabﬁement définie.
                    strsql_ingredient_film_afficher_data += """ HAVING id_telephone= %(value_id_film_selected)s"""

                    mc_afficher.execute(strsql_ingredient_film_afficher_data, valeur_id_film_selected_dictionnaire)

                # Récupère les données de la requête.
                data_genres_films_afficher = mc_afficher.fetchall()
                print("data_genres ", data_genres_films_afficher, " Type : ", type(data_genres_films_afficher))

                # Différencier les messages.
                if not data_genres_films_afficher and id_telephone == 0:
                    flash("""La table "t_telephone" est vide. !""", "warning")
                elif not data_genres_films_afficher and id_telephone > 0:
                    # Si l'utilisateur change l'id_film dans l'URL et qu'il ne correspond à aucun film
                    flash(f"Le telephone {id_telephone} demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données téléphone et personnes affichés !!", "success")

        except Exception as Exception_films_genres_afficher:
            code, msg = Exception_films_genres_afficher.args
            flash(f"{error_codes.get(code, msg)} ", "danger")
            flash(f"Exception tel_personnes_afficher : {sys.exc_info()[0]} "
                  f"{Exception_films_genres_afficher.args[0]} , "
                  f"{Exception_films_genres_afficher}", "danger")

    # Envoie la page "HTML" au serveur.
    return render_template("gestion_tel_pers/tel_personne_afficher.html", data=data_genres_films_afficher)


"""
    nom: edit_personne_tel_selected
    On obtient un objet "objet_dumpbd"

    Récupère la liste de tous les ingredient du film sélectionné par le bouton "MODIFIER" de "ustensile_plat_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les ingredient contenus dans la "t_genre".
    2) Les ingredient attribués au téléphone selectionné.
    3) Les ingredient non-attribués au film sélectionné.

    On signale les erreurs importantes

"""


@obj_mon_application.route("/edit_tel_pers_selected", methods=['GET', 'POST'])
def edit_tel_pers_selected():
    if request.method == "GET":
        try:
            with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
                strsql_genres_afficher = """SELECT * FROM t_telephone ORDER BY id_telephone ASC"""
                mc_afficher.execute(strsql_genres_afficher)
            data_genres_all = mc_afficher.fetchall()
            print("dans edit_genre_film_selected ---> data_genres_all", data_genres_all)

            # Récupère la valeur de "id_film" du formulaire html "ustensile_plat_afficher.html"
            # l'utilisateur clique sur le bouton "Modifier" et on récupère la valeur de "id_film"
            # grâce à la variable "id_film_genres_edit_html" dans le fichier "ustensile_plat_afficher.html"
            # href="{{ url_for('edit_genre_film_selected', id_film_genres_edit_html=row.id_film) }}"
            id_film_genres_edit = request.values['id_telephone_edit']

            # Mémorise l'id du mail dans une variable de session
            # (ici la sécurité de l'application n'est pas engagée)
            # il faut éviter de stocker des données sensibles dans des variables de sessions.
            session['session_id_film_genres_edit'] = id_film_genres_edit

            # Constitution d'un dictionnaire pour associer l'id du mail sélectionné avec un nom de variable
            valeur_id_film_selected_dictionnaire = {"value_id_telephone_selected": id_film_genres_edit}

            # Récupère les données grâce à 3 requêtes MySql définie dans la fonction ingredient_film_afficher_data
            # 1) Sélection du film choisi
            # 2) Sélection des ingredient "déjà" attribués pour le film.
            # 3) Sélection des ingredient "pas encore" attribués pour le film choisi.
            # ATTENTION à l'ordre d'assignation des variables retournées par la fonction "ingredient_film_afficher_data"
            data_genre_film_selected, data_genres_films_non_attribues, data_genres_films_attribues = \
                ingredient_film_afficher_data(valeur_id_film_selected_dictionnaire)

            print(data_genre_film_selected)
            lst_data_film_selected = [item['id_telephone'] for item in data_genre_film_selected]
            print("lst_data_film_selected  ", lst_data_film_selected,
                  type(lst_data_film_selected))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les personnes qui ne sont pas encore sélectionnés.
            lst_data_genres_films_non_attribues = [item['id_personne'] for item in data_genres_films_non_attribues]
            session['session_lst_data_genres_films_non_attribues'] = lst_data_genres_films_non_attribues
            print("lst_data_genres_films_non_attribues  ", lst_data_genres_films_non_attribues,
                  type(lst_data_genres_films_non_attribues))

            # Dans le composant "tags-selector-tagselect" on doit connaître
            # les personnes qui sont déjà sélectionnés.
            lst_data_genres_films_old_attribues = [item['id_personne'] for item in data_genres_films_attribues]
            session['session_lst_data_genres_films_old_attribues'] = lst_data_genres_films_old_attribues
            print("lst_data_genres_films_old_attribues  ", lst_data_genres_films_old_attribues,
                  type(lst_data_genres_films_old_attribues))

            print(" data data_genre_film_selected", data_genre_film_selected, "type ", type(data_genre_film_selected))
            print(" data data_genres_films_non_attribues ", data_genres_films_non_attribues, "type ",
                  type(data_genres_films_non_attribues))
            print(" data_genres_films_attribues ", data_genres_films_attribues, "type ",
                  type(data_genres_films_attribues))

            # Extrait les valeurs contenues dans la table "t_personnes", colonne "nom_pers"
            # Le composant javascript "tagify" pour afficher les tags n'a pas besoin de l'id_persnne
            lst_data_genres_films_non_attribues = [item['num_telephone'] for item in data_genres_films_non_attribues]
            print("lst_all_genres gf_edit_genre_film_selected ", lst_data_genres_films_non_attribues,
                  type(lst_data_genres_films_non_attribues))

        except Exception as Exception_edit_genre_film_selected:
            code, msg = Exception_edit_genre_film_selected.args
            flash(f"{error_codes.get(code, msg)} ", "danger")
            flash(f"Exception edit_tel_pers_selected : {sys.exc_info()[0]} "
                  f"{Exception_edit_genre_film_selected.args[0]} , "
                  f"{Exception_edit_genre_film_selected}", "danger")

    return render_template("gestion_tel_pers/tel_personne_modifier_tags_dropbox.html",
                           data_genres=data_genres_all,
                           data_film_selected=data_genre_film_selected,
                           data_genres_attribues=data_genres_films_attribues,
                           data_genres_non_attribues=data_genres_films_non_attribues)


"""
    nom: update_genre_film_selected

    Récupère la liste de tous les ingredient du film sélectionné par le bouton "MODIFIER" de "ustensile_plat_afficher.html"
    
    Dans une liste déroulante particulière (tags-selector-tagselect), on voit :
    1) Tous les ingredient contenus dans la "t_genre".
    2) Les ingredient attribués au film selectionné.
    3) Les ingredient non-attribués au film sélectionné.

    On signale les erreurs importantes
"""


@obj_mon_application.route("/update_tel_personne_selected", methods=['GET', 'POST'])
def update_tel_personne_selected():
    if request.method == "POST":
        try:
            # Récupère l'id du film sélectionné
            id_film_selected = session['session_id_film_genres_edit']
            print("session['session_id_film_genres_edit'] ", session['session_id_film_genres_edit'])

            # Récupère la liste des ingredient qui ne sont pas associés au film sélectionné.
            old_lst_data_genres_films_non_attribues = session['session_lst_data_genres_films_non_attribues']
            print("old_lst_data_genres_films_non_attribues ", old_lst_data_genres_films_non_attribues)

            # Récupère la liste des ingredient qui sont associés au film sélectionné.
            old_lst_data_genres_films_attribues = session['session_lst_data_genres_films_old_attribues']
            print("old_lst_data_genres_films_old_attribues ", old_lst_data_genres_films_attribues)

            # Effacer toutes les variables de session.
            session.clear()

            # Récupère ce que l'utilisateur veut modifier comme ingredient dans le composant "tags-selector-tagselect"
            # dans le fichier "genres_films_modifier_tags_dropbox.html"
            new_lst_str_genres_films = request.form.getlist('name_select_tags')
            print("new_lst_str_genres_films ", new_lst_str_genres_films)

            # OM 2021.05.02 Exemple : Dans "name_select_tags" il y a ['4','65','2']
            # On transforme en une liste de valeurs numériques. [4,65,2]
            new_lst_int_genre_film_old = list(map(int, new_lst_str_genres_films))
            print("new_lst_genre_film ", new_lst_int_genre_film_old, "type new_lst_genre_film ",
                  type(new_lst_int_genre_film_old))

            # Pour apprécier la facilité de la vie en Python... "les ensembles en Python"
            # https://fr.wikibooks.org/wiki/Programmation_Python/Ensembles
            # OM 2021.05.02 Une liste de "id_genre" qui doivent être effacés de la table intermédiaire "t_pers_telephone".
            lst_diff_genres_delete_b = list(
                set(old_lst_data_genres_films_attribues) - set(new_lst_int_genre_film_old))
            print("lst_diff_genres_delete_b ", lst_diff_genres_delete_b)

            # Une liste de "id_genre" qui doivent être ajoutés à la "t_pers_telephone"
            lst_diff_genres_insert_a = list(
                set(new_lst_int_genre_film_old) - set(old_lst_data_genres_films_attribues))
            print("lst_diff_genres_insert_a ", lst_diff_genres_insert_a)

            # SQL pour insérer une nouvelle association entre
            # "fk_telephone"/"id_telephone" et "fk_personne"/"id_personne" dans la "t_pers_telephone"
            strsql_insert_genre_film = """INSERT INTO t_pers_telephone (fk_personne, fk_telephone) VALUES (%(value_fk_personne)s, %(value_fk_telephone)s)"""

            # SQL pour effacer des association(s) existantes entre "id_telephone" et "id_personne" dans la "t_pers_telephone"
            strsql_delete_genre_film = """DELETE FROM t_pers_telephone WHERE fk_personne = %(value_fk_personne)s AND fk_telephone = %(value_fk_telephone)s"""

            with MaBaseDeDonnee() as mconn_bd:
                # Pour le mail sélectionné, parcourir la liste des ingredient à INSÉRER dans la "t_pers_telephone".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_genre_ins in lst_diff_genres_insert_a:
                    # Constitution d'un dictionnaire pour associer l'id du telephone sélectionné avec un nom de variable
                    # et "id_personne_ins" (l'id du genre dans la liste) associé à une variable.
                    valeurs_film_sel_genre_sel_dictionnaire = {"value_fk_telephone": id_film_selected,
                                                               "value_fk_personne": id_genre_ins}

                    mconn_bd.mabd_execute(strsql_insert_genre_film, valeurs_film_sel_genre_sel_dictionnaire)

                # Pour le telephone sélectionné, parcourir la liste des personnes à EFFACER dans la "t_pers_telephone".
                # Si la liste est vide, la boucle n'est pas parcourue.
                for id_genre_del in lst_diff_genres_delete_b:
                    # Constitution d'un dictionnaire pour associer l'id du mail sélectionné avec un nom de variable
                    # et "id_personne_del" (l'id du personne dans la liste) associé à une variable.
                    valeurs_film_sel_genre_sel_dictionnaire = {"value_fk_telephone": id_film_selected,
                                                               "value_fk_personne": id_genre_del}

                    # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
                    # la subtilité consiste à avoir une méthode "mabd_execute" dans la classe "MaBaseDeDonnee"
                    # ainsi quand elle aura terminé l'insertion des données le destructeur de la classe "MaBaseDeDonnee"
                    # sera interprété, ainsi on fera automatiquement un commit
                    mconn_bd.mabd_execute(strsql_delete_genre_film, valeurs_film_sel_genre_sel_dictionnaire)

        except Exception as Exception_update_genre_film_selected:
            code, msg = Exception_update_genre_film_selected.args
            flash(f"{error_codes.get(code, msg)} ", "danger")
            flash(f"Exception update_personne_tel_selected : {sys.exc_info()[0]} "
                  f"{Exception_update_genre_film_selected.args[0]} , "
                  f"{Exception_update_genre_film_selected}", "danger")

    # Après cette mise à jour de la table intermédiaire "t_genre_film",
    # on affiche les films et le(urs) genre(s) associé(s).
    return redirect(url_for('tel_personne_afficher', id_telephone=id_film_selected))


"""
    nom: personne_tel_afficher_data

    Récupère la liste de tous les tele du film sélectionné par le bouton "MODIFIER" de "personne_tel_afficher.html"
    Nécessaire pour afficher tous les "TAGS" des personnes, ainsi l'utilisateur voit les personnes à disposition
    
    On signale les erreurs importantes
"""


def ingredient_film_afficher_data(valeur_id_film_selected_dict):
    print("valeur_id_film_selected_dict...", valeur_id_film_selected_dict)
    try:

        strsql_film_selected = """SELECT id_telephone, num_telephone FROM t_telephone WHERE id_telephone = %(value_id_telephone_selected)s"""

        strsql_genres_films_non_attribues = """SELECT id_personne, prenom_pers, nom_pers FROM t_personne 
                                                    WHERE id_personne not in(SELECT id_personne as idPersonneTel FROM t_pers_telephone
                                                    INNER JOIN t_personne ON t_personne.id_personne = t_pers_telephone.fk_personne
                                                    INNER JOIN t_telephone ON t_telephone.id_telephone = t_pers_telephone.fk_telephone
                                                    WHERE id_telephone = %(value_id_telephone_selected)s)"""

        strsql_genres_films_attribues = """SELECT id_personne, nom_pers, prenom_pers FROM t_pers_telephone
                                            INNER JOIN t_personne ON t_personne.id_personne = t_pers_telephone.fk_personne
                                            INNER JOIN t_telephone ON t_telephone.id_telephone = t_pers_telephone.fk_telephone
                                            WHERE id_telephone = %(value_id_telephone_selected)s"""

        # Du fait de l'utilisation des "context managers" on accède au curseur grâce au "with".
        with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
            # Envoi de la commande MySql
            mc_afficher.execute(strsql_genres_films_non_attribues, valeur_id_film_selected_dict)
            # Récupère les données de la requête.
            data_genres_films_non_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("ingredient_film_afficher_data ----> data_genres_films_non_attribues ",
                  data_genres_films_non_attribues,
                  " Type : ",
                  type(data_genres_films_non_attribues))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_film_selected, valeur_id_film_selected_dict)
            # Récupère les données de la requête.
            data_film_selected = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_film_selected  ", data_film_selected, " Type : ", type(data_film_selected))

            # Envoi de la commande MySql
            mc_afficher.execute(strsql_genres_films_attribues, valeur_id_film_selected_dict)
            # Récupère les données de la requête.
            data_genres_films_attribues = mc_afficher.fetchall()
            # Affichage dans la console
            print("data_genres_films_attribues ", data_genres_films_attribues, " Type : ",
                  type(data_genres_films_attribues))

            # Retourne les données des "SELECT"
            return data_film_selected, data_genres_films_non_attribues, data_genres_films_attribues
    except pymysql.Error as pymysql_erreur:
        code, msg = pymysql_erreur.args
        flash(f"{error_codes.get(code, msg)} ", "danger")
        flash(f"pymysql.Error Erreur dans ingredient_film_afficher_data : {sys.exc_info()[0]} "
              f"{pymysql_erreur.args[0]} , "
              f"{pymysql_erreur}", "danger")
    except Exception as exception_erreur:
        code, msg = exception_erreur.args
        flash(f"{error_codes.get(code, msg)} ", "danger")
        flash(f"Exception Erreur dans ingredient_film_afficher_data : {sys.exc_info()[0]} "
              f"{exception_erreur.args[0]} , "
              f"{exception_erreur}", "danger")
    except pymysql.err.IntegrityError as IntegrityError_ingredient_film_afficher_data:
        code, msg = IntegrityError_ingredient_film_afficher_data.args
        flash(f"{error_codes.get(code, msg)} ", "danger")
        flash(f"pymysql.err.IntegrityError Erreur dans ingredient_film_afficher_data : {sys.exc_info()[0]} "
              f"{IntegrityError_ingredient_film_afficher_data.args[0]} , "
              f"{IntegrityError_ingredient_film_afficher_data}", "danger")
