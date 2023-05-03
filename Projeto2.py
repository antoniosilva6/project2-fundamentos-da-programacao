#########################
# Projeto 2             #
# Antonio Dias da Silva #
# numero: 102879        #
#########################

###############
# TAD Gerador #
###############

# Construtores

def cria_gerador(bits, seed):
    """
    A funcao cria gerador recebe um inteiro, bits, correspondente ao numero de bits
    do gerador e um inteiro positivo, seed, correspondente ao estado inicial.
    Verifica a validade dos argumentos e devolve o gerador na representacao
    escolhida, ou seja, [bits, seed].
    (int, int) -> gerador
    """
    if type(bits) != int or type(seed) != int:
        raise ValueError("cria_gerador: argumentos invalidos")
    if bits != 32 and bits != 64:
        raise ValueError("cria_gerador: argumentos invalidos")
    if bits == 32 and seed > 2**32:
        raise ValueError("cria_gerador: argumentos invalidos")
    if bits == 64 and seed > 2**64:
        raise ValueError("cria_gerador: argumentos invalidos")
    if seed <= 0:
        raise ValueError("cria_gerador: argumentos invalidos")

    return [bits, seed]

def cria_copia_gerador(gerador):
    """
    A funcao cria_copia_gerador recebe um gerador e devolve uma copia nova do
    gerador, na mesma representacao escolhida.
    (gerador) -> gerador
    """
    copiaGerador = []
    for elem in range(len(gerador)):
        copiaGerador.append(gerador[elem])

    return copiaGerador

# Seletores

def obtem_bits(gerador):
    """
    A funcao obtem_bits devolve o numero de bits do gerador sem o alterar.
    (gerador) -> int
    """
    return gerador[0]

def obtem_estado(gerador):
    """
    A funcao obtem_estado devolve o estado atual do gerador sem o alterar.
    (gerador) -> int
    """
    return gerador[1]

# Modificadores

def define_estado(gerador, seed):
    """
    A funcao define_estado define o novo valor do estado do gerador como sendo
    seed e devolve a seed.
    (gerador, int) -> int
    """
    gerador[1] = seed
    return seed

def atualiza_estado(gerador):
    """
    A funcao atualiza_estado atualiza o estado do gerador de acordo com o
    algoritmo xorshift de geracao de numeros pseudoaleatorios, e devolve o
    novo estado.
    (gerador) -> int
    """
    if obtem_bits(gerador) == 32:
        gerador[1] ^= (gerador[1] << 13) & 0xFFFFFFFF
        gerador[1] ^= (gerador[1] >> 17) & 0xFFFFFFFF
        gerador[1] ^= (gerador[1] << 5) & 0xFFFFFFFF
        return gerador[1]
    else:
        gerador[1] ^= (gerador[1] << 13) & 0xFFFFFFFFFFFFFFFF
        gerador[1] ^= (gerador[1] >> 7) & 0xFFFFFFFFFFFFFFFF
        gerador[1] ^= (gerador[1] << 17) & 0xFFFFFFFFFFFFFFFF
        return gerador[1]

# Reconhecedor

def eh_gerador(arg):
    """
    A funcao eh_gerador devolve True caso o arg seja um TAD gerador e False
    caso contrario.
    (universal) -> boolean
    """
    return type(arg) == list and len(arg) == 2 and \
           type(arg[1]) == int and type(arg[0]) == int and \
           ((arg[0] == 32 and arg[1] < 2**32) or (arg[0] == 64 and arg[1] < 2**64)) and \
           arg[1] > 0

# Teste

def geradores_iguais(gerador1, gerador2):
    """
    A funcao gerador_iguais recebe dois geradores e devolve True caso estes
    sejam geradores e iguais e False caso contrario.
    (gerador, gerador) -> boolean
    """
    return eh_gerador(gerador1) and eh_gerador(gerador2) and \
        obtem_estado(gerador1) == obtem_estado(gerador2) and \
        obtem_bits(gerador1) == obtem_bits(gerador2)

# Transformador

def gerador_para_str(gerador):
    """
    A funcao gerador_para_str devolve a cadeia de caracteres coorespondente ao
    gerador, ou seja, [bits, seed] -> 'xorshift'bits'(s='seed')'.
    Exemplo: [32, 1] -> 'xorshift32(s=1)'
    (gerador) -> string
    """
    return "xorshift" + str(gerador[0]) + "(s=" + str(gerador[1]) + ")"

