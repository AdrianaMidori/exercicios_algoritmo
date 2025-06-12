# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual número ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50

num = int(input("Informe o número que deseja gerar a tabuada: "))

for i in range(10):
    contaux = i + 1
    mult = num * contaux
    print(f"{num} x {contaux} = {mult}")

#Outra forma de fazer usando parâmetros no range    

for i in range(1,11) :
    mult = num * i   
    print(f"Outro range : {num} x {i} = {mult}") 
