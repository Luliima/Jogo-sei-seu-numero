


import random

def adivinhe_numero():
    print("Bem vindo, irei adivinhar o numero que está pensando!")
    print("Pense em um número entre 1 e 100 que irei analisar.")

    limite_inferior = 1
    limite_superior = 100
    tentativas = 0
    resposta = None

    while resposta != 'certo':
        palpite = random.randint(limite_inferior, limite_superior)
        print("Eu acho que o número é:", palpite)
        resposta = input("Digite 'c' se o palpite estiver correto, 'm' se o número é menor, 'a' se o número é maior: ").lower()

        if resposta == 'menos':
            limite_superior = palpite - 1
        elif resposta == 'mais':
            limite_inferior = palpite + 1

        tentativas += 1

    print(f"Eu acertei! O número é {palpite}.")
    print(f"Levou {tentativas} tentativas.")

adivinhe_numero()