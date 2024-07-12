import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / 'meu_banco.db')

cur = con.cursor() # para executar comandos no banco

# cur.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')


data = ("Henrique", "rique@gmail.com")
# cur.execute('INSERT INTO clientes (nome, email) VALUES(?, ?);', data)

data1 = ("Henrique Augusto", "rique@gmail.com", 2)
# cur.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', data1 )

data2 =(2,)
# cur.execute('DELETE FROM clientes WHERE id=?;', data2)


data3 = [
        ('Nome1', 'nome1@gmail.com'),
        ('Nome2', 'nome2@gmail.com'),
        ('Nome3', 'nome3@gmail.com'),
        ('Nome4', 'nome4@gmail.com'),
         ]

# cur.executemany('INSERT INTO clientes (nome, email) VALUES(?, ?);', data3)

# cur.execute('SELECT * FROM clientes WHERE id = 1')
# result = cur.fetchone()
# print(result)

cur.row_factory = sqlite3.Row
cur.execute('SELECT * FROM clientes')
result = cur.fetchall()
for row in result:
    print(dict(row))

# cur.row_factory = sqlite3.Row
# cur.execute('SELECT * FROM clientes WHERE id = 1')
# result = cur.fetchone()
# print(dict(result))


try:
    cur.execute('INSERT INTO clientes (nome, email) VALUES(?, ?);',('Nome5', 'nome5@gmail.com'))
    cur.execute('INSERT INTO clientes (nome, email) VALUES(?, ?);',(8,'Nome6', 'nome6@gmail.com'))
    con.commit()
except Exception as exc:
    print(f'Ops! Um erro ocorreu! {exc}')
    con.rollback()
# finally:
#     con.commit()
# con.commit()
con.close()

# -------------------------------------------------------------------------------------------------------------

# # Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
# class UsuarioTelefone:
#     def __init__(self, nome, numero, plano):
#         self.nome = nome
#         self.numero = numero
#         self.plano = plano

#     # Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
#     def fazer_chamada(self, destinatario, duracao):
#         custo = self.plano.custo_chamada(duracao)
        
#         # Verifique se o saldo do plano é suficiente para a chamada.
#         if self.plano.verificar_saldo() >= custo:
#             # Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.
#             self.plano.deduzir_saldo(custo)
#             # E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:
#             return f"Chamada para {destinatario} realizada com sucesso. Saldo restante: {self.plano.verificar_saldo():.2f}"
#         else:
#             return "Saldo insuficiente para realizar a chamada."

# # Classe Plano, ela representa o plano de um usuário de telefone:
# class Plano:
#     def __init__(self, saldo_inicial):
#         self.saldo = saldo_inicial

#     # Crie um método para verificar_saldo e retorne o saldo atual:
#     def verificar_saldo(self):
#         return self.saldo

#     # Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
#     def custo_chamada(self, duracao):
#         custo_por_minuto = 0.10
#         return duracao * custo_por_minuto

#     # Crie um método deduzir_saldo para deduz o valor do saldo do plano:
#     def deduzir_saldo(self, valor):
#         self.saldo -= valor

# # Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
# class UsuarioPrePago(UsuarioTelefone):
#     def __init__(self, nome, numero, saldo_inicial):
#         super().__init__(nome, numero, Plano(saldo_inicial))

# # Recebendo as informações do usuário:
# nome = input("Digite o nome do usuário: ")
# numero = input("Digite o número do usuário: ")
# saldo_inicial = float(input("Digite o saldo inicial do plano: "))

# # Objeto de UsuarioPrePago com os dados fornecidos:
# usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
# destinatario = input("Digite o número do destinatário: ")
# duracao = int(input("Digite a duração da chamada em minutos: "))

# # Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
# print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
