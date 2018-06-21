from src.Item import Item
from src.Card import Card


class BuyOrder(object):
    item_list = []
    quantity_list = []
    total_price = 0

    def add_product(self, item, quantity):
        answer = self.search_product(item)
        if (answer is None):
            self.item_list.append(item)
            self.quantity_list.append(quantity)
            self.total_price += item.get_preco() * quantity
        else:
            self.quantity_list[answer[1]] += quantity
            self.total_price += quantity * item.get_preco()

    def remove_product(self, item):
        answer = self.search_product(item)
        if (answer is not None):
            self.total_price -= answer[0].get_preco()
            self.item_list.remove(answer[0])
            self.quantity_list.pop(answer[1])

    def get_item_list_name(self):
        return self.item_list

    def get_total_price(self):
        return self.total_price

    def pagar_conta(self, wallet):
        wallet.sacar_dinheiro(self.get_total_price())

    def search_product(self, item):
        j = 0
        for i in self.item_list:
            if (hasattr(item, 'get_nome') and i.get_nome() == item.get_nome()) or (i.get_nome() == item):
                return i, j
            j += 1
        return None
