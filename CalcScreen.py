import sys
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
QVBoxLayout, QWidget, QInputDialog, QMessageBox, QMainWindow)
import Calculations as C
import sqlite3
import StartScreen as SC

class VelocityCalculate(QDialog,QWidget):

    def __init__(self, title, left, top, width, height):
        super().__init__()
        self.combo = QComboBox(self)
        self.setWindowTitle(title)
        self.setGeometry(left, top, width, height)
        self.initUI()

    def initUI(self):
        self.combo.addItem("Knoten")
        self.combo.addItem("Km/h")
        self.textbox = QLineEdit(self)
        self.textbox.setText("")
        self.l1 = QLabel("Velocity")
        text = self.combo.itemText(self.combo.currentIndex()-1) if self.combo.currentIndex() == 1 else self.combo.itemText(self.combo.currentIndex() +1)
        self.l1.setText("Geschwindigkeit in " + text)
        self.cancel = QPushButton("Cancel")
        self.cancel.clicked.connect(self.close)
        self.calculate = QPushButton("Berechnen")
        self.calculate.clicked.connect(self.action)
        self.CreateGrid()
        self.windowLayout = QVBoxLayout()
        self.windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(self.windowLayout)

    def CreateGrid(self):
        self.horizontalGroupBox = QGroupBox("")
        self.mainLayout = QGridLayout()
        self.mainLayout.setColumnStretch(1, 4)
        self.mainLayout.setColumnStretch(2, 4)
        self.mainLayout.addWidget(self.combo,0,1)
        self.mainLayout.addWidget(self.textbox,0,0)
        self.mainLayout.addWidget(self.l1,1,0)
        self.mainLayout.addWidget(self.calculate,3,3)
        self.mainLayout.addWidget(self.cancel,3,2)
        self.horizontalGroupBox.setLayout(self.mainLayout)

    def action(self):
        if self.combo.currentIndex() == 1:
            value = C.FlightPath.distanceCalcculator(SC.start.b1.text(),self.combo.currentText(), int(self.textbox.text()))
            self.l1.setText("Geschwindigkeit in " + self.combo.itemText(self.combo.currentIndex()-1) + ": " + str(value))
        elif self.combo.currentIndex() == 0:
            value = C.FlightPath.distanceCalcculator(SC.start.b1.text(),self.combo.currentText(), int(self.textbox.text()))
            self.l1.setText("Geschwindigkeit in " + self.combo.itemText(self.combo.currentIndex()+1) + ": " + str(value))
