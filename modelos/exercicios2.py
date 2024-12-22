class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro('hb20', 'cinza', '2012')

print(vars(carro1))

class Restaurante:
    def __init__(self, nome, categoria, custo, avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.custo = custo
        self.avaliacao = avaliacao

    def __str__(self):
        return f'nome: {self.nome}| categoria: {self.categoria}'


    
restaurante1 = Restaurante('jojo ramen', 'japonesa', 'caro', '5 estrelas' )
print(restaurante1)

print(vars(restaurante1))

class Cliente():
    def __init__(self, nome, idade, sexo, categoria):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.categoria = categoria

    def __str__(self):
        return f'{self.nome}, {self.idade}, {self.sexo}, {self.categoria}'

cliente1 = Cliente('bob', 34, 'M', 'premium')
print(cliente1)

    
        