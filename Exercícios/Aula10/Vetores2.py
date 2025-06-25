# Desenvolver um programa que efetue a leitura de dez elementos de um vetor.
# No final, apresente o total da soma de todos os elementos que sejam ímpares.

vetor = []
for i in range (10):
   num = int (input(f'{i}- Insira um numero: '))
   vetor.append(num)

soma = 0
for i in vetor:
  if i % 2 != 0: #se for impar, somar 
     #soma = soma + i
     soma += i
      
print (f'A soma dos números ímpares informados é : {soma}') 