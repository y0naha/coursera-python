n = int(input("Digite o valor de n: "))
i = 1
j = 1

while j <= n:
    if (i % 2 != 0):
        print(i)
        i = i + 1
        j = j + 1
    else:
        i = i + 1
