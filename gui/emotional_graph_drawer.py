from PyQt5.QtWidgets import *

from gui_forms.emotional_graph import Ui_Form
from model.emotion_type import EmotionType
from model.exchange_value_name import ExchangeValueName
from services.peaks import get_emotion_peaks
from services.plots import plot_pivots


class EmotionalGraphDrawer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(EmotionalGraphDrawer, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushbutton_event_hadler)

    def pushbutton_event_hadler(self):
        epsilom = self.doubleSpinBox.value()
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

        emotion_arr, date_arr, pivots = get_emotion_peaks(start_date, finish_date, epsilom,
                                                          exchange_value_name, emotion_type)

        plot_pivots(emotion_arr, pivots, date_arr)
