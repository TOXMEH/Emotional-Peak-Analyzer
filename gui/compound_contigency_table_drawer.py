from PyQt5.QtWidgets import *

from gui.ContigencyTable import ContigencyTable
from gui_forms.compound_contigency_table_form import Ui_Form
from model.emotion_type import EmotionType
from model.exchange_value_name import ExchangeValueName
from services.peaks import get_emotions, get_exchange_peaks, get_bears_and_bulls


class CompoundContingencyTableDrawer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(CompoundContingencyTableDrawer, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushbutton_event_hadler)

    def pushbutton_event_hadler(self):
        exchange_epsilom = self.doubleSpinBox.value()
        emotion_epsilom = self.spinBox.value()
        start_date = self.dateEdit.date().toPyDate()
        finish_date = self.dateEdit_2.date().toPyDate()
        exchange_value_name = None
        if self.radioButton.isChecked():
            exchange_value_name = ExchangeValueName.EUR
        elif self.radioButton_2.isChecked():
            exchange_value_name = ExchangeValueName.GBP
        elif self.radioButton_3.isChecked():
            exchange_value_name = ExchangeValueName.JPY

        exchange_arr, exchange_date_arr, exchange_pivots = get_exchange_peaks(start_date, finish_date,
                                                                              exchange_epsilom,
                                                                              exchange_value_name)

        second_index_type = None
        if self.verticalSlider_2.value() == 1:
            second_index_type = EmotionType.POSITIVE
        else:
            second_index_type = EmotionType.NEGATIVE

        native_emotion_pos_peak_arr, native_emotion_pos_peak_date_arr, native_emotion_pos_pivots = get_emotions(
            start_date, finish_date,
            exchange_value_name,
            EmotionType.POSITIVE, emotion_epsilom)
        native_emotion_neg_peak_arr, native_emotion_neg_peak_date_arr, native_emotion_neg_pivots = get_emotions(
            start_date, finish_date,
            exchange_value_name,
            EmotionType.NEGATIVE, emotion_epsilom)

        native_emotion_neg_peak_date_arr = native_emotion_neg_peak_date_arr[
            native_emotion_pos_pivots == 1]
        native_emotion_pos_peak_date_arr = native_emotion_pos_peak_date_arr[
            native_emotion_neg_pivots == 1]

        usd_emotion_pos_peak_arr, usd_emotion_pos_peak_date_arr, usd_emotion_pos_pivots = get_emotions(start_date,
                                                                                                       finish_date,
                                                                                                       ExchangeValueName.USD,
                                                                                                       EmotionType.POSITIVE,
                                                                                                       emotion_epsilom)
        usd_emotion_neg_peak_arr, usd_emotion_neg_peak_date_arr, usd_emotion_neg_pivots = get_emotions(start_date,
                                                                                                       finish_date,
                                                                                                       ExchangeValueName.USD,
                                                                                                       EmotionType.NEGATIVE,
                                                                                                       emotion_epsilom)

        usd_emotion_neg_peak_date_arr = usd_emotion_neg_peak_date_arr[usd_emotion_pos_pivots == 1]
        usd_emotion_pos_peak_date_arr = usd_emotion_pos_peak_date_arr[usd_emotion_neg_pivots == 1]

        native_bears_after_neg, native_bulls_after_neg = get_bears_and_bulls(exchange_date_arr, exchange_pivots,
                                                                             native_emotion_neg_peak_date_arr)

        native_bears_after_pos, native_bulls_after_pos = get_bears_and_bulls(exchange_date_arr, exchange_pivots,
                                                                             native_emotion_pos_peak_date_arr)

        usd_bears_after_neg, usd_bulls_after_neg = get_bears_and_bulls(exchange_date_arr, exchange_pivots,
                                                                       usd_emotion_neg_peak_date_arr)

        usd_bears_after_pos, usd_bulls_after_pos = get_bears_and_bulls(exchange_date_arr, exchange_pivots,
                                                                       usd_emotion_pos_peak_date_arr)

        if second_index_type == EmotionType.POSITIVE:
            native_bears_after_neg += usd_bears_after_neg
            native_bulls_after_neg += usd_bulls_after_neg
            native_bears_after_pos += usd_bears_after_pos
            native_bulls_after_pos += usd_bulls_after_pos
        else:
            native_bears_after_neg += usd_bears_after_pos
            native_bulls_after_neg += usd_bulls_after_pos
            native_bears_after_pos += usd_bears_after_neg
            native_bulls_after_pos += usd_bulls_after_neg

        self.contigency_table = ContigencyTable(self)
        self.contigency_table.set_parameters(native_bears_after_neg, native_bulls_after_neg, native_bears_after_pos,
                                             native_bulls_after_pos)
        self.contigency_table.show()
