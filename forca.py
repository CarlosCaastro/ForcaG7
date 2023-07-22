import random
import os
import error

def escolher_palavra_aleatoria(arquivo):
    with open(arquivo, 'r') as file:
        palavras = file.readlines()
        palavra_aleatoria = random.choice(palavras).strip().lower()
    return palavra_aleatoria

def inicializar_palavra_adivinhada(palavra):
    return ''.join(['_'] * len(palavra))

def mostrar_forca(erros):
    if erros == 0:
        print(error.erro_0)
    elif erros == 1:
        print(error.erro_1)
    elif erros == 2:
        print(error.erro_2)
    elif erros == 3:
        print(error.erro_3)
    elif erros == 4:
        print(error.erro_4)
    elif erros == 5:
        print(error.erro_5)
    else:
        print(error.erro_6)

def mostrar_letras_escolhidas(letras):
    print("Letras escolhidas:", " ".join(letras))

def mostrar_palavra_adivinhada(palavra_adivinhada):
    print("Palavra:", " ".join(palavra_adivinhada))

def jogar_novamente():
    resposta = input("Deseja jogar novamente? (s/n): ")
    return resposta.lower() == 's'

def jogo_da_forca():
    print("Bem-vindo ao Jogo da Forca do Grupo 07!")

    while True:
        tipo_escolhido = input("Escolha o tipo (Frutas, Objetos, ...) ou digite 'sair' para encerrar o programa: ").lower()

        if tipo_escolhido == 'sair':
            print("Obrigado por jogar! Encerrando o programa.")
            return

        arquivo = f"palavras/{tipo_escolhido}.txt"

        if os.path.exists(arquivo):
            break
        else:
            print(f"O tipo '{tipo_escolhido}' não existe. Escolha novamente!")

    palavra = escolher_palavra_aleatoria(arquivo)
    palavra_adivinhada = list(inicializar_palavra_adivinhada(palavra))
    letras_escolhidas = []
    erros = 0
    
    while True:
        mostrar_forca(erros)
        mostrar_letras_escolhidas(letras_escolhidas)
        mostrar_palavra_adivinhada(palavra_adivinhada)

        letra = input("Escolha uma letra: ").lower()

        if letra in letras_escolhidas:
            print("Você já escolheu essa letra. Tente novamente!")
            continue

        letras_escolhidas.append(letra)
        
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_adivinhada[i] = letra

            if '_' not in palavra_adivinhada:
                print("Parabéns! Você acertou a palavra:", palavra)
                break
        else:
            erros += 1

            if erros == 6:
                mostrar_forca(erros)
                print("Você perdeu! A palavra era:", palavra)
                break
            
    if jogar_novamente():
        jogo_da_forca()
    else:
        print("Obrigado por jogar!") 
        
jogo_da_forca()