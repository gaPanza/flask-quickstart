
import pytest
from src.BuyOrder import BuyOrder
from unittest.mock import *
from src.Card import Card
from src.Item import Item


class TestBuyOrder(object):
    @pytest.fixture
    def buy_order(self):
        return BuyOrder()

    @patch('src.Item.Item')
    def test_adicionar_produto(self, item, buy_order):
        item.get_preco.return_value = 10
        item.get_nome.return_value = "Produto"
        buy_order.add_product(item, 2)
        assert buy_order.search_product("Produto") is not None

    def test_remover_produto(self, buy_order):
        buy_order.remove_product("Produto")
        assert buy_order.search_product("Produto") is None

    @patch('src.Item.Item')
    def test_preco_total(self, item, buy_order):
        item.get_preco.return_value = 100
        item.get_nome.return_value = "Produto1"
        buy_order.add_product(item, 2)
        assert buy_order.get_total_price() == 200

    @patch('src.Card.Card')
    @patch('src.Item.Item')
    def test_pagar_conta(self, item, card, buy_order):
        item.get_preco.return_value = 100
        item.get_nome.return_value = "Produto1"
        buy_order.add_product(item, 2)
        card.get_balance.return_value = 0
        buy_order.pagar_conta(card)
        assert card.get_balance() == 0

    # def test_adicionar_produto(self, buy_order):
    #     item = Item("Produto", "lala", 10)
    #     buy_order.add_product(item, 2)
    #     assert buy_order.search_product("Produto") is not None
    #
    # def test_remover_produto(self, buy_order):
    #     buy_order.remove_product("Produto")
    #     assert buy_order.search_product("Produto") is None
    #
    # def test_preco_total(self, buy_order):
    #     item = Item("Produto1", "lala", 100)
    #     buy_order.add_product(item, 2)
    #     item = Item("Produto2", "lala", 200)
    #     buy_order.add_product(item, 1)
    #     item = Item("Produto3", "lala", 150)
    #     buy_order.add_product(item, 5)
    #     assert buy_order.get_total_price() == 100 * 2 + 200 * 1 + 150 * 5
    #
    # def test_pagar_conta(self, buy_order):
    #     item = Item("Produto1", "lala", 100)
    #     buy_order.add_product(item, 2)
    #     item = Item("Produto2", "lala", 200)
    #     buy_order.add_product(item, 1)
    #     item = Item("Produto3", "lala", 150)
    #     buy_order.add_product(item, 5)
    #     card = Card(1150, "Gustavo Albino")
    #     buy_order.pagar_conta(card)
    #     assert card.get_balance() == 0