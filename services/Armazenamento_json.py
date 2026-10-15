import json


class ArmazenamentoJson():
    def __init__(self, pasta):
        self.caminho = pasta / "database" /  "musicas.json"

    def carregar(self):

        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                return json.load(arquivo)  
        except FileNotFoundError:
            return []

    def salvar(self, musicas):
        with open(self.caminho, "w", encoding="utf-8") as arquivo:
            dicionario_musicas = []
            for musica in musicas:
                dicionario_musicas.append(self.converte_musica_para_json(musica))    
            json.dump(dicionario_musicas, arquivo, indent=4)

    def converte_musica_para_json(self, musica):
        dicionario = {"nome": musica.nome, "link": musica.link}
        return dicionario
