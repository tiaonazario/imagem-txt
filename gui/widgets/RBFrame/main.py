from gui.tools.GridLayout.main import GridLayout
from gui.widgets.RBFrame.styles import *
from gui.widgets.GetDir.main import GetDir
from qt_packages import *


class RBFrame(QWidget):
    def __init__(self, getDir: GetDir):
        super().__init__()

        ##################################################################
        # Initial properties
        self.GetDir = getDir

        ##################################################################
        # Instantiatle the objects
        self.Rb_Folder = QRadioButton("Folder")
        self.Rb_File = QRadioButton("File")
        self.Frame_Spacer = QFrame()
        self.Label_Line = QLabel()

        ##################################################################
        # Add to layout
        self.Grid = GridLayout(self)
        self.Grid.addWidget(self.Rb_Folder, 0, 0, 1, 1)
        self.Grid.addWidget(self.Rb_File, 0, 1, 1, 1)
        self.Grid.addWidget(self.Frame_Spacer, 0, 2, 1, 1)
        self.Grid.addWidget(self.Label_Line, 1, 0, 1, 3)

        ##################################################################
        # Configure sizes
        self.setFixedSize(460, 20)
        self.Rb_Folder.setFixedWidth(60)
        self.Rb_File.setFixedWidth(60)
        self.Label_Line.setFixedHeight(1)

        ##################################################################
        # Configure style sheets
        self.Rb_Folder.setStyleSheet(css_Rb)
        self.Rb_File.setStyleSheet(css_Rb)
        self.Label_Line.setStyleSheet(css_Label_Line)

        ##################################################################
        # Click
        self.Rb_Folder.setChecked(True)
        self.Rb_Folder.toggled.connect(self.onClicked)

    def onClicked(self):
        self.GetDir.rbCheck = self.Rb_Folder.isChecked()
