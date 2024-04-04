# Desafio Trilha Python DIO - Sistema Bancário POO

Neste desafio foi proposto otimizarmos ainda mais o [sistema bancário anterior](https://github.com/devcaiada/bank-system-python-optimized) com a Programação Orientada a Objetos (POO).

## Diagrama do desafio

Para isso temos um diagrama das soluções a serem desenvolvidas em console conforme imagem abaixo:

![diagrama](https://github.com/devcaiada/bank-system-py-poo/blob/main/.idea/images/Trilha%20Python%20-%20desafio.png?raw=true)


## Código main

Abaixo podemos verificar como nosso código main ficou mais limpo que o anterior, sem a necessidade de criarmos funções para ela.

~~~python
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
~~~

Os atributos e métodos se encontram no arquivo **desafio_dio_python.py** nesse repositório.

## Saídas

O sistema foi construído para ser executado em console. Segue abaixo algumas das saídas mais importantes.

### Novo Usuário

![new_user](https://github.com/devcaiada/bank-system-py-poo/blob/main/.idea/images/novo_usuario.png?raw=true)

### Nova Conta

![new_account](https://github.com/devcaiada/bank-system-py-poo/blob/main/.idea/images/nova_conta.png?raw=true)

### Extrato

![extrato](https://github.com/devcaiada/bank-system-py-poo/blob/main/.idea/images/extrato.png?raw=true)

### Listagem das Contas

![account_list](https://github.com/devcaiada/bank-system-py-poo/blob/main/.idea/images/listar_contas.png?raw=true)

---