# ------------------ FUNCOES ------------------
def usuario_escolhe_jogada(n,m):
    usuario_retira = int(input("Quantas peças você vai tirar? "))
    if (usuario_retira > n or usuario_retira > m):
        print("\nOops! Jogada inválida! Tente de novo.\n")
        return usuario_retira
    else:
        while(usuario_retira <= m):
            n = n - usuario_retira
            print(f"Voce tirou {usuario_retira} peças.")
        return n

# def computador_escolhe_jogada(n,m):
#     if (usuario_escolhe_jogada(n,m)):

#     return

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if(n % (m+1) == 0):
        print("Voce começa!")
        usuario_escolhe_jogada(n,m)
    else:
        print("Computador começa!")
        computador_escolhe_jogada(n,m)

# ------------------ INPUTS ------------------

print("Bem-vindo ao jogo do NIM! Escolha: \n")

modo_jogo = int(input("1 - para jogar uma partida isolada \n"
"2 - para jogar um campeonato "))

if (modo_jogo == 1 or modo_jogo == 2 ):
    if (modo_jogo == 1):
        print("\nVoce escolheu uma partida isolada!\n\n"
        "**** Rodada 1 ****\n")
        # print(jogo_solo())
    else:
        print("\nVoce escolheu um campeonato!\n\n"
        "**** Rodada 1 ****\n")
        print(partida())
else:
    print("Opção inválida")
    exit()

