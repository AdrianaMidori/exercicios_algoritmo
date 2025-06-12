valor = float(input('Informe o valor da prestação: '))
taxa = float(input('Informe a taxa de juros: '))
tempo = int(input('Informe a quantidade dias em atraso: '))
acrescimo = (valor * taxa/100) * tempo
prestacao = valor + (acrescimo)
print(f'O valor do acrescimo é de : {acrescimo:.2f}')
print(f'O valor da prestação acrescida dos juros é de {prestacao:.2f}')