def obter_numero(mensagem):
    x = int(input(mensagem))
    return x

def soma_numeros(a, b):
    c = a + b
    return c

# entrada
numero_1 = obter_numero("Informe um número inteiro: ")
numero_2 = obter_numero("Informe um número inteiro: ")

# processamento
soma = soma_numeros(numero_1, numero_2)

# saida
print(f"A soma dos dois número é :", soma)