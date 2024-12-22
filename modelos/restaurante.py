from modelos.avaliacao import Avaliacao

class Restaurante:
    '''Representa um restaurante e suas características'''

    restaurantes = []
    def __init__(self, nome, categoria):

        '''Inicializa uma instancia de Restaurante
        
            Parametros:
            - nome (str): O nome do restaurante;
            - categoria (str): a categoria do estaurante'''
        
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
        self._avaliacao = []

    def __str__(self):

        '''Retorna a representação em string do restaurante (o que vai retornar quando o restaurante é printado)'''
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_resaurantes(cls):
        '''Exibe a lista de todos os restaurantes'''
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        '''Retorna um símbolo indicando o estado de atividade do restaurante'''
        return '☒' if self._ativo else '☐'
    
    def alternar_estado(self):
        '''Altena o estado de ativo do restaurante'''
        self._ativo = not self._ativo

    
    def receber_avaliacao(self, cliente, nota):
        '''Função que registra uma avaliação para o restaurante
            Parâmetros:
            - cliente(str): O nome do cliente que realizou a avaliação;
            - nota(float): a nota que o cliente atribuiu ao restaurante'''
        if 0< nota < 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        '''retorna a media das avaliações de um restaurante'''
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    








'''
def cadastrar_restaurante_por_input():
    nome = input('digite o nome do restaurante: ')
    categoria = input('digite a categoria do restaurante: ')
    novo_restaurante = Restaurante(nome, categoria)
    return novo_restaurante

cadastrar_restaurante_por_input()
Restaurante.listar_resaurantes()'''

#print(vars(restaurante_pizza))
#print(restaurante_pizza)

'''nome_do_restaurante = restaurante_praca.nome
print(restaurante_praca.nome)
if restaurante_praca.ativo:
    print('o restaurante esta ativo')
else:
    print('o restaurante esta inativo')

categoria = Restaurante.categoria

restaurante_praca.nome = 'bistro'
print(restaurante_praca.nome, ',', restaurante_praca.categoria)
restaurante_pizza2 = Restaurante()
restaurante_pizza2.nome = 'pizza place'
restaurante_pizza2.categoria = 'fast food'
if restaurante_pizza2.categoria == 'fast food':
    print('a categoria é fast food')
else:
    print('a categoria não é fast food')

restaurante_pizza2.ativo = True'''