# Funcoes de Alto Nivel

def gera_numero_aleatorio(gerador, numero):
    """
    A funcao gera_numero_aleatorio atualiza o estado do gerador e devolve um
    aleatorio no intervalo [1, numero] obtido a partir do novo estado do gerador
    como 1 + (s % numero).
    (gerador, int) -> int
    """
    s = atualiza_estado(gerador)
    return 1 + (s % numero)

def gera_carater_aleatorio(gerador, caracter):
    """
    A funcao gera_carater_aleatorio atualiza o estado do gerador e devolve um
    caracter aleatorio no intervalo de 'A' a caracter (maiusculo), a partir do
    novo estado s de g como o caracter na posicao s % len(letras).
    (gerador, string) -> string
    """
    s = atualiza_estado(gerador)
    letras = [chr(n) for n in range(ord("A"), ord(caracter) + 1)]
    posicao = s % len(letras)
    return letras[posicao]

##################
# TAD Coordenada #
##################

# Construtor

def cria_coordenada(coluna, linha):
    """
    A funcao cria_coordenada recebe os valores correspondestes a coluna e linha.
    Verifica a validade dos argumentos e devolve a coordenada de acordo com a
    representacao escolhida, ou seja, (coluna, linha)
    (string, int) -> coordenada
    """
    if (type(coluna) == str and len(coluna) == 1) and type(linha) == int:
        if ord('A') <= ord(coluna) <= ord('Z'):
            if 1 <= linha <= 99:

                return coluna, linha

    raise ValueError("cria_coordenada: argumentos invalidos")

# Seletores

def obtem_coluna(coordenada):
    """
    A funcao obtem_coluna devolve a coluna da respetiva coordenada.
    (coordenada) -> string
    """
    return coordenada[0]

def obtem_linha(coordenada):
    """
    A funcao obtem_linha devolve a linha da respetiva coordenada.
    (coordenada) -> int
    """
    return coordenada[1]

# Reconhecedor

def eh_coordenada(arg):
    """
    A funcao eh_coordenada recebe um arg e devolve True apenas se este for uma
    coordenada e False caso contrario.
    (universal) -> boolean
    """
    return type(arg) == tuple and len(arg) == 2 and \
           len(arg[0]) == 1 and chr(65) <= arg[0] <= chr(90) and \
           1 <= arg[1] <= 99

# Teste

def coordenadas_iguais(coordenada1, coordenada2):
    """
    A funcao coordenadas_iguais recebe duas coordenadas e devolve True apenas
    se estas forem coordenadas e iguais.
    (coordenada, coordenada) -> boolean
    """
    return eh_coordenada(coordenada1) and eh_coordenada(coordenada2) and \
        obtem_linha(coordenada1) == obtem_linha(coordenada2) and \
        obtem_coluna(coordenada1) == obtem_coluna(coordenada2)

# Transformadores

def coordenada_para_str(coordenada):
    """
    A funcao coordenada_para_str devolve a cadeia de caracteres correspondente
    a coordenada, ou seja, (coluna, linha) -> ''coluna''linha''.
    Exemplo: ('B', 1) -> 'B01'
    (coordenada) -> string
    """
    if obtem_linha(coordenada) < 10:
        return str(coordenada[0]) + str(0) + str(coordenada[1])
    return str(coordenada[0]) + str(coordenada[1])

def str_para_coordenada(str):
    """
    A funcao str_para_coordenada recebe uma cadeia de caracteres correspondente
    a uma coordenada e devolve a coordenada de acordo com o TAD coordeanda.
    (string) -> coordenada
    """
    return str[0], int(str[1]) * 10 + int(str[2])

# Funcoes de Alto Nivel

