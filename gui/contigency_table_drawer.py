from PyQt5.QtWidgets import *

from gui.ContigencyTable import ContigencyTable
from gui_forms.contigency_form import Ui_Form
from model.emotion_type import EmotionType
from model.exchange_value_name import ExchangeValueName
from services.peaks import get_emotions, get_exchange_peaks, get_bears_and_bulls


class ContigencyTableDrawer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(ContigencyTableDrawer, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushbutton_event_hadler)

    def pushbutton_event_hadler(self):
        exchange_epsilon = self.doubleSpinBox.value()
        emotion_epsilon = self.spinBox.value()
        start_date = self.dateEdit.date().toPyDate()
        finish_date = self.dateEdit_2.date().toPyDate()

        exchange_value_name = ExchangeValueName.EUR
        if self.radioButton_2.isChecked():
            exchange_value_name = ExchangeValueName.GBP
        elif self.radioButton_3.isChecked():
            exchange_value_name = ExchangeValueName.JPY

        exchange_arr, exchange_date_arr, exchange_pivots = get_exchange_peaks(start_date, finish_date,
                                                                              exchange_epsilon,
                                                                              exchange_value_name)

        if self.verticalSlider_2.value() == 1:
            exchange_value_name = ExchangeValueName.USD

        emotion_pos_peak_arr, emotion_pos_peak_date_arr, emotion_pos_pivots = get_emotions(start_date, finish_date,
                                                                                           exchange_value_name,
                                                                                           EmotionType.POSITIVE,
                                                                                           emotion_epsilon)
        emotion_neg_peak_arr, emotion_neg_peak_date_arr, emotion_neg_pivots = get_emotions(start_date, finish_date,
                                                                                           exchange_value_name,
                                                                                           EmotionType.NEGATIVE,
                                                                                           emotion_epsilon)

        emotion_neg_peak_date_arr = emotion_neg_peak_date_arr[emotion_pos_pivots == 1]
        emotion_pos_peak_date_arr = emotion_pos_peak_date_arr[emotion_neg_pivots == 1]

        bears_after_neg, bulls_after_neg = get_bears_and_bulls(exchange_date_arr, exchange_pivots,
                                                               emotion_neg_peak_date_arr)

        bears_after_pos, bulls_after_pos = get_bears_and_bulls(exchange_date_arr, exchange_pivots,
                                                               emotion_pos_peak_date_arr)

        self.contigency_table = ContigencyTable(self)
        self.contigency_table.set_parameters(bears_after_neg, bulls_after_neg, bears_after_pos, bulls_after_pos)
        self.contigency_table.show()
