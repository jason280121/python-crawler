
#13:37
#pip install pyqt6
#pyqt6  pyqt6  Project description
#The documentation for the latest release can be found here.
#右一角 Modules 進入
#另一個內建，較難用

from PyQt6 import QtWidgets
#python與電腦連動, 取得電腦，與介面有關係，資料夾上下傳檔案，與軟體有關聯性

import sys


#視窗程式開始
app = QtWidgets.QApplication(sys.argv)

#放入基底元件
form  =  QtWidgets.QWidget()


#顯示元件
form.show()

#視窗程式結束
sys.exit(app.exec())




