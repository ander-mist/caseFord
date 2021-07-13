asc = {
    "H": "65",
    "G": "66",
    "C": "67",
    "M": "68",
    "A": "69",
    "F": "70",
}

def divide_por_dois(lista_de_numeros):
    for index, num in enumerate(lista_de_numeros):
        numero_inteiro = int(num / 2)
        lista_de_numeros[index] = str(numero_inteiro)
    return lista_de_numeros

def transforma_numero_em_letra(numeros):
    numeros_convertidos = list()
    flag = True
    for num in numeros:
        for letra in asc:
            if num == asc[letra]:
                flag = False
                numeros_convertidos.append(letra)
        if flag:
            numeros_convertidos.append(num)
        flag = True
    return numeros_convertidos

def descriptografa(lista_de_numeros):
    numeros_divididos = divide_por_dois(lista_de_numeros)
    numeros_convertidos = transforma_numero_em_letra(numeros_divididos)
    codigo_descriptografado = ''.join(numeros_convertidos)
    return codigo_descriptografado