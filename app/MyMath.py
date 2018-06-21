class DivisionByZero(Exception):
    pass


class MyMath(object):

    def soma(self, a, b):
        return a+b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if (b > 0):
            return a/b
        else:
            raise DivisionByZero

    def fatorial(self, a):
        total = 1
        for i in range(2, a+1):
            total *= i

        return total

    def elevar(self, a, b):
        if (b > 0):
            total = a
            for i in range(1, b):
                total *= a
            return total
        else:
            return 1

    def mod(self, a, b):
        if (b > 0):
            return a % b
        else:
            raise DivisionByZero

    def binario_para_decimal(self, a):
        decimal = 0
        count = 0
        for i in str(a)[::-1]:
            decimal += int(i) * self.elevar(2, count)
            count += 1
        return decimal

    def decimal_para_binario(self, a):
        binario = ''
        while (a > 1):
            binario += str(a % 2)
            a = int(a / 2)
        binario += str(a % 2)
        binario = binario[::-1]
        return int(binario)
