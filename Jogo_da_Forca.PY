import random
from time import sleep

lista_palavras = ['IRAQUE', 'BELGICA', 'ZAMBIA']
lista_certa = list()
lista_digitadas = list()
chances = 6
erros = 0
acertos = 0

palavra = random.choice(lista_palavras)

print('\033[0;34m\n___JOGO DA FORCA____\033[m\n')
print('~=' *16)
for c in range (1,4):
    print(f'\033[0;3{c}m',c,'\033[m')
    sleep(0.5)
print('...')
sleep(0.5)
print('Já escolhi a palavra!')
sleep(1.5)
print(''' 
_______
|     |
|     L___
|
                     ''')
sleep(0.5)

total_palavras = len(palavra)
print(f'A palavra tem {total_palavras} letras')

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in lista_certa else "*"
    print(senha)
    print(f'Tentativas = {lista_digitadas}')
    print('Se a palavra aparecer completa, aperte \033[0;36m"Enter"\033[m para finalizar')
    sleep(0.7)
    tentativa = input("\nDigite uma letra:").upper().strip()
    if tentativa.isdigit():
        print('\033[0;31mVocê digitou um número?\033[m')
        sleep(0.5)
    if tentativa in lista_digitadas:
        print('Você já digitou essa letra')
        continue
    else:
        lista_digitadas += tentativa
        if tentativa in palavra:
            lista_certa += tentativa
            acertos += 1
            print('Você acertou uma letra')
            print(f'Acertos: {acertos}')
            sleep(0.8)
        else:
            chances -= 1
            erros +=1
            print(f'Você errou... Tens ainda {chances} chances')
            sleep(0.5)
    if erros == 1:
        print(''' 
_______
|     |
|     L___ 
|       O
                     ''')
        print('\033[0;31mCABEÇA\033[m')
        sleep(0.5)
    elif erros == 2:
        print(''' 
_______
|     |
|     L___ 
|       O
        |                 ''')
        print('\033[0;31mTRONCO\033[m')
        sleep(0.5)
    elif erros == 3:
        print(''' 
_______
|     |
|     L___ 
|       O
        |/                 ''')
        print('\033[0;31mBRAÇO ESQUERDO\033[m')
        sleep(0.5)
    elif erros == 4:
        print(''' 
_______
|     |
|     L___ 
|       O
       \|/                 ''')
        print('\033[0;31mBRAÇO DIREITO\033[m')
        sleep(0.5)
       
    elif erros == 5:
        print(''' 
_______
|     |
|     L___ 
|       O
       \|/                 
       /''')
        print('\033[0;31mPERNA DIREITA\033[m')
        sleep(0.5)
    elif erros == 6:
        print(''' 
_______
|     |
|     L___ 
|       O
       \|/                 
       / \ ''')
        print('\033[0;31mPERNA ESQUERDA... ENFORCADO!\033[m')
        sleep(0.5)
    if chances == 0:
        print('\nVocê \033[0;31mPERDEU!!!\033[m')
        print(f'A palavra era: {palavra}')
        sleep(0.7)
        print('\nAté a próxima!')
        break
    if senha == palavra:
        print('\nVocê \033[0;36mCONSEGUIU!\033[m')
        print(f'A palavra era {palavra}')
        print('Parabéns, até a próxima!')
        break
print('\nFim do programa')
        
    
    






