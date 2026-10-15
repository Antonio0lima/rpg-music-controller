
from csv import Error

from models import musica
from models.musica import Musica

class PlaylistController():
    def __init__(self, playlist_service, armazenamento_json):
        self.playlist_service = playlist_service
        self.armazenamento_json = armazenamento_json

    def carregar_playlist(self):
        musicas = self.armazenamento_json.carregar()

        lista_musicas = []
        for musica in musicas:
            lista_musicas.append(Musica(musica["nome"], musica["link"]))
        self.playlist_service.definir_musicas(lista_musicas)

    def cadastrar(self, nome, link):
        self.playlist_service.cadastrar(nome, link)
        musicas = self.playlist_service.listar()
        try:
            
            self.armazenamento_json.salvar(musicas)

            return True
        except OSError:
            return False

    def editar(self, indice, nome, link):
        self.playlist_service.editar(indice, nome, link)

        musicas = self.playlist_service.listar()

        try:
            self.armazenamento_json.salvar(musicas)
            return True
        except OSError:
            return False

    def excluir(self, indice):
        self.playlist_service.excluir(indice)

        musicas = self.playlist_service.listar()

        try:
            self.armazenamento_json.salvar(musicas)
            return True
        except OSError:

            return False

    def listar(self):
        return self.playlist_service.listar()