def obtem_coordenadas_vizinhas(coordenada):
    """
    A funcao obtem_coordenadas_vizinhas recebe uma coordenada e devolve um tuplo
    com todas as coordenadas vizinha de acordo com os limites máximos do campo.
    As coordenadas no tuplo começam pela coordenada na diagonal de acima-esquerda
    e seguindo no sentido horario.
    (coordenada) -> tuplo
    """
    resultado = ()
    linha, coluna = obtem_linha(coordenada), obtem_coluna(coordenada)

    if coluna != "A" and coluna != "Z" and linha != 1 and linha != 99:
        resultado += (cria_coordenada(chr(ord(coluna) - 1), linha - 1),)
        resultado += (cria_coordenada(coluna, linha - 1),)
        resultado += (cria_coordenada(chr(ord(coluna) + 1), linha - 1),)
        resultado += (cria_coordenada(chr(ord(coluna) + 1), linha),)
        resultado += (cria_coordenada(chr(ord(coluna) + 1), linha + 1),)
        resultado += (cria_coordenada(coluna, linha + 1),)
        resultado += (cria_coordenada(chr(ord(coluna) - 1), linha + 1),)
        resultado += (cria_coordenada(chr(ord(coluna) - 1), linha),)

    elif coluna != "A" and coluna != "Z" and linha == 1:
        resultado += (cria_coordenada(chr(ord(coluna) + 1), linha),)
        resultado += (cria_coordenada(chr(ord(coluna) + 1), linha + 1),)
        resultado += (cria_coordenada(coluna, linha + 1),)
        resultado += (cria_coordenada(chr(ord(coluna) - 1), linha + 1),)
        resultado += (cria_coordenada(chr(ord(coluna) - 1), linha),)

    elif coluna != "A" and coluna != "Z" and linha == 99:
        resultado += (cria_coordenada(chr(ord(coluna) - 1), linha - 1),)
        resultado += (cria_coordenada(coluna, linha - 1),)
        resultado += (cria_coordenada(chr(ord(coluna) + 1), linha - 1),)
        resultado += (cria_coordenada(chr(ord(coluna) + 1), linha),)
        resultado += (cria_coordenada(chr(ord(coluna) - 1), linha),)

    elif coluna == "A" and linha != 1 and linha != 99:
        resultado += (cria_coordenada(coluna, linha - 1),)
        resultado += (cria_coordenada(chr(ord(coluna) + 1), linha - 1),)
        resultado += (cria_coordenada(chr(ord(coluna) + 1), linha),)
        resultado += (cria_coordenada(chr(ord(coluna) + 1), linha + 1),)
        resultado += (cria_coordenada(coluna, linha + 1),)

    elif coluna == "Z" and linha != 1 and linha != 99:
        resultado += (cria_coordenada(chr(ord(coluna) - 1), linha - 1),)
        resultado += (cria_coordenada(coluna, linha - 1),)
        resultado += (cria_coordenada(coluna, linha + 1),)
        resultado += (cria_coordenada(chr(ord(coluna) - 1), linha + 1),)
        resultado += (cria_coordenada(chr(ord(coluna) - 1), linha),)

    elif coluna == "A" and linha == 1:
        resultado += (cria_coordenada(chr(ord(coluna) + 1), linha),)
        resultado += (cria_coordenada(chr(ord(coluna) + 1), linha + 1),)
        resultado += (cria_coordenada(coluna, linha + 1),)

    elif coluna == "A" and linha == 99:
        resultado += (cria_coordenada(coluna, linha - 1),)
        resultado += (cria_coordenada(chr(ord(coluna) + 1), linha - 1),)
        resultado += (cria_coordenada(chr(ord(coluna) + 1), linha),)

    elif coluna == "Z" and linha == 1:
        resultado += (cria_coordenada(coluna, linha - 1),)
        resultado += (cria_coordenada(chr(ord(coluna) - 1), linha + 1),)
        resultado += (cria_coordenada(chr(ord(coluna) - 1), linha),)

    elif coluna == "Z" and linha == 99:
        resultado += (cria_coordenada(chr(ord(coluna) - 1), linha - 1),)
        resultado += (cria_coordenada(coluna, linha - 1),)
        resultado += (cria_coordenada(chr(ord(coluna) - 1), linha),)

    return resultado

def obtem_coordenada_aleatoria(coordenada, gerador):
    """
    A funcao obtem_coordenada_aleatoria recebe uma coordenada e um gerador e
    devolve uma coordenada gerada aleatoriamente. A coordenada define a maior
    coluna e maior linha possiveis.
    (coordenada, gerador) -> coordenada
    """
    coluna = gera_carater_aleatorio(gerador, obtem_coluna(coordenada))
    linha = gera_numero_aleatorio(gerador, obtem_linha(coordenada))
    coordenadaAleatoria = cria_coordenada(coluna,linha)
    return coordenadaAleatoria

