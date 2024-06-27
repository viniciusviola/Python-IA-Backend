{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "44e73bde",
   "metadata": {},
   "source": [
    "# Variáveis de classe e variáveis de instância\n",
    "\n",
    "\n",
    "### Atributos do objeto\n",
    "\n",
    "Todos os objetos nascem com o mesmo número de atributos de classe e de instância. Atributos de instância são diferentes para cada objeto (cada objeto tem uma cópia), já os atributos de classe são compartilhados entre os objetos."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ccda2b33",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Estudante:\n",
    "    escola = \"DIO\" #variável de classe, única para todos os objetos\n",
    "    \n",
    "    def __init__(self, nome, matricula):\n",
    "        self.nome = nome # self é instância\n",
    "        self.matricula = matricula\n",
    "    def __str__(self):\n",
    "        return f\"{self.nome} - {self.matricula} - {self.escola}\"\n",
    "    \n",
    "def mostrar_valores(*objs):\n",
    "    for obj in objs:\n",
    "        print(obj)\n",
    "    \n",
    "aluno_1 = Estudante(\"Guilherme\", 1) # variável de instância\n",
    "aluno_2 = Estudante(\"Giovanna\", 2) # variável de instância\n",
    "\n",
    "mostrar_valores(aluno_1, aluno_2)\n",
    "\n",
    "aluno_1.matricula = 3\n",
    "\n",
    "mostrar_valores(aluno_1, aluno_2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "65456aa0",
   "metadata": {},
   "source": [
    "# Métodos de classe e métodos estáticos\n",
    "\n",
    "### Métodos de classe\n",
    "Estão ligados à classe e não ao objeto. Eles têm acesso ao estado da classe, pois recebem um parâmetro que aponta para a classe e não para a instância do objeto\n",
    "\n",
    "### Métodos estáticos\n",
    "Não recebe um primeiro argumento explícito. Ele também é um método vinculado à classe e não ao objeto da classe. Este método não pode acessar ou modificar o estado da classe. Ele está presente em uma classe porque faz sentido que o método esteja presente na classe\n",
    "\n",
    "\n",
    "### Classe x Estático\n",
    "- De classe recebe um primeiro parâmtero que aponta para a classe, enquanto um método estático não\n",
    "- De classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou modificá-lo\n",
    "- Geralmente usamos o método de classe para criar métodos de fábrica\n",
    "- Geralmente usamos métodos estáticos para criar funções utilitárias\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c90e949b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Guilherme 28\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "class Pessoa:\n",
    "    def __init__(self, nome, idade):\n",
    "        self.nome = nome\n",
    "        self.idade = idade\n",
    "    \n",
    "    @classmethod\n",
    "    def criar_de_data_nascimento(cls, ano, mes, dia, nome):\n",
    "        #print(cls)\n",
    "        idade = 2022 - ano\n",
    "        return cls(nome, idade)\n",
    "    \n",
    "    @staticmethod\n",
    "    def e_maior_idade(idade):\n",
    "        return idade >= 18\n",
    "    \n",
    "    \n",
    "p = Pessoa.criar_de_data_nascimento(1994, 3, 21,\"Guilherme\")\n",
    "\n",
    "print(p.nome, p.idade)\n",
    "\n",
    "print(Pessoa.e_maior_idade(18))\n",
    "print(Pessoa.e_maior_idade(8))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8880672b",
   "metadata": {},
   "source": [
    "# Interfaces\n",
    "\n",
    "Definem o que uma classe deve fazer e não como\n",
    "\n",
    "# Python tem interface?\n",
    "\n",
    "O conceito de interface é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas. Em Python utilizamos classes abstratas para criar contratos. Classes abstratas não podem ser instanciadas\n",
    "\n",
    "\n",
    "# Módulo ABC\n",
    "Por padrão, o Python não fornece classes abstratas. O Python vem com um módulo que fornece a base para definir as classes abstratas, e o nome do módulo é ABC. O ABC funciona decorando métodos da classe base como abstratos e, em seguida, registrando classes concretas como implementações da base abstrata. Um método se torna abstrato quando decorado com @abstractmethod"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d8c237bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ligando a TV...\n",
      "Ligado!\n",
      "Desligando a TV...\n",
      "Desligado!\n",
      "Philco\n",
      "Ligando o Ar Condicionado...\n",
      "Ligado!\n",
      "Desligando o Ar Condicionado...\n",
      "Desligado!\n",
      "LG\n"
     ]
    }
   ],
   "source": [
    "from abc import ABC,abstractmethod,abstractproperty\n",
    "\n",
    "class ControleRemoto(ABC):\n",
    "    @abstractmethod\n",
    "    def ligar(self):\n",
    "        pass\n",
    "    \n",
    "    @abstractmethod\n",
    "    def desligar(self):\n",
    "        pass\n",
    "    \n",
    "    @property\n",
    "    @abstractproperty\n",
    "    def marca(self):\n",
    "        pass\n",
    "    \n",
    "    \n",
    "class ControleTv(ControleRemoto):\n",
    "    def ligar(self):\n",
    "        print(\"Ligando a TV...\")\n",
    "        print(\"Ligado!\")\n",
    "        \n",
    "    def desligar(self):\n",
    "        print(\"Desligando a TV...\")\n",
    "        print(\"Desligado!\")\n",
    "    \n",
    "    @property\n",
    "    def marca(self):\n",
    "        return print(\"Philco\")\n",
    "\n",
    "class ControleArCondicionado(ControleRemoto):\n",
    "    def ligar(self):\n",
    "        print(\"Ligando o Ar Condicionado...\")\n",
    "        print(\"Ligado!\")\n",
    "        \n",
    "    def desligar(self):\n",
    "        print(\"Desligando o Ar Condicionado...\")\n",
    "        print(\"Desligado!\")\n",
    "        \n",
    "    @property\n",
    "    def marca(self):\n",
    "        return print(\"LG\")\n",
    "        \n",
    "controle = ControleTv()\n",
    "controle.ligar()\n",
    "controle.desligar()\n",
    "controle.marca\n",
    "\n",
    "controle = ControleArCondicionado()\n",
    "controle.ligar()\n",
    "controle.desligar()\n",
    "controle.marca"
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
