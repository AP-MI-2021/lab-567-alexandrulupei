from Domain.vanzarecarte import getId, getTitlu, getGen, getPret, getTipreducere
from Logic.CRUD import adaugareVanzare, getById, stergeVanzare, modificaVanzare


def test_adaugaVanzare():
    lista = []
    lista = adaugareVanzare("1", "Moarte pe nil", "politist", 50, "gold", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getTitlu(getById("1", lista)) == "Moarte pe nil"
    assert getGen(getById("1", lista)) == "politist"
    assert getPret(getById("1", lista)) == 50
    assert getTipreducere(getById("1", lista)) == "gold"

def test_stergeVanzare():
    lista = []
    lista = adaugareVanzare("1", "Moarte pe nil", "politist", 50, "gold", lista)
    lista = adaugareVanzare("2", "Criminalul ABC", "politist", 1000, "gold", lista)

    lista = stergeVanzare("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    lista = stergeVanzare("3", lista)

    assert len(lista) == 1
    assert getById("2", lista) is not None


def test_modificaVanzare():
    lista = []
    lista = adaugareVanzare("1", "Moarte pe nil", "politist", 50, "gold", lista)
    lista = adaugareVanzare("2", "Criminalul ABC", "politist", 1000, "gold", lista)

    lista = modificaVanzare("1", "Flori", "drama", 500, "silver", lista)

    vanzareModificata = getById("1", lista)
    assert getId(vanzareModificata) == "1"
    assert getTitlu(vanzareModificata) == "Flori"
    assert getGen(vanzareModificata) == "drama"
    assert getPret(vanzareModificata) == 500
    assert getTipreducere(vanzareModificata) == "silver"

    vanzareNemodificata = getById("2", lista)
    assert getId(vanzareNemodificata) == "2"
    assert getTitlu(vanzareNemodificata) == "Criminalul ABC"
    assert getGen(vanzareNemodificata) == "politist"
    assert getPret(vanzareNemodificata) == 1000
    assert getTipreducere(vanzareNemodificata) == "gold"

    lista = []
    lista = adaugareVanzare("1", "Moarte pe nil", "politist", 50, "gold", lista)
    lista = adaugareVanzare("3", "Criminalul ABC", "politist", 1000, "gold", lista)

    lista = modificaVanzare("3", "Flori", "drama", 500, "silver", lista)

    vanzareNemodificata = getById("1", lista)
    assert getId(vanzareNemodificata) == "1"
    assert getTitlu(vanzareNemodificata) == "Moarte pe nil"
    assert getGen(vanzareNemodificata) == "politist"
    assert getPret(vanzareNemodificata) == 50
    assert getTipreducere(vanzareNemodificata) == "gold"