###############
# TAD Parcela #
###############

# Construtores

def cria_parcela():
    """
    A funcao cria_parcela devolve uma parcela tapada e sem mina escondida. A
    representacao escolhida foi ['tapadas', 'desminadas', 'desmarcadas'], de
    modo a representar todos os estados possiveis de cada parcela.
    () -> parcela
    """
    return ['tapadas', 'desminadas', 'desmarcadas']

def cria_copia_parcela(parcela):
    """
    A funcao cria_copia_parcela recebe uma parcela e devolve uma nova copia da
    parcela.
    (parcela) -> parcela
    """
    return [parcela[0], parcela[1], parcela[2]]

# Modificadores

def limpa_parcela(parcela):
    """
    A funcao limpa_parcela altera o estado da parcela para limpa e devolve a
    propria parcela.
    (parcela) -> parcela
    """
    parcela[0] = 'limpas'
    return parcela

def marca_parcela(parcela):
    """
    A funcao marca_parcela altera o estado da parcela para marcada e devolve a
    propria parcela.
    (parcela) -> parcela
    """
    parcela[2] = 'marcadas'
    return parcela

def desmarca_parcela(parcela):
    """
    A funcao desmarca_parcela altera o estado da parcela para desmarcada e
    devolve a propria parcela.
    (parcela) -> parcela
    """
    parcela[2] = 'desmarcadas'
    return parcela

def esconde_mina(parcela):
    """
    A funcao esconde_parcela altera o estado da parcela para uma parcela com uma
    mina escondida e devolve a propria parcela.
    (parcela) -> parcela
    """
    parcela[1] = 'minadas'
    return parcela

# Reconhecedores

def eh_parcela(arg):
    """
    A funcao eh_parcela recebe um arg e devolve True apenas se for uma parcela
    e False caso contrario.
    (universal) -> boolean
    """
    return type(arg) == list and len(arg) == 3 and \
           (arg[0] == 'tapadas' or arg[0] == 'limpas') and \
           (arg[1] == 'desminadas' or arg[1] == 'minadas') and \
           (arg[2] == 'marcadas' or arg[2] == 'desmarcadas')

def eh_parcela_tapada(parcela):
    """
    A funcao eh_parcela_tapada recebe uma parcela e devolve True apenas se esta
    estiver tapada e False caso contrario.
    (parcela) -> boolean
    """
    return parcela[0] == 'tapadas' and parcela[2] == 'desmarcadas'

def eh_parcela_marcada(parcela):
    """
    A funcao eh_parcela_marcada recebe uma parcela e devolve True apenas se
    esta estiver marcada e False caso contrario.
    (parcela) -> boolean
    """
    return parcela[2] == 'marcadas'

def eh_parcela_limpa(parcela):
    """
    A funcao eh_parcela_limpa recebe uma parcela e devolve True apenas se esta
    estiver limpa e False caso contrario.
    (parcela) -> boolean
    """
    return parcela[0] == 'limpas'

def eh_parcela_minada(parcela):
    """
    A funcao eh_parcela_minada recebe uma parcela e devolve True apenas se esta
    estiver tapada e esconder uma mina e False caso contrario.
    (parcela) -> boolean
    """
    return parcela[1] == 'minadas' and eh_parcela_tapada(parcela)

#Teste

def parcelas_iguais(parcela1, parcela2):
    """
    A funcao parcelas_iguais recebe duas parcelas e devolve True apenas se ambas
    forem parcelas e iguas.
    (parcela, parcela) -> boolean
    """
    return eh_parcela(parcela1) and eh_parcela(parcela2) and \
           parcela1[0] == parcela2[0] and \
           parcela1[1] == parcela2[1] and \
           parcela1[2] == parcela2[2]

# Transformador

def parcela_para_str(parcela):
    """
    A funcao parcela_para_str recebe uma parcela e devolve a cadeia de caracteres
    que representa o estado da parcela.
    ('#'): parcelas tapadas
    ('@'): parcelas marcadas
    ('?'): parcelas limpas sem minas
    ('X'): parcelas limpas com minas
    (parcela) -> string
    """
    if eh_parcela_marcada(parcela):
        return '@'
    if eh_parcela_tapada(parcela):
        return '#'
    if eh_parcela_limpa(parcela) and parcela[1] == 'desminadas':
        return '?'
    if eh_parcela_limpa(parcela) and eh_parcela_minada(parcela):
        return 'X'

