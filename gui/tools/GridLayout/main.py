from qt_packages import *


class GridLayout(QGridLayout):
    def __init__(self, widget: QWidget, spc: int = 0, cm: tuple = (0, 0, 0, 0)):
        super().__init__()

        widget.setLayout(self)

        self.setSpacing(spc)
        self.setContentsMargins(cm[0], cm[1], cm[2], cm[3])
