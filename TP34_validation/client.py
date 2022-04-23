from PyQt5.QtWidgets import(
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox
)
import requests
import sys

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initIG()

    def initIG(self):
        self.setWindowTitle("Multiplication égyptienne")
        self.setFixedSize(530,400)
        self.lblAvalue = QLabel("Enter A value:", self)
        self.lblAvalue.move(10,10)
        self.inputAvalue = QLineEdit(self)
        self.inputAvalue.move(10,40)
        self.lblBvalue = QLabel("Enter B value", self)
        self.lblBvalue.move(10,70)
        self.inputBvalue = QLineEdit(self)
        self.inputBvalue.move(10,100)
        self.lblNbIt = QLabel("Resultat de la multiplication et nombre d'itération pour obtenir le resultat", self)
        self.lblNbIt.move(50, 180)
        self.lblResultat = QLabel("", self)
        self.lblResultat.move(50,210)
        self.button = QPushButton("Calcul", self)
        self.button.move(10, 130)
        self.show()
        self.button.clicked.connect(self.on_click)


    def on_click(self):
        if(self.inputBvalue.text() != "" and self.inputAvalue.text() != "" and self.inputAvalue.text().isnumeric() and self.inputAvalue.text().isnumeric()):
            A = int(self.inputAvalue.text())
            B = int(self.inputBvalue.text())
            resultServ = self.__query(A, B)
            print(resultServ)
            if resultServ:
                self.lblResultat.setText(f"{A} * {B} = {resultServ['ABmulti']} obtenu en {resultServ['multiIT']} iterations")
                self.lblResultat.adjustSize()
                self.show()   
        else:
            QMessageBox.about(self, "Error", "Les facteurs indiqués sont incorrectes. Veillez insérer des entiers !")

    def __query(self, Avalue :int, Bvalue :int):
        url = "http://%s/multiEgy/?I1=%d&I2=%d" % ("localhost:8000",Avalue,Bvalue)
        print(url)
        req = requests.get(url)
        if(req.status_code == requests.codes.NOT_FOUND):
            QMessageBox.about(self, "Error", "IP not found")
        if(req.status_code == requests.codes.OK):
            return req.json()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()