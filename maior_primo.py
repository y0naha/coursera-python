def éPrimo(n):
    cont = 2
    while (n != cont):
        if (n % cont == 0):
            cont += 1
            return False
            # print("Não é primo")
        else:
            cont += 1
    return True


# print(éPrimo(100))
# print(éPrimo(7))
# print(éPrimo(9))
# print(éPrimo(97))
# print(éPrimo(234))


def maior_primo(k):
    i = 2
    if (k >= 2):
        while (k != i):
            if éPrimo(i):
                ultimoPrimo = i
                i += 1
            else:
                i += 1
        return ultimoPrimo
    else:
        return print("Número inválido")

# print(maior_primo(100))
