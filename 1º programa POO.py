{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "230864e6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Buzina\n",
      "Correndo\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'bicicleta: cor = verde, modelo = caloi, ano = 1990, valor = 500'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Python tem um próprio gerenciamento de memória\n",
    "class bicicleta:\n",
    "    def __init__(self, cor, modelo, ano, valor):\n",
    "#self é a referência explicita para o objeto, representa a instância\n",
    "        self.cor = cor #Atributos\n",
    "        self.modelo = modelo\n",
    "        self.ano = ano\n",
    "        self.valor = valor\n",
    "    \n",
    "    def buzinar(self):\n",
    "        print(\"Buzina\")\n",
    "    def parar(self):\n",
    "        print(\"Parar\")\n",
    "    def correr(self):\n",
    "        print(\"Correndo\")\n",
    "        \n",
    "#     def __str__(self):\n",
    "#         return f'Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}'\n",
    "    \n",
    "    def __str__(self):\n",
    "        return f\"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}\"\n",
    "\n",
    "b1 = bicicleta(\"vermelha\", \"caloi\", 2022, 890)\n",
    "# print(b1)\n",
    "\n",
    "b1.buzinar()\n",
    "b1.correr()\n",
    "\n",
    "b2 = bicicleta(\"verde\", \"caloi\", 1990, 500)\n",
    "bicicleta.__str__(b2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1bc2d360",
   "metadata": {},
   "outputs": [],
   "source": []
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
