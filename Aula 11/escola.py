from escolaFuncoes import cadastrar, listagem, mensagem, mensagem_personalizada
#Se eu quisesse importar todas as funções, mas não é recomendável no caso de outras bibliotecas
#from escolaFuncoes import *

#As funções (def) devem ser colocadas em um "Text File"

vetor =[]

while True:
    mensagem()
    op = int (input('1 - Cadastro \n2 - Listagem\n9 - Sair\nInforme a opção : '))
    match op :
        case 1:
            cadastrar(vetor)
        case 2:
            listagem(vetor)
        case 9:
            print("Obrigado por acessar o nosso programa.")
            break
        case _:
            mensagem_personalizada('Opção inválida.')

