def contarVagasOcupadasEmCorredor(corredor):
    contador = 0
    for vaga in corredor:
        if vaga == 1:
            contador +=1
    return contador

def contarVagasLivresEmAndar(andar):
    vagasLivres = 0
    for corredor in andar:        
        vagasLivres +=  (len(corredor)) - contarVagasOcupadasEmCorredor(corredor)
    return vagasLivres

def encontrarAndarMaisLivre(edificioGaragem):
    andarMaisLivre = edificioGaragem[:1]

    for andar in edificioGaragem:
        if(contarVagasLivresEmAndar(andarMaisLivre) < contarVagasLivresEmAndar(andar)):
            andarMaisLivre = andar
    return andarMaisLivre

def numeroDoAndarMaisLivre(edificioGaragem):
    andarMaisLivre = encontrarAndarMaisLivre(edificioGaragem)
    return edificioGaragem.index(andarMaisLivre)+1

def criarTuplaAndarEVagas(edificioGaragem):
    tuplaAndarEVagas =[]
    for andar in edificioGaragem:
        tuplaAndarEVagas.append((edificioGaragem.index(andar)+1, contarVagasLivresEmAndar(andar)))
    return tuplaAndarEVagas

def vagas(tupla):
    return tupla[1]

#Para essa função são retornadas o andar e as quantidade de vagas em ordem crescente
#Andares com total de vagas livres iguais serão ordenados pelo número do andar
def ordenarAndaresPorVagasLivres(edificioGaragem):
    tuplaAndarEVagas = criarTuplaAndarEVagas(edificioGaragem)
    tuplaAndarEVagas.sort(key = vagas)

    return tuplaAndarEVagas

def calcularValorTotalArrecadado(edificioGaragem, valorVaga):
    valorTotal = 0
    vagasOcupadas = 0
    for andar in edificioGaragem:
        for corredor in andar:
            vagasOcupadas += contarVagasOcupadasEmCorredor(corredor)
    valorTotal = vagasOcupadas*valorVaga

    return valorTotal
    

