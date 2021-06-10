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


class FormWTFAjouterTelephone(FlaskForm):
    """
        Dans le formulaire "tel_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_num_regexp = "^(0|0041|\+41)?[1-9\s][0-9\s]{1,12}$"
    nom_num_wtf = StringField("Entrer le numéro ", validators=[Length(min=2, max=21, message="min 2 max 20"),
                                                                   Regexp(nom_num_regexp,
                                                                          message="Vous devez écrire le numéro avec cette forme: 07x xxx xx xx")
                                                                   ])
    submit = SubmitField("Enregistrer le numéro")


class FormWTFUpdateTelephone(FlaskForm):
    """
        Dans le formulaire "tel_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_num_update_regexp = "^(0|0041|\+41)?[1-9\s][0-9\s]{1,12}$"
    nom_genre_update_wtf = StringField("Entrer le numéro ", validators=[Length(min=2, max=10, message="min 2 max 20"),
                                                                          Regexp(nom_num_update_regexp,
                                                                                 message="Vous devez écrire le numéro avec cette forme: 07x xxx xx xx")
                                                                          ])
    submit = SubmitField("Update numéro")


class FormWTFDeleteTelephone(FlaskForm):
    """
        Dans le formulaire "tel_delete_wtf.html"

        nom_genre_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_genre_delete_wtf = StringField("Effacer le numéro")
    submit_btn_del = SubmitField("Effacer numéro")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
