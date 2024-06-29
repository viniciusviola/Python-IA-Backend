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
file = open('lorem.txt', 'r')
print(file.read())
print(file.readline())
print(file.readlines())


# for linha in file.readline():
#     print(linha)


# for linha in file.readlines():
#     print(linha)

while len(linha:= file.readline()):
    print(linha)

file.close()

"""
write() e writelinhes() para escrever em um arquivo. Deve-se abrir o arquivo no modo correto 
"""
file = open('./teste.txt', 'w')
print(file.write('Escrevendo dados em um novo arquivo'))
file.writelines(["escrevendo ", "um ", "novo ", " texto"])

file.close()

