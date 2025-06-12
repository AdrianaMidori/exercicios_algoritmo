# Tendo como dados de entrada a altura em metros e o sexo de uma pessoa ("M" masculino e "F" feminino),
# construa um programa que calcule seu peso ideal, utilizando as seguintes fórmulas:
# - para homens: (72.7*h)-58
# - para mulheres: (62.1*h)-44.7

genero = input("Informe o gênero da pessoa ('M') para Masculino e ('F') para Feminino ")
h = float(input("Informe a altura : "))
if genero == 'M' or genero == 'm':
    pesoideal = (72.7*h) -58
    print(f"O peso ideal para um homem da sua altura é {pesoideal:.2f}")
elif genero == 'F' or genero == 'f': 
    pesoideal = (62.1*h) -44.7
    print(f"O peso ideal para uma mulher da sua altura é {pesoideal:.2f}")
else:
    print("Informação inválida")   

