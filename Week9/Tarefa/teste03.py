import re

#####  FunÃÂ§ÃÂµes Padroes  #####

def le_assinatura():
    # A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos
    print("Bem-vindo ao detector automÃÂ¡tico de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relacao Type-Token:"))
    hlr = float(input("Entre a Razao Hapax Legomana:"))
    sal = float(input("Entre o tamanho medio de sentenca:"))
    sac = float(input("Entre a complexidade media da sentenca:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    # A funcao que le textos na interface com o usuÃÂ¡rio
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    # A funcao recebe uma texto e devolve uma lista das sentencas dentro do texto (separa pontuacao final)
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    # A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca (separa por virgulas)
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    #Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas    
    valorLinguistico = 0
    
    for i in range(0,6):
        valor = as_a[i] - as_b[i]
        
        if (valor < 0): 
            valor *= -1
            
        valorLinguistico += valor
    
    return valorLinguistico / 6

def calcula_assinatura(texto):
    # Essa funcao recebe um texto e deve devolver a assinatura do texto.
    
    # quebro o texto em suas partes 
    conjSentencas = separa_sentencas(texto)
    
    conjFrases = extrai_frases(conjSentencas)

    conjPalavras = extrai_palavras(conjFrases)
    
    #calculo cada membro da assinatura
    wal = calcula_tamanho_medio_palavra(conjPalavras)
    ttr = calcula_typen_token(conjPalavras)
    hlr = calcula_Hapax_Legomana(conjPalavras)
    
    sal = calcula_tamanho_medio_sentencas(conjSentencas)
    sac = calcula_complexidade_sentenca(conjFrases, len(conjSentencas))
    pal = calcula_tamanho_medio_frase(conjFrases)
   
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    # Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.    
    assinaturas = []
    for te in textos:
        assinaturas.append(calcula_assinatura(te))

    #defino a assinatura com maior grau de similaridade (menor divergencia)
    grauSimilaridade = 1000.0
    numTex = -1
    
    for i in range( 0, len(assinaturas)):
        
        similaridade = compara_assinatura(ass_cp, assinaturas[i])
        
        #print(similaridade)
        
        if (similaridade < grauSimilaridade):
            grauSimilaridade = similaridade
            numTex = i + 1

    return numTex

############################
#####  Minhas Funcoes  #####
############################

def extrai_frases(sentencas):
    # extrai todas as frases de um texto    
    frases = []
    for sentenca in sentencas:
        frases += separa_frases(sentenca)

    return frases

def extrai_palavras(sentencas):
    # extrai todas as palavras de um texto    
    palavras = []
    frases = extrai_frases(sentencas)
    for frase in frases:
        palavras += separa_palavras(frase)
    
    return palavras

def calcula_tamanho_medio_palavra(palavras):
    # Calcula a media simples do numero de caracteres por palavra    
    tamanho = 0
    for pal in palavras:
        tamanho += len(pal)
    
    return tamanho / len(palavras)

def calcula_typen_token(palavras):
    # Calcula Numero de palavras diferentes utilizadas em um texto divididas pelo total de palavras.    
    numPalavrasDif = n_palavras_diferentes(palavras)

    return numPalavrasDif / len(palavras)
    
def calcula_Hapax_Legomana(palavras):
    # Calcula Numero de palavras utilizadas uma vez dividido pelo numero total de palavras
    numPalavasUnicas = n_palavras_unicas(palavras)
    
    return numPalavasUnicas / len(palavras)
    
def calcula_tamanho_medio_sentencas(sentencas):
    # Media simples do nÃºmero de caracteres por sentenÃ§a, sem os caracteres delimitadores
    # delimitadores = .!?
    
    tamanho = 0
    
    for sentenca in sentencas:
        s = re.sub(r'[.!?]+', "", sentenca)
        tamanho += len(s)
    
    return tamanho / len(sentencas)

def calcula_complexidade_sentenca(frases, numeroSentencas):
    # nÃºmero total de frases divido pelo nÃºmero de sentenÃ§as    
    numFrases = len(frases)

    return numFrases / numeroSentencas

def calcula_tamanho_medio_frase(frases):
    # soma do numero de caracteres em cada frase dividida pelo numero de frases no texto, sem os separadores, sem os caracteres delimitadores    
    tamanho = 0
    
    for frase in frases:
        f =  re.sub(r'[,:;]+', "", frase)
        tamanho += len(f)
            
    return tamanho / len(frases)

def main():
    
    # capturo a assinatura padrao
    assinaturaPadrao = le_assinatura()
    
    #assinaturaPadrao = [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
    
    #capturo os textos
    textos = le_textos()
    
    #print(assinaturas)

    numSimilar = avalia_textos(textos, assinaturaPadrao)
    
    print("O autor do texto {} esta infectado com COH-PIAH".format(numSimilar))
    
main()