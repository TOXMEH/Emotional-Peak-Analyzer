from PyQt5.QtWidgets import *

from gui_forms.histogram_drawer_form import Ui_Form
from model.emotion_type import EmotionType
from model.exchange_value_name import ExchangeValueName
from model.peak_type import PeakType
from services.peaks import get_peaks


class HistogramDrawer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(HistogramDrawer, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushbutton_event_hadler)

    def pushbutton_event_hadler(self):
        start_date = self.dateEdit.date().toPyDate()
        finish_date = self.dateEdit_2.date().toPyDate()
        corpora_name = None
        if self.radioButton.isChecked():
            corpora_name = ExchangeValueName.EUR
        elif self.radioButton_2.isChecked():
            corpora_name = ExchangeValueName.GBP
        elif self.radioButton_3.isChecked():
            corpora_name = ExchangeValueName.JPY
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
        peak_arr = get_peaks(start_date, finish_date, corpora_name, emotion_type, peak_type)
