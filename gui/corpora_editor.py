from PyQt5.QtWidgets import *

from gui_forms.corpora_editor_form import Ui_Form
from model.exchange_corpus import get_words_of_corpus
from model.exchange_value_name import ExchangeValueName


class CorporaEditor(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(CorporaEditor, self).__init__()
        self.setupUi(self)
        self.listWidget.itemActivated.connect(self.itemActivated_event)

    def itemActivated_event(self, item):
        self.label.setText(item.text())
        self.listWidget_2.clear()
        exchange_value_name = ExchangeValueName(item.text())
        items = get_words_of_corpus(exchange_value_name)
        self.listWidget_2.addItems(items)
