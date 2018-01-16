import os,sys
import glob
import cv2
from main import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PIL import Image
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        #self.resizestoryimages()
        self.drawstories()

    def drawstories(self):
        images=glob.glob("./Story images/*.jpg")
        for i in images :
            image=QImage(i)
            self.story1.setPixmap(QPixmap.fromImage(image))

    def resizestoryimages(self):
        images=os.listdir("./Story images/")
        for i in images:
            image=cv2.imread("./Story images/"+i)
            cv2.imwrite("./Story images/new"+i,cv2.resize(image,(200,200)))

if __name__ ==  "__main__" :
    app =QApplication(sys.argv)
    w=MainWindow()
    w.resize(667,900)
    w.show()
    sys.exit(app.exec_())
