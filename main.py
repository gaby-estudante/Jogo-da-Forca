# ------------------- FUNÇÕES -----------------

import random

# Lista de palavras separadas por nível de dificuldade
palavras = { # MELHORIA: separar por categorias (ex: nome, comida, animal, país)
    "facil": [
        "gato", "casa", "bola", "livro", "mesa",
        "porta", "dado", "pato", "fogo", "vento"
    ],

    "medio": [
        "python", "codigo", "classe", "objeto", "rede",
        "dados", "servidor", "memoria", "interface", "sistema"
    ],

    "dificil": [
        "algoritmo", "criptografia", "processador",
        "compilador", "inteligencia",
        "programacao", "tecnologia", "seguranca",
        "variavel", "aplicacao"
    ]
}

# Pede pro usuário escolher um nível de dificuldade
def escolher_dificuldade():
    while True:
        nivel = input("Escolha uma dificuldade para iniciar (facil / medio / dificil): ").lower()

        if nivel in palavras:
            return nivel
        else:
            print("Dificuldade inválida.")


# Escolhe uma palavra aleatoriamente
def escolher_palavra(dificuldade):
    return random.choice(palavras[dificuldade])


# Pede uma letra ao usuário
def pedir_letra(letras_usadas):
    while True:
        try:
            letra = input("Digite uma letra: ").lower()

            if len(letra) != 1:
                raise ValueError("Digite apenas uma letra por vez.")

            if not letra.isalpha():
                raise ValueError("Digite apenas letras.")

            if letra in letras_usadas:
                raise ValueError("Você já usou essa letra.")

            return letra
            
        except ValueError as erro: # Tratamento de exceções
            print("Erro:", erro)


# Mostra como está a palavra descobrida até o momento
def atualizar_palavra(palavra, letras_descobertas, letra):
    acertou = False

    for i in range(len(palavra)):
        if palavra[i] == letra:
            letras_descobertas[i] = letra
            acertou = True

    return acertou

def mostrar_palavra(letras_descobertas):
    print("Palavra:", " ".join(letras_descobertas))

#--------------------------------------------------------------------

# MAIN

def jogar():

    print("====== JOGO DA FORCA ======")

    dificuldade = escolher_dificuldade()
    palavra = escolher_palavra(dificuldade)

    letras_descobertas = ["_"] * len(palavra)
    letras_usadas = set()

    tentativas = 5 # POSSIVEL MELHORIA: CADA NIVEL TER UM LIMITE DE TENTATIVAS

    while tentativas > 0 and "_" in letras_descobertas:

        print("\nTentativas restantes:", tentativas)
        print("Letras usadas:", " ".join(sorted(letras_usadas)))

        mostrar_palavra(letras_descobertas)

        letra = pedir_letra(letras_usadas)

        letras_usadas.add(letra)

        acertou = atualizar_palavra(palavra, letras_descobertas, letra)

        if acertou:
            print("Boa! Você acertou uma letra.")
        else:
            tentativas -= 1
            print("Errou!")

    # Mensagem para caso de ganhar ou perder
    if "_" not in letras_descobertas:
        print("\nParabéns! Você ganhou! :)")
    else:
        print("\nNão foi dessa vez! :(")

    # Mostra a palavra completa
    print("A palavra era:", palavra)


jogar()