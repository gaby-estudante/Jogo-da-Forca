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
        nivel = input("Escolha dificuldade (facil / medio / dificil): ").lower()

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

        except ValueError as erro:
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
