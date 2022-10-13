from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import cv2
from sys import *
from PIL import Image, ImageFilter 
from PIL.ImageQt import ImageQt

def prominent_colour():

	image = cv2.imread("test.png")
	orig = image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (7, 7), 0)
	(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
	img = Image.open("test.png")
	return img.getpixel((maxLoc[0],maxLoc[1]))

def blur_image():

	#would get song cover
	#currentSongCover()

	#blur image
	original_image = Image.open("test.png")
	blurred_image = original_image.filter(ImageFilter.GaussianBlur(radius=15))
	#convert to pixmap
	qim = ImageQt(blurred_image)
	#return pixmap

	pixmap = QPixmap.fromImage(qim)

	return pixmap

class ClickSlider(QtWidgets.QSlider):

    sliderPressedWithValue = QtCore.QSignal(int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sliderPressed.connect(self.on_slider_pressed)

    def on_slider_pressed(self):
        self.sliderPressedWithValue.emit(self.value())

class ui(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi('main.ui', self)


		#check if image is bright to set title colour
		image = cv2.imread("test.png")
		L, A, B = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2LAB))
		L = L/np.max(L)
		if np.mean(L) < 0.5:
			self.title.setStyleSheet("background-color:transparent;color: white;font:17px")
			self..setStyleSheet("background-color:transparent;color: white;font:17px")

		else:
			self.title.setStyleSheet("background-color:transparent;color: black;font:17px")

		#set background and cover image
		self.background_image.setPixmap(blur_image().scaled(579,575,Qt.KeepAspectRatio))
		self.album_cover.setPixmap(QPixmap("test.png"))
		self.album_cover.setScaledContents(True)

		#progress slider acent colour
		color = f"({prominent_colour()[0]}, {prominent_colour()[1]},{prominent_colour()[2]})"

		self.progress_slider.setStyleSheet("""
		QSlider::groove:horizontal {
		height: 3px; background-color: #454545;border-radius: 1px;padding-left: 0px;padding-right: 0px;
		}

		QSlider::sub-page:horizontal {
		height: 3px; background-color: rgb%s;border-radius: 1px;padding-left: 0px;padding-right: 0px;
		}


		QSlider::handle:horizontal {
		background-color: rgb%s;border: 4px solid #454545;width: 9px;min-height: 13px;margin: -7px 0;border-radius: 8px;
		}

		QSlider::handle:horizontal:hover {
		background-color: rgb%s;border: 3px solid #454545;width: 11px;min-height: 13px;margin: -7px 0;border-radius: 8px;
		}

		QSlider::handle:horizontal:pressed {
		background-color: rgb%s;border: 5px solid #454545;width: 7px;min-height: 13px;margin: -7px 0;border-radius: 8px;}""" % (color,color,color,color))





if __name__ == "__main__":
    app = QApplication(argv)
    w = ui()
    w.show()
    exit(app.exec_())