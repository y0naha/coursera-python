largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

linha = 0
coluna = 0
while linha < altura:
    while coluna < largura:
        if linha == 0 or linha == (altura-1) or coluna==0 or (coluna == largura-1):
            print("#", end = "")
        else:
            print(" ", end = "")
        coluna = coluna + 1
    linha += 1
    print()
    coluna = 0