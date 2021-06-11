import sys
from PySide2.QtWidgets import QApplication, QWidget


class Form():
    def ManinWindow(self, Window):
        win.setWindowTitle("PySide2 GUI")
        win.resize(400, 300)


# __Main__
if __name__ == '__main__':
    app = QApplication(sys.argv)
    F = Form()
    win = QWidget()
    F.ManinWindow(win)
    win.show()
    sys.exit(app.exec_())
