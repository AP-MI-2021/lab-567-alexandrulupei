from Logic.CRUD import stergeVanzare, adaugareVanzare

show_menu = """
    Puteti introduce multe comenzi simultan, pe care le  separati prin ';',inclusiv la final, fiecare functia avand structura
    Adaugare: add,id, gen, titlu, pret, tipul reducerii
    Stergere: delete,id-ul vanzarii
    Afisare Lista: showall
    Stop: stop
    """
def runnewMenu(lista):
    while True:
        print(show_menu)
        stop = False
        commands = input("Introduceti comenzile, despartite de ';'").split(';')
        for i in range(len(commands)):
            com = commands[i].split(',')
            if com[0] == 'add':
                try:
                    lista = adaugareVanzare(com[1],com[2],com[3],com[4],com[5],lista)
                except IndexError as ie:
                    print(f"Eroare: {ie}")
            elif com[0] == 'delete':
                    lista = stergeVanzare(com[1],lista)
            elif com[0] == 'showall':
                print(lista)
            elif com[0] == 'stop':
                stop = True
                break
        if stop is True:
            break