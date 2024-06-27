import textwrap
def menu():
    menu = """\n
    ================= MENU =================
    O que deseja fazer?
    [s]\tSacar
    [d]\tDepositar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques ):

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo o suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor de saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        numero_saques += 1
        print(f"\n=== Saque realizado com sucesso! ==={numero_saques}")
        # extrato_dict['saque'].append(valor)
    else:
        print('\n@@@ Operação falhou! O valor informado é inválido. @@@')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("\n==============================")


def cria_usuario(usuarios):
    """
    nome, data de nascimento, cpf e endereço (endereço é string com o formato: logadouro, nro - bairro - cidade/sigla estado).
    Deve ser armazenado somente os números do CPF. não podemos cadastrar 2 usuários com o mesmo CPF.
    """
    cpf = input("Qual o seu CPF (Somente números)? ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    data_nascimento = input("Qual sua data de nascimento (dd-mm-aaaa)? ")
    nome_usuario = input("Qual seu nome completo? ")
    endereco = input("Informe o endereço (logadouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome_usuario, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n===== Usuário criado com sucesso! =====\n")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    """
    O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número da conta e usuário.
    O número da conta é sequencial, iniciando em 1. O númeroda agência é fixo: "0001". O usuário pode ter mais de
    uma conta, mas uma conta pertence a somente um usuário.
    """
    cpf = input("Informe o usuário (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n===== Conta criada com sucesso! =====\n")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
def listar_contas(contas):
    for conta in contas:
        linha = f"""
        Titular: {conta['usuario']['nome']}
        Agência: {conta['agencia']}
        Número da Conta: {conta['numero_conta']}\n"""
        print("=" * 100)
        print(textwrap.dedent(linha))


"""
Dica: Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado
para cada usuário da lista
"""
def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    numero_saques = 0
    limite_valor_saque = 500
    extrato = ""
    usuarios = [] #{cpf: '', dados: {}}
    contas_correntes = []

    while True:
        opcao = menu()

        if opcao == 's':
            valor = float(input("Qual valor deseja sacar: "))
            saldo, extrato = sacar(
                saldo= saldo,
                valor=valor,
                extrato= extrato,
                limite= limite_valor_saque,
                numero_saques= numero_saques,
                limite_saques= LIMITE_SAQUE,
                )

        elif opcao == 'd':
            valor = float(input("Qual valor deseja depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato= extrato)

        elif opcao == 'nc':
            numero_conta = len(contas_correntes) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas_correntes.append(conta)
        elif opcao == 'lc':
            listar_contas(contas_correntes)
        elif opcao == 'nu':
            cria_usuario(usuarios)
        elif opcao == 'q':
            break
        pass

main()

