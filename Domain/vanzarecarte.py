def creeazaVanzare(id, titlu, gen, pret, tipreducere):
    '''

    :param id:
    :param titlu:
    :param gen:
    :param pret:
    :param tipreducere:
    :return:
    '''
    return {
    "id": id,
    "titlu": titlu,
    "gen": gen,
    "pret": pret,
    "tipreducere": tipreducere
    }


def getId(vanzare):
    return vanzare["id"]


def getTitlu(vanzare):
    return vanzare["titlu"]


def getGen(vanzare):
    return vanzare["gen"]


def getPret(vanzare):
    return vanzare["pret"]


def getTipreducere(vanzare):
    return vanzare["tipreducere"]


def toString(vanzare):
    return "Id: {}, Titlu: {}, Gen: {}, Pret: {}, TipReducere: {}".format(
    getId(vanzare),
    getTitlu(vanzare),
    getGen(vanzare),
    getPret(vanzare),
    getTipreducere(vanzare)
    )