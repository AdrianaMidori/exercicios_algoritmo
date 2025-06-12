# Construir um programa que efetue o cálculo do 
# salario líquido de um professor. Para fazer este programa,
# você deverá possuir alguns dados, tais como: valor da hora aula,
# número de horas trabalhadas no mês e percentual de desconto do INSS.
# Em primeiro lugar, deve estabelecer qual será o seu salário bruto para
# efetuar o desconto a ter o valor do salário líquido


vlrHoraAula = float(input("Informe o valor da hora aula: "))
horasTrabalhadas = float(input("Informe a quantidade de horas trabalhadas: "))
descInss = float(input("Informe o percentual de desconto do INSS: "))

salarioBruto = vlrHoraAula * horasTrabalhadas
salarioLiquido = salarioBruto - (salarioBruto*(descInss/100))

print(f"O valor do salario bruto é {salarioBruto}")
print(f"O salário líquido é {salarioLiquido}")

