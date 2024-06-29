from PyQt5 import QtWidgets, uic
class ComboSimpleController:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frm_lista_desplegables.ui")
        self.ventana.show()
        app.exec()
