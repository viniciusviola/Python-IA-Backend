{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e7c1bb7d",
   "metadata": {},
   "source": [
    "# Geradores\n",
    "\n",
    "São tipos especiais de iteradores, ao contrário das listas ou outros iteráveis, não armazenam todos os seus valores na memória.\n",
    "\n",
    "São definidos usando funções regulares, mas, ao invés de retornar valores usando \"return\", utilizam \"yield\".\n",
    "\n",
    "## Cracterísticas de geradores\n",
    "\n",
    "- Uma vez que um item gerado é consumido, ele é esquecido e não pode ser acessado novamente\n",
    "- O estado interno de um gerador é mantido entre chamadas\n",
    "- A execução de um gerador é pausada na declaração \"yield\" e retomada daí na próxima vez que ele for chamado\n",
    "\n",
    "## Exemplo: Recuperando dados de uma API\n",
    "\n",
    "- Solicitar dados por páginas (paginação).\n",
    "- Fornecer um produto por vez entre as chamadas\n",
    "- Quando todos os produtos de uma página forem retornados, verificar se existem novas páginas\n",
    "- Tratar o consumo da API como uma lista Python\n",
    "\n",
    "\n",
    "Usar gerador quando for código simples, fazer controle de fluxo, otimizar memória\n",
    "\n",
    "Uma tarefa ou algo mais complexo e melhor utilizar um iterador, poder estender o comportamento para outras classes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6240d962",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "\n",
    "def fetch_products(api_url, max_pages = 100):\n",
    "    page = 1\n",
    "    while page <= max_pages:\n",
    "        response = requests.geet(f\"{api_url}?page={page}\")\n",
    "        data = response.json()\n",
    "        for product in data['products']:\n",
    "            yield product\n",
    "        if 'next_page' not in data:\n",
    "            break\n",
    "        page += 1\n",
    "\n",
    "for product in fetch_products():\n",
    "    print(product['name'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6f2dff5c",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "def meu_gerador(numeros: list[int]):\n",
    "    for numero in numeros:\n",
    "        yield numero * 2\n",
    "\n",
    "for i in meu_gerador(numeros=[1,2,3]):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1831a564",
   "metadata": {},
   "source": [
    "# Desafio\n",
    "\n",
    "## Introdução\n",
    "\n",
    "Com o conhecimento adquirido sobre decoradores, geradores e iteradores, implementar as seguintes funcionalidades no sistema:\n",
    "\n",
    "- Decorador de log: \n",
    "    deve ser aplicado a todas as funções de transações (depósito, saque, criação de conta, etc), o decorador deve registrar (printar) a data e hora de cada transação, bem como o tipo de transação\n",
    "- Gerador de relatórios: \n",
    "    Criar um gerador que permita iterar sobre as transações de uma conta e retorne, uma a uma, as transações que foram realizadas. Esse gerador deve também ter uma forma de filtrar as transações baseado em seu tipo (por exemplo, apenas saques ou apenas depósitos)\n",
    "- Iterador personalizado: \n",
    "    ContaIterador, que permita iterar sobre todas as contas do banco, retornando informações básicas de cada conta (número, saldo atual, etc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "173e92db",
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
