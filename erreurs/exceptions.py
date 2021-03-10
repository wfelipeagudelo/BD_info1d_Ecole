"""
    Fichier : exceptions.py
    Auteur : OM 2021.03.07
    Classes pour définir des erreurs particulières (personnalisées), qui n'existent que dans mon projet à moi.
    Quand il y a une erreur on doit définir des messages "clairs" sur un affichage à destination des "personnes".
    On ne doit pas les laisser devant des erreurs incompréhensibles.
    Dérivation des classes standard des "except" dans les blocs "try...except"
"""


class ErreurFichierSqlDump(Exception):
    """Erreur qui doit être affichée lorsque le fichier DUMP à un problème"""
    pass


class ErreurFichierConfig(Exception):
    """Erreur qui doit être affichée lorsque le fichier de configuration Config_App.yml à un problème"""
    pass


class ErreurConnectionBD(Exception):
    """Erreur qui doit être affichée lorsque la connection à la bd pose un problème"""
    pass


class ErreurExtractNameBD(Exception):
    """Erreur qui doit être affichée lorsque c'est impossible d'extraire le nom de la BD depuis le fichier DUMP """
    pass
