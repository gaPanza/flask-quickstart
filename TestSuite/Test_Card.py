import pytest
from src.Card import Card, NotEnoughMoney


class TestCard(object):

    def setup(self):
        print("setup             class: %s", __name__)

    @pytest.fixture
    def carteira_cheia(self):
        return Card(200, "Gustavo Albino")

    @pytest.fixture
    def carteira_vazia(self):
        return Card(0, "Vinicius Albino")

    def test_get_owner(self, carteira_cheia):
        assert carteira_cheia.get_owner() == "Gustavo Albino"

    def test_depositar_dinheiro(self, carteira_vazia):
        carteira_vazia.depositar_dinheiro(200)
        assert carteira_vazia.get_balance() == 200

    def test_sacar_dinheiro(self, carteira_cheia):
        carteira_cheia.sacar_dinheiro(100)
        assert carteira_cheia.get_balance() == 100

    def test_sacar_dinheiro_sem_fundos(self, carteira_vazia):
        with pytest.raises(NotEnoughMoney):
            carteira_vazia.sacar_dinheiro(carteira_vazia.get_balance() + 0.0001)

    def test_transferir_dinheiro(self, carteira_cheia, carteira_vazia):
        carteira_cheia.transferir_dinheiro(100, carteira_vazia)
        assert carteira_cheia.get_balance() == 100 and carteira_vazia.get_balance() == 100

    def test_transferir_dinheiro_sem_fundos(self, carteira_vazia, carteira_cheia):
        with pytest.raises(NotEnoughMoney):
            carteira_vazia.transferir_dinheiro(100, carteira_cheia)
