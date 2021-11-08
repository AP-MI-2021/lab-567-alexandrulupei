from Domain.vanzarecarte import toString, getGen, getTitlu, getPret, getTipreducere
from Logic.CRUD import adaugareVanzare, stergeVanzare, modificaVanzare, getById
from Logic.functionalitati import discount, modificaredupatitlu, pretminimgen, ordonaredupapret, titluridistinctedupagen


def printMenu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Aplicare discount")
    print("5. Modifica genul unei carti dupa titlul acesteia")
    print("6. Determinarea prețului minim pentru fiecare gen")
    print("7. Ordonarea vânzărilor crescător după preț")
    print("8.  Afișarea numărului de titluri distincte pentru fiecare gen")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare vanzari")
    print("x. Iesire")


def uiadaugavanzare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul: ")
        titlu = input("Dati titlul: ")
        gen = input("Dati genul: ")
        pret = float(input('Dati pretul: '))
        tipdiscount = input("Dati nr. de tipdiscount: ")

        rezultat = adaugareVanzare(id, titlu, gen, pret, tipdiscount, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uistergevanzare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul vanzarii de sters: ")

        rezultat = stergeVanzare(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uimodificaVanzare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul: ")
        titlu = input("Dati titlul: ")
        gen = input("Dati genul: ")
        pret = float(input('Dati pretul: '))
        tipdiscount = input("Dati nr. de tipdiscount: ")

        rezultat = modificaVanzare(id, titlu, gen, pret, tipdiscount, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat

    except ValueError as ve:
        print("Eroare: {}".format(ve))



def showAll(lista):
    for vanzare in lista:
        print(toString(vanzare))


def uiaplicarediscount(lista, undoList, redoList):
    try:
        rezultat = discount(lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uimodificaredupatitlu(lista):
    try:
        titlu = input("Dati titlul vanzarii de modificat:")
        gen = input("Dati noul gen")
        return modificaredupatitlu(titlu, gen, lista)

    except ValueError as ve:
        print("Eroare: {}".format(ve))



def uipretminimgen(lista):
    try:
        rezultat = pretminimgen(lista)
        for gen in rezultat:
            print("Genul {} are pretul minim {}".format(gen, rezultat[gen]))

    except ValueError as ve:
        print("Eroare: {}".format(ve))



def uiordonaredupapret(lista):
    try:
        rezultat = ordonaredupapret(lista)
        showAll(rezultat)

    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uititluridistinctedupagen(lista, ):
    try:
        rezultat = titluridistinctedupagen(lista)
        for gen in rezultat:
            print("Genul {} are {} titluti distincte".format(gen, rezultat[gen]))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def runMenu(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiadaugavanzare(lista, undoList, redoList)
        elif optiune == "2":
            lista = uistergevanzare(lista, undoList, redoList)
        elif optiune == "3":
            lista = uimodificaVanzare(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiaplicarediscount(lista, undoList, redoList)
        elif optiune == "5":
            lista = uimodificaredupatitlu(lista)
        elif optiune == "6":
            uipretminimgen(lista)
        elif optiune == "7":
            uiordonaredupapret(lista)
        elif optiune == "8":
            uititluridistinctedupagen(lista)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati:")
