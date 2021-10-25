from Domain.vanzarecarte import creeazaVanzare, getId, getTitlu, getPret, getTipreducere


def adaugareVanzare(id, titlu, gen, pret, tipreducere, lista):
    '''

    :param id:
    :param titlu:
    :param gen:
    :param pret:
    :param tipreducere:
    :return:  o lista continand atat elementele vechi, cat si noua vanzare
    '''
    vanzare = creeazaVanzare(id, titlu, gen, pret, tipreducere)
    return lista + [vanzare]


def stergeVanzare(id, lista):
    '''
    sterge o vanzare dupa id
    :param id:
    :param lista:
    :return: o noua lista fara vanzarea repectiva
    '''
    return [vanzare for vanzare in lista if getId(vanzare) != id]


def modificaVanzare(id, titlu, gen, pret, tipreducere, lista):
    '''
    modifica o vanzare dupa id
    :param id:
    :param titlu:
    :param gen:
    :param pret:
    :param tipreducere:
    :param lista:
    :return:
    '''
    listanoua=[]
    for vanzare in lista:
        if getId(vanzare) == id:
            vanzarenoua = creeazaVanzare(id, titlu, gen, pret, tipreducere)
            listanoua.append(vanzarenoua)
        else:
            listanoua.append(vanzare)
    return listanoua


def getById(id, lista):
    '''
    gaseste o vanzare dupa id
    :param id:
    :param lista:
    :return:
    '''
    for vanzare in lista:
        if getId(vanzare) == id:
            return vanzare
    return None