# Funcoes de Alto Nivel

def alterna_bandeira(parcela):
    """
    A funcao alterna_bandeira recebe uma parcela e altera o seu estado:
    desmarcada se estiver marcada  e marca se estiver tapada, devolvendo True.
    Em qualquer outro caso, não modifica a parcela e devolve False.
    (parcela) -> boolean
    """
    if eh_parcela_marcada(parcela):
        parcela[2] = 'desmarcadas'
        return True

    elif eh_parcela_tapada(parcela) and not eh_parcela_marcada(parcela):
        marca_parcela(parcela)
        return True

    return False


#############
# TAD Campo #
#############

# Construtores

def cria_campo(colunas, linhas):
    """
    A funcao cria_campo recebe uma cadeia de caracteres e um inteiro positivo,
    correspondestes a ultima coluna e ultima linha, respetivamente, do campo.
    Verifica a validade dos argumento e devolve o campo como um tuplo de tuplos
    em que dentro de cada tuplo estão a parcelas que preenchem o campo.
    (string, int) -> campo
    """
    if (type(colunas) == str and len(colunas) == 1) and type(linhas) == int:
        if ord('A') <= ord(colunas) <= ord('Z'):
            if 1 <= linhas <= 99:
                campo = ()
                numColunas = (ord(colunas) - ord('A')) + 1
                for i in range(linhas):
                    linha = ()
                    for j in range(numColunas):
                        linha += (cria_parcela(),)
                    campo += (linha,)
                return campo

    raise ValueError('cria_campo: argumentos invalidos')

def cria_copia_campo(campo):
    """
    A funcao cria_copia_campo recebe um campo e devolve uma nova copia do campo.
    (campo) -> campo
    """
    copiaCampo = ()
    for linha in campo:
        copiaParcela = ()
        for parcela in linha:
            copiaParcela += (cria_copia_parcela(parcela),)
        copiaCampo += (copiaParcela,)
    return copiaCampo

# Seletores

def obtem_ultima_coluna(campo):
    """
    A funcao obtem_ultima_coluna devolve a cadeia de caracteres que corresponde
    a ultima coluna do campo.
    (campo) -> string
    """
    return chr(len(campo[0]) + 64)

def obtem_ultima_linha(campo):
    """
    A funcao obtem_ultima_linha devolve o inteiro positivo que corresponde a
    ultima linha do campo.
    (campo) -> int
    """
    return len(campo)

def obtem_parcela(campo, coordenada):
    """
    A obtem_parcela devolve a parcela do campo que corresponde a coordenada
    passadas como argumento.
    (campo, coordenada) -> parcela
    """
    linha = obtem_linha(coordenada) - 1
    coluna = ord(obtem_coluna(coordenada)) - 65

    return campo[linha][coluna]

def obtem_coordenadas(campo, s):
    """
    A funcao obtem_coordenadas devolve um tuplo com todas as coordenadas
    correspondentes ao estado s, passado como argumento.
    (campo, string) -> tuplo
    """
    res = ()
    for linha in range(len(campo)):
        for coluna in range(len(campo[linha])):
            if campo[linha][coluna][0] == s:
                res += (cria_coordenada(chr(coluna + 65), linha + 1),)
            elif campo[linha][coluna][2] == s:
                res += (cria_coordenada(chr(coluna + 65), linha + 1),)
            elif eh_parcela_tapada(campo[linha][coluna]) and campo[linha][coluna][1] == s:
                res += (cria_coordenada(chr(coluna + 65), linha + 1),)

    return res

def obtem_numero_minas_vizinhas(campo, coordenada):
    """
    A funcao obtem_numero_minas_vizinhas devolve o numero de parcelas vizinhas
    da parcela na coordenada dada como argumento que escondem uma mina.
    (campo, coordenada) -> int
    """
    coordenadasVizinhas = obtem_coordenadas_vizinhas(coordenada)
    coordenadasMinadas = obtem_coordenadas(campo,'minadas')
    numMinasVizinhas = 0

    for coordenada in coordenadasMinadas:
        if coordenada in coordenadasVizinhas:
            numMinasVizinhas += 1

    return numMinasVizinhas

# Reconhecedores

