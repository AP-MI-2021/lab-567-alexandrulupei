from Domain.vanzarecarte import creeazaVanzare, getId, getTitlu, getGen, getPret, getTipreducere


def test_Vanzare():
    vanzare = creeazaVanzare("1", "Moarte pe nil", "politist", 50, "gold")
    assert getId(vanzare) == "1"
    assert getTitlu(vanzare) == "Moarte pe nil"
    assert getGen(vanzare) == "politist"
    assert getPret(vanzare) == 50
    assert getTipreducere(vanzare) == "gold"