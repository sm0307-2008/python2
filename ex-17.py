#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu)

anoatual = int(input('Qual o ano atual?: '))
anodonascimento = int(input('Digite o ano que você nasceu: '))

if anoatual - anodonascimento >= 16:
    print('Pode votar')
else:
    print('Não pode votar')
