import pytest
import sys
from src.MyMath import MyMath, DivisionByZero


@pytest.mark.skipif(sys.platform == 'linux', reason="nao roda no linux")
class TestMath(object):
    soma_valores = [(10, 10, 20), (20, 20, 40), (10, 20, 30)]
    divisao_valores = [(10, 2, 5), (10, 5, 2), (30, 10, 3), (3, 3, 1), (5, 2, 2.5)]
    multiplicacao_valores = [(10, 2, 20), (20, 5, 100), (100, 3, 300)]
    fatorial = [(5, 120), (4, 24)]
    elevacao_valores = [(2, 10, 1024), (5, 1, 5), (0, 10, 0)]
    mod_valores = [(10, 2, 0), (11, 2, 1), (10, 3, 1), (11, 3, 2), (12, 3, 0), (0, 2, 0)]
    binario_valores = [(1001, 9), (1111, 15), (0000, 0), (1101, 13), (111111, 63), (11011, 27), (1011, 11), (0, 0)]
    decimal_valores = [(10, 1010), (15, 1111), (63, 111111), (1, 1), (0, 0)]

    def setup(self):
        print("setup             class: %s", __name__)

    @pytest.fixture
    def math_class(self):
        return MyMath()

    @pytest.mark.parametrize('a, b, resultado', soma_valores)
    def teste_soma(self, math_class, a, b, resultado):
        assert math_class.soma(a, b) == resultado

    @pytest.mark.parametrize('a, b, resultado', divisao_valores)
    def teste_divisao(self, math_class, a, b, resultado):
        assert math_class.divisao(a, b) == resultado

    def teste_divisao_por_zero(self, math_class):
        with pytest.raises(DivisionByZero):
            math_class.divisao(10, 0)

    @pytest.mark.parametrize('a, b, resultado', multiplicacao_valores)
    def teste_multiplicacao(self, math_class, a, b, resultado):
        assert math_class.multiplicacao(a, b) == resultado

    @pytest.mark.parametrize('a, resultado', fatorial)
    def teste_fatorial(self, math_class, a, resultado):
        assert math_class.fatorial(a) == resultado

    def teste_fatorial_de_zero(self, math_class):
        assert math_class.fatorial(0) == 1

    @pytest.mark.parametrize('a, b, resultado', elevacao_valores)
    def teste_elevacao(self, math_class, a, b, resultado):
        assert math_class.elevar(a, b) == resultado

    def teste_elevar_a_zero(self, math_class):
        assert math_class.elevar(10, 0) == 1

    @pytest.mark.parametrize('a, b, resultado', mod_valores)
    def teste_mod(self, math_class, a, b, resultado):
        assert math_class.mod(a, b) == resultado

    def teste_mod_por_zero(self, math_class):
        with pytest.raises(DivisionByZero):
            math_class.mod(10, 0)

    @pytest.mark.parametrize('a, resultado', binario_valores)
    def teste_binario_decimal(self, math_class, a, resultado):
        assert math_class.binario_para_decimal(a) == resultado

    @pytest.mark.parametrize('a, resultado', decimal_valores)
    def teste_decimal_binario(self, math_class, a, resultado):
        assert math_class.decimal_para_binario(a) == resultado
