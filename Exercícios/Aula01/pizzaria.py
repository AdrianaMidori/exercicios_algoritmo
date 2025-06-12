# Uma pizzaria necessita de um programa que efetuará o
#cálculo de conta por cliente, o programa solicitará 
#ao usuário o valor total e o número de clientes. O
#programa fará


 totalconta = float(input('Informe o valor da conta :'))
 numclientes = int(input('Informe o número de clientes :'))
 valorPorCliente = totalconta/numclientes
 print (f"O valor é R$  {valorPorCliente} por cliente")

 print("O valor é de R$ {0} por cliente".format(valorPorCliente))

