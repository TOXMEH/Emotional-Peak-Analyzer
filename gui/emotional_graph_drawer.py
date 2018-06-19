import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *

from gui_forms.emotional_graph import Ui_Form
from model.emotion_type import EmotionType
from model.exchange_value_name import ExchangeValueName
from services.peaks import get_emotions


class EmotionalGraphDrawer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(EmotionalGraphDrawer, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushbutton_event_handler)
        self.pushButton_2.clicked.connect(self.pushbutton2_event_handler)

    def get_form_values(self):
        self.epsilom = self.spinBox.value()
        self.start_date = self.dateEdit.date().toPyDate()
        self.finish_date = self.dateEdit_2.date().toPyDate()
        self.exchange_value_name = ExchangeValueName.JPY
        if self.radioButton.isChecked():
            self.exchange_value_name = ExchangeValueName.EUR
        elif self.radioButton_2.isChecked():
            self.exchange_value_name = ExchangeValueName.GBP

        self.emotion_type = EmotionType.NEGATIVE
        if self.verticalSlider.value() == 1:
            self.emotion_type = EmotionType.POSITIVE

        self.emotion_arr, self.date_arr = get_emotions(self.start_date, self.finish_date, self.exchange_value_name,
                                                       self.emotion_type)

    def pushbutton_event_handler(self):
        self.get_form_values()

        plt.xlim(min(self.date_arr), max(self.date_arr))
        plt.ylim(min(self.emotion_arr) * 0.99, max(self.emotion_arr) * 1.01)
        plt.plot(self.date_arr, self.emotion_arr, 'k:', alpha=0.5)
        plt.scatter(self.date_arr[self.emotion_arr >= self.epsilom], self.emotion_arr[self.emotion_arr >= self.epsilom],
                    color='g')
        plt.show()

    def pushbutton2_event_handler(self):
        self.get_form_values()
        plt.hist(self.emotion_arr, bins=len(self.emotion_arr) * 2)
        plt.show()
