import sys
import traceback

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt

import os
import time
import re
import threading

import read_file_gui
import manually_dec_gui
import plot_settings_gui

import processing

TEXT = ''
PROCESSING_FLAG = 0


def log_uncaught_exceptions(ex_cls, ex, tb):
    error = f'{ex_cls.__name__}: {ex}:\n'
    error += ''.join(traceback.format_tb(tb))
    print(error)
    QtWidgets.QMessageBox.critical(None, 'Error', f'Непредвиденная ошибка\n\n{error}', )
    sys.exit()


sys.excepthook = log_uncaught_exceptions


class LogAnalysis(QtWidgets.QMainWindow):
    def __init__(self):
        super(LogAnalysis, self).__init__()
        self.ui = read_file_gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_filter.clicked.connect(self.time_filter)
        self.ui.pushButton_source.clicked.connect(self.source)
        self.ui.pushButton_find.clicked.connect(self.search)
        self.ui.pushButton_cmd.clicked.connect(self.text_decoding)
        self.ui.pushButton_new_search.clicked.connect(self.new_search)
        self.ui.pushButton_cancel_search.clicked.connect(self.cancel_new_search)
        self.ui.pushButton_man_dec.clicked.connect(self.manually_decoding)
        self.ui.pushButton_plot.clicked.connect(self.plot_settings)
        self.ui.pushButton_find_up.clicked.connect(self.find_up)
        self.ui.pushButton_find_down.clicked.connect(self.find_down)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.lineEdit_new_search.returnPressed.connect(self.new_search)
        self.ui.lineEdit_find.returnPressed.connect(self.search)

        self.statusbar_widgets = [QtWidgets.QLabel(''),
                                  QtWidgets.QLabel(''),
                                  QtWidgets.QLabel('')]
        self.statusbar_widgets[0].setFixedWidth(250)
        self.statusbar_widgets[1].setFixedWidth(130)
        self.statusbar_widgets[2].setFixedWidth(45)

        for i, lbl in enumerate(self.statusbar_widgets):
            self.statusbar_widgets[i].setStyleSheet('border: 0;')
            self.ui.statusbar.addPermanentWidget(lbl)
        self.ui.statusbar.setStyleSheet('border: 0;')

        self.app_man_dec = ManuallyDecoding()
        self.app_plot_settings = PlotSettings()

    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_F10 and e.modifiers() & Qt.ControlModifier:
    #         self.clear_format()
    #
    # def change_format(self):
    #     format_ = QtGui.QTextCharFormat()
    #     format_.setBackground(Qt.red)
    #     cursor = self.ui.plainTextEdit.textCursor()
    #     cursor.select(QtGui.QTextCursor.Document)
    #     cursor.mergeCharFormat(format_)
    #     # cursor.setPosition(0)
    #     # cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)

    def closeEvent(self, event):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Question)
        msg.setWindowIcon(QtGui.QIcon(':/icons/icons/Launcher.ico'))
        msg.setWindowTitle('LogAnalysis')
        msg.setText('Завершить работу?')
        yes_btn = msg.addButton('Да', QtWidgets.QMessageBox.AcceptRole)
        msg.addButton('Нет', QtWidgets.QMessageBox.RejectRole)

        msg.exec()

        if msg.clickedButton() == yes_btn:
            sys.exit()
        else:
            event.ignore()

    def open_file(self):
        file_name = QtWidgets.QFileDialog.getOpenFileName(self, filter='Файлы отчетов (*.rpt);;'
                                                                       'Текстовые файлы(*.txt);;Все файлы (*)')
        path = file_name[0]
        if path:
            global TEXT, PROCESSING_FLAG

            PROCESSING_FLAG = 0
            self.ui.label_dec_cnt.clear()
            self.ui.progressBar.setValue(0)
            TEXT = processing.open_file(os.path.abspath(path))
            if TEXT == 'Can_not_open':
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setWindowTitle('Ошибка')
                msg.setText('Невозможно открыть файл')
                msg.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
                msg.exec()
                return

            self.setWindowTitle('LogAnalysis - ' + path)
            try:
                date_pattern = r'\[(\d\d)\.(\d\d)\.(\d\d\d\d), (\d\d):(\d\d):(\d\d)'
                day, month, year, hour, minute, second = map(int, re.findall(date_pattern, TEXT[:50])[0])
                day_f, month_f, year_f, hour_f, minute_f, second_f = map(int, re.findall(date_pattern, TEXT[-300:])[0])
                self.ui.dateTimeEdit_1.setDateTime((QtCore.QDateTime(year, month, day, hour, minute, second)))
                self.app_plot_settings.ui.dateTimeEdit_start.setDateTime(QtCore.QDateTime(year, month, day,
                                                                                          hour, minute, second))
                self.ui.dateTimeEdit_2.setDateTime(QtCore.QDateTime(year_f, month_f, day_f, hour_f, minute_f, second_f))
                self.app_plot_settings.ui.dateTimeEdit_finish.setDateTime(QtCore.QDateTime(year_f, month_f, day_f,
                                                                                           hour_f, minute_f, second_f))
            except IndexError:
                pass

            self.set_text()

    def save_file(self):
        text = self.ui.plainTextEdit.toPlainText()
        file_name = QtWidgets.QFileDialog.getSaveFileName(self, filter='Файлы отчетов (*.rpt);;'
                                                                       'Текстовые файлы (*.txt);;Все файлы (*)')
        path = file_name[0]
        if path:
            processing.save_file(os.path.abspath(path), text)

    def progressbar(self):
        while not PROCESSING_FLAG:
            time.sleep(0.05)
            self.ui.progressBar.setValue(processing.PROGRESS)
        return

    def text_decoding(self):
        global PROCESSING_FLAG

        self.ui.plainTextEdit.setFocus()
        self.ui.pushButton_source.setEnabled(False)
        self.ui.pushButton_cmd.setEnabled(False)
        self.ui.pushButton_find.setEnabled(False)
        self.ui.pushButton_plot.setEnabled(False)
        self.ui.pushButton_filter.setEnabled(False)
        self.ui.pushButton_man_dec.setEnabled(False)
        self.ui.pushButton_new_search.setEnabled(False)

        if not TEXT:
            pass
        elif not PROCESSING_FLAG:
            time1 = time.perf_counter()
            text = self.ui.plainTextEdit.toPlainText()

            progressing = threading.Thread(target=self.progressbar, args=[])
            progressing.start()

            decoding_text = processing.cmd_decoding(text)

            self.ui.plainTextEdit.setPlainText(decoding_text)
            time2 = time.perf_counter()
            self.ui.label_dec_cnt.setText(f'Время обработки: {time2 - time1:.1f} c')

            PROCESSING_FLAG = 1

            progressing.join()
            self.ui.progressBar.setValue(100)

        self.ui.pushButton_source.setEnabled(True)
        self.ui.pushButton_cmd.setEnabled(True)
        self.ui.pushButton_find.setEnabled(True)
        self.ui.pushButton_plot.setEnabled(True)
        self.ui.pushButton_filter.setEnabled(True)
        self.ui.pushButton_man_dec.setEnabled(True)
        self.ui.pushButton_new_search.setEnabled(True)

    def new_search(self):
        if not self.ui.lineEdit_new_search.text():
            format_ = QtGui.QTextCharFormat()
            format_.clearBackground()
            cursor = self.ui.plainTextEdit.textCursor()
            cursor.select(QtGui.QTextCursor.Document)
            cursor.mergeCharFormat(format_)
            self.ui.label_search.clear()
        else:
            pattern = self.ui.lineEdit_new_search.text().lower()
            search_highlight = SearchHighLight(parent=self.ui.plainTextEdit.document())
            search_highlight.search_text(pattern)
            self.ui.label_search.setText(f'Результатов: {search_highlight.counter}')
            self.ui.plainTextEdit.textCursor().setPosition(0)

    def find_down(self):
        pattern = self.ui.lineEdit_new_search.text()
        if self.ui.plainTextEdit.find(pattern):
            self.ui.plainTextEdit.setFocus()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Информация")
            msg.setText("Поиск окончен")
            msg.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
            msg.exec()
            self.ui.plainTextEdit.setFocus()

    def find_up(self):
        pattern = self.ui.lineEdit_new_search.text()
        if self.ui.plainTextEdit.find(pattern, QtGui.QTextDocument.FindBackward):
            self.ui.plainTextEdit.setFocus()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Информация")
            msg.setText("Поиск окончен")
            msg.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
            msg.exec()
            self.ui.plainTextEdit.setFocus()

    def cancel_new_search(self):
        self.ui.lineEdit_new_search.setText('')
        format_ = QtGui.QTextCharFormat()
        format_.clearBackground()
        cursor = self.ui.plainTextEdit.textCursor()
        cursor.select(QtGui.QTextCursor.Document)
        cursor.mergeCharFormat(format_)
        self.ui.label_search.clear()

    def search(self):
        text = self.ui.plainTextEdit.toPlainText()
        searched_text = processing.filter_by_word(text, self.ui.lineEdit_find.text())
        if searched_text.strip():
            self.ui.plainTextEdit.setPlainText(searched_text)
            n_lines = searched_text.count("\n")
            self.statusbar_widgets[1].setText(f'Число строк: {n_lines}')
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Информация")
            msg.setText("По вашему запросу ничего не найдено")
            msg.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
            msg.exec()

    def set_text(self):
        self.ui.plainTextEdit.setPlainText(TEXT)

        n_lines = TEXT.count("\n")

        self.statusbar_widgets[1].setText(f'Число строк: {n_lines}')

        try:
            date_pattern = r'\[(\d\d)\.(\d\d)\.(\d\d\d\d), (\d\d):(\d\d):(\d\d)'
            day, month, year, hour, minute, second = map(int, re.findall(date_pattern, TEXT[:50])[0])
            day_f, month_f, year_f, hour_f, minute_f, second_f = map(int,
                                                                     re.findall(date_pattern, TEXT[-400:])[0])

            self.statusbar_widgets[0].setText(f'{str(day).rjust(2, "0")}.{str(month).rjust(2, "0")}.{year} '
                                              f'{str(hour).rjust(2, "0")}:{str(minute).rjust(2, "0")}:'
                                              f'{str(second).rjust(2, "0")} — '
                                              f'{str(day_f).rjust(2, "0")}.{str(month_f).rjust(2, "0")}.'
                                              f'{year_f} {str(hour_f).rjust(2, "0")}:{str(minute_f).rjust(2, "0")}:'
                                              f'{str(second_f).rjust(2, "0")}')
        except Exception:
            self.statusbar_widgets[0].setText('')
        self.statusbar_widgets[2].setText(processing.ENCODING)

    def source(self):
        global PROCESSING_FLAG
        PROCESSING_FLAG = 0

        self.set_text()
        self.ui.label_search.clear()

        self.ui.label_dec_cnt.clear()
        self.ui.progressBar.setValue(0)

    def time_filter(self):
        text = self.ui.plainTextEdit.toPlainText()
        datetime1 = self.ui.dateTimeEdit_1.dateTime().toString('yyyy-MM-dd-HH-mm-ss')
        datetime2 = self.ui.dateTimeEdit_2.dateTime().toString('yyyy-MM-dd-HH-mm-ss')
        filtered_text = processing.time_filter(text, datetime1, datetime2)
        if filtered_text.strip() == '':
            self.ui.plainTextEdit.clear()
            self.statusbar_widgets[0].setText('')
            self.statusbar_widgets[1].setText(f'Число строк: {0}')

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle('Информация')
            msg.setText('О данном промежутке информация отсутствует')
            msg.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
            msg.exec()
        else:
            self.ui.plainTextEdit.setPlainText(filtered_text)

            n_lines = filtered_text.count("\n")
            self.statusbar_widgets[1].setText(f'Число строк: {n_lines}')
            date_pattern = r'\[(\d\d)\.(\d\d)\.(\d\d\d\d), (\d\d):(\d\d):(\d\d)'
            day, month, year, hour, minute, second = map(int, re.findall(date_pattern, filtered_text[:50])[0])
            day_f, month_f, year_f, hour_f, minute_f, second_f = map(int,
                                                                     re.findall(date_pattern, filtered_text[-400:])[0])
            self.statusbar_widgets[0].setText(f'{str(day).rjust(2, "0")}.{str(month).rjust(2, "0")}.{year} '
                                              f'{str(hour).rjust(2, "0")}:{str(minute).rjust(2, "0")}:'
                                              f'{str(second).rjust(2, "0")} — '
                                              f'{str(day_f).rjust(2, "0")}.{str(month_f).rjust(2, "0")}.'
                                              f'{year_f} {str(hour_f).rjust(2, "0")}:{str(minute_f).rjust(2, "0")}:'
                                              f'{str(second_f).rjust(2, "0")}')

    def manually_decoding(self):
        self.app_man_dec.ui.plainTextEdit.clear()
        self.app_man_dec.ui.plainTextEdit_2.clear()
        self.app_man_dec.setWindowModality(Qt.ApplicationModal)
        self.app_man_dec.show()

    def plot_settings(self):
        if PROCESSING_FLAG:
            self.app_plot_settings.setWindowModality(Qt.ApplicationModal)
            self.app_plot_settings.show()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Информация")
            msg.setText("Сначала необходимо произвести обработку")
            msg.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
            msg.exec()


