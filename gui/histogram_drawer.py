import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *

from gui_forms.histogram_drawer_form import Ui_Form
from model.emotion_type import EmotionType
from model.exchange_value_name import ExchangeValueName
from model.peak_type import PeakType
from services.peaks import get_emotion_peaks, get_exchange_peaks, get_next_exchange_peak


class HistogramDrawer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(HistogramDrawer, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushbutton_event_hadler)

    def pushbutton_event_hadler(self):
        exchange_epsilom = self.doubleSpinBox.value()
        emotion_epsilom = self.doubleSpinBox1.value()
        start_date = self.dateEdit.date().toPyDate()
        finish_date = self.dateEdit_2.date().toPyDate()
        exchange_value_name = None
        if self.radioButton.isChecked():
            exchange_value_name = ExchangeValueName.EUR
        elif self.radioButton_2.isChecked():
            exchange_value_name = ExchangeValueName.GBP
        elif self.radioButton_3.isChecked():
            exchange_value_name = ExchangeValueName.JPY
        emotion_type = None
        if self.verticalSlider.value() == 1:
            emotion_type = EmotionType.POSITIVE
        else:
            emotion_type = EmotionType.NEGATIVE
        peak_type = None
        if self.verticalSlider_2.value() == 1:
            peak_type = PeakType.BEAR
        else:
            peak_type = PeakType.BULL
        _, exchange_peak_date_arr, exchange_pivots = get_exchange_peaks(start_date, finish_date,
                                                                        exchange_epsilom,
                                                                        exchange_value_name)
        _, emotion_peak_date_arr, emotion_pivots = get_emotion_peaks(start_date, finish_date, emotion_epsilom,
                                                                     exchange_value_name, emotion_type)

        exchange_peak_date_arr = exchange_peak_date_arr[exchange_pivots == peak_type.value]
        emotion_peak_date_arr = emotion_peak_date_arr[emotion_pivots == 1]

        signifficant_peak_arr = []
        lag_arr = []
        for el in emotion_peak_date_arr:

            next_exchange_peak = get_next_exchange_peak(el, exchange_peak_date_arr)

            if next_exchange_peak is not None:
                signifficant_peak_arr.append(el)
                lag = (next_exchange_peak - el).days
                lag_arr.append(lag)

        lag_arr.extend(lag_arr)
        lag_arr.extend(lag_arr)
        lag_arr.extend(lag_arr)
        plt.hist(lag_arr, bins=len(lag_arr) * 2)
        plt.show()
