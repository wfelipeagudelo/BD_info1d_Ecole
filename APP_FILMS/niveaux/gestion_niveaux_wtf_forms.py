"""
    Fichier : gestion_niveaux_wtf_forms.py
    Auteur : DeadWay, merci M. Maccaud
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Length
from wtforms.validators import Regexp


class FormWTFAjouterNiveaux(FlaskForm):
    """
        Dans le formulaire "niveaux_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_genre_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_genre_wtf = StringField("Entrer le niveaux", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_genre_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    submit = SubmitField("Enregistrer le niveaux")


class FormWTFUpdateNiveaux(FlaskForm):
    """
        Dans le formulaire "instruments_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_genre_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_genre_update_wtf = StringField("Entrer le niveaux ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(nom_genre_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    submit = SubmitField("Update niveaux")


class FormWTFDeleteNiveaux(FlaskForm):
    """
        Dans le formulaire "niveaux_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "niveaux".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_niveaux".
    """
    nom_genre_delete_wtf = StringField("Effacer le niveaux")
    submit_btn_del = SubmitField("Effacer Niveaux")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
