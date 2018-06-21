import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    '''
    t_med_plv = float(input("Entre o tamanho medio de palavra: "))
    type_token = float(input("Entre a relação Type-Token: "))
    hapax = float(input("Entre a Razão Hapax Legomana: "))
    t_med_sent = float(input("Entre o tamanho médio de sentença: "))
    comp_sent = float(input("Entre a complexidade média da sentença: "))
    t_med_fras = float(input("Entre o tamanho medio de frase: "))
    '''

    t_med_plv = 4.79
    type_token = 0.72
    hapax = 0.56
    t_med_sent = 80.5
    comp_sent = 2.5
    t_med_fras = 31.6

    return [t_med_plv, type_token, hapax, t_med_sent, comp_sent, t_med_fras]

def le_textos():
    i = 1
    textos = [
        'Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.',
        'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.',
        'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.'
    ]

    '''
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    '''

    return textos

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    if type(texto) != list:
        aux = texto
        texto = []
        texto.append(aux)
    #as_signb = []
    for i in texto:
        sentencas = []
        sentencas = separa_sentencas(str(i))
        frases = []
        ntotal_sent = 0
        sum_csent = 0
        for i in range(len(sentencas)):
            frasei = separa_frases(str(sentencas[i]))
            frases.append(frasei)
            ntotal_sent += 1
            sum_csent = sum_csent + len(sentencas[i])
        words = []
        ntotal_frase = 0
        sum_cfrase = 0
        for lin in range(len(frases)):
            for col in range(len(frases[lin])):
                words_i = separa_palavras(str(frases[lin][col]))
                words.append(words_i)
                ntotal_frase += 1
                sum_cfrase = sum_cfrase + len(str(frases[lin][col]))
        matrix_list = []
        for lin in range(len(words)):
            for col in range(len(words[lin])):
                matrix_list.append(words[lin][col])
        words = matrix_list[:]
        sum_compar_word = 0
        ntotal_word = 0
        for lin in range(len(words)):
            for col in range(len(words[lin])):
                sum_compar_word = sum_compar_word + len(str(words[lin][col]))
            ntotal_word += 1
        ass_txt = []
        ass_txt.append(t_med_plv(sum_compar_word, ntotal_word))
        ass_txt.append(type_token(words, ntotal_word))
        ass_txt.append(hapax(words, ntotal_word))
        ass_txt.append(t_med_sent(sum_csent, ntotal_sent))
        ass_txt.append(comp_sent(ntotal_frase, ntotal_sent))
        ass_txt.append(t_med_fras(sum_cfrase, ntotal_frase))
    return ass_txt

def t_med_plv(sum_word, ntotal_word):
    '''Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.'''
    if sum_word != 0:
        t_med_plv = sum_word / ntotal_word
    else:
        t_med_plv = 0
    return t_med_plv

def type_token(lista_palavras, ntotal_word):
    '''Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras.'''
    ndif_word = n_palavras_diferentes(lista_palavras)
    if ntotal_word != 0:
        type_token = ndif_word / ntotal_word
    else:
        type_token = 0
    return type_token

def hapax(lista_palavras, ntotal_word):
    '''Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras.'''
    nuniq_word = n_palavras_unicas(lista_palavras)
    if ntotal_word !=0:
        hapax = nuniq_word / ntotal_word
    else:
        nuniq_word = 0
    return nuniq_word

def t_med_sent(sum_ncaract, n_sent):
    '''Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças.'''
    if n_sent != 0:
        t_med_sent = sum_ncaract / n_sent
    else:
        t_med_sent = 0
    return t_med_sent

def comp_sent(ntotal_frase, ntotal_sent):
    '''Complexidade de sentença é o número total de frases divido pelo número de sentenças.'''
    if ntotal_sent != 0:
        comp_sent = ntotal_frase / ntotal_sent
    else:
        comp_sent = 0
    return comp_sent

def t_med_fras(sum_ncaract, ntotal_frase):
    '''Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto.'''
    if ntotal_frase != 0:
        t_med_fras = sum_ncaract / ntotal_frase
    else:
        t_med_fras = 0
    return t_med_fras

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

def compara_assinatura(as_signa, ass_txt):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    lis = []
    sum_mod = 0
    if type(ass_txt[0]) is list:
        for lin in range(len(ass_txt)):
            for col in range(len(ass_txt[lin])):
                sum_mod += abs(as_signa[col] - ass_txt[lin][col])
            sab = sum_mod / 6
            lis.append(sab)
        return lis
    else:
        for i in range(len(ass_txt)):
            sum_mod += abs(as_signa[i] - ass_txt[i])
        sab = sum_mod / 6

        return sab

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    aux_assc = (ass_cp[:])
    aux_assc.sort()
    for indice in range(len(ass_cp)):
        if aux_assc[0] == ass_cp[indice]:
            copiah = indice

    return copiah

def main():
    as_signa = le_assinatura()
    textos = le_textos()
    as_signb = calcula_assinatura(textos)
    ass_cp = compara_assinatura(as_signa,ass_txt)
    copiah = avalia_textos(textos,ass_cp) + 1

    return print("O autor do texto %d está infectado com COH-PIAH" %(copiah))

main()


'''

Texto 01
Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.

Texto 02
Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.

Texto 03
NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.

'''