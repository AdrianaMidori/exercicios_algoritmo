# Um programa que fará a leitura da idade de uma pessoa
# e irá informar se é
#    Criança : 0-12 
#    Adolescente: 13-17 anos
#    Adulto: 18-64 anos
#    Idoso: 65 anos ou mais.

idade =int (input("Informe a idade: "))

if idade>= 0 and idade <=12:
    print ("Criança")

elif idade >=13 and idade <= 17:
    print ("Adolescente")

elif idade >= 18 and idade <= 64:
    print ("Adulto")

elif idade >= 65:
    print ("Idoso")   
else:
    print("Informação inválida")    