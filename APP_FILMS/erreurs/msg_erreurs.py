"""
    Fichier : msg_erreurs.py
    Auteur : OM 2021.03.16
    Erreurs particulières (personnalisées), qui n'existent que dans mon projet à moi.
    Quand il y a une erreur on doit définir des messages "clairs" sur un affichage à destination des "personnes".
    On ne doit pas les laisser devant des erreurs incompréhensibles.
    Dérivation des classes standard des "except" dans les blocs "try...except"
"""

msg_erreurs = {
    "ErreurConnexionBD": {
        "message": "Pas de connexion à la BD ! Il faut démarrer un serveur MySql",
        "status": 400
    },
    "ErreurDoublonValue": {
        "message": "Cette valeur existe déjà.",
        "status": 400
    },
    "ErreurDictionnaire": {
        "message": "(OM du 104) Une valeur du dictionnaire n'existe pas !!!",
        "status": 400
    },
    "ErreurStructureTable": {
        "message": "Il y a un problème dans la structure des tables",
        "status": 400
    },
    "ErreurNomBD": {
        "message": "Problème avec le nom de la base de donnée",
        "status": 400
    },
    "ErreurPyMySql": {
        "message": "Problème en relation avec la BD",
        "status": 400
    },
    "ErreurDeleteContrainte": {
        "message": "Impossible d'effacer, car cette valeur est référencée ailleurs",
        "status": 400
    }
}
