import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

	def __init__(self, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)


		#self.windowTitleChanged.connect(self.onWindowTitleChange)
		#self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
		#self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))
		#self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))
		





		self.setWindowTitle("Voice Correction Tool")
		label = QLabel("TestText")
		label.setAlignment(Qt.AlignCenter)
		self.setCentralWidget(label)

	# SLOT: This accepts a string, e.g. the window title, and prints it
	def onWindowTitleChange(self, s):
		print(s)

	# SLOT: This has default parameters and can be called without a value
	def my_custom_fn(self, a="HELLLO!", b=5):
		print(a, b)

	def contextMenuEvent(self, event):
    	print("Context menu event!")
    	#super(MainWindow, self).contextMenuEvent(event)

app = QApplication(sys.argv)
print('App Started')



window = MainWindow()
window.show()



app.exec_()
print('App Finished')