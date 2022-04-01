from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys
import socket

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client_openstreetmap")
        self.setFixedSize(400, 400)
        self.label1 = QLabel("Enter your ip:", self)
        self.text1 = QLineEdit(self)
        self.text1.setText("localhost:8000")
        self.text1.move(15, 30)
        self.label2 = QLabel("Enter your API key Shodan:", self)
        self.label2.move(10, 60)
        self.text2 = QLineEdit(self)
        self.text2.move(15, 90)
        self.label3 = QLabel("Enter the ip to find its location:", self)
        self.label3.move(10, 120)
        self.text3 = QLineEdit(self)
        self.text3.move(15, 150)
        self.label4 = QLabel("Enter the website to find its location", self)
        self.label4.move(200, 120)
        self.text4 = QLineEdit(self)
        self.text4.move(200, 150)
        self.loc_IP = QLabel("IP: ", self)
        self.loc_IP.move(200, 190)
        self.loc_orga = QLabel("Organisation: ", self)
        self.loc_orga.move(200, 210)
        self.loc_country = QLabel("Country: ", self)
        self.loc_country.move(200, 230)
        self.loc_lat = QLabel("Latitude: ", self)
        self.loc_lat.move(200, 250)
        self.loc_long = QLabel("Longitude: ", self)
        self.loc_long.move(200, 270)
        self.button = QPushButton("Send", self)
        self.button.move(10, 200)

        self.button.clicked.connect(self.on_click)
        #self.button.pressed.connect(self.on_click)
        self.show()

    def on_click(self):
        hostname = self.text1.text()
        api_key =  self.text2.text()
        ip_loc = self.text3.text()
        dns_loc = self.text4.text()

        if hostname == "" or api_key == "" or not((ip_loc == "") ^ (dns_loc == "")) :
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            resultserv = self.__query(hostname, api_key, ip_loc, dns_loc)
            if resultserv:
                self.loc_IP.setText("IP: %s"%(resultserv["IP"]))
                self.loc_IP.adjustSize()
                self.loc_orga.setText("Organisation: %s"%(resultserv["Organization"]))
                self.loc_orga.adjustSize()
                self.loc_country.setText("Country: %s"%(resultserv["Country"]))
                self.loc_country.adjustSize()
                self.loc_lat.setText("Latitude: %s"%(resultserv["Latitude"]))
                self.loc_lat.adjustSize()
                self.loc_long.setText("Longitude: %s"%(resultserv["Longitude"]))
                self.loc_long.adjustSize()
                self.show()
                url = "https://www.openstreetmap.org/?mlat=%s&mlon=%s#map=12" % (resultserv["Latitude"],resultserv["Longitude"])
                QDesktopServices.openUrl(QUrl(url))

    def __query(self, hostname, api_key, ip_loc, dns_loc):
        if(dns_loc != "" and ip_loc == ""):
            ip_loc = socket.gethostbyname(dns_loc)
        url = "http://%s/ip/%s?key=%s" % (hostname,ip_loc,api_key)
        print(url)
        r = requests.get(url)
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()