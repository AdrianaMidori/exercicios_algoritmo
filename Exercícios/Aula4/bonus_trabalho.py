# A empresa XKW concedeu um bônus de 20% do valor do salário a todos os funcionários
# com tempo de trabalho na empresa igual ou superior a 5 anos e de 10% aos demais.
# Faça um programa que receba o salário e o tempo de serviço de um funcionário, calcule e
# mostre o valor do bônus recebido por ele.

salario = float (input("Informe o salário do funcionário: "))
tempo = int(input("Informe o tempo de trabalho na empresa em anos: "))
bonus = 0.0
if tempo >= 5:
    bonus = salario*0.2
else:
    bonus = salario*0.1

print(f"O valor do bonus desse funcionário é de R$ {bonus:.2f}") 



