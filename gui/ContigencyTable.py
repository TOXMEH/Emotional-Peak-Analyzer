from PyQt5.QtWidgets import *
# from scipy import stats.fisher_exact
from scipy.stats import stats

from gui_forms.contigency_table import Ui_Form


class ContigencyTable(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ContigencyTable, self).__init__()
        self.setupUi(self)

    def set_parameters(self, bears_after_neg, bulls_after_neg, bears_after_pos, bulls_after_pos):
        self.tableWidget.setItem(0, 0, QTableWidgetItem(str(bears_after_pos)))
        self.tableWidget.setItem(0, 1, QTableWidgetItem(str(bulls_after_pos)))
        self.tableWidget.setItem(1, 0, QTableWidgetItem(str(bears_after_neg)))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(str(bulls_after_neg)))

        fisher_probability: float
        _, fisher_probability = stats.fisher_exact(
            [[bears_after_pos, bulls_after_pos], [bears_after_neg, bulls_after_neg]])

        self.label_3.setText(str(fisher_probability))
