#7) Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores
total_eleitores = int(input('Numero total de eleitores: '))
voto_branco = int(input('Numero total de votos brancos: '))
voto_nulo = int(input('Numero total de votos nulos: '))
voto_valido = int(input('Numero total de votos validos: '))

print('porcetagem branco: ',voto_branco/total_eleitores*100,'%')
print('porcetagem nulo: ', voto_nulo/total_eleitores*100,'%')
print('porcetagem valida: ', voto_valido/total_eleitores*100,'%')
