# Desenvolver um programa que efetue a leitura de dez elementos em um vetor.
# Construir um vetor B de mesmo tipo, observando a seguinte lei de formação:
# Se o valor do elemento for par, o valor deverá ser multiplicado por 5.
# Sendo ímpar, deverá ser somado com 5
# Ao final mostrar o conteúdo do vetor B.    

vetorA= []
vetorB= []

# for i in range(10):
#     num = int(input('Informe um número inteiro: '))
#     vetorA.append(num)
#     #se for par, multiplicar por 5
#     if vetorA[i] % 2 == 0:
#         vetorB.insert(i, vetorA[i] * 5)
#     else: #se for impar, somar com 5
#        vetorB.insert(i, vetorA[i] + 5)

for i in range(10):
   num = int(input('Informe um número inteiro: '))
   vetorA.append(num)

#A variável j receberá o conteúdo do vetorA
for j in vetorA:
   #se for par, multiplicar por 5
   if j % 2 == 0:
      resultado = j * 5
   else: #se for impar, somar com 5
      resultado = j + 5
   vetorB.append(resultado)

for j in vetorB:
    print(j)

#print (f"Valores do vetor A: {vetorA}" )
#print (f"Valores do vetor B: {vetorB}")           