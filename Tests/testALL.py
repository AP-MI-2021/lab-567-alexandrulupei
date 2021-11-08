from Tests.testCRUD import test_adaugaVanzare, test_stergeVanzare, test_modificaVanzare
from Tests.testDomain import test_Vanzare
from Tests.testFunctionalitati import test_aplicarediscount, test_modificaredupatitlu, test_undo_redo


def runalltests():
    test_Vanzare()
    test_adaugaVanzare()
    test_stergeVanzare()
    test_modificaVanzare()
    test_aplicarediscount()
    test_modificaredupatitlu()
    test_undo_redo()