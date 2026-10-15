import sys
from pathlib import Path
from PySide6 import QtWidgets

from services.Playlist_service import PlaylistService
from services.Armazenamento_json import ArmazenamentoJson
from services.Playlist_controller import PlaylistController

from ui.main_window import MyMainWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    pasta = Path(__file__).resolve().parent
    playlist_service = PlaylistService()
    armazenamento_json = ArmazenamentoJson(pasta)
    playlist_controller = PlaylistController(playlist_service, armazenamento_json)

    playlist_controller.carregar_playlist()


    widget = MyMainWidgets(playlist_controller)
    widget.resize(800,600)
    widget.show()

    sys.exit(app.exec())