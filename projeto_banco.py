
print('''

                    ===  ===================================== ===
                           BEM-VINDO NOVAMENTE AO BANCO DIO
                    ===  ===================================== ===

''')

menu = '''

Selecione a opção desejada:                    

[1] - DEPOSITAR
[2] - SACAR
[3] - EXTRATO
[4] - SAIR

=> '''

saldo = 0
limite = 500
extrato = ''
num_saques = 0
valor = 0

while True:
    opcao = input(menu)
    if opcao == '1':
        valor = float(input('---> Informe o valor a ser depositado: R$ '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito + R$ {valor:.2f}\n'

        else:
            print('-> A operação não pôde ser concluída, o valor informado não é válido.')

    elif opcao == '2':
        valor = float(input('---> Informe o valor do saque: R$ '))
        
        ### Verificações:
        excedeu_saldo = valor > saldo
        excedeu_lim = valor > limite
        excedeu_lim_saques = num_saques >= 3

        if excedeu_saldo:
            print('-> Operação não concluída | Saldo Insuficiente!!!')
        elif excedeu_lim:
            print('-> Operação não concluída | O valor do saque excede o limite.')
        elif excedeu_lim_saques:
            print('-> Operação não concluída | Número máximo diário de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque - R$ {valor:.2f}\n'
            num_saques += 1
        else:
            print('Operação não concluída. O valor informado não é válido.')

    elif opcao == '3':
        print('\n=============== EXTRATO ===============\n')
        if not extrato:
            print('Não foram realizadas movimentaçoes...\n')
            print(f'Saldo: R$ {saldo:.2f}\n')
        else:
            print(extrato)
            print(f'Saldo: R$ {saldo:.2f}\n')
        print('=============== ======= ===============')

    elif opcao =='4':
        print('Obrigado pela preferência!')
        break

    else:
        print('Operação inválida....')


