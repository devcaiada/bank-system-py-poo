from desafio_dio_python import *

clientes = []
contas = []

while True:
    opcao = menu()

    if opcao == '1':
        depositar(clientes)

    elif opcao == '2':
        sacar(clientes)

    elif opcao == '3':
        exibir_extrato(clientes)

    elif opcao == '4':
        criar_cliente(clientes)

    elif opcao == '5':
        numero_conta = len(contas) + 1
        criar_conta(numero_conta, clientes, contas)

    elif opcao == '6':
        listar_contas(contas)

    elif opcao == '0':
        break

    else:
        print("\nXXX Operação inválida, por favor selecione novamente a operação desejada. XXX")