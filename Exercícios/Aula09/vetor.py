nome = "Luis"
#Criando um vetor
vetor = [] #Iniciando o vetor vazio

#Criando um vetor com valores pré-cadastrados
frutas = ['banana', 'maçã', 'pera'] 

#Adicionando valores
vetor.append("Paulo")
frutas.append("Mamão")
frutas.append(nome)
frutas.append(45)
frutas.append(4.70)
frutas.insert(1,"açai")

print(vetor)
print(frutas)

fruta = input("Informe o nome de uma fruta: ")
frutas.append(fruta)

#Remove pelo valor
frutas.remove("Luis")
frutas.remove(45)
frutas.remove(4.7)

#Remove a ultima posição de frutas
frutas.pop()

#Remove pela posição
frutas.pop(0)

#O python vai tentar fazer uma operação, utiliznado essa função não vai dar erro, vai para o except
try:
    frutas.remove("João") #Não existe o valor "João"
except:
    print("Informação não encontrada.")

#Ordena em ordem crescente ou alfabética
frutas.sort()    

#Ordena em ordem decrescente 
frutas.reverse()

for f in frutas:
    print(f)

for i in range(0, len(frutas), 2):
    print(frutas[i])


#Remove todos de uma vez
#frutas.clear()        

frutas[0] = 'banana da terra'
print(frutas)

