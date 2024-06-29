from PyQt5 import QtWidgets, uic
from service import MayorMenorService
class MayorMenorController:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frm_MayorMenor.ui")
        self.ventana.btncalcular.clicked.connect(self.onclickbtncalcular)
        self.ventana.show()
        app.exec()
    def onclickbtncalcular(self):
        resultado = 0
        try:
            n1 = int (self.ventana.txtnumero1.txt())
            n2= int (self.ventana.txtnumero2.txt())
            n3 = int (self.ventana.txtnumero3.txt())
            n4 = int (self.ventana.txtnumero4.txt())
            if self.ventana.rbmayor.isChecked():
                resultado = MayorMenorService.mayor(n1, n2, n3, n4)
            elif self.ventana.rbmenor.isChecked():
                resultado = MayorMenorService.menor(n1, n2, n3, n4)
            else:
                resultado = 0
        except:
            resultado = 0
        finally:
            self.ventana.lblresultado.setText(str(resultado))
