# lista = [7, 3, 33, 12, 3, 3, 3, 7, 12, 100]

def remove_repetidos(lista):
    novaLista = []
    for i in lista:
        if i not in novaLista:
            novaLista.append(i)
        i += 1
        novaLista.sort()
    return novaLista

# print(remove_repetidos(lista))
