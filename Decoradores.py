{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c2603aa0",
   "metadata": {},
   "source": [
    "### Recapitulando\n",
    "Funções em Python são objetos de primeira classe. Isso significa que as funções podem ser passadas e usadas como argumentos\n",
    "\n",
    "#### Inner Functions\n",
    "É possível definir funções dentro de outras funções. Tais funções são chamadas de funções internas\n",
    "\n",
    "#### Retornando funções de funções\n",
    "Python também permite que você use funções como valores de retorno\n",
    "\n",
    "# Decoradores\n",
    "\n",
    "## Decorador Simples\n",
    "Agora que entendemos que funções são como qualquer outro objeto em Python, podemos seguir em frente e ver a mágica que é o decorador Python\n",
    "\n",
    "## Açúcar Sintático\n",
    "Decoradores podem ser usados de maneira mais simples com o símbolo @\n",
    "\n",
    "## Finções de decoração com argumentos\n",
    "Podemos usar *args e **kwargs na função interna, com isso ele aceitará um número arbitrário de argumentos posicionais e de palavras-chave"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5cb287c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Faz algo antes de executar\n",
      "Olá Mundo Nome\n",
      "Faz algo depois de executar\n"
     ]
    }
   ],
   "source": [
    "def meu_decorador(funcao):\n",
    "    def envelope(*args, **kwargs):\n",
    "        print(\"Faz algo antes de executar\")\n",
    "        funcao(*args, **kwargs)\n",
    "        print(\"Faz algo depois de executar\")\n",
    "    return envelope\n",
    "\n",
    "@meu_decorador\n",
    "def ola_mundo(nome):\n",
    "    print(f\"Olá Mundo {nome}\")\n",
    "\n",
    "# ola_mundo = meu_decorador(ola_mundo)\n",
    "ola_mundo(\"Nome\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "bcc53fd5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estou aprendendo Python\n",
      "Estou aprendendo Python\n",
      "PYTHON\n"
     ]
    }
   ],
   "source": [
    "import functools\n",
    "\n",
    "def duplicar(func):\n",
    "    @functools.wraps(func)\n",
    "    def envelope(*args, **kwargs):\n",
    "        func(*args, **kwargs)\n",
    "        return func(*args, **kwargs)\n",
    "    return envelope\n",
    "\n",
    "@duplicar\n",
    "def aprender(tecnologia):\n",
    "    print(f\"Estou aprendendo {tecnologia}\")\n",
    "    return tecnologia.upper()\n",
    "func = aprender(\"Python\")\n",
    "\n",
    "print(func)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1f63ba5a",
   "metadata": {},
   "source": [
    "## Retornando valores de funções decoradas\n",
    "O decorador pode decidir se retorna o valor da função decorada ou não. Para que o valor seja retornado a função de envelope deve retornar o valor da função decorada\n",
    "\n",
    "## Introspecção\n",
    "É a capacidade de um objeto saber sobre seus próprios atributos em tempo de execução"
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
