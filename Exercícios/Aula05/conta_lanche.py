# O cardápio de uma lanchonete é o seguinte:

# Especificação     Código      Preço
# Cachorro quente   100         12,00
# Hambúrguer        103         12,00
# Cheeseburguer     104         13,00
# Refrigerante      105          8,00

# Escrever um programa que leia o código do item pedido, a quantidade e calcule o valor
# a ser pago por aquele lanche.
# A cada iteração deve perguntar se o usuário deseja continuar, a resposta for
# igual a 'n', o programa encerrará a execução.
# No final, deverá ser apresentado o valor total


# soma = 0
# while True:
#     codigo = int (input("Informe o código do produto: "))
#     quant = int (input("Informe a quantidade desse produto: "))
#     if codigo == 100 or codigo == 103:
#        soma = soma + (12.0*quant)
#     elif codigo == 104:
#        soma = soma + (13.0*quant)
#     elif codigo == 105:
#        soma = soma + (8.0*quant)
#     else:
#        print ("Código Inexistente.")
#     aux = input("Consumiu mais produtos? (S/N)")
#     if aux == "n" or aux == "N":
#       break

# print(f"O valor total da conta é : R$ {soma:.2f}")    
CACHORRO_QUENTE = 12
HAMBURGUER = 12
CHEESEBURGUER = 13
REFRIGERANTE = 8

vlorproduto = 0.0
soma = 0.0
while True:
    codigo = int (input("Informe o código do produto: "))
    if codigo == 100:
         vlorproduto = CACHORRO_QUENTE
    elif codigo == 103:
         vlorproduto = HAMBURGUER
    elif codigo == 104:
        vlorproduto = CHEESEBURGUER
    elif codigo == 105:
        vlorproduto = REFRIGERANTE
    else:
        print ("Código Inexistente.")
        aux = input("Consumiu mais produtos? (S/N)")
        if aux == "s" or aux == "S":
           continue

    quant = int (input("Informe a quantidade desse produto: "))
    soma = soma + (vlorproduto*quant) 
    aux = input("Consumiu mais produtos? (S/N)")
    if aux == "n" or aux == "N":
        break

print(f"O valor total da conta é : R$ {soma:.2f}")    



