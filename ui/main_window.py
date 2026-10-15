from PySide6 import QtCore, QtWidgets
from services.Playlist_controller import PlaylistController

class MyMainWidgets(QtWidgets.QWidget):
    def __init__(self, playlist_controller: PlaylistController):
        super().__init__()
        self.playlist_controller = playlist_controller
        
        self.setWindowTitle("Music Controller")

       
        # entr  ada

        
        self.input_nome_musica = QtWidgets.QLineEdit()
        self.input_link_musica = QtWidgets.QLineEdit()

        
        #texto
        self.texto = QtWidgets.QLabel("Playlist de Músicas")
        self.texto_selecionado = QtWidgets.QLabel("Nenhuma musica selecionada")
        self.label_nome_musica = QtWidgets.QLabel("Nome da música")
        self.label_link_musica = QtWidgets.QLabel("Link da música")
        
        #Botões
        self.botao_excluir_selecionado = QtWidgets.QPushButton("Excluir música")
        self.botao_cadastrar = QtWidgets.QPushButton("Cadastrar")
        self.botao_editar = QtWidgets.QPushButton("Editar música")
        self.botao_salvar_edicao = QtWidgets.QPushButton("Salvar edição")

        #Lista de Musicas (Objeto de Widgets)
        self.lista_musicas_widget = QtWidgets.QListWidget()


       

        #Renderização
        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.label_nome_musica)
        self.layout.addWidget(self.input_nome_musica)
        self.layout.addWidget(self.label_link_musica)
        self.layout.addWidget(self.input_link_musica)

        self.layout.addWidget(self.botao_cadastrar)
   
        self.layout.addWidget(self.texto)
        self.layout.addWidget(self.lista_musicas_widget)
        self.layout.addWidget(self.texto_selecionado)
        self.layout.addWidget(self.botao_excluir_selecionado)
        self.layout.addWidget(self.botao_editar)
        self.layout.addWidget(self.botao_salvar_edicao)

        self.botao_cadastrar.clicked.connect(self.cadastrar)
        self.botao_excluir_selecionado.clicked.connect(self.excluir_selecionado)
        self.lista_musicas_widget.itemSelectionChanged.connect(self.mostrar_selecionado)
        self.botao_editar.clicked.connect(self.editar_selecionado)
        self.botao_salvar_edicao.clicked.connect(self.salvar_edicao)

        for musica in self.playlist_controller.listar():
            self.lista_musicas_widget.addItem(musica.nome)
        
    @QtCore.Slot()
 

    def cadastrar(self):
        nome = self.input_nome_musica.text().strip()
        link = self.input_link_musica.text().strip()

        if nome and link:
            salvou = self.playlist_controller.cadastrar(nome, link)

            self.lista_musicas_widget.addItem(nome)
            self.input_nome_musica.clear()
            self.input_link_musica.clear()

            if not salvou:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Atenção",
                    "A música foi cadastrada, mas não foi salva no arquivo."
                )
        else:
            QtWidgets.QMessageBox.warning(
                self,
                "Atenção",
                "Preencha o nome e o link da música."
            ) 
    def mostrar_selecionado(self):
        pos_item_atual = self.lista_musicas_widget.currentRow()
        musicas = self.playlist_controller.listar()

        if 0 <= pos_item_atual < len(musicas):
            musica = musicas[pos_item_atual]
            self.texto_selecionado.setText(
                f"Música: {musica.nome}\nLink: {musica.link}"
            )
        else:
            self.texto_selecionado.setText("Nenhuma música selecionada")
    def excluir_selecionado(self):
        pos_item_atual = self.lista_musicas_widget.currentRow()

        if pos_item_atual != -1:
            salvou = self.playlist_controller.excluir(pos_item_atual)
            self.lista_musicas_widget.takeItem(pos_item_atual)
            self.mostrar_selecionado()

            if not salvou:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Atenção",
                    "A música foi excluída da memória, mas não foi salva no arquivo."
                )

    def editar_selecionado(self):
        pos_item_atual = self.lista_musicas_widget.currentRow()
        
        if pos_item_atual != -1:
            musicas = self.playlist_controller.listar()

            self.input_nome_musica.setText(musicas[pos_item_atual].nome)
            self.input_link_musica.setText(musicas[pos_item_atual].link)

    def salvar_edicao(self):
        pos_item_atual = self.lista_musicas_widget.currentRow()

        if pos_item_atual != -1:
            nome = self.input_nome_musica.text().strip()
            link = self.input_link_musica.text().strip()

            if nome and link:
                if not self.playlist_controller.editar(pos_item_atual, nome,link):
                    QtWidgets.QMessageBox.warning(self,"Atenção","A música foi editada da memória, mas não foi salva no arquivo.")
                self.lista_musicas_widget.item(pos_item_atual).setText(nome)
                self.mostrar_selecionado()
                self.input_link_musica.clear()
                self.input_nome_musica.clear()
            else:
                QtWidgets.QMessageBox.warning(self,"Atenção", "Preencha o nome e o link da música")
            
    