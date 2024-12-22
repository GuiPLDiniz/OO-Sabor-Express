class Musica:
    def __init__(self, nome, artista, duracao):
        
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1= Musica('faint', 'Linkin Park', 240)
print(vars(musica1))

'''musica1 = Musica()

musica1.nome = 'faint'
musica1.artista = 'Linkin Park'
musica1.duracao = 3

musica2 = Musica()
musica2.nome = 'otherside'
musica2.artista = 'RHCP'
musica2.duracao = 5

musica3 = Musica()
musica3.nome = 'Lux Aeterna'
musica3.artista = 'metallica'
musica3.duracao = 5

print(vars(musica3))
print(f'Musica: {musica1.nome} banda: {musica1.artista} duração: {musica1.duracao}')'''