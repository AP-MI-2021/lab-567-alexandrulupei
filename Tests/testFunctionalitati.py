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

def test_undo_redo():
    undoList = []
    redoList = []
    lista = []

    lista = adaugareVanzare("1", "Moarte pe nil", "mare", 150, "gold", lista)
    assert len(lista) == 1
    undoList.append(lista)

    lista = adaugareVanzare("2", "ABC", "drama", 100, "silver", lista)
    assert len(lista) == 2
    undoList.append(lista)

    lista = adaugareVanzare("3", "AC", "mare", 1000, "silver", lista)
    undoList.append(lista)
    assert len(lista) == 3



    assert len(undoList) == 3
    redoList.append(lista)
    lista = undoList.pop()
    print(lista)
    assert len(undoList) == 2

    redoList.append(lista)
    lista = undoList.pop()
    assert len(undoList) == 1

    redoList.append(lista)
    lista = undoList.pop()
    assert len(undoList) == 0
    assert len(redoList) == 3

    redoList = []
    lista.clear()
    lista = adaugareVanzare("1", "Moarte pe nil", "mare", 150, "gold", lista)
    assert len(lista) == 1
    undoList.append(lista)
    redoList.clear()

    lista = adaugareVanzare("2", "ABC", "drama", 100, "silver", lista)
    assert len(lista) == 2
    undoList.append(lista)
    redoList.clear()

    lista = adaugareVanzare("4", "ACc", "marec", 1000, "silver", lista)
    undoList.append(lista)
    redoList.clear()
    assert len(redoList) == 0
    assert len(undoList) == 3

    undoList.pop()
    redoList.append(lista)

    assert len(redoList) == 1
    assert len(undoList) == 2

    undoList.pop()
    redoList.append(lista)

    assert len(redoList) == 2
    assert len(undoList) == 1

    redoList.pop()
    undoList.append(lista)

    assert len(redoList) == 1
    assert len(undoList) == 2

    redoList.pop()
    undoList.append(lista)

    assert len(redoList) == 0
    assert len(undoList) == 3

    undoList.pop()
    redoList.append(lista)

    assert len(redoList) == 1
    assert len(undoList) == 2

    lista = adaugareVanzare("5", "A4C", "mar4e", 1000, "silver", lista)
    undoList.pop()
    redoList.append(lista)

    assert len(redoList) == 2
    assert len(undoList) == 1

    undoList.pop()
    redoList.append(lista)

    assert len(redoList) == 3
    assert len(undoList) == 0


    redoList.pop()
    undoList.append(lista)

    assert len(redoList) == 2
    assert len(undoList) == 1

    redoList.pop()
    undoList.append(lista)

    assert len(redoList) == 1
    assert len(undoList) == 2

    if len(redoList) > 0:
        redoList.pop()
    assert len(redoList) == 0