def eh_campo(arg):
    """
    A funcao eh_campo recebe um arg e devolve True apenas se este for um campo.
    (universal) -> boolean
    """
    if type(arg) == tuple:
        for linha in range(len(arg)):
            if type(arg[linha]) != tuple:
                return False
            for parcela in arg[linha]:
                if not eh_parcela(parcela):
                    return False
        return True
    return False

def eh_coordenada_do_campo(campo, coordenada):
    """
    A funcao eh_coordenada_do_campo recebe um campo e uma coordenada e devolve True
    apenas se esta coordenada estiver dentro dos limites do campo dado.
    (campo, coordenada) -> boolean
    """
    ultimaColuna = obtem_ultima_coluna(campo)
    ultimaLinha = obtem_ultima_linha(campo)
    return ord(coordenada[0]) <= ord(ultimaColuna) and coordenada[1] <= ultimaLinha

# Teste

def campos_iguais(campo1, campo2):
    """
    A funcao campos_iguais recebe dois campos e devolve True apenas se estes forem
    campos e iguais.
    (campo, campo) -> boolean
    """
    if eh_campo(campo1) and eh_campo(campo2):
        if len(campo1) != len(campo2):
            return False
        for linha in range(len(campo1)):
            if len(campo1[linha]) != len(campo2[linha]):
                return False
            for parcela in range(len(campo1[linha])):
                if not parcelas_iguais(campo1[linha][parcela], campo2[linha][parcela]):
                    return False
        return True
    return False

# Transformador

def campo_para_str(campo):
    """
    A funcao campo_para_str devolve uma cadeia de caracteres que representa o campo
    de minas.
    (campo) -> string
    """
    campoStr = ''
    letras = '   '

    for i in range(ord(obtem_ultima_coluna(campo)) - 64):
        letras += chr(65 + i)
    letras += '\n'

    limiteSup = '  ' + '+' + (ord(obtem_ultima_coluna(campo)) - 64) * '-' + '+' + '\n'
    limiteInf = '  ' + '+' + (ord(obtem_ultima_coluna(campo)) - 64) * '-' + '+'
    campoStr += letras + limiteSup

    for i in range(obtem_ultima_linha(campo)):
        if i < 9:
            campoStr += "0" + str(i + 1) + "|"
        else:
            campoStr += str(i + 1) + "|"
        for j in range(ord(obtem_ultima_coluna(campo)) - 64):
            parcelaStr = parcela_para_str(obtem_parcela(campo, cria_coordenada(chr(j + 65), i + 1)))

            if parcelaStr == '?':
                num = obtem_numero_minas_vizinhas(campo,cria_coordenada(chr(j + 65), i + 1))

                if num == 0:
                    campoStr += ' '

                else:
                    campoStr += str(num)

            else:
                campoStr += parcelaStr

            if j + 1 == ord(obtem_ultima_coluna(campo)) - 64:
                campoStr += "|\n"

    campoStr += limiteInf
    return campoStr

# Funcoes de Alto Nivel

def coloca_minas(campo, coordenada, gerador, numMinas):
    """
    A funcao coloca_minas recebe um campo, uma coordenada, um gerador e o numero
    de minas a colocar no campo. Devolve o campo alterado, escondendo as minas de
    forma aleatoria, mas sem coincidir com a coordenada dada, bem como com as suas
    coordenadas vizinhas.
    (campo, coordenada, gerador, int) -> campo
    """
    while numMinas > 0:
        coordenadasVizinhas = obtem_coordenadas_vizinhas(coordenada)
        coordenadaAleatoria = obtem_coordenada_aleatoria(cria_coordenada(obtem_ultima_coluna(campo),obtem_ultima_linha(campo)), gerador)
        parcela = obtem_parcela(campo,coordenadaAleatoria)

        while coordenadaAleatoria in coordenadasVizinhas or coordenadaAleatoria == coordenada or eh_parcela_minada(parcela):
            coordenadaAleatoria = obtem_coordenada_aleatoria(
                cria_coordenada(obtem_ultima_coluna(campo), obtem_ultima_linha(campo)), gerador)
            parcela = obtem_parcela(campo, coordenadaAleatoria)

        esconde_mina(parcela)
        numMinas -= 1

    return campo

