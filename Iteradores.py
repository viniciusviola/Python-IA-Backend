{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f75b6f96",
   "metadata": {},
   "source": [
    "# Iteradores\n",
    "Trabalhar com sequências grandes\n",
    "\n",
    "Em python, um iterador é um objeto que contém um número contável de valores que podem ser iterados, o que significa que você pode percorrer todos os valores. O protocolo do iterador é uma maneira do Python fazer a iteração de um objeto, que consiste em dois métodos especiais `__iter__()` e `__next__()`\n",
    "\n",
    "Utilizado para ler arquivos grandes\n",
    "- Economiza memória evitando carregar todas as linhas do arquivo\n",
    "- Iterar linha a linha do arquivo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ad91801b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "class MeuIterador:\n",
    "    def __init__(self, numeros: list[int]):\n",
    "        self.numeros =  numeros\n",
    "        self.contador = 0\n",
    "        \n",
    "    def __iter__(self):\n",
    "        return self\n",
    "    \n",
    "    def __next__(self):\n",
    "        try:\n",
    "            self.contador += 1\n",
    "            numero = self.numeros[self.contador]\n",
    "            \n",
    "            return numero * 2\n",
    "        except IndexError:\n",
    "            raise StopIteration\n",
    "\n",
    "for i in MeuIterador(numeros = [1, 2, 3]):\n",
    "    print(i)"
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
