from gui.tools.GridLayout.main import GridLayout
from gui.widgets.Output.main import Output
from gui.widgets.RBFrame.main import RBFrame
from gui.widgets.GetDir.main import GetDir
from gui.pages.Home.styles import *
from libs import *
from qt_packages import *


class Home(QWidget):
    def __init__(self):
        super().__init__()

        ##################################################################
        # Instantiatle the objects
        self.Label_TitlePage = QLabel("Img ➜ txt")
        self.GetDir_Images = GetDir("Images:")
        self.RBFrame = RBFrame(self.GetDir_Images)
        self.GetDir_Save = GetDir("Save:")
        self.Btn_Export = QPushButton()
        self.Output = Output()

        ##################################################################
        # Add to layout
        self.Grid = GridLayout(self, 10, (20, 20, 20, 20))
        self.Grid.addWidget(self.Label_TitlePage, 0, 0, Qt.AlignHCenter)
        self.Grid.addWidget(self.RBFrame, 1, 0, Qt.AlignHCenter)
        self.Grid.addWidget(self.GetDir_Images, 2, 0, Qt.AlignHCenter)
        self.Grid.addWidget(self.GetDir_Save, 3, 0, Qt.AlignHCenter)
        self.Grid.addWidget(self.Btn_Export, 4, 0, Qt.AlignHCenter)
        self.Grid.addWidget(self.Output, 5, 0, Qt.AlignHCenter)

        ##################################################################
        # Configure sizes
        self.Label_TitlePage.setFixedHeight(40)
        self.Btn_Export.setFixedSize(30, 30)
        self.Output.setFixedWidth(460)

        # Icons
        self.Btn_Export.setIcon(QIcon('img/icons/export'))
        self.Btn_Export.setIconSize(QSize(30, 30))

        ##################################################################
        # Configure style sheets
        self.Label_TitlePage.setStyleSheet(css_Label_TitlePage)
        self.Btn_Export.setStyleSheet(css_Btn)

        ##################################################################
        # Click
        self.Btn_Export.clicked.connect(self.click)

    def click(self):
        # self.Output.reset()
        try:
            path = self.GetDir_Images.getText()
            pathSave = self.GetDir_Save.getText()
            self.Output.reset()

            if self.GetDir_Images.rbCheck:
                convert = ImgsTxt(path, pathSave, self.Output)
                alert = convert.alert
            else:
                convert = ImgTxt(path, pathSave)
                alert = convert.alert
        except Exception:
            alert = "Error!"

        self.Output.add(alert)
