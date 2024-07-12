"""
Por que precisamos manipular arquivos?
São essenciais para qualquer tipo de programação, pois fornecem um meio de armazenar e recuperar os dados.
São fundamentais para gerar persistência do sistema

Conceito de arquivo em informática
É um container no computador onde as informações são armazenadas em formato digital.  Existem dois tipos
de arquivos que podemos manipular em Python: de texto e binários


Pq precisamos manipular arquivos?
Usar função 'open()' quando terminar o uso fechar 'close()' para liberar capacidade computacional

Modos de abertura de arquivo - deve ser escolhido de acordo com o que precisa ser feito
leitura ('r'), gravação ('w') e anexar ('a')

"""

# file = open('example.txt', 'r')

# file = open('example.txt', 'w')

# file = open('example.txt', 'a')

"""
Lendo um arquivo
Pode-se usar: 'read()', 'readline()' ou 'readlines()' dependendo da necessidade

readline lê uma linha por vez, readlines retorna uma lista onde cada elemento é uma linha do arquivo
"""
# file = open('lorem.txt', 'r')
# print(file.read())
# print(file.readline())
# print(file.readlines())


# for linha in file.readline():
#     print(linha)


# for linha in file.readlines():
#     print(linha)

# while len(linha:= file.readline()):
#     print(linha)

# file.close()

"""
write() e writelinhes() para escrever em um arquivo. Deve-se abrir o arquivo no modo correto 
"""
# file = open('./teste.txt', 'w')
# print(file.write('Escrevendo dados em um novo arquivo'))
# file.writelines(["escrevendo ", "um ", "novo ", " texto"])

# file.close()

"""
Python oferece funções para gerenciar arquivos e diretórios. Podemos criar, renomear e excluir arquivos e diretórios
usando os módulos 'os' e 'shutil'
"""
import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

print(ROOT_PATH)

# os.mkdir(ROOT_PATH / "novo-diretorio")

# arquivo = open(ROOT_PATH / "novo-arquivo.txt",'w')
# arquivo.close()

# os.rename(ROOT_PATH/'novo-arquivo.txt', ROOT_PATH/'novo.txt')

# os.remove(ROOT_PATH/"novo.txt")

# shutil.move(ROOT_PATH/"novo-arquivo.txt", ROOT_PATH/"novo-diretorio"/"novo-arquivo.txt")

"""
Tratar errps é uma parte importante da manipulação de arquivos.
Python oferece uma variedade de exceções que nos permite lidar com erros comuns

FileNotFoundError - não encontrado no diretório especificado

PermissionError - s/ permissão para ler ou escrever

IOError - falta de espaço no servidor por exemplo
UnicodeDecodeError - codificação inadequada
UnicodeEncodeError - tentar escrever em codificação inadequada
"""

# try:
#     arquivo = open("meu_arquivo.py")
# except FileNotFoundError as exc:
#     print("Arquivo não encontrado")
#     print(exc)

# try:
#     arquivo = open(ROOT_PATH / "novo-diretorio")
# except IsADirectoryError as exc:
#     print(f"Não foi possível abrir o arquivo: {exc}")
# except Exception as exc:
#     print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")



import csv

# try:
#     with open(ROOT_PATH/'usuarios.csv', 'w', encoding='utf-8') as arquivo:
#         escritor = csv.writer(arquivo)
#         escritor.writerow(['id', 'nome'])
#         escritor.writerow(['1', 'Maria'])
#         escritor.writerow(['2', 'João'])
# except IOError as exc:
#     print(f'Erro ao criar o arquivo. {exc}')

# try:
#     with open(ROOT_PATH/'usuarios.csv', 'r', newline='', encoding='utf-8') as arquivo:
#         leitor = csv.reader(arquivo)
#         for row in leitor:
#             print(row)
        
# except IOError as exc:
#     print(f'Erro ao criar o arquivo. {exc}')


try:
    with open(ROOT_PATH/'usuarios.csv', 'r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for row in leitor:
            print(row['id'], row['nome'])
        
except IOError as exc:
    print(f'Erro ao criar o arquivo. {exc}')