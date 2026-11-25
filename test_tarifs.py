import pytest

from tarifs import appliquer_remise, prix_ttc


def test_remise_simple():
    assert appliquer_remise(100, 15) == 85.0


def test_remise_nulle_et_totale():
    assert appliquer_remise(80, 0) == 80.0
    assert appliquer_remise(80, 100) == 0.0


def test_remise_hors_bornes():
    with pytest.raises(ValueError):
        appliquer_remise(100, 120)


def test_prix_ttc():
    assert prix_ttc(100) == 120.0
    assert prix_ttc(10, 0.055) == 10.55


def test_prix_ttc_negatif():
    with pytest.raises(ValueError):
        prix_ttc(-1)
