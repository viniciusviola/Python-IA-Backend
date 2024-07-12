from abc import ABC, abstractmethod
import textwrap
from datetime import datetime, timezone


class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""
            Agência:\t{conta.agencia}
            C/C:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\tR${conta.saldo:.2f}
        """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0
    
    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("\n@@@ Você excedeu o número de transações permitidas para hoje! @@@")
            return
        
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ({self.cpf})>"


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
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
            # numero_saques += 1
            # print(f"\n=== Saque realizado com sucesso! ==={numero_saques}")
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
        self._limite_saques = limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor de saque excede o limite. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
        else:
            return super().sacar(valor)
        return False
    
    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"
    
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
                "data": datetime.now(timezone.utc).strftime("%d-%m-%Y %H:%M:%S"),
            }
        )
    
    def gerar_relatorio(self, tipo_transacao = None):
        for transacao in self._transacoes:
            if tipo_transacao is None or transacao['tipo'].lower() == tipo_transacao.lower():
                yield transacao




    # def transacoes_do_dia(self):
    #     data_atual = datetime.now(timezone.utc).date()
    #     transacoes = []
    #     for transacao in self._transacoes:
    #         data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
    #         if data_atual == data_transacao:
    #             transacoes.append(transacao)
    #     return transacoes

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
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

def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(* args, ** kwargs)
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open('log.txt', 'a') as arquivo:
            arquivo.write(
            f"[{data_hora}] Função '{func.__name__}' executada com argumentos {args} e {kwargs}."
            f"Retornou {resultado}\n"
            )
        
        return resultado
    return envelope

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

@log_transacao
def exibir_extrato(clientes):

    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n========== EXTRATO ==========")

    # transacoes = conta.historico.transacoes
    extrato = ""
    ten_transacao = False
    for transacao in conta.historico.gerar_relatorio(tipo_transacao="saque"):
        tem_transacao = True
        extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"
    if not tem_transacao:
        print("Não foram realizadas movimentações.")
    
    print(extrato)
    print(f"\nSaldo:\t\tR$ {conta.saldo:.2f}")
    print("\n==============================")

@log_transacao
def criar_cliente(clientes):
    
    cpf = input("Qual o seu CPF (Somente números)? ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    nome_usuario = input("Informe o nome completo: ")
    endereco = input("Informe o endereço (logadouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome_usuario, data_nascimento=data_nascimento, cpf= cpf, endereco= endereco)
    clientes.append(cliente)
    print("\n===== Usuário criado com sucesso! =====\n")

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

@log_transacao
def criar_conta(numero_conta, clientes, contas):
    
    cpf = input("Informe o usuário (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
        return
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("\n===== Conta criada com sucesso! =====\n")
      
def listar_contas(contas):
    for conta in ContasIterador(contas):
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return
    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)

@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return
    valor = float(input("Informe o valor do Saque: "))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)


def main():
    clientes = [] #{cpf: '', dados: {}}
    contas = []

    while True:
        opcao = menu()

        if opcao == 's':
            sacar(clientes)
            

        elif opcao == 'd':
            depositar(clientes)

        elif opcao == 'e':
            exibir_extrato(clientes)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'nu':
            criar_cliente(clientes)
        elif opcao == 'q':
            break
        pass

main()

