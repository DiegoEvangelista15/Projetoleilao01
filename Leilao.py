import os

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')



print('Bem vindo ao Leilao!!!\n')

aposta = {}
aposta_finalizada = False

def maior_valor(aposta_totais):
    maior_valor = 0
    for i in aposta_totais:
        aposta_qtd = aposta_totais[i]
        if aposta_qtd > maior_valor:
            maior_valor = aposta_qtd
            winner = i
    print(f'O vencedor foi {winner} com a aposta de R$ {maior_valor}')


while not aposta_finalizada:
    nome = input('Qual o nome do apostador?\n')
    aposta_valor = (input('Qual sua aposta?\nR$ '))
    if aposta_valor.isdigit():
        aposta_valor = float(aposta_valor)
        aposta[nome] = aposta_valor
        apostadores_continuar = input('Existem outros apostadores? Digite sim ou nao.\n')
        if apostadores_continuar == 'nao':
            aposta_finalizada = True
            maior_valor(aposta)
        elif apostadores_continuar == 'yes':
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
    else:
        print('Voce tem que digitar um numero!!!')
