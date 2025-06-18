#Faça um programa que realizará a leitura de duas notas de um aluno, calcule a média e informe se o aluno está aprovado
#se a média for maior ou igual a 7 senão informe que o aluno está reprovado. A média também deverá ser exibida em ambos os casos.

# Altere o programa para pedir uma nota extra de recuperação e refazer a media com a nova nota e a media anterior

nota1 = float (input("Informe a primeira nota do aluno: "))
nota2 = float (input("Informe a segunda nota do aluno: "))
media = (nota1+nota2)/2

print(f"A média do aluno é {media:.2f}")
if media >=7: 
   print("Aluno aprovado.")
else:
   #print("Aluno reprovado.")
   #Fluxo antigo
   recuperacao = float(input("Nota de recuperação: "))
   novamedia = (media + recuperacao)/2
   if novamedia >= 5:
       print ("Aprovado")
   else:
      print("Reprovado")
   print(f'A média final é {novamedia:.2f}')