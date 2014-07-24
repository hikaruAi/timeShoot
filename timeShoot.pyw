from PyQt4 import QtCore, QtGui
import os, shutil
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
#####################3
n=0
def toVideo(n):
    global MainForm, app
    formatsList=["png","jpg","mp4","avi","mov"]
    
    formato=formatsList[MainForm.formatBox.currentIndex()]
    file=MainForm.ouputText.text()
    
    shutil.copy(os.getcwd()+"\\ffmpeg.exe",os.path.dirname(file))
    
    MainForm.setWindowTitle("Encoding Wait")
    os.chdir(os.path.dirname(file))
    comand="ffmpeg -f image2"+" -i "+os.path.basename(file)+"%d.jpg -r 10 "+os.path.basename(file)+"."+formato
    print(comand)
    os.system(comand)
    for i in range(0,n):
        os.remove(file+str(i)+".jpg")
        app.processEvents()
    MainForm.setWindowTitle("Finnished")
    os.remove(os.getcwd()+"\\ffmpeg.exe")
##########################################
def default():
    global MainForm
    MainForm.ouputText.setText(QtGui.QDesktopServices.storageLocation(5))
    MainForm.stopButton.setEnabled(False)
    MainForm.setWindowTitle("timeShoot")
def screenShoot(file,format):
    screen=QtGui.QPixmap.grabWindow(QtGui.QApplication.desktop().winId())
    screen.save(file,format,-1)
    screen=None
    del screen
def browse():
    global MainForm
    file=QtGui.QFileDialog.getSaveFileName(MainForm,"Save as...",QtGui.QDesktopServices.storageLocation(5))
    MainForm.ouputText.setText(file)
def mainClick():
    global MainForm
    MainForm.stopButton.setEnabled(True)
    if MainForm.mainButton.text()=="Start":
        print("START")
        MainForm.setWindowTitle("timeShoot - Shooting")
        MainForm.timer.setInterval(int(MainForm.delayBox.value()*1000))
        MainForm.timer.start()
        MainForm.mainButton.setText("Pause")
        print("Started")
    elif MainForm.mainButton.text()=="Pause":
        MainForm.setWindowTitle("timeShoot - Paused")
        MainForm.timer.stop()
        MainForm.mainButton.setText("Start")
        print("Paused")
    else:
        pass
def timerEvent():
    global MainForm, n
    formatsList=["png","jpg","mp4","avi","mov"]
    if MainForm.formatBox.currentIndex()<2:
        nombre=MainForm.ouputText.text()+str(n)+"."+formatsList[MainForm.formatBox.currentIndex()]
        screenShoot(nombre,formatsList[MainForm.formatBox.currentIndex()])
    else:
        nombre=MainForm.ouputText.text()+str(n)+".jpg"
        screenShoot(nombre,"jpg")
    n+=1
def stopClick():
    global MainForm, n
    MainForm.timer.stop()
    m=n
    n=0
    MainForm.setWindowTitle("timeShoot")
    MainForm.mainButton.setText("Start")
    if MainForm.formatBox.currentIndex()>1:
        toVideo(m)
    
