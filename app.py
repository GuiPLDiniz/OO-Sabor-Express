
from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')


restaurante_praca.receber_avaliacao('bob', 10)
restaurante_praca.receber_avaliacao('patrick', 7)
restaurante_praca.receber_avaliacao('lula molusco', 2)

# restaurante_mexicano = Restaurante('mexican food', ' Mexicana')
# restaurante_japones = Restaurante('japa', 'Japonesa')
# restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_resaurantes()

if __name__ == '__main__':
    main()