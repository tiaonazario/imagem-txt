from gui.tools.GridLayout.main import GridLayout
from gui.widgets.GetDir.styles import *
from qt_packages import *


class GetDir(QWidget):
    def __init__(self, text: str = ""):
        super().__init__()

        ##################################################################
        # Initial properties
        # (True = Folder, False = File)
        self.rbCheck = True

        ##################################################################
        # Instantiatle the objects
        self.Label_Text = QLabel(text)
        self.LE_Path = QLineEdit('...')
        self.Btn_Folder = QPushButton()

        ##################################################################
        # Add to layout
        self.Grid = GridLayout(self, 10)
        self.Grid.addWidget(self.Label_Text, 0, 0)
        self.Grid.addWidget(self.LE_Path, 0, 1)
        self.Grid.addWidget(self.Btn_Folder, 0, 2)

        ##################################################################
        # Configure sizes
        self.setFixedSize(460, 25)
        self.Label_Text.setFixedSize(50, 25)
        self.LE_Path.setFixedHeight(25)
        self.Btn_Folder.setFixedHeight(25)

        # Icon
        self.Btn_Folder.setIcon(QIcon('img/icons/folder'))

        ##################################################################
        # Configure style sheets
        self.LE_Path.setStyleSheet(css_LE_Path)

        self.Btn_Folder.clicked.connect(self.getDir)

    def setRbCheck(self, rbCheck: bool = True):
        self.rbCheck = rbCheck

    def setDir(self, text: str = ""):
        self.LE_Path.setText(text)

    def getDir(self):
        if self.rbCheck:
            dir_name = QFileDialog.getExistingDirectory(self)
            self.setDir(dir_name)
        else:
            dir_name = QFileDialog.getOpenFileName(
                self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
            self.setDir(dir_name[0])

    def getText(self):
        return self.LE_Path.text()
