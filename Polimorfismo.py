{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "9e8d737f",
   "metadata": {},
   "source": [
    "# O que é polimorfismo?\n",
    "\n",
    "Classes polimorficas em Python\n",
    "\n",
    "A palavra polimorfismo significa ter muitas formas. Na programação, polimorfismo significa o mesmo nome de função (mas assinaturas diferentes) sendo usado para tipos diferentes\n",
    "\n",
    "Se comporta de formas diferentes dependendo do tipo de informação, objeto que é passado para o método\n",
    "\n",
    "\n",
    "# Polimorfismo com herança\n",
    "\n",
    "Na herança, a classe filha herda os métodos da classe pai. No entanto, é possível modificar um método em uma classe filha herdada da classe pai. Isso é particulamente útil nos casos em que o método herdado da classe pai não se encaixaperfeitamente na classe filha"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7805dd8d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Voando...\n",
      "Avestruz não voa\n",
      "Avião está decolando\n"
     ]
    }
   ],
   "source": [
    "class Passaro:\n",
    "    def voar(self):\n",
    "        print(\"Voando...\")\n",
    "\n",
    "class Pardal(Passaro):\n",
    "    def voar(self):\n",
    "        super().voar()\n",
    "#        print(\"Pardal voa\")\n",
    "\n",
    "class Avestruz(Passaro):\n",
    "    def voar(self):\n",
    "        print(\"Avestruz não voa\")\n",
    "\n",
    "def plano_de_voo(obj):\n",
    "    obj.voar()\n",
    "\n",
    "    # Exemplo ruim do uso de herança para \"ganhar\" o método voar\n",
    "class Aviao(Passaro):\n",
    "    def voar(self):\n",
    "        print(\"Avião está decolando\")\n",
    "\n",
    "plano_de_voo(Pardal())\n",
    "plano_de_voo(Avestruz())\n",
    "plano_de_voo(Aviao())"
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
