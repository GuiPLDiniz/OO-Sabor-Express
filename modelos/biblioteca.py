from exercicios5 import Livro
livro_bibilioteca = Livro('o aluguel', 'bob', 2012)

print(f'antes de emprestar: Disponibilidade: {livro_bibilioteca.disponivel}')
livro_bibilioteca.emprestar()
print(f'depois de emprestar: Disponibilidade: {livro_bibilioteca.disponivel}')


ano_especifico = 2012
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f'livros disponiveis em {ano_especifico}: {livros_disponiveis_ano}')