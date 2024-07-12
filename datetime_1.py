{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "05dd9f13",
   "metadata": {},
   "source": [
    "## Objetivo geral\n",
    "\n",
    "Aprender a trabalhar com datas, horas e fusos horários em ỳthon, dominando o módulo 'datetime para manipulações precisas\n",
    "\n",
    "## O que é o módulo datetime?\n",
    "\n",
    "Em Python é usado para lidar com datas e horas. Ele possui várias classes úteis como daate, time e timedelta"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "16bca586",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2023-07-10\n",
      "2024-06-22\n",
      "2023-07-10 00:00:00\n",
      "2024-06-22 11:15:30.932166\n",
      "10:20:05\n"
     ]
    }
   ],
   "source": [
    "from datetime import date, datetime, time\n",
    "\n",
    "data = date(2023, 7, 10)\n",
    "\n",
    "print(data)\n",
    "\n",
    "print(date.today())\n",
    "\n",
    "data_hora = datetime(2023, 7, 10)\n",
    "\n",
    "print(data_hora)\n",
    "print(datetime.today())\n",
    "\n",
    "hora = time(10, 20, 5)\n",
    "\n",
    "print(hora)"
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