def limpa_campo(campo, coordenada):
    """
    A funcao limpa_campo recebe um campo e altera o estado da parcela na coordenada
    dada como argumento para limpa, caso esta parcela tenha uma mina escondida, o
    campo e devolvido caso contrario sao limpas todas as parcelas vizinhas tapadas
    que não tenham mina.
    (campo, coordenada) -> campo
    """
    limpa_parcela(obtem_parcela(campo, coordenada))

    if eh_parcela_minada(obtem_parcela(campo, coordenada)):
        return campo

    for coordenadaVizinha in obtem_coordenadas_vizinhas(coordenada):
        if eh_coordenada_do_campo(campo, coordenadaVizinha) and \
                not eh_parcela_minada(obtem_parcela(campo, coordenadaVizinha)) and \
                not eh_parcela_limpa(obtem_parcela(campo, coordenadaVizinha)):
            limpa_campo(campo, coordenadaVizinha)

    return campo


# Funcoes Adicionais

def jogo_ganho(campo):
    """
    A funcao jogo_ganho e uma funcao auxiliar que recebe um campo do jogo das
    minas e devolve True se todas as parcelas sem minas se encontram limpas,
    ou False caso contrario.
    (campo) -> boolean
    """
    desminadas = obtem_coordenadas(campo, 'desminadas')
    soma = 0
    for coordenada in desminadas:
        parcela = obtem_parcela(campo, coordenada)
        if eh_parcela_limpa(parcela):
            soma += 1

    if soma == len(desminadas):
        return True
    return False


def turno_jogador(campo):
    """
    A funcao turno_jogador recebe um campo e oferece ao jogador a opcao de escolher
    uma acao e uma coordenada. A funcao vai alterar o campo consoante a acao
    escolhida pelo jogador (limpar ou marcar). A funcao apenas devolve False caso
    o jogador tenha limpo uma parcela que continha uma mina.
    (campo) -> boolean
    """
    while True:
        escolhaAcao = input('Escolha uma ação, [L]impar ou [M]arcar:')
        if escolhaAcao == 'M' or escolhaAcao == 'L':
            break

    while True:
        coordenada = input('Escolha uma coordenada:')
        if len(coordenada) == 3 or ord('A') <= ord(coordenada[0]) <= ord('Z') or \
            ord('1') <= ord(coordenada[1]) <= ord('9') or \
            ord('1') <= ord(coordenada[2]) <= ord('9'):
            break

    if escolhaAcao == 'M':
        coordenadaM = str_para_coordenada(coordenada)
        alterna_bandeira(obtem_parcela(campo, coordenadaM))

        return True

    if escolhaAcao == 'L':
        coordenadaL = str_para_coordenada(coordenada)
        limpa_campo(campo, coordenadaL)
        parcela = obtem_parcela(campo, coordenadaL)

        if eh_parcela_minada(parcela):
            return False

        return True

def minas(coluna, linha, numParcelasMinadas, bits, seed):
    """
    A funcao minas e a funcao principal que permite jogar o jogo, recebe a ultima
    coluna e linha do campo, o numero de parcelas minadas, o tamanho e o estado
    inicial do gerador. Verifica os argumentos e devolve True caso o jogador ganhe
    o jogo e False caso contrario.
    (string, int, int, int, int) -> boolean
    """
    if (type(coluna) != str and len(coluna) != 1) or type(linha) != int:
        raise ValueError('minas: argumentos invalidos')
    if ord('A') >= ord(coluna) >= ord('Z'):
        raise ValueError('minas: argumentos invalidos')
    if 1 > linha > 99:
        raise ValueError('minas: argumentos invalidos')
    if (ord(coluna) - 64) * linha < numParcelasMinadas < 0:
        raise ValueError('minas: argumentos invalidos')
    if type(bits) != int or type(seed) != int:
        raise ValueError('minas: argumentos invalidos')
    if (bits != 32 or bits != 64) or seed <= 0:
        raise ValueError('minas: argumentos invalidos')
    if bits == 32 and seed > 2**32:
        raise ValueError('minas: argumentos invalidos')
    if bits == 64 and seed > 2 ** 64:
        raise ValueError('minas: argumentos invalidos')

    campo = cria_campo(coluna, linha)
    gerador = cria_gerador(bits, seed)
    coordenada = obtem_coordenada_aleatoria(cria_coordenada(coluna, linha), gerador)
    coloca_minas(campo, coordenada, gerador, numParcelasMinadas)

    pass
