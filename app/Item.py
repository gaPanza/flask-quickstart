class Item(object):
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def get_nome(self):
        return self.nome

    def get_descricao(self):
        return self.descricao

    def get_preco(self):
        return self.preco