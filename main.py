from functions import escolher_palavra, mostrar_palavra , pedir_letra , atualizar_palavra , escolher_dificuldade


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
