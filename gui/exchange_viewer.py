import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import *
from zigzag import peak_valley_pivots

from gui_forms.exchange_viewer_form import Ui_Form
from model.exchange_value import get_exchange_values_between
from model.exchange_value_name import ExchangeValueName


class ExchangeViewer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ExchangeViewer, self).__init__()

        self.setupUi(self)

        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    def plot_pivots(self, X, pivots, date_arr):
        plt.xlim(min(date_arr), max(date_arr))
        plt.ylim(X.min() * 0.99, X.max() * 1.01)
        plt.plot(date_arr, X, 'k:', alpha=0.5)
        plt.plot(date_arr[pivots != 0], X[pivots != 0], 'k-')
        plt.scatter(date_arr[pivots == 1], X[pivots == 1], color='g')
        plt.scatter(date_arr[pivots == -1], X[pivots == -1], color='r')
        plt.show()

    def on_pushButton_clicked(self):
        epsilom = self.doubleSpinBox.value()
        start_date = self.dateEdit.date().toPyDate()
        finish_date = self.dateEdit_2.date().toPyDate()
        exchange_value_name = None
        if self.radioButton.isChecked():
            exchange_value_name = ExchangeValueName.EUR
        elif self.radioButton_2.isChecked():
            exchange_value_name = ExchangeValueName.GBP
        elif self.radioButton_3.isChecked():
            exchange_value_name = ExchangeValueName.JPY
        ex_arr = get_exchange_values_between(start_date, finish_date)
        exchange_arr = [getattr(ex_el, exchange_value_name.value) for ex_el in ex_arr]
        date_arr = [p.date_val for p in ex_arr]

        X = np.array(exchange_arr)
        date_arr = np.array(date_arr)
        pivots = peak_valley_pivots(X, epsilom, (-1) * epsilom)

        self.plot_pivots(X, pivots, date_arr)
