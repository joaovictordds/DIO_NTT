import textwrap

def menu():

    menu = '''\n
    ============ MENU ===========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuario
    [q]\tSair
    => '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso! ===')
    else:
        print('\n --- A operação falhou, o valor informado é inválido. ---')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('--- A operação falhou! Não há saldo suficiente para realizar esta operação.. ---')
    elif excedeu_limite:
        print('--- A operação falhou! O valor do saque superar o limite. ---')
    elif excedeu_saques:
        print('--- A operação falhou! Número máximo de saques excedido. ---')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque\t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n=== Saque realizado com sucesso!===')
    else:
        print('\n --- A operação falhou. O valor informado eé inválido. ---')
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n========== EXTRATO ==========\n')
    print('Não foram realizas movimentações' if not extrato else extrato)
    print(f'\nSaldo\t\tR$ {saldo:.2f}')
    print('=============================')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (apenas números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('--- Já existe usuário cadastrado com este CPF! ---')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data denascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro - nro - bairro - cidade - estado/sigla): ')

    usuarios.append({'nome':nome, 'data_nascimento':data_nascimento, 'cpf':cpf, 'endereco':endereco})
    
    print('=== Usuario cadastrado com sucesso! ===')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print('\n===Conta cadastrada com sucesso! ===')
        return {'agencia':agencia,'numero_conta':numero_conta, 'usuario':usuario}
    
    print('\n--- Usuário não encontrado, tente novamente.. ---')

def listar_contas(contas):
    for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}'''
        
        print('=' * 100)
        print(textwrap.dedent(linha))

def main(): # Função principal que chama as funções

    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    num_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o valor do depósito R$: '))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 's':
            valor = float(input('Informe o valor do saque R$: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=num_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 'nu':
            criar_usuario(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 'lc':
            listar_contas(contas)
        
        elif opcao == 'q':
            break

        else:
            print('Operação inválda, por favor, selecione novamente a opção desejada.')

main()
