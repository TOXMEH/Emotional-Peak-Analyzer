from PyQt5.QtWidgets import QMainWindow

from gui.compound_contigency_table_drawer import CompoundContingencyTableDrawer
from gui.contigency_table_drawer import ContigencyTableDrawer
from gui.corpora_editor import CorporaEditor
from gui.emotional_graph_drawer import EmotionalGraphDrawer
from gui.exchange_viewer import ExchangeViewer
from gui.histogram_drawer import HistogramDrawer
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
        self.pushButton_2.clicked.connect(self.on_pushButton_2_clicked)
        self.emotional_graph_drawer = EmotionalGraphDrawer(self)
        self.pushButton_6.clicked.connect(self.on_pushButton_6_clicked)
        self.corpora_editor = CorporaEditor(self)
        self.pushButton_5.clicked.connect(self.on_pushButton_5_clicked)
        self.histogram_drawer = HistogramDrawer(self)
        self.pushButton_7.clicked.connect(self.on_pushButton_7_clicked)
        self.contigency_table_drawer = ContigencyTableDrawer(self)
        self.pushButton_8.clicked.connect(self.on_pushButton_8_clicked)
        self.compound_contingency_table_drawer = CompoundContingencyTableDrawer(self)

    def on_pushButton_clicked(self):
        self.exchange_viewer_widget.show()

    def on_pushButton_2_clicked(self):
        self.emotional_graph_drawer.show()

    def on_pushButton_6_clicked(self):
        self.corpora_editor.show()

    def on_pushButton_5_clicked(self):
        self.histogram_drawer.show()

    def on_pushButton_7_clicked(self):
        self.contigency_table_drawer.show()

    def on_pushButton_8_clicked(self):
        self.compound_contingency_table_drawer.show()
