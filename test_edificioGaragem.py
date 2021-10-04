import pytest

from edificioGaragem import contarVagasOcupadasEmCorredor, contarVagasLivresEmAndar,numeroDoAndarMaisLivre, criarTuplaAndarEVagas ,ordenarAndaresPorVagasLivres,calcularValorTotalArrecadado
#teste para exemplo dado
corredor1 = [1, 1, 0, 1, 0, 0]
corredor2 = [1, 1, 1, 1, 1, 0]
andar1 = [corredor1, corredor2]

corredor3 = [0, 0, 0, 1, 0, 0]
corredor4 = [0, 1, 0, 1, 1, 0]
andar2 = [corredor3, corredor4]

edGaragem = [andar1, andar2]

valorVaga = 10

def testeContarVagasCorredor():
    assert contarVagasOcupadasEmCorredor(corredor1) == 3

def testeVagasLivresAndar():
    assert contarVagasLivresEmAndar(andar1) == 4

def testeEncontrarAndarMaisLivre():
    assert numeroDoAndarMaisLivre(edGaragem) == 2

def testeDeCriarListaDeTuplasDosAndares():
    lista = criarTuplaAndarEVagas(edGaragem)
    assert lista == [(1,4),(2,8)]

def testeDeOrdenarAndaresPorVagasLivres():
    lista = ordenarAndaresPorVagasLivres(edGaragem)
    assert lista == [(1,4),(2,8)]

def testeValorArrecadado():
    assert calcularValorTotalArrecadado(edGaragem, valorVaga) == 120
    
#teste com outros valores
def testeContarVagasOcupadasEmCorredorQualquer():
    corredor = [0,0,0,0,0,1,1,1,1,1]
    assert contarVagasOcupadasEmCorredor(corredor) == 5

def testeVagasLivresEmAndarQualquer():
    corredor1 = [0, 0, 0, 0, 0, 0, 0]
    corredor2 = [1, 1, 1, 1, 1, 1, 0]
    corredor3 = [0, 0, 1, 0, 1, 0]
    corredor4 = [1, 0, 1, 1, 0, 1]
    andar    = [corredor1, corredor2, corredor3, corredor4]
    assert contarVagasLivresEmAndar(andar) == 14

def testeEncontrarAndarMaisLivreQualquer():
    corredor1 = [0, 0, 0, 0, 1, 1]
    corredor2 = [1, 1, 1, 1, 0, 1]
    corredor3 = [0, 0, 1, 0, 1]
    corredor4 = [1, 0, 1, 1, 0]
    corredor5 = [1, 0, 1, 1, 1, 1]
    corredor6 = [1, 0, 1, 0, 1, 0]
    andar1    = [corredor1, corredor2]
    andar2    = [corredor3, corredor4]
    andar3    = [corredor5, corredor6]
    edificioGaragem = [andar1, andar2, andar3]
    assert numeroDoAndarMaisLivre(edificioGaragem) == 1

def testeOrdenarAndaresPorVagasLivresQualquer():
    corredor1 = [0, 0, 0, 0, 1, 1]
    corredor2 = [1, 1, 1, 1, 0, 1]
    corredor3 = [0, 0, 1, 0, 0]
    corredor4 = [1, 0, 1, 1, 0]
    corredor5 = [1, 0, 0, 1, 1, 1]
    corredor6 = [1, 0, 1, 0, 1, 0]
    andar1    = [corredor1, corredor2]
    andar2    = [corredor3, corredor4]
    andar3    = [corredor5, corredor6]
    edificioGaragem = [andar1, andar2, andar3]
    lista = ordenarAndaresPorVagasLivres(edificioGaragem)
    assert lista == [(1,5),(3,5), (2,6)]

def testeValorArrecadadoQualquer():
    corredor1 = [0, 0, 0, 0, 1, 1]
    corredor2 = [1, 1, 1, 1, 0, 1]
    corredor3 = [0, 0, 1, 0, 1]
    corredor4 = [1, 0, 1, 1, 0]
    corredor5 = [1, 0, 0, 1, 1, 1]
    corredor6 = [1, 0, 1, 0, 1, 0]
    andar1    = [corredor1, corredor2]
    andar2    = [corredor3, corredor4]
    andar3    = [corredor5, corredor6]
    edificioGaragem = [andar1, andar2, andar3]
    valorVaga = 10
    assert calcularValorTotalArrecadado(edificioGaragem, valorVaga) == 190
