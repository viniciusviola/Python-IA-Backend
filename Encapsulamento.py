{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7df730c5",
   "metadata": {},
   "source": [
    "# Encapsulamento\n",
    "\n",
    "Um dos conceitos fundamentais em programação orientada a objetos. Ele descreve a ideia de agrupar dados e os metódos que manipulam esses dados em uma unidade. Isso impõe restrições ao acesso direto a variáveis e métodos e pode evitar a modificação acidental de dados. Para evitar alterações acidentais, a variável de um objeto só pode ser alterada pelo método desse objeto\n",
    "\n",
    "Objetivo é proteger os dados de um objeto\n",
    "\n",
    "# Modificadores de acesso\n",
    "\n",
    "Em linguagens como java e C++, existem palavras reservadas para definir o nível de acesso aos atributos e metódos da classe. Em Python não temos palavras reservadas, porém, usamos convenções no nome do recurso, para definir se a variável é pública ou privada\n",
    "\n",
    "# Público/Privado\n",
    "\n",
    "Todos os recursos são públicos, a menos que o nome inicie com underline. Ou seja, o interpretador python não irá garantir a proteção do recurso, mas por ser uma convenção amplamente adotada na comunidade, quando encontramos uma variável e/ou método com nome iniciado por underline, sabemos que não deveríamos manipular o seu valor diretamente, ou invocar o método fora do escopo da classe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e0e53731",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "200\n"
     ]
    }
   ],
   "source": [
    "class Conta:\n",
    "    def __init__(self, nro_agencia, saldo = 0):\n",
    "        self._saldo = saldo\n",
    "        self.nro_agencia = nro_agencia\n",
    "        \n",
    "    def depositar(self, valor):\n",
    "        self._saldo += valor\n",
    "    \n",
    "    def sacar(self, valor):\n",
    "        self._saldo -= valor\n",
    "    \n",
    "    def mostrar_saldo(self):\n",
    "        return self._saldo\n",
    "\n",
    "conta = Conta(\"0001\", 100)\n",
    "conta.depositar(100)\n",
    "\n",
    "print(conta.mostrar_saldo())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7cb7c315",
   "metadata": {},
   "source": [
    "# property()\n",
    "\n",
    "Com o property() do Python, você pode criar atributos gerenciados em suas classes. Você pode usar atributos gerenciados, também conhecidos como propriedades, quando precisar modificar sua implementação interna sem alterar a API pública da classe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "b479c02f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "20\n",
      "0\n",
      "15\n",
      "Nome: Guilherme \t Idade: 28\n"
     ]
    }
   ],
   "source": [
    "class Foo:\n",
    "    def __init__(self, x=None):\n",
    "        self._x = x\n",
    "        \n",
    "    @property\n",
    "    def x(self):\n",
    "        return self._x or 0\n",
    "    \n",
    "    @x.setter\n",
    "    def x(self, value):\n",
    "        self._x += value\n",
    "        \n",
    "    @x.deleter\n",
    "    def x(self):\n",
    "        self._x = 0\n",
    "    \n",
    "foo = Foo(10)\n",
    "print(foo.x)\n",
    "\n",
    "foo.x = 10\n",
    "\n",
    "print(foo.x)\n",
    "\n",
    "del(foo.x)\n",
    "print(foo.x)\n",
    "\n",
    "foo.x = 15\n",
    "print(foo.x)\n",
    "\n",
    "\n",
    "\n",
    "class Pessoa:\n",
    "    def __init__(self, nome, ano_nascimento):\n",
    "        self.nome = nome\n",
    "        self._ano_nascimento = ano_nascimento\n",
    "    \n",
    "#     @property       \n",
    "#     def nome(self):\n",
    "#         return self._nome\n",
    "    \n",
    "    @property\n",
    "    def idade(self):\n",
    "        _ano_atual = 2022\n",
    "        return _ano_atual - self._ano_nascimento\n",
    "    \n",
    "pessoa = Pessoa(\"Guilherme\", 1994)\n",
    "print(f\"Nome: {pessoa.nome} \\t Idade: {pessoa.idade}\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
