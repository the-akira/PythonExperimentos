class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.nome, self.sobrenome)

    @property
    def nome_completo(self):
        return '{} {}'.format(self.nome, self.sobrenome)

    def __repr__(self):
        return "Pessoa('{}', '{}', {})".format(self.nome, self.sobrenome, self.idade)