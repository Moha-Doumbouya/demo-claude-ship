"""Prépare l'état de départ d'un cas pratique dans votre clone du dépôt d'exercice.

Usage : python preparer_cas.py cp3 | cp4 | cp6

Le script modifie des fichiers de travail, il ne commite et ne pousse rien.
Pour revenir à l'état propre : git checkout -- . puis supprimez les fichiers créés.
"""
import pathlib
import sys

ICI = pathlib.Path(__file__).parent

# CP3 : un changement qui contient deux défauts à faire trouver par /code-review.
#  - la remise cumulée applique les remises au prix d'origine au lieu de les enchaîner ;
#  - aucune vérification que la liste n'est pas vide de sens (remise > 100 au cumul).
CP1 = '''

def appliquer_remises(prix_ht: float, pourcentages: list[float]) -> float:
    """Applique plusieurs remises successives (ex. : 10 % puis 5 %)."""
    total = 0.0
    for p in pourcentages:
        total += prix_ht * p / 100
    return round(prix_ht - total, 2)
'''

# CP4 : des fichiers qu'il ne faut pas embarquer dans la pull request.
CP2_FICHIERS = {
    ".env": "API_KEY=valeur-factice-pour-l-exercice\n",
    "notes_perso.txt": "Idées en vrac, à ne pas publier.\n",
}
CP2_CODE = '''

def prix_unitaire(prix_lot: float, quantite: int) -> float:
    """Prix d'une unité dans un lot."""
    if quantite <= 0:
        raise ValueError("la quantité doit être positive")
    return round(prix_lot / quantite, 2)
'''

# CP6 : une nouvelle fonction et son test ; le test échoue (arrondi au mauvais pas),
# la CI du dépôt échoue donc sur la pull request : c'est ce que la watch doit corriger.
CP4_CODE = '''

def arrondir_au_psychologique(prix: float) -> float:
    """Arrondit au prix psychologique supérieur en ,99 (ex. : 12,30 -> 12,99)."""
    return int(prix) + 0.9
'''
CP4_TEST = '''

def test_arrondi_psychologique():
    from tarifs import arrondir_au_psychologique
    assert arrondir_au_psychologique(12.30) == 12.99
    assert arrondir_au_psychologique(7.00) == 7.99
'''


def ajouter(fichier: str, texte: str) -> None:
    chemin = ICI / fichier
    chemin.write_text(chemin.read_text(encoding="utf-8") + texte, encoding="utf-8")


def main() -> None:
    cas = sys.argv[1] if len(sys.argv) > 1 else ""
    if cas == "cp3":
        ajouter("tarifs.py", CP1)
    elif cas == "cp4":
        ajouter("tarifs.py", CP2_CODE)
        for nom, contenu in CP2_FICHIERS.items():
            (ICI / nom).write_text(contenu, encoding="utf-8")
    elif cas == "cp6":
        ajouter("tarifs.py", CP4_CODE)
        ajouter("test_tarifs.py", CP4_TEST)
    else:
        sys.exit("Usage : python preparer_cas.py cp3 | cp4 | cp6")
    print(f"{cas} prêt. Vérifiez avec : git status")


if __name__ == "__main__":
    main()
