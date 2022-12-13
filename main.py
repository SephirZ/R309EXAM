# lien git :
import socket
import threading
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
client = socket.socket()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        lab1 = QLabel("Serveur ")
        lab2 = QLabel("Port")
        lab3 = QLabel("Message")
        self.__host = QLineEdit("127.0.0.1")
        self.__port = QLineEdit("coucou")
        self.__connexion = QPushButton("Connexion")
        self.__chat = QLineEdit("")
        self.__chat.setReadOnly(True)
        self.__msg = QLineEdit("")
        self.__msg.setReadOnly(True)
        self.__send = QPushButton("Envoyer")
        self.__send.setEnabled(False)
        quit = QPushButton("Quitter")
        delete = QPushButton("Effacer")
        grid.addWidget(lab1, 0, 0)
        grid.addWidget(self.__host, 0, 1)
        grid.addWidget(self.__port, 1, 1)
        grid.addWidget(self.__connexion, 2, 0, 1, 2)
        grid.addWidget(self.__chat,3,0,1,2)
        grid.addWidget(lab3, 4,0)
        grid.addWidget(self.__msg, 4, 1)
        grid.addWidget(self.__send, 5,0, 1, 2)
        grid.addWidget(delete,6,0)
        grid.addWidget(lab2, 1, 0)
        grid.addWidget(quit, 6, 1)
        self.__connexion.clicked.connect(self.initcon)
        quit.clicked.connect(self.actionQuitter)
        self.__send.clicked.connect(self.SendMsg)
        delete.clicked.connect(self.deletemsg)
        self.setWindowTitle("Un logiciel de chat")

    def initcon(self):
        if self.__connexion.text()=='Connexion':
            try:
                client.connect((str(self.__host.text()), int(self.__port.text())))
            except:
                msg2 = QMessageBox()
                msg2.setWindowTitle('Erreur')
                msg2.setText('Le serveur n\'est pas démarré')
                msg2.exec_()
            else:
                self.__connexion.setText('Deconnexion')
                self.__send.setEnabled(True)
                self.__msg.setReadOnly(False)
        else:
            self.__connexion.setText('Connexion')
            client.send('deco-server'.encode())

    def SendMsg(self):
        client.send(str(self.__msg.text()).encode())
        self.__chat.setText(str(self.__msg.text()))
        msg = client.recv(1024).decode()
        self.__chat.setText(msg)

    def deletemsg(self):
        self.__msg.setText('')

    def actionQuitter(self):
        client.send('deco-server'.encode())
        client.close()
        QCoreApplication.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
