largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))

linha = 1
coluna = 1
while linha <= altura:
    while coluna <= largura:
        retangulo = (linha*coluna)
        retangulo = "#"
        print(retangulo,end = "")
        coluna = coluna + 1
    linha += 1
    print()
    coluna = 1
