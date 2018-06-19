import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *

from gui_forms.histogram_drawer_form import Ui_Form
from model.emotion_type import EmotionType
from model.exchange_value_name import ExchangeValueName
from model.peak_type import PeakType
from services.peaks import get_emotions, get_exchange_peaks, get_next_exchange_peak


class HistogramDrawer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(HistogramDrawer, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushbutton_event_hadler)

    def pushbutton_event_hadler(self):
        exchange_epsilom = self.doubleSpinBox.value()
        emotion_epsilom = self.spinBox.value()
        start_date = self.dateEdit.date().toPyDate()
        finish_date = self.dateEdit_2.date().toPyDate()
        exchange_value_name = ExchangeValueName.JPY
        if self.radioButton.isChecked():
            exchange_value_name = ExchangeValueName.EUR
        elif self.radioButton_2.isChecked():
            exchange_value_name = ExchangeValueName.GBP

        emotion_type = EmotionType.NEGATIVE
        if self.verticalSlider.value() == 1:
            emotion_type = EmotionType.POSITIVE

        peak_type = PeakType.BULL
        if self.verticalSlider_2.value() == 1:
            peak_type = PeakType.BEAR

        _, exchange_peak_date_arr, exchange_pivots = get_exchange_peaks(start_date, finish_date,
                                                                        exchange_epsilom,
                                                                        exchange_value_name)

        if self.verticalSlider_3.value() == 1:
            exchange_value_name = ExchangeValueName.USD

        emotion_peak_arr, emotion_peak_date_arr = get_emotions(start_date, finish_date, exchange_value_name,
                                                               emotion_type)

        exchange_peak_date_arr = exchange_peak_date_arr[exchange_pivots == peak_type.value]
        emotion_peak_date_arr = emotion_peak_date_arr[emotion_peak_arr >= emotion_epsilom]

        significant_peak_arr = []
        lag_arr = []
        for el in emotion_peak_date_arr:

            next_exchange_peak = get_next_exchange_peak(el, exchange_peak_date_arr)

            if next_exchange_peak is not None:
                significant_peak_arr.append(el)
                lag = (next_exchange_peak - el).days
                lag_arr.append(lag)

        plt.hist(lag_arr, bins=len(lag_arr) * 2)
        plt.show()
