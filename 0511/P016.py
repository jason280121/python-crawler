
#15:05

from PyQt6 import QtWidgets
#python與電腦連動, 取得電腦，與介面有關係，資料夾上下傳檔案，與軟體有關聯性
import sys


#建立主要視窗, 基底元件, 框架
app = QtWidgets.QApplication(sys.argv)


#建立視窗元件
widget  =  QtWidgets.QWidget()

#視窗標題
widget.setWindowTitle('Hello jason')

#尺吋
widget.resize(500,600)


#網格
grid = QtWidgets.QGridLayout(widget)



#設定label
label = QtWidgets.QLabel(widget)


#label 設定文字
label.setText('Test')
# label.move(30,30)
grid.addWidget(label,0,0)



#lable2 設定文字
label2=QtWidgets.QLabel(widget)
label2.setText('POIUY')
# label2.move(30,60)
grid.addWidget(label2,1,0)


#input 輸入框1
input1 = QtWidgets.QLineEdit(widget)
# input1.move(70,30)
grid.addWidget(input1,0,1)


#area
text1 = QtWidgets.QTextEdit(widget)
# text1.move(100,100)
grid.addWidget(text1,1,1)



#設定showLabel 顯示3,0
showLabel = QtWidgets.QLabel(widget)
grid.addWidget(showLabel,3,0)


#button重覆執行test()顯示
def test():
    # print('Hello')
    # print(input1.text())
    # print(text1.toPlainText())
    showLabel.setText(input1.text())


#加button按鈕
btn = QtWidgets.QPushButton(widget)
btn.setText('按我')
grid.addWidget(btn,2,0)
btn.clicked.connect(test)


#顯示劃面
widget.show()


#關閉系統
sys.exit(app.exec())

