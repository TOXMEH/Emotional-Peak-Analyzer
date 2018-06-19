import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *

from gui_forms.score_viewer_form import Ui_Form
from model.reddit_submission import get_rates


class ScoreViewer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ScoreViewer, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushbutton_event_hadler)

    def pushbutton_event_hadler(self):
        start_date = self.dateEdit.date().toPyDate()
        finish_date = self.dateEdit_2.date().toPyDate()

        score_arr = [x.score for x in get_rates(start_date, finish_date)]

        plt.hist(score_arr, bins=len(score_arr) * 2)
        plt.show()
