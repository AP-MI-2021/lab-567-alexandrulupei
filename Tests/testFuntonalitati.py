from Domain.vanzarecarte import getId, getTitlu, getPret, getTipreducere, getGen, creeazaVanzare
from Logic.CRUD import adaugareVanzare, getById
from Logic.functionalitati import discount, getmodificaredupatitlu


def test_aplicarediscount():
    lista = []
    lista = adaugareVanzare("1", "Moarte pe nil", "politist", 100, "gold", lista)
    lista = adaugareVanzare("2", "Criminalul ABC", "politist", 1000, "silver", lista)

    lista = discount(lista)

    assert getPret(getById("1", lista)) == 90
    assert getPret(getById("2", lista)) == 950
