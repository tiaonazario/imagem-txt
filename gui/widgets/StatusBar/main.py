from gui.tools.GridLayout.main import GridLayout
from qt_packages import *
from gui.widgets.StatusBar.styles import *


class StatusBar(QWidget):
    def __init__(self):
        super().__init__()

        ##################################################################
        # Instantiatle the objects
        self.Label_Copyright = QLabel("© 2022 - By Tião Nazário")
        self.Label_Line = QLabel()

        ##################################################################
        # Add to layout
        self.Grid = GridLayout(self)
        self.Grid.addWidget(self.Label_Line, 0, 0)
        self.Grid.addWidget(self.Label_Copyright, 1, 0, Qt.AlignHCenter)

        ##################################################################
        # Configure sizes
        self.setFixedSize(500, 20)
        self.Label_Line.setFixedHeight(1)

        ##################################################################
        # Configure style sheets
        self.Label_Line.setStyleSheet(css_Label_Line)
