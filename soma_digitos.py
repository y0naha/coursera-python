soma = 0
numero = int(input("Digite um número inteiro: "))
while(numero > 0):
    soma = soma + (numero % 10) 
    numero = (numero // 10)
print(soma)