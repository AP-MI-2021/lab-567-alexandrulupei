from Domain.vanzarecarte import toString
from Logic.CRUD import adaugareVanzare, stergeVanzare, modificaVanzare
from Logic.functionalitati import discount


def printMenu():
    print("1. Adaugare vanzare")
    print("2. Stergere vanzare")
    print("3. Modificare vanzare")
    print("4. Aplicare discount")
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
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")