class ManuallyDecoding(QtWidgets.QWidget):
    def __init__(self):
        super(ManuallyDecoding, self).__init__()
        self.ui = manually_dec_gui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.decoding)

    def decoding(self):
        text = self.ui.plainTextEdit.toPlainText()
        self.ui.plainTextEdit_2.setPlainText(processing.manually_decoding(text))


class PlotSettings(QtWidgets.QWidget):
    def __init__(self):
        super(PlotSettings, self).__init__()
        self.ui = plot_settings_gui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.checkBox_um1_all.stateChanged.connect(self.check_all)
        self.ui.pushButton_um1.clicked.connect(self.plot_um)
        self.ui.comboBox_marker.addItems(['+', '*', 'x', 'o', '.'])
        self.ui.comboBox_markersize.addItems(map(str, range(1, 11)))
        self.ui.comboBox_markersize.setCurrentIndex(5)
        self.ui.comboBox_um.addItems(['УМ-1', 'УМ-2'])

    def check_all(self):
        if self.ui.checkBox_um1_all.isChecked():
            self.ui.checkBox_um1_Uk.setChecked(True)
            self.ui.checkBox_um1_Ikol.setChecked(True)
            self.ui.checkBox_um1_Ia.setChecked(True)
            self.ui.checkBox_um1_Un.setChecked(True)
            self.ui.checkBox_um1_In.setChecked(True)
            self.ui.checkBox_um1_Uvak.setChecked(True)
            self.ui.checkBox_um1_Ivak.setChecked(True)
            self.ui.checkBox_um1_Uipup.setChecked(True)
            self.ui.checkBox_um1_Uips1.setChecked(True)
            self.ui.checkBox_um1_Uips2.setChecked(True)
            self.ui.checkBox_um1_Pvyh.setChecked(True)
            self.ui.checkBox_um1_Potr.setChecked(True)
        else:
            self.ui.checkBox_um1_Uk.setChecked(False)
            self.ui.checkBox_um1_Ikol.setChecked(False)
            self.ui.checkBox_um1_Ia.setChecked(False)
            self.ui.checkBox_um1_Un.setChecked(False)
            self.ui.checkBox_um1_In.setChecked(False)
            self.ui.checkBox_um1_Uvak.setChecked(False)
            self.ui.checkBox_um1_Ivak.setChecked(False)
            self.ui.checkBox_um1_Uipup.setChecked(False)
            self.ui.checkBox_um1_Uips1.setChecked(False)
            self.ui.checkBox_um1_Uips2.setChecked(False)
            self.ui.checkBox_um1_Pvyh.setChecked(False)
            self.ui.checkBox_um1_Potr.setChecked(False)

    def plot_um(self):
        um_dict = {'УМ-1': '31', 'УМ-2': '32'}
        time_scope = (list(map(int, self.ui.dateTimeEdit_start.dateTime().toString('yyyy MM dd HH mm ss').split())),
                      list(map(int, self.ui.dateTimeEdit_finish.dateTime().toString('yyyy MM dd HH mm ss').split())))
        um = um_dict[self.ui.comboBox_um.currentText()]
        one_fig = 0
        params = []
        rationing = 0
        faults_flag = 0
        marker = self.ui.comboBox_marker.currentText()
        markersize = int(self.ui.comboBox_markersize.currentText())
        if self.ui.checkBox_rationing.isChecked():
            rationing = 1
        if self.ui.checkBox_one_um1.isChecked():
            one_fig = 1
        if self.ui.checkBox_faults.isChecked():
            faults_flag = 1
        if self.ui.checkBox_um1_all.isChecked():
            params += ['Uк', 'Iкол', 'Iа', 'Uн', 'Iн', 'Uвак', 'Iвак', 'Uипуп', 'Uипс1', 'Uипс2', 'Pвых', 'Pотр']
        else:
            if self.ui.checkBox_um1_Uk.isChecked():
                params.append('Uк')
            if self.ui.checkBox_um1_Ikol.isChecked():
                params.append('Iкол')
            if self.ui.checkBox_um1_Ia.isChecked():
                params.append('Iа')
            if self.ui.checkBox_um1_Un.isChecked():
                params.append('Uн')
            if self.ui.checkBox_um1_In.isChecked():
                params.append('Iн')
            if self.ui.checkBox_um1_Uvak.isChecked():
                params.append('Uвак')
            if self.ui.checkBox_um1_Ivak.isChecked():
                params.append('Iвак')
            if self.ui.checkBox_um1_Uipup.isChecked():
                params.append('Uипуп')
            if self.ui.checkBox_um1_Uips1.isChecked():
                params.append('Uипс1')
            if self.ui.checkBox_um1_Uips2.isChecked():
                params.append('Uипс2')
            if self.ui.checkBox_um1_Pvyh.isChecked():
                params.append('Pвых')
            if self.ui.checkBox_um1_Potr.isChecked():
                params.append('Pотр')

        if not params:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setWindowTitle("Информация")
            msg.setText("Не выбран ни один параметр")
            msg.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
            msg.exec()
            return

        koefs = dict()
        if self.ui.checkBox_set_koefs.isChecked():
            try:
                if self.ui.lineEdit_k_Uk.text():
                    koefs['Uк'] = float(self.ui.lineEdit_k_Uk.text())
                if self.ui.lineEdit_k_Ikol.text():
                    koefs['Iкол'] = float(self.ui.lineEdit_k_Ikol.text())
                if self.ui.lineEdit_k_Ia.text():
                    koefs['Iа'] = float(self.ui.lineEdit_k_Ia.text())
                if self.ui.lineEdit_k_Un.text():
                    koefs['Uн'] = float(self.ui.lineEdit_k_Un.text())
                if self.ui.lineEdit_k_In.text():
                    koefs['Iн'] = float(self.ui.lineEdit_k_In.text())
                if self.ui.lineEdit_k_Uvak.text():
                    koefs['Uвак'] = float(self.ui.lineEdit_k_Uvak.text())
                if self.ui.lineEdit_k_Ivak.text():
                    koefs['Iвак'] = float(self.ui.lineEdit_k_Ivak.text())
                if self.ui.lineEdit_k_Uipup.text():
                    koefs['Uипуп'] = float(self.ui.lineEdit_k_Uipup.text())
                if self.ui.lineEdit_k_Uips1.text():
                    koefs['Uипс1'] = float(self.ui.lineEdit_k_Uips1.text())
                if self.ui.lineEdit_k_Uips2.text():
                    koefs['Uипс2'] = float(self.ui.lineEdit_k_Uips2.text())
                if self.ui.lineEdit_k_Pvyh.text():
                    koefs['Pвых'] = float(self.ui.lineEdit_k_Pvyh.text())
                if self.ui.lineEdit_k_Potr.text():
                    koefs['Pотр'] = float(self.ui.lineEdit_k_Potr.text())
            except ValueError:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setWindowTitle("Информация")
                msg.setText("Некорректный формат коэффициентов")
                msg.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
                msg.exec()
                return

        processing.plot(params, um, one_fig, marker, rationing, time_scope, markersize, faults_flag, koefs)


class SearchHighLight(QtGui.QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pattern = QtCore.QRegularExpression()
        self.format_ = QtGui.QTextCharFormat()
        self.format_.setBackground(Qt.green)
        self.counter = 0

    def highlightBlock(self, text):
        match_iterator = self.pattern.globalMatch(text.lower())
        while match_iterator.hasNext():
            self.counter += 1
            match = match_iterator.next()
            self.setFormat(match.capturedStart(), match.capturedLength(), self.format_)

    def search_text(self, text):
        bad_symbols = '.[]\\() '
        text = list(text)
        for i, ch in enumerate(text):
            if ch in bad_symbols:
                text[i] = '\\' + ch
        text = ''.join(text)
        self.pattern = QtCore.QRegularExpression(text)
        self.rehighlight()


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = LogAnalysis()
    application.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

# start /b designer
# pyuic5 read_file_gui.ui -o read_file_gui.py
# pyrcc5 resources.qrc -o resources_rc.py
# pyinstaller -F -w -n "LogAnalysis" -i ".\icons\Launcher.ico" main.py
# matplotlib==3.2.2
