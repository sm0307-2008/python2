# Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.
print('Digite as Notas do aluno; ')
nota1 = float(input ('Digite a primeira nota: '))
nota2 = float(input ('Digite a primeira nota: '))
media = (nota1+nota2)/2
print(f'esta é a media do aluno {media}')
if media >= 6:
    print('Este aluno está aprovado!')
else:
    print('Este aluno está reprovado!')
