from PyQt5 import QtWidgets, uic
class MayorMenorController:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frm_MayorMenor.ui")
        self.ventana.show()
        app.exec()