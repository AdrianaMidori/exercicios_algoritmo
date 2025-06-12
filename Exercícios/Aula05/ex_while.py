# Um programa que fará a leitura de números que representará a idade de pessoas
# ao final do programa, o mesmo deverá informar o somatório das idades,
# o número de pessoas e a média das idades

soma = 0
numpessoas = 0
while True:
    idade = int(input("Informe a sua idade: "))  
    soma = soma + idade
    numpessoas = numpessoas + 1 
    resp = input("Deseja continuar? (s/n)")
    if resp == 'n' or resp == 'N':
        break
    

media = soma / numpessoas
print (f"A soma das idades é : {soma}")
print (f"O número de pessoas é {numpessoas}")
print (f"A média das idades é : {media:.2f}")

