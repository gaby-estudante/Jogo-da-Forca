# FUNÇÕES

import random

# Lista de palavras separadas por nível de dificuldade e categoria
palavras = {
    "facil": {
        "animal": ["gato", "pato", "rato", "tatu", "lobo"],
        "comida": ["bolo", "pao", "uva", "ovo", "mel"],
        "objeto": ["mesa", "bola", "dado", "copo", "porta"],
        "tecnologia": ["mouse", "tecla", "tela", "cabo", "rede"],
        "pais": ["chile", "peru", "china", "india", "cuba"]
    },

    "medio": {
        "animal": ["tigre", "zebra", "cobra", "panda", "foca"],
        "comida": ["pizza", "feijao", "macarrao", "lasanha", "biscoito"],
        "objeto": ["janela", "cadeira", "garrafa", "espelho", "mochila"],
        "tecnologia": ["python", "codigo", "classe", "objeto", "servidor"],
        "pais": ["brasil", "canada", "mexico", "franca", "italia"]
    },

    "dificil": {
        "animal": ["ornitorrinco", "chimpanze", "crocodilo", "rinoceronte", "hipopotamo"],
        "comida": ["parmegiana", "estrogonofe", "cappuccino", "croissant", "hamburguer"],
        "objeto": ["helicoptero", "microscopio", "refrigerador", "calculadora", "ventilador"],
        "tecnologia": ["algoritmo", "criptografia", "processador", "compilador", "programacao"],
        "pais": ["australia", "argentina", "alemanha", "portugal", "noruega"]
    }
}

# Pede pro usuário escolher um nível de dificuldade
def escolher_dificuldade():
    while True:
        nivel = input("Escolha uma dificuldade (facil / medio / dificil): ").lower()

        if nivel in palavras:
            return nivel
        else:
            print("Dificuldade inválida.")


# Pede pro usuário escolher uma categoria
def escolher_categoria(dificuldade):

    categorias = palavras[dificuldade].keys()

    print("\nCategorias disponíveis:")
    for c in categorias:
        print("-", c)

    while True:
        categoria = input("Escolha uma categoria: ").lower()

        if categoria in palavras[dificuldade]:
            return categoria
        else:
            print("Categoria inválida.")


# Escolhe uma palavra aleatoriamente
def escolher_palavra(dificuldade, categoria):
    return random.choice(palavras[dificuldade][categoria])


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
            
        except ValueError as erro:
            print("Erro:", erro)


# Mostra como está a palavra descoberta
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

# CODIGO MAIN

def jogar():

    print("====== JOGO DA FORCA ======")

    dificuldade = escolher_dificuldade()
    categoria = escolher_categoria(dificuldade)

    palavra = escolher_palavra(dificuldade, categoria)

    letras_descobertas = ["_"] * len(palavra)
    letras_usadas = set()

    tentativas = 0
    if (dificuldade) == "facil":
        tentativas = 5
    elif (dificuldade)  == "medio":
        tentativas = 8
    elif (dificuldade) == "dificil":
        tentativas = 10

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

    if "_" not in letras_descobertas:
        print("\nParabéns! Você ganhou! :)")
    else:
        print("\nNão foi dessa vez! :(")

    print("A palavra era:", palavra)


jogar()
