from Domain.vanzarecarte import toString
from Logic.CRUD import adaugareVanzare, stergeVanzare, modificaVanzare
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
    print("a. Afisare vanzari")
    print("x. Iesire")


def uiadaugavanzare(lista):
    id = input("Dati id-ul: ")
    titlu = input("Dati titlul: ")
    gen = input("Dati genul: ")
    pret = float(input('Dati pretul: '))
    tipdiscount = input("Dati nr. de tipdiscount: ")
    return adaugareVanzare(id, titlu, gen, pret, tipdiscount, lista)


def uistergevanzare(lista):
    id = input("Dati id-ul prajiturii de sters: ")
    return stergeVanzare(id, lista)


def uimodificaVanzare(lista):
    id = input("Dati id-ul: ")
    titlu = input("Dati titlul: ")
    gen = input("Dati genul: ")
    pret = float(input('Dati pretul: '))
    tipdiscount = input("Dati nr. de tipdiscount: ")
    return modificaVanzare(id, titlu, gen, pret, tipdiscount, lista)


def showAll(lista):
    for vanzare in lista:
        print(toString(vanzare))


def uiaplicarediscount(lista):
    return discount(lista)


def uimodificaredupatitlu(lista):
    titlu = input("Dati titlul vanzarii de modificat:")
    gen = input("Dati noul gen")
    return modificaredupatitlu(titlu, gen, lista)


def uipretminimgen(lista):
    rezultat = pretminimgen(lista)
    for gen in rezultat:
        print("Genul {} are pretul minim {}".format(gen, rezultat[gen]))


def uiordonaredupapret(lista):
    rezultat = ordonaredupapret(lista)
    showAll(rezultat)


def uititluridistinctedupagen(lista):
    rezultat = titluridistinctedupagen(lista)
    for gen in rezultat:
        print("Genul {} are {} titluti distincte".format(gen, rezultat[gen]))


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiadaugavanzare(lista)
        elif optiune == "2":
            lista = uistergevanzare(lista)
        elif optiune == "3":
            lista = uimodificaVanzare(lista)
        elif optiune == "4":
            lista = uiaplicarediscount(lista)
        elif optiune == "5":
            lista = uimodificaredupatitlu(lista)
        elif optiune == "6":
            uipretminimgen(lista)
        elif optiune == "7":
            uiordonaredupapret(lista)
        elif optiune == "8":
            uititluridistinctedupagen(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati:")