from PyQt5.QtWidgets import QMainWindow

from gui.exchange_viewer import ExchangeViewer
from gui_forms.main_window_form import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # # Make some local modifications.
        # self.colorDepthCombo.addItem("2 colors (1 bit per pixel)")
        #
        # # Connect up the buttons.
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.exchange_viewer_widget = ExchangeViewer(self)

    def on_pushButton_clicked(self):
        self.exchange_viewer_widget.show()
