import time
import sys
from PyQt5.QtCore import Qt, QThread
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from reverse_timer_form import Ui_MainWindow
from config import MY_STYLESHEET_OFF, MY_STYLESHEET_ON


class Work(QThread):
    finish_signal = QtCore.pyqtSignal()

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.start_alarm = False

    def run(self):
        """Запускает таймер в отдельном потоке"""
        hours = self.main_window.ui.spinBox_hour.value()
        minutes = self.main_window.ui.spinBox_min.value()
        seconds = self.main_window.ui.spinBox_sec.value()
        hours *= 3600
        minutes *= 60
        total_timer = sum([hours, minutes, seconds])
        while total_timer:
            minute, sec = divmod(total_timer, 60)
            self.main_window.ui.spinBox_hour.setValue(total_timer // 3600)
            self.main_window.ui.spinBox_min.setValue(minute % 60)
            self.main_window.ui.spinBox_sec.setValue(sec)
            time.sleep(1)
            total_timer -= 1
        else:
            self.main_window.ui.spinBox_hour.setValue(0)
            self.main_window.ui.spinBox_hour.setValue(0)
            self.main_window.ui.spinBox_sec.setValue(0)
            self.finish_signal.emit()


class MyReverseTimer(QWidget):
    def __init__(self):
        super(MyReverseTimer, self).__init__(parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.ProgressThread_instance = Work(main_window=self)
        self.ui.pushButton_start.clicked.connect(self.starting_a_thread)
        self.ui.pushButton_stop.clicked.connect(self.stop_a_thread)
        self.ProgressThread_instance.finish_signal.connect(self.end_the_timer)

    def end_the_timer(self):
        """При завершении таймера восстанавливает кнопки вверх и вниз"""
        self.ui.pushButton_start.show()
        self.ui.spinBox_hour.setStyleSheet(MY_STYLESHEET_ON)
        self.ui.spinBox_min.setStyleSheet(MY_STYLESHEET_ON)
        self.ui.spinBox_sec.setStyleSheet(MY_STYLESHEET_ON)
        self.ui.pushButton_stop.hide()

    def starting_a_thread(self):
        """Запускаем отдельный поток"""
        self.ProgressThread_instance.start()
        self.ui.spinBox_hour.setStyleSheet(MY_STYLESHEET_OFF)
        self.ui.spinBox_min.setStyleSheet(MY_STYLESHEET_OFF)
        self.ui.spinBox_sec.setStyleSheet(MY_STYLESHEET_OFF)
        self.ui.pushButton_start.hide()
        self.ui.pushButton_stop.show()

    def stop_a_thread(self):
        """Останавливает поток"""
        self.ProgressThread_instance.terminate()
        self.ui.pushButton_stop.hide()
        self.ui.pushButton_start.show()
        self.ui.spinBox_hour.setValue(self.ui.spinBox_hour.value())
        self.ui.spinBox_hour.setValue(self.ui.spinBox_min.value())
        self.ui.spinBox_sec.setValue(self.ui.spinBox_sec.value())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_prog = MyReverseTimer()
    main_prog.show()
    sys.exit(app.exec_())
