from abc import ABC, abstractclassmethod, abstractproperty
import textwrap

from datetime import datetime



class Cliente:
    def __init__(self, conta, transacao):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
    
class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo o suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            # extrato += f"Saque:\tR$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\n=== Saque realizado com sucesso! ==={numero_saques}")
            return True
            
        else:
            print('\n@@@ Operação falhou! O valor informado é inválido. @@@')

        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            # extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print('\n@@@ Operação falhou! O valor informado é inválido. @@@')
            return False
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor de saque excede o limite. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
    
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

