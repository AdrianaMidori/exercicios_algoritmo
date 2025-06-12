# contador vai de 0 a 4
#for contador in range(5):
#   print(contador)
   

soma = 0
for contador in range(5):
    numero = float(input("Informe o número: "))
    soma = soma + numero

print(f"A soma é {soma}")    

#outra forma do range
for contador in range(7, 2, -1):
    print(contador)