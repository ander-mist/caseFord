codigo = '1HGCM82633A004352'

asc = {
    "H": "65",
    "G": "66",
    "C": "67",
    "M": "68",
    "A": "69",
    "F": "70",
}

def multiplica_por_dois(codigo_com_numeros):
    codigo_multiplicado = list()
    for num in codigo_com_numeros:
        codigo_multiplicado.append(int(num) * 2)
    return codigo_multiplicado


def transformaLetraEmNumero(codigo):
    cripto = list()
    flag = True
    for i in codigo:
        for j in asc:
            if i == j:
                flag = False
                cripto.append(asc[j])
        if flag != False:
            cripto.append(i)
        flag = True 
    return cripto

def criptografa(codigo):
    codigo_com_numeros = transformaLetraEmNumero(codigo)
    numeros_multiplicados = multiplica_por_dois(codigo_com_numeros)
    return numeros_multiplicados
