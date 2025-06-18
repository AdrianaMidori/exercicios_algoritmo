#Programa que solicita a idade e informa se a pessoa é maior de idade
idade = int(input("Informe a sua idade:"))
if idade >= 18:
  print ("Maior de idade")
  print ("Ainda dentro do if")
else:
  print("Menor de idade.")  
print("Fim, fora do if")
