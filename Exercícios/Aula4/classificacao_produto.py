# Construa um programa que leia o código de um determinado produto e mostre a sua classificação
# Código classificação
# 1 - Alimento não-perecível
# 2, 3 ou 4 - Alimento perecível
# 5 ou 6 - Vestuário
# 7 - Higiene pessoal
# 8, 9, 10 - Utensílios domésticos
# Qualquer outro código - Inválido

# codigo = int(input("Informe o código do produto [1-10]: "))
# if codigo == 1:
#     print("Classificação Alimento não-perecível")
# elif codigo >= 2 and codigo <=4:
#     print("Alimento perecível") 
# elif codigo == 5 or codigo == 6:
#     print("Vestuário") 
# elif codigo == 7:
#     prinf("Higiene pessoal") 
# elif codigo >= 8 and codigo <= 10: 
#     print("Utensílios domésticos")
# else:
#     print("Código Inválido.")                

codigo = int(input("Informe o código: "))
match codigo:
    case 1:
        print("Alimento não perecível")
    case 2 | 3 | 4:
        print("Alimento perecível")
    case 5 | 6:
        print("Vestuário") 
    case 7:
        print("Higiene pessoal") 
    case 8 | 9 | 10:
        print("Utensílios domésticos")         
    case _:
        print ("Invalido")    