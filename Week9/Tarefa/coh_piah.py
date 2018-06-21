import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    '''
    wal = 4.79
    ttr = 0.72
    hlr = 0.56
    sal = 80.5
    sac = 2.5
    pal = 31.6
    '''

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    '''
    textos = [
        'Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.',
        'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.',
        'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.'
    ]
    '''

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
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
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    valor = 0

    for i in range(0,6):
        val = as_a[i] - as_b[i]
        if val < 0:
            val = val * (-1)
        valor += val
    sab = valor / 6

    return sab

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    csent = separa_sentencas(texto)
    cfrases = all_frases(csent)
    cwords = all_words(cfrases)

    wal = tam_medio(cwords)
    ttr = type_token(cwords)
    hlr = hapax(cwords)
    sal = tam_medio_sent(cwords)
    sac = complex_sent(cfrases,len(csent))
    pal = tam_medio_frase(cfrases)

    return [wal,ttr,hlr,sal,sac,pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    sign = []
    for text in textos:
        sign.append(calcula_assinatura(text))
    gsimil = 100.0
    ntext = -1
    for i in range(0,len(sign)):
        similaridade = compara_assinatura(ass_cp, sign[i])
        if similaridade < gsimil:
            gsimil = similaridade
            ntext = i + 1
    return ntext

#############################
#       MINHAS FUNÇÕES      #
#############################

def all_frases(sentencas):
    '''Função todas as frases do texto'''
    frases = []
    for sentenca in sentencas:
        frases += separa_frases(sentenca)
    return frases

def all_words(sentencas):
    '''Função todas as palavras do texto'''
    palavras = []
    frases = all_frases(sentencas)
    for frase in frases:
        palavras += separa_palavras(frase)

    return palavras

def tam_medio(palavras):
    '''Função que calcula o tamanho médio de palavras'''
    tam = 0
    for pal in palavras:
        tam += len(pal)
    return tam / len(palavras)

def type_token(palavras):
    '''Função de relação Type-Token'''
    n_words_dif = n_palavras_diferentes(palavras)

    return (n_words_dif / len(palavras))

def hapax(palavras):
    '''Função razão Hapax Legomana'''
    n_words_unic = n_palavras_unicas(palavras)

    return (n_words_unic / len(palavras))

def tam_medio_sent(sentencas):
    '''Função tamanho médio de sentença'''
    tam = 0
    for sentenca in sentencas:
        sent = re.sub(r'[.!?]+', "", sentenca)
        tam += len(sent)

    return (tam / len(sentencas))

def complex_sent(frases,nsent):
    '''Função complexidade de sentença'''
    nfrases = len(frases)
    
    return nfrases / nsent

def tam_medio_frase(frases):
    '''Função tamanho médio de frase'''
    tam = 0
    for frase in frases:
        fras = re.sub(r'[.!?]+', "", frase)
        tam += len(fras)

    return tam / len(frases)

def main():
    '''IMPLEMENTAR'''
    le_assinatura()

    ntext = avalia_textos(le_textos(),le_assinatura())

    print("O autor do texto %d está infectado com COH-PIAH" %(ntext))

main()