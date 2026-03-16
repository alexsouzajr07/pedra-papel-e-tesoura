import random

opcoes = ["pedra", "papel", "tesoura"]

while True:
    jogador = input("Escolha pedra, papel ou tesoura (ou 'sair'): ")

    if jogador == "sair":
        print("Fim do jogo!")
        break

    computador = random.choice(opcoes)

    print("Computador escolheu:", computador)

    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você venceu!")
    else:
        print("Você perdeu!")

    print()