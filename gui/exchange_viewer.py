from PyQt5.QtWidgets import *

from gui_forms.exchange_viewer_form import Ui_Form
from model.exchange_value_name import ExchangeValueName
from services.peaks import get_exchange_peaks
from services.plots import plot_pivots


class ExchangeViewer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ExchangeViewer, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushbutton_event_hadler)

    def pushbutton_event_hadler(self):
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

        exchange_arr, date_arr, pivots = get_exchange_peaks(start_date, finish_date, epsilom,
                                                            exchange_value_name)

        plot_pivots(exchange_arr, pivots, date_arr)
