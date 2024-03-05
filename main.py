import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self, cv2=None):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.images = ['rosol.jpg','pierogi.jpg','schabowy.jpg']
        self.black_withe_images = ['rosol_black.jpg','pierogi_black.jpg','schabowy_black.jpg']
        self.ui.rosol.clicked.connect(self.setRosol)
        self.ui.pierogi.clicked.connect(self.setPierogi)
        self.ui.schabowy.clicked.connect(self.setSchabowy)



    def setRosol(self):
        if(self.ui.black_white.isChecked()):
            pixmap = QPixmap(f'./images/{self.black_withe_images[0]}')
            pixmap = pixmap.scaled(self.ui.image.width(), self.ui.image.height())
            self.ui.image.setPixmap(pixmap)
        else:
            pixmap = QPixmap(f'./images/{self.images[0]}')
            pixmap = pixmap.scaled(self.ui.image.width(), self.ui.image.height())
            self.ui.image.setPixmap(pixmap)
    def setPierogi(self):
        if (self.ui.black_white.isChecked()):
            pixmap = QPixmap(f'./images/{self.black_withe_images[1]}')
            pixmap = pixmap.scaled(self.ui.image.width(), self.ui.image.height())
            self.ui.image.setPixmap(pixmap)
        else:
            pixmap = QPixmap(f'./images/{self.images[1]}')
            pixmap = pixmap.scaled(self.ui.image.width(), self.ui.image.height())
            self.ui.image.setPixmap(pixmap)
    def setSchabowy(self):
        if (self.ui.black_white.isChecked()):
            pixmap = QPixmap(f'./images/{self.black_withe_images[2]}')
            pixmap = pixmap.scaled(self.ui.image.width(), self.ui.image.height())
            self.ui.image.setPixmap(pixmap)
        else:
            pixmap = QPixmap(f'./images/{self.images[2]}')
            pixmap = pixmap.scaled(self.ui.image.width(), self.ui.image.height())
            self.ui.image.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())
