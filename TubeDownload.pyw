from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import sys
from tkinter import filedialog
from pytube import YouTube
from tkinter import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
            Form.setFixedSize(621, 363)
        Form.resize(621, 363)
        Form.setStyleSheet(u"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 421, 31))
        self.label.setStyleSheet(u"font-size: 20px;")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 70, 481, 41))
        self.lineEdit.setStyleSheet(u"font-size: 15px;")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 221, 21))
        self.label_2.setStyleSheet(u"font-size: 15px;")
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 210, 491, 31))
        self.comboBox.setStyleSheet(u"font-size: 13px;")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 120, 371, 31))
        self.label_3.setStyleSheet(u"font-size: 15px;")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 150, 321, 41))
        self.lineEdit_2.setStyleSheet(u"font-size: 15px;")
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(340, 150, 75, 41))
        self.pushButton_2.setStyleSheet(u"font-size: 15px; font: bold;")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 250, 181, 71))
        self.pushButton.setStyleSheet(u"font-size: 15px;")
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 330, 261, 21))
        self.progressBar.setStyleSheet(u"font-size: 15px;")
        self.progressBar.setValue(0)
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(500, 70, 81, 41))
        self.pushButton_3.setStyleSheet(u"font-size: 15px; font: bold;")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(470, 120, 141, 81))
        self.textBrowser_2 = QTextBrowser(Form)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(320, 260, 291, 91))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"TubeDownload", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:15pt; font-weight:600; text-decoration: underline; color:#ff0000;\">YouTube</span><span style=\" font-size:15pt;\"> video and audio downloader</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Write video url:</span></p></body></html>", None))

        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Choose a directory to download:</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Choose", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"DOWNLOAD", None))
        self.progressBar.setFormat(QCoreApplication.translate("Form", u"%p%", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Search", None))
    # retranslateUi



if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('welcome.ico'))

    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()


    def download():
    	url = ui.lineEdit.text()
    	sel_video = ui.comboBox.currentData()
    	sel_video_v = ui.comboBox.currentText()
    	directory = ui.lineEdit_2.text()
    	if url == '':
    		ui.textBrowser_2.setHtml(u"{}".format("Введите ссылку на видео!"))
    	elif sel_video_v == '':
    		ui.textBrowser_2.setHtml(u"{}".format("Нажмите на кнопку Search!"))
    	else:
    		ui.progressBar.setValue(50)
    		yt = YouTube(url).streams.get_by_itag(sel_video)
    		yt.download(directory)
    		ui.progressBar.setValue(100)
    		ui.textBrowser_2.setHtml(u"{}".format("Видео скачано!"))




    def select_directory():
        root = Tk()
        root.withdraw()
        folder_selected = filedialog.askdirectory()
        ui.lineEdit_2.setText(folder_selected) #  + "/"


    def search():

        url = ui.lineEdit.text()

        if url == '':
        	ui.textBrowser_2.setHtml(u"{}".format("Введите ссылку на видео!"))

        yt = YouTube(url)
        image_url = yt.thumbnail_url
        for st in yt.streams:
            ui.comboBox.addItem("itag: " + str(st.itag) + ", Format: " + str(st.mime_type) +
             ", resolution: " + str(st.resolution) + ", fps: " + str(st.fps), st.itag)





# https://youtu.be/cVJQjMZDQO8
# https://youtu.be/LXb3EKWsInQ


ui.pushButton_2.clicked.connect(select_directory)
ui.pushButton_3.clicked.connect(search)
ui.pushButton.clicked.connect(download)


sys.exit(app.exec_())