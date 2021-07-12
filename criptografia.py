codigo = '1HGCM82633A004352'

asc = {
    "H": "65",
    "G": "66",
    "C": "67",
    "M": "68",
    "A": "69",
    "F": "70",
}


def transformaNumeroEmLetra(codigo):
    cripto = list()
    for i in codigo:
        for j in asc:
            cripto.append(i)
            if i == j:
                i = j
    return cripto

if __name__ == 'main':
    print('teste')