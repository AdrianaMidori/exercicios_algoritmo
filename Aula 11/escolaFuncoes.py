def mensagem():
    print("Sistema de alunos")

def mensagem_personalizada(msg):
    print(msg)

def cadastrar(v):
    aluno = {}
    aluno['nome'] = input ("Informe o nome: ")
    aluno['nota1'] = float(input('Informe nota 1: '))
    aluno['nota2'] = float(input('Informe nota 2: '))
    v.append(aluno)

def calcularMedia(a,b):
    return (a + b) / 2

def mensagem_situacao(m):
    if (m >= 7):
        return "Aprovado"
    else:
        return "Reprovado"

def listagem(v):
    for aluno in v:
        media = calcularMedia(aluno['nota1'], aluno['nota2'])
        situacao = mensagem_situacao(media)
        print(f'{aluno["nome"]} - {aluno["nota1"]} - {aluno["nota2"]} - '
              f'{media} - {situacao}')