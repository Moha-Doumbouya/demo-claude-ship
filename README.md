# Dépôt d'exercice · formation /ship

Petit projet Python (calcul de prix) qui sert de terrain aux cas pratiques.

## Mise en place (une fois, avant la formation)

1. Créez un dépôt **privé** sur github.com (pas un fork, pas un dépôt public : `/ship` ne commite pas vos changements dans un dépôt public).
2. Copiez-y ces fichiers, y compris `.github/workflows/tests.yml`, et poussez-les sur `main`.
3. Vérifiez que l'onglet Actions affiche une exécution verte de `tests`.
4. Clonez-le sur votre poste (macOS, Linux ou WSL : sur Windows natif, aucune watch ne démarre).

## Lancer les tests

```
pip install pytest
pytest -q
```

## Préparer un cas pratique

```
python preparer_cas.py cp3    # changement à faire relire (CP3)
python preparer_cas.py cp4    # fichiers à ne pas embarquer (CP4, CP5)
python preparer_cas.py cp6    # test qui échoue en CI (CP6)
```

Le script ne commite et ne pousse rien. Retour à l'état propre : `git checkout -- .` puis supprimez `.env` et `notes_perso.txt` s'ils existent.
