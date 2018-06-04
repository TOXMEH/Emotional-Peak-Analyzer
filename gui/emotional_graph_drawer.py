import numpy as np
from PyQt5.QtWidgets import *
from zigzag import peak_valley_pivots

from gui_forms.emotional_graph import Ui_Form
from model.emotion_type import EmotionType
from model.exchange_value_name import ExchangeValueName
from services.plots import plot_pivots
from tools.analyzed_submissions import get_emotions_between


class EmotionalGraphDrawer(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(EmotionalGraphDrawer, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushbutton_event_hadler)

    def pushbutton_event_hadler(self):
        epsilom = self.doubleSpinBox.value()
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
        em_arr = get_emotions_between(start_date, finish_date)
        emotion_arr = []
        date_arr = []
        for post in em_arr:
            date_arr.append(post['date'].date())
            corpora = post['corpora']
            for el in corpora:
                if el['name'] == corpora_name.value:
                    if emotion_type == EmotionType.POSITIVE:
                        emotion_arr.append(el['positive_mentions'])
                    else:
                        emotion_arr.append(el['negative_mentions'])
        # date_arr = [p['date'].date() for p in em_arr]

        X = np.array(emotion_arr)
        date_arr = np.array(date_arr)

        emotion_arr[0] += 1
        start_pos = 0
        i = 1
        zeros = 0
        while i < len(emotion_arr):
            emotion_arr[i] += 1
            # if emotion_arr[i] > 0:
            #     print(emotion_arr[i])
            if emotion_arr[i] == 1:
                zeros += 1
            elif zeros > 0:
                j = start_pos + 1
                step = abs(emotion_arr[i] - emotion_arr[start_pos]) / (i - start_pos)
                if step == 0:
                    step = 0.001
                while j < i:
                    if emotion_arr[i] >= emotion_arr[start_pos]:
                        emotion_arr[j] = np.math.ceil(step * (j - start_pos))
                    else:
                        emotion_arr[j] = np.math.ceil(step * (i - j - start_pos))
                    j += 1
                zeros = 0
                start_pos = i
            else:
                start_pos = i
            i += 1
        emotion_arr = [x if x != 0 else 0.1 for x in emotion_arr]

        pivots = peak_valley_pivots(np.array(emotion_arr).astype(np.double), epsilom,
                                    (-1) * epsilom)

        plot_pivots(X, pivots, date_arr)
