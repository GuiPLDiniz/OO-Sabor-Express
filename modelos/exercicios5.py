class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self.disponivel = True

        
    def __str__(self):
        return f'livro: {self._titulo}, autor: {self._autor}, ano: {self._ano_publicacao}'
    
    def emprestar(self):
        self.disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis

    


livro1 = Livro('Nome do vento', "Patrick Rothfuss", 2012)
livro2 = Livro('O hobitt', 'Tolkien', 1920)
livro3 = Livro('ficticio', 'fulaninho', 2012)

Livro.livros = [livro1, livro2, livro3]

'''
print(livro1,'\n', livro2, f'disponibilidade = {livro2.disponivel}')

livro2.emprestar()
print(f'Livro 2 disponibilidade: {livro2.disponivel}')

Livro.livros = [livro1, livro2, livro3]

Livro.verificar_disponibilidade(2012)'''


