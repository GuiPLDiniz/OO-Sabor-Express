class Pessoa():
    def __init__(self, nome = '', idade =0, profissao=''):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return f'nome: {self._nome}, idade: {self._idade}, profissão: {self._profissao}'
    
    def aniversario(self):
        self._idade += 1

    @property
    def saudacao(self):
        if self._profissao:
            return f'Olá, sou {self._nome}! Trabalho como {self._profissao}.'
        else:
            return f'Olá, sou {self._nome}!'


    

pessoa1 = Pessoa(nome='bob',idade= 19, profissao='cozinheiro')
pessoa2 = Pessoa(nome='seu sirigueijo', idade=50, profissao='empresario')
pessoa3 = Pessoa(nome='patrick',idade= 21)

print(pessoa1)
print(pessoa2)
print(pessoa3)

pessoa1.aniversario()
pessoa2.aniversario()

print(pessoa1)
print(pessoa2)
print(pessoa3)

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)