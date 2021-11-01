from Domain.vanzarecarte import getId, getTitlu, getPret, getTipreducere, getGen, creeazaVanzare
from Logic.CRUD import adaugareVanzare, getById
from Logic.functionalitati import discount, modificaredupatitlu, pretminimgen, ordonaredupapret, titluridistinctedupagen


def test_aplicarediscount():
    lista = []
    lista = adaugareVanzare("1", "Moarte pe nil", "politist", 100, "gold", lista)
    lista = adaugareVanzare("2", "Criminalul ABC", "politist", 1000, "silver", lista)

    lista = discount(lista)

    assert getPret(getById("1", lista)) == 90
    assert getPret(getById("2", lista)) == 950

def test_modificaredupatitlu():
    lista = []
    lista = adaugareVanzare("1", "Moarte pe nil", "politist", 100, "gold", lista)
    lista = adaugareVanzare("2", "ABC", "drama", 1000, "silver", lista)

    lista = modificaredupatitlu("nil", "de ce", lista)

    assert getGen(getById("1", lista)) == "de ce"
    assert getGen(getById("2", lista)) == "drama"


def test_pretminimgen():
    lista = []
    lista = adaugareVanzare("1", "Moarte pe nil", "mare", 150, "gold", lista)
    lista = adaugareVanzare("2", "ABC", "drama", 100, "silver", lista)
    lista = adaugareVanzare("3", "AC", "mare", 1000, "silver", lista)

    rezultat = pretminimgen(lista)

    assert len(rezultat) == 2
    assert rezultat["mare"] == 150
    assert rezultat["drama"] == 100


def test_ordonaredupapret():
    lista = []
    lista = adaugareVanzare("1", "Moarte pe nil", "mare", 150, "gold", lista)
    lista = adaugareVanzare("2", "ABC", "drama", 100, "silver", lista)
    lista = adaugareVanzare("3", "AC", "mare", 1000, "silver", lista)

    rezultat = ordonaredupapret(lista)

    assert getId(rezultat[0]) == "2"
    assert getId(rezultat[1]) == "1"
    assert getId(rezultat[2]) == "3"


def test_titluridistinctedupagen():
    lista = []
    lista = adaugareVanzare("1", "Moarte pe nil", "mare", 150, "gold", lista)
    lista = adaugareVanzare("2", "ABC", "drama", 100, "silver", lista)
    lista = adaugareVanzare("3", "AC", "mare", 1000, "silver", lista)

    rezultat = titluridistinctedupagen(lista)

    assert len(rezultat) == 2
    assert rezultat["mare"] == 2
    assert rezultat["drama"] == 1