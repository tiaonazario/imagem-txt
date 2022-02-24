from gui.tools import *
from gui.widgets.MenuBar.styles import *
from qt_packages import *


class MenuBar(QWidget):
    def __init__(self, widget: QMainWindow):
        super().__init__()

        self.widget = widget

        ##################################################################
        # Instantiatle the objects
        self.Label_Title = QLabel("Img ➜ txt")
        self.Btn_Minimize = QPushButton()
        self.Btn_Close = QPushButton()
        self.Label_Line = QLabel()

        ##################################################################
        # Add to layout
        self.Grid = GridLayout(self)
        self.Grid.addWidget(self.Label_Title, 0, 0, 1, 1)
        self.Grid.addWidget(self.Btn_Minimize, 0, 1, 1, 1)
        self.Grid.addWidget(self.Btn_Close, 0, 2, 1, 1)
        self.Grid.addWidget(self.Label_Line, 1, 0, 1, 3)

        ##################################################################
        # Settings
        # sizes
        self.setFixedSize(500, 30)
        self.Label_Title.setFixedHeight(30)
        self.Btn_Minimize.setFixedSize(40, 30)
        self.Btn_Close.setFixedSize(40, 30)
        self.Label_Line.setFixedHeight(1)

        # Icons
        self.Btn_Minimize.setIcon(QIcon('img/icons/minimize'))
        self.Btn_Close.setIcon(QIcon('img/icons/close'))

        ##################################################################
        # Configure style sheets
        self.Label_Title.setStyleSheet(css_Label_Title)
        self.Btn_Minimize.setStyleSheet(css_Btn_Minimize)
        self.Btn_Close.setStyleSheet(css_Btn_Close)
        self.Label_Line.setStyleSheet(css_Label_Line)

        ##################################################################
        # Clicks
        self.mouseMoveEvent = self.moveItem
        self.Btn_Minimize.clicked.connect(self.widget.showMinimized)
        self.Btn_Close.clicked.connect(self.widget.close)

    def moveItem(self, event):
        if event.buttons() == Qt.LeftButton:
            self.widget.move(self.widget.pos() +
                             event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
