import sys

from PyQt5.QtWidgets import QApplication

from gui.emotional_graph_drawer import EmotionalGraphDrawer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EmotionalGraphDrawer()

    window.show()
    sys.exit(app.exec_())
