from PyQt5 import QtWidgets, uic
from service import CalculadoraService
class CalculadoraController:

    def __init__(self) -> None:
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/calculadora_prototipo.ui")
        self.ventana.btncalcular.clicked.connect(self.onclickbtncalcular)
        self.ventana.show()
        app.exec()
    
    def onclickbtncalcular(self):
        resultado = 0
        operacion = ""
        try:
            num1 = int(self.ventana.txtnumero1.text())
            num2 = int(self.ventana.txtnumero2.text())
            if self.ventana.rbsuma.isChecked():
                resultado = CalculadoraService.suma(num1, num2)
                operacion = "Suma"
            elif self.ventana.rbresta.isChecked():
                resultado = CalculadoraService.resta(num1, num2)
                operacion = "Resta"
            elif self.ventana.rbmultiplica.isChecked():
                resultado = CalculadoraService.multiplicacion(num1, num2)
                operacion = "Multiplicación"
            elif self.ventana.rbdivide.isChecked():
                resultado = CalculadoraService.division(num1, num2)
                operacion = "División"
            else:
                resultado = 0
                operacion = "Elegir Operacion"
        except:
            operacion = "Ingresar valores numéricos"
        finally:
            self.ventana.lblresultado.setText(operacion+" = "+str(resultado))