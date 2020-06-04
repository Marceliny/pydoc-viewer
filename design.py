# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_temp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import get_modules
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 553)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.example = QtWidgets.QTextBrowser(self.centralwidget)
        self.example.setObjectName("example")
        self.gridLayout_5.addWidget(self.example, 1, 3, 1, 1)

        self.all_modules = QtWidgets.QListWidget(self.centralwidget)
        self.all_modules.setObjectName("all_modules")
        self.gridLayout_5.addWidget(self.all_modules, 0, 1, 1, 1)
        self.all_modules.itemSelectionChanged.connect(lambda: get_modules.list_functions(self))

        self.shell_output = QtWidgets.QTextBrowser(self.centralwidget)
        self.shell_output.setObjectName("shell_output")
        self.gridLayout_5.addWidget(self.shell_output, 1, 4, 1, 1)

        self.turkish_doc = QtWidgets.QTextBrowser(self.centralwidget)
        self.turkish_doc.setObjectName("turkish_doc")
        self.gridLayout_5.addWidget(self.turkish_doc, 1, 1, 1, 1)

        self.english_doc = QtWidgets.QTextBrowser(self.centralwidget)
        self.english_doc.setObjectName("english_doc")
        self.gridLayout_5.addWidget(self.english_doc, 0, 4, 1, 1)
        # self.english_doc.textChanged.connect(lambda: get_modules.print_doc_tr(self))


        self.all_funcs = QtWidgets.QListWidget(self.centralwidget)
        self.all_funcs.setObjectName("all_funcs")
        self.gridLayout_5.addWidget(self.all_funcs, 0, 3, 1, 1)
        self.all_funcs.itemSelectionChanged.connect(lambda: get_modules.print_doc(self))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyDoc Viewer"))


if __name__ == "__main__":
    import sys
    from main import mainloop
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    get_modules.list_modules(ui)
    sys.exit(app.exec_())

