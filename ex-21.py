#A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que didere que o mês possua 4 semanas exatas).everá ser acrescido das horas extras, caso tenham sido trabalhadas (cons


horas_trabalhadas = int(input('Qual o números de horas trabalhadas: '))
horas_extras = horas_trabalhadas - 40

if horas_trabalhadas > 40:
    pg1 = (horas_trabalhadas-horas_extras)*10
    pg2 = horas_extras*10*1.5
    print((pg1+pg2)*4)
else:
    print(horas_trabalhadas*4)
