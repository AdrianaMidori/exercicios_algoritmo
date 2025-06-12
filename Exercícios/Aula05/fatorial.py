#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5! = 5.4.3.2.1 = 120

num = int(input("Informe um número inteiro: "))

fator = 1
for i in range(num+1):
    if i > 0:
       fator = fator * i

print(f"O fatorial de {num} é : {fator}")   


#O mesmo fatorial usando o range com mais parâmetros
fator = 1
saida = ''
for i in range(num, 0, -1):

    fator = fator * i
    saida = saida + str(i)
    if i != 1:
        saida = saida + '.'

print(f"Msg 2 => O fatorial de {num} é : {saida} = {fator}")      

