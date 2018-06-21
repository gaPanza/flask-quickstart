class NotEnoughMoney(Exception):
    pass


class Card(object):
    def __init__(self, balance, owner):
        self.__balance = balance
        self.__owner = owner

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    def depositar_dinheiro(self, qntd):
        self.__balance += qntd

    def sacar_dinheiro(self, qntd):
        if (self.__balance - qntd) >= 0:
            self.__balance -= qntd
        else:
            raise NotEnoughMoney("Not enough money to withdraw")

    def transferir_dinheiro(self, qntd, card):
        self.sacar_dinheiro(qntd)
        card.depositar_dinheiro(qntd)