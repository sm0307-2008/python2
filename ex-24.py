#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

print('login')

numero_conta = int(input('Digite teu número de dados: '))
saldo = float(input('Digite teu saldo: '))
debito= float(input('Digite teu debito: '))
credito = float(input('Digite teu crédito: '))

saldo_atual =  saldo - (debito + credito)
print(saldo_atual)
if saldo_atual >= 0:
    print('saldo positivo')
else:
    print('saldo negativo')
