from Domain.vanzarecarte import getTipreducere, creeazaVanzare, getId, getTitlu, getGen, getPret


def discount(lista):
    '''
    Determina reducerea pretului unei vanzari
    :param tipdiscount:
    :param lista:
    :return:
    '''
    listanoua = []
    for vanzare in lista:
        if "silver" in getTipreducere(vanzare):
            vanzarenoua = creeazaVanzare(
                getId(vanzare),
                getTitlu(vanzare),
                getGen(vanzare),
                getPret(vanzare) - (getPret(vanzare) * 0.05),
                getTipreducere(vanzare)
            )
            listanoua.append(vanzarenoua)
        elif "gold" in getTipreducere(vanzare):
            vanzarenoua = creeazaVanzare(
                getId(vanzare),
                getTitlu(vanzare),
                getGen(vanzare),
                getPret(vanzare) - (getPret(vanzare) * 0.1),
                getTipreducere(vanzare)
            )
            listanoua.append(vanzarenoua)
        else:
            listanoua.append(vanzare)
    return listanoua


def modificaredupatitlu(title, gen, lista):
    '''
    gaseste o vanzare dupa titlu si o modifica
    :param gen:
    :param title:
    :param lista:
    :return:
    '''
    listanoua = []
    for vanzare in lista:
        if title in getTitlu(vanzare):
            vanzaremod = creeazaVanzare(
                getId(vanzare),
                getTitlu(vanzare),
                gen,
                getPret(vanzare),
                getTipreducere(vanzare)
            )
            listanoua.append(vanzaremod)
        else:
            listanoua.append(vanzare)
    lista.clear()
    lista = listanoua
    return lista


def delete(x):
    temp_list = list(x)  # converting to list
    temp_list.clear()  # clearing list
    x = tuple(temp_list)  # converting to tuple


def deletethis(this, lista):
    listanoua = []
    for vanzare in lista:
        if not this in getGen(vanzare):
            listanoua.append(vanzare)
    lista.clear()
    lista = listanoua
    return lista


def pretminimgen(lista):
    '''

    :param lista:
    :return:
    '''
    rezultat = {}
    for vanzare in lista:
        gen = getGen(vanzare)
        pret = getPret(vanzare)
        if gen in rezultat:
            if pret < rezultat[gen]:
                rezultat[gen] = pret
        else:
            rezultat[gen] = pret
    return rezultat


def ordonaredupapret(lista):
    '''

    :param lista:
    :return:
    '''
    return sorted(lista, key=lambda vanzare: getPret(vanzare))


def titluridistinctedupagen(lista):
    genuri = {}
    titluri = {}

    for vanzare in lista:
        titlu = getTitlu(vanzare)
        gen = getGen(vanzare)
        if gen in genuri:
            if titlu not in titluri:
                genuri[gen] = genuri[gen] + 1
                titluri[titlu] = titlu
        else:
            genuri[gen] = 1
            titluri[titlu] = titlu
    return genuri
