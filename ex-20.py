#(considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.

hora1 = int(input("qual a hora de inicio do jogo: "))
hora2 = int(input('qual a hora de termino do jogo: '))

if hora1 > hora2:
    duracao = 24- (hora1-hora2)
else:
    duracao = hora2-hora1
print(f'a duração do jogo é {duracao}h')
