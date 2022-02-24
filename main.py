import sys
from gui.pages.Home.main import Home
from gui.tools.GridLayout.main import GridLayout
from gui.widgets.MenuBar.main import MenuBar
from gui.widgets.StatusBar.main import StatusBar
from styles import *
from qt_packages import *


class App(QMainWindow):
    def __init__(self):
        super().__init__()

        ##################################################################
        # Remove items
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        ##################################################################
        # Instantiatle the objects
        self.CentralWidget = QWidget()
        self.MenuBar = MenuBar(self)
        self.PageContents = Home()
        self.StatusBar = StatusBar()

        ##################################################################
        # Add to layout
        self.setCentralWidget(self.CentralWidget)
        self.Grid = GridLayout(self.CentralWidget)
        self.Grid.addWidget(self.MenuBar, 0, 0)
        self.Grid.addWidget(self.PageContents, 1, 0)
        self.Grid.addWidget(self.StatusBar, 2, 0)

        ##################################################################
        # Configure sizes
        self.setFixedSize(500, 600)

        ##################################################################
        # Configure style sheets
        self.CentralWidget.setStyleSheet(css_CentralWidget)
        self.MenuBar.setStyleSheet(css_MenuBar)
        self.PageContents.setStyleSheet(css_PageContents)
        self.StatusBar.setStyleSheet(css_StatusBar)


if __name__ == "__main__":
    _app = QApplication(sys.argv)
    app = App()
    app.show()

    sys.exit(_app.exec())
