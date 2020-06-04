import random
import os

"""FUNÇÕES"""
def desenha_caveira():
    print("             **********************                 ")
    print("            *                      *                ")
    print("            *   **            **   *                ")
    print("            *   **            **   *                ")
    print("            *                      *                ")
    print("            *                      *                ")
    print("            *          O           *                ")
    print("            *                      *                ")
    print("            *                      *                ")
    print("            *     ************     *                ")
    print("            *                      *                ")
    print("             **********************                 ")
def desenha(erros):
    if erros == 0:
        print()
        print("  |-------|")
        print("  |       | ")
        print("  |         ")
        print("  |         ")
        print("  |         ")
        print("  |         ")
        print("__|__        ")
        print()
    elif erros == 1:
        print()
        print("  |-------|")
        print("  |       | ")
        print("  |       O  ")
        print("  |         ")
        print("  |         ")
        print("  |         ")
        print("__|__        ")
        print()
    elif erros == 2:
        print()
        print("  |------| ")
        print("  |      | ")
        print("  |      O ")
        print("  |      | ")
        print("  |      | ")
        print("  |       ")
        print("__|__     ")
        print()
    elif erros == 3:
        print()
        print("  |------| ")
        print("  |      | ")
        print("  |      O ")
        print("  |      |\\ ")
        print("  |      | ")
        print("  |        ")
        print("__|__     ")
        print()
    elif erros == 4:
        print()
        print("  |------| ")
        print("  |      | ")
        print("  |      O ")
        print("  |     /|\\ ")
        print("  |      | ")
        print("  |       ")
        print("__|__     ")
        print()
    elif erros == 5:
        print()
        print("  |------| ")
        print("  |      | ")
        print("  |      O ")
        print("  |     /|\\ ")
        print("  |      | ")
        print("  |       \\ ")
        print("__|__     ")
        print()
    
    elif erros == 6:
        print()
        print("  |------| ")
        print("  |      | ")
        print("  |      O ")
        print("  |     /|\\ ")
        print("  |      | ")
        print("  |     / \\ ")
        print("__|__     ")
        print()
    
        

def sorteia_palavra():
    with open('palavras.txt', 'r') as arquivo:
        """ ou: arquivo = open('palavras.txt', 'r') """
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())
        arquivo.close()
        
        num = random.randrange(0,len(palavras))
        return palavras[num]
    """Sorteia uma palavra que está no arquivo palavras.txt"""
    
def acha_letra(chute, palavra_Secreta, letras_acertadas):
        posicao = 0
        for letra in palavra_secreta:
            if(letra == chute.upper()):
                letras_acertadas[posicao] = letra
            posicao += 1
            """Acha a posição da letra encontrada"""
def limpa_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
"""CÓDIGO"""
letras_erradas = []
palavra_secreta = list(sorteia_palavra().upper())
letras_acertadas = []
for letra in palavra_secreta:
    letras_acertadas.append("_")
acertou = False
enforcou = False
erros = 0
print('\n')
print('*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('*********************************')


while(not acertou and not enforcou) :
    desenha(erros)
    print("\n\n",letras_acertadas, "\n")
    chute = input("Digite uma letra: ")

    limpa_tela()
    
    if (chute.upper() in palavra_secreta):
        print("Achei {}" .format(chute.upper()))
        acha_letra(chute, palavra_secreta, letras_acertadas)
    else:
        letras_erradas.append(chute.upper())
        print("Não achei: {}" .format(letras_erradas))
        erros += 1
    
    acertou = "_" not in letras_acertadas
    enforcou = erros == 6

if(acertou):
    desenha(erros)
    print('Você ganhou!!')
    print("Fim de jogo!")
else:
    desenha(erros)
    print('Você perdeu!!')
    print("Fim de jogo!")
    desenha_caveira()

