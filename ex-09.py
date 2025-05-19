#9) O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor. 

#valor inical do carro
custo = 25000
print(f'Seu carro na fábrica custa {custo}')

#valor com os cálculos
custofinal = custo*(1+(0.45+0.28)) 

#resultado final
print(f'Seu custo final é R${custofinal}')
