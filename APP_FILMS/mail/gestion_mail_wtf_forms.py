"""
    Fichier : gestion_mail_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Length
from wtforms.validators import Regexp


class FormWTFAjouterMails(FlaskForm):
    """
        Dans le formulaire "mail_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_mail_regexp = "^[^@]+@[^@]+\.[^@]+"
    nom_genre_wtf = StringField("Entrer le mail ", validators=[Length(min=2, max=255, message="min 2 max 20"),
                                                                   Regexp(nom_mail_regexp,
                                                                          message="Vous devez écrire le mail avec cette forme: utilisateur@domaine.com, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    submit = SubmitField("Enregistrer la personne")


class FormWTFUpdateMail(FlaskForm):
    """
        Dans le formulaire "mail_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_mail_update_regexp = "^[^@]+@[^@]+\.[^@]+"
    nom_genre_update_wtf = StringField("Entrer le mail ", validators=[Length(min=2, max=255, message="min 2 max 20"),
                                                                          Regexp(nom_mail_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    submit = SubmitField("Update mail")


class FormWTFDeleteMail(FlaskForm):
    """
        Dans le formulaire "mail_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_genre_delete_wtf = StringField("Effacer le mail")
    submit_btn_del = SubmitField("Effacer Mail")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
