"""Calculs de prix d'une petite boutique (dépôt d'exercice de la formation /ship)."""

TVA_NORMALE = 0.20


def appliquer_remise(prix_ht: float, pourcentage: float) -> float:
    """Retourne le prix HT après une remise exprimée en pourcentage (0 à 100)."""
    if not 0 <= pourcentage <= 100:
        raise ValueError("la remise doit être comprise entre 0 et 100")
    return round(prix_ht * (1 - pourcentage / 100), 2)


def prix_ttc(prix_ht: float, taux: float = TVA_NORMALE) -> float:
    """Retourne le prix TTC arrondi au centime."""
    if prix_ht < 0:
        raise ValueError("le prix HT ne peut pas être négatif")
    return round(prix_ht * (1 + taux), 2)
