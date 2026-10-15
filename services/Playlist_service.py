from models.musica import Musica


class PlaylistService():
    def __init__(self):
        self._musicas = []

    def cadastrar(self, nome, link):
        musica = Musica(nome, link)
        self._musicas.append(musica)

    def editar(self, indice, nome, link):
        self._musicas[indice].nome = nome
        self._musicas[indice].link = link

    def excluir(self, indice):
        self._musicas.pop(indice)
    def listar(self):
        return self._musicas.copy()

    def definir_musicas(self, musicas):
        self._musicas = musicas