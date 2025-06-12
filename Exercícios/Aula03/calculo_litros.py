# Efetuar o cálculo da quantidade de litros de combustível gasta em uma viagem,
# utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo,
# o usuário deve fornecer o tempo gasto (TEMPO) e a velocidade média (VELOCIDADE)
# durante a viagem. Desta forma, será possível obter a distância percorria com a fórmula
# DISTANCIA = TEMPO * VELOCIDADE.
# Possuindo o valor da distância, basta calcular a quantidade de litros de combustível
# utilizada na viagem com a fórmula :
# LITROS_USADOS = DISTANCIA / 12
# Ao final, o programa deve apresentar os valores da velocidade média (VELOCIDADE),
# tempo gasto na viagem (TEMPO), a distancia percorrida (DISTANCIA) e a quantidade de litros (LITROS_USADOS) 
# utilizada na viagem

tempo = float(input('Informe o tempo de duração da viagem em horas: '))
velocidade_media = float(input('Informe a velocidade média da viagem em Km/h: '))
distancia = tempo * velocidade_media
litros_usados = distancia / 12
print(f'A velocidade média durante a viagem foi de  {velocidade_media} Km/h')
print(f'O tempo gasto na viagem foi de: {tempo}')
print(f'Distancia percorrida: {distancia} Km')
#delimitando a quantidade de casas decimais depois da virgula
print(f'Quantidade de litros utilizados na viagem: {litros_usados:.3f}')
