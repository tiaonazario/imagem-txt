from gui.tools.GridLayout.main import GridLayout
from gui.widgets.Output.styles import *
from qt_packages import *


class Output(QScrollArea):
    def __init__(self):
        super().__init__()

        self.TextEdit = QTextEdit()

        ##################################################################
        # Add to layout
        self.Grid = GridLayout(self)
        self.Grid.addWidget(self.TextEdit)

        ##################################################################
        # Configure style sheets
        self.setStyleSheet(css_Output)
        self.TextEdit.setStyleSheet(css_TextEdit)

    def add(self, text: str):
        self.TextEdit.append(text)

    def reset(self):
        self.TextEdit.setText("")
