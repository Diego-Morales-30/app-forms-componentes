from PyQt5 import QtWidgets, uic
class ComboSimpleController:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frm_lista_desplegables.ui")
        self.agregarElementos()
        self.ventana.btnver.clicked.connect(self.verResultado)
        self.ventana.show()
        app.exec()
    
    def agregarElementos(self):
        self.ventana.cbopais.addItem("Perú", "PA01")
        self.ventana.cbopais.addItem("Argentina", "PA02")
        self.ventana.cbopais.addItem("Brasil", "PA03")
        self.ventana.cbopais.addItem("Uruguay", "PA04")
        paises = ["Chile", "Ecuador", "Venezuela"]
        self.ventana.cbopais.addItems(paises)
    
    def verResultado(self):
        textpais = self.ventana.cbopais.currentText()
        codpais = self.ventana.cbopais.currentData()
        index = self.ventana.cbopais.currentIndex()
        self.ventana.lblresultado.setText(textpais + 
                                          "-" + str(index))
    