def MAKE_mainForm():
    MainForm = QtGui.QWidget()
    MainForm.setObjectName(_fromUtf8("MainForm"))
    MainForm.resize(281, 120)
    MainForm.browseButton = QtGui.QPushButton(MainForm)
    MainForm.browseButton.setGeometry(QtCore.QRect(150, 30, 51, 21))
    MainForm.browseButton.setFlat(False)
    MainForm.browseButton.setObjectName(_fromUtf8("browseButton"))
    MainForm.ouputText = QtGui.QLineEdit(MainForm)
    MainForm.ouputText.setGeometry(QtCore.QRect(10, 30, 141, 20))
    MainForm.ouputText.setObjectName(_fromUtf8("ouputText"))
    MainForm.label = QtGui.QLabel(MainForm)
    MainForm.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
    MainForm.label.setObjectName(_fromUtf8("label"))
    MainForm.label_2 = QtGui.QLabel(MainForm)
    MainForm.label_2.setGeometry(QtCore.QRect(10, 60, 91, 16))
    MainForm.label_2.setObjectName(_fromUtf8("label_2"))
    MainForm.formatBox = QtGui.QComboBox(MainForm)
    MainForm.formatBox.setGeometry(QtCore.QRect(120, 80, 69, 22))
    MainForm.formatBox.setObjectName(_fromUtf8("formatBox"))
    MainForm.formatBox.addItem(_fromUtf8(""))
    MainForm.formatBox.addItem(_fromUtf8(""))
    MainForm.formatBox.addItem(_fromUtf8(""))
    MainForm.formatBox.addItem(_fromUtf8(""))
    MainForm.formatBox.addItem(_fromUtf8(""))
    MainForm.label_3 = QtGui.QLabel(MainForm)
    MainForm.label_3.setGeometry(QtCore.QRect(120, 60, 61, 16))
    MainForm.label_3.setObjectName(_fromUtf8("label_3"))
    MainForm.delayBox = QtGui.QDoubleSpinBox(MainForm)
    MainForm.delayBox.setGeometry(QtCore.QRect(10, 80, 81, 22))
    MainForm.delayBox.setDecimals(3)
    MainForm.delayBox.setMinimum(0.001)
    MainForm.delayBox.setMaximum(999999.999)
    MainForm.delayBox.setSingleStep(5.0)
    MainForm.delayBox.setProperty("value", 5.0)
    MainForm.delayBox.setObjectName(_fromUtf8("delayBox"))
    MainForm.mainButton = QtGui.QPushButton(MainForm)
    MainForm.mainButton.setGeometry(QtCore.QRect(210, 10, 61, 41))
    MainForm.mainButton.setObjectName(_fromUtf8("mainButton"))
    MainForm.stopButton = QtGui.QPushButton(MainForm)
    MainForm.stopButton.setGeometry(QtCore.QRect(210, 60, 61, 41))
    MainForm.stopButton.setObjectName(_fromUtf8("stopButton"))
    QtCore.QMetaObject.connectSlotsByName(MainForm)
    MainForm.setTabOrder(MainForm.browseButton, MainForm.delayBox)
    MainForm.setTabOrder(MainForm.delayBox, MainForm.formatBox)
    MainForm.setTabOrder(MainForm.formatBox, MainForm.mainButton)
    MainForm.setTabOrder(MainForm.mainButton, MainForm.stopButton)
    MainForm.setTabOrder(MainForm.stopButton, MainForm.ouputText)
    MainForm.setWindowTitle(QtGui.QApplication.translate("MainForm", "Title", None, QtGui.QApplication.UnicodeUTF8))
    MainForm.browseButton.setText(QtGui.QApplication.translate("MainForm", "Browse", None, QtGui.QApplication.UnicodeUTF8))
    MainForm.label.setText(QtGui.QApplication.translate("MainForm", "Output :", None, QtGui.QApplication.UnicodeUTF8))
    MainForm.label_2.setText(QtGui.QApplication.translate("MainForm", "Delay (seconds) :", None, QtGui.QApplication.UnicodeUTF8))
    MainForm.formatBox.setItemText(0, QtGui.QApplication.translate("MainForm", "png", None, QtGui.QApplication.UnicodeUTF8))
    MainForm.formatBox.setItemText(1, QtGui.QApplication.translate("MainForm", "jpg", None, QtGui.QApplication.UnicodeUTF8))
    MainForm.formatBox.setItemText(2, QtGui.QApplication.translate("MainForm", "mp4", None, QtGui.QApplication.UnicodeUTF8))
    MainForm.formatBox.setItemText(3, QtGui.QApplication.translate("MainForm", "avi", None, QtGui.QApplication.UnicodeUTF8))
    MainForm.formatBox.setItemText(4, QtGui.QApplication.translate("MainForm", "mov", None, QtGui.QApplication.UnicodeUTF8))
    MainForm.label_3.setText(QtGui.QApplication.translate("MainForm", "Format:", None, QtGui.QApplication.UnicodeUTF8))
    MainForm.mainButton.setText(QtGui.QApplication.translate("MainForm", "Start", None, QtGui.QApplication.UnicodeUTF8))
    MainForm.stopButton.setText(QtGui.QApplication.translate("MainForm", "Stop", None, QtGui.QApplication.UnicodeUTF8))
    MainForm.timer=QtCore.QTimer()
    ##############EVENTS########
    QtCore.QObject.connect(MainForm.browseButton, QtCore.SIGNAL(_fromUtf8("clicked()")),browse)
    QtCore.QObject.connect(MainForm.mainButton, QtCore.SIGNAL(_fromUtf8("clicked()")),mainClick)
    QtCore.QObject.connect(MainForm.timer, QtCore.SIGNAL(_fromUtf8("timeout()")),timerEvent)
    QtCore.QObject.connect(MainForm.stopButton, QtCore.SIGNAL(_fromUtf8("clicked()")),stopClick)
    return(MainForm)

##########################################
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainForm=MAKE_mainForm()
    default()
    MainForm.show()
    sys.exit(app.exec_())