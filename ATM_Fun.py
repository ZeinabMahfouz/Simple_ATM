{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e7087e99-aeff-4dd7-8a15-d2edbb54f8f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def check_pin():\n",
    "  global attempts\n",
    "  while attempts>0:\n",
    "    user_pin=int(input ('Enter you pin number  '))\n",
    "    if user_pin==pin :\n",
    "      print ('Pin is correct')\n",
    "      return True\n",
    "    else :\n",
    "      attempts-=1\n",
    "      if attempts>0:\n",
    "        print ('Invalid pin enter you pin number you have '+str(attempts)+'  attempts')\n",
    "      else:\n",
    "        print('You exceed the limit of attempts and you card is blocked')\n",
    "        return False\n",
    "    return False\n",
    "def process():\n",
    "    print(\"\\n--- ATM Menu ---\")\n",
    "    print(\"1. Balance Check\")\n",
    "    print(\"2. Deposit\")\n",
    "    print(\"3. Withdraw\")\n",
    "    print(\"4. Exit\")\n",
    "    print(\"----------------\")\n",
    "def balance_check():\n",
    "  print(f'Your current balance is: ${balance:.2f}')\n",
    "def Withdraw():\n",
    "  global balance\n",
    "  amount=float(input('Enter the amount you want to withdraw  :'))\n",
    "  if amount<=balance :\n",
    "    balance -= amount\n",
    "    print (f'Withdrawal successful. Your new balance is: ${balance:.2f}')\n",
    "    return True\n",
    "  else:\n",
    "    print (' Insufficient balance')\n",
    "    return False\n",
    "def Deposit():\n",
    "  global balance\n",
    "  amount=float(input('Enter the amount you want to deposit  :'))\n",
    "  balance += amount\n",
    "  print (f'Deposit successful. Your new balance is: ${balance:.2f}')\n",
    "  return True\n",
    "def another_process():\n",
    "  num =int(input('Do you want another process  1/Yes  ,2/No   '))\n",
    "  if num in [1,2]:\n",
    "    return num\n",
    "  else:\n",
    "    print('Invalid input. Please enter 1 or 2.')\n",
    "    return another_process()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4b4cf43-ea4a-4983-bad5-13154565df88",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d643de61-28a0-408c-853a-2d34eec75fbb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "969b1e93-b8c6-48da-a4dd-39f75ba52446",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12ef523f-29f8-4931-953f-7bd3cc9f073a",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
