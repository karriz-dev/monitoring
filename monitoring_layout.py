from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("monitoring.ui")
        #self.ui.setWindowFlags(Qt.SplashScreen)
        self.ui.show()

    def change_status_text(self, message):
        self.ui.label_7.setText(""+message)

    def change_frame_color(self, r, g, b):
        stylesheet = "background-color: rgb({0}, {1}, {2})".format(r,g,b)
        print(stylesheet)
        self.ui.widget.setStyleSheet(stylesheet)
        self.ui.widget_2.setStyleSheet(stylesheet)
        self.ui.widget_3.setStyleSheet(stylesheet)
        self.ui.widget_4.setStyleSheet(stylesheet)
        self.ui.widget_5.setStyleSheet(stylesheet)