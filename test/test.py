#!/usr/bin/python3 
# -*- coding: utf-8 -*-
# '''
# class Employee:
#     '所有员工的基类'
#     empCount = 0

#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1

#     def displayCount(self):
#         print("Total Employee",Employee.empCount)

#     def displayEmployee(self):
#         print("Name:",self.name,",Salary:",self.salary)  

# emp1 = Employee("Zara",2000)
# emp2 = Employee("Manni",5000)

# emp1.displayEmployee()
# emp2.displayEmployee()

# print("Total Employee:",Employee.empCount)
# '''
# import sys
# from PyQt5.Qt import *
# # sys.path.append(r'C:\Users\asus\.PyCharmCE2019.2\system\python_stubs\-643338342\PyQt5')
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QLabel的学习')
#         self.resize(500,500)
#         # self.setup_ui()
#         # self.QObject信号的操作()
#         # self.QObject类型判定()
#         # self.QObject对象删除()
#     def setup_ui(self):
#         label = QLabel(self)
#         label.setText('xxx')
#     def QObject信号的操作(self):
#         pass
#         # self.obj = QObject()
#         # # def destory_cao(obj):
#         # #     print('对象被释放了',obj)
#         # # self.obj.destroyed.connect(destory_cao)
#         # # del self.obj
#         # def obj_name_cao(name):
#         #     print('对象名称发生了改变',name)
#         # def obj_name_cao2(name):
#         #     print('对象名称发生了改变',name)
#         # self.obj.objectNameChanged.connect(obj_name_cao)
#         # self.obj.objectNameChanged.connect(obj_name_cao2)
#         # print(self.obj.receivers(self.obj.objectNameChanged)) #连接槽的个数
#         # self.obj.setObjectName('xxx')
#         # # print(self.obj.signalsBlocked(),'1')
#         # # self.obj.blockSignals(True)
#         # # # self.obj.objectNameChanged.disconnect()
#         # # self.obj.setObjectName('ooo')
#         # # print(self.obj.signalsBlocked(),'2')
#         # # self.obj.blockSignals(False)
#         # # # self.obj.objectNameChanged.connect(obj_name_cao)
#         # # self.obj.setObjectName('xxoo')
#         # btn = QPushButton(self)
#         # btn.setText('点击我')
#         # def cao():
#         #     print('点我做什么？')
#         # btn.clicked.connect(cao)
#     def QObject类型判定(self):
#         pass
#         # # obj = QObject()
#         # # w = QWidget()
#         # # btn = QPushButton()
#         # # label = QLabel()

#         # # objs = [obj,w,btn,label]
#         # # for o in objs:
#         # #     # print(o,o.isWidgetType())
#         # #     print(o.inherits('QWidget'))
#         # label1 = QLabel(self)
#         # label1.setText('社会我顺哥')
#         # label1.move(100,100)
#         # label2 = QLabel(self)
#         # label2.setText('人狠话不多')
#         # label2.move(150,150)
#         # btn = QPushButton(self)
#         # btn.setText('点我')
#         # btn.move(200,200)
#         # for widget in self.findChildren(QLabel):
#         #     # print(widget)
#         #     # if widget.isWidgetType():
#         #     if widget.inherits('QLabel'):
#         #         # print('是')
#         #         widget.setStyleSheet('background-color:cyan;')
#     def QObject对象删除(self):
#         pass
#         # obj1 = QObject()
#         # self.obj1 = obj1
#         # obj2 = QObject()
#         # obj3 = QObject()
#         # obj3.setParent(obj2)
#         # obj2.setParent(obj1)
#         # obj1.destroyed.connect(lambda : print('obj1被释放了'))
#         # obj2.destroyed.connect(lambda : print('obj2被释放了'))
#         # obj3.destroyed.connect(lambda : print('obj3被释放了'))
#         # # del obj2
#         # obj2.deleteLater()
#         # print(obj1.children())
#         # print(obj2)
# # class App(QApplication):
# #     def notify(self,receiver,evt):
# #         if receiver.inherits('QPushButton') and evt.type() == QEvent.MouseButtonPress:
# #             print(receiver,evt)
# #         return super().notify(receiver,evt)
# # class Btn(QPushButton):
# #     def event(self,evt):
# #         if evt.type() == QEvent.MouseButtonPress:
# #             print(evt)
# #         return super().event(evt)
# #     def mousePressEvent(self, *args,**kwargs):
# #         print('鼠标被按下了。。。')
# #         return super().mousePressEvent(*args,**kwargs)
# class MyObject(QObject):
#     def timerEvent(self,evt):
#         print(evt,'1')
# # class MyLabel(QLabel):
# #     def __init__(self,*args,**kwargs):
# #         super().__init__(*args,**kwargs)
# #         self.setText('10')
# #         self.move(100,100)
# #         self.setStyleSheet('font-size:22px;')       
# #     def timerEvent(self, *args, **kwargs):
# #         # print('xxx')
# #         current_sec = int(self.text())
# #         current_sec -= 1
# #         self.setText(str(current_sec))
# #         if current_sec == 0:
# #             print('停止')
# #             self.killTimer(self.timer_id)
# #     def setSec(self,sec):
# #         self.setText(str(sec))
# #     def startMyTimer(self,ms):
#         # self.timer_id = self.startTimer(ms)
# class MyWidget(QWidget):
#     def timerEvent(self, *args, **kwargs):
#         print('xx')
#         current_w = self.width()
#         current_h = self.height()
#         self.resize(current_w + 10,current_h + 10)
# if __name__ == '__main__':
#     app = QApplication(sys.argv)

#         # win1 = QWidget()
#         # win1.setStyleSheet('background-color:red;') #设置控件窗口的颜色
#         # win1.resize(500,500) #设置控件的大小尺寸
#         # win1.setWindowTitle('red')
#         # win1.show()

#         # win2 = QWidget()
#         # win2.setStyleSheet('background-color:green;')
#         # #win2.setParent(win1)
#         # win2.setWindowTitle('green')
#         # win2.resize(500,500)
#         # win2.show()
        
#         # win_root = QWidget()

#         # label1 = QLabel()
#         # label1.setText('label1')
#         # label1.setParent(win_root)

#         # label2 = QLabel()
#         # label2.setText('label2')
#         # label2.move(50,50)
#         # label2.setParent(win_root)

#         # label3 = QLabel()
#         # label3.setText('label2')
#         # label3.move(30,30)
#         # label3.setParent(win_root)

#         # btn = QPushButton(win_root)
#         # btn.move(100,100)
#         # btn.setText('btn')
#         # win_root.show()

#         # for sub_widget in win_root.findChildren(QLabel):
#         #     print(sub_widget)
#         #     sub_widget.setStyleSheet('background-color:cyan;')
#         # btn = QPushButton(self)
#         # btn.setText('点击我')
#         # window = Window()
#         # window = QWidget()
#         # def cao(title):
#         #     print('标题改变了',title)
#         #     window.blockSignals(True)
#         #     window.setWindowTitle('撩课-' + title)
#         #     window.blockSignals(False)
#         # window.windowTitleChanged.connect(cao)
#         # window.setWindowTitle('Hello Sz')
#         # window.setWindowTitle('Hello Sz1')
#         # window.setWindowTitle('Hello Sz2')
#         # window.show()
#     window = MyWidget()
#     # btn = Btn(window)
#     # btn.setText('按钮')
#     # btn.move(100,100)
#     # def cao():
#     #     print('按钮被点击了')
#     # btn.pressed.connect(cao)
#     window.setWindowTitle('QObject定时器的使用')
#     window.resize(500,500)
#     print(QWidget.__bases__)
#     # label = MyLabel(window)
#     # label.setSec(5)
#     # label.startMyTimer(500)
#     # obj = MyObject()
#     # timer_id = obj.startTimer(1000) #参数，第一个是毫秒间隔的时间 第二个参数是充分值
#     # obj.killTimer(timer_id)
#     window.startTimer(1000)
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
    # window.setFixedSize(500,500)
    # window.resize(500,500)

    # window.setFixedSize(500,500)   #该方法固定窗口大小
    # window.move(200,100)

    # label = QLabel(window)
    # label.setText("社会顺")
    # label.move(100,100)
    # label.setStyleSheet('background-color:cyan;')

    # def changeCao():
    #     new_content = label.text() + '社会顺'
    #     label.setText(new_content)
    #     # label.resize(label.width()+100,label.height())
    #     label.adjustSize()
    # btn = QPushButton(window)
    # btn.setText('增加内容')
    # btn.move(150,150)
    # btn.clicked.connect(changeCao)
    # print(type(label.text))
    # print(type(label.text()))


    # window.setGeometry(0,0,150,150)
    # print(window.x())
    # print(window.width())
    # print(window.geometry())

    # red = QWidget(window)
    # red.resize(100,100)
    # red.setStyleSheet("background-color:red;")
    # red.move(300,0)

    # # green = QWidget(window)
    # # green.resize(100,100)
    # # green.setStyleSheet('background-color:green;')
    # # green.move(300,50)

    # column_count = 4 #每行控件的个数
    # widget_count = 100  #总的控件数量
    # widget_width = window.width() / column_count
    # row_count = (widget_count - 1) // column_count + 1
    # widget_height = window.height() / row_count
    # for i in range(0,widget_count):
    #     w = QWidget(window)
    #     w.resize(int(widget_width),int(widget_height))
    #     widget_x = i % column_count * widget_width
    #     widget_y = i // column_count * widget_height
    #     w.move(int(widget_x),int(widget_y))
    #     w.setStyleSheet('background-color:red;border:1px solid yellow;')
    #     w.show()
    # widget_width = int(window.width() / column_count) #窗口宽度/列数 求得控件的宽度
    # row_count = int((widget_count - 1) / column_count + 1) #控件的行数
    # widget_height = int(window.height() / row_count) #窗口高度/行数 求得控件的宽度 /表示正常除法求得的商，是float //表示正常除法求得的商，int是个整数，%表示正常除法求得的余数,是int
    # # print(window.width(),window.height(),widget_width,row_count,widget_height)
    # for i in range(0,row_count):
    #     widget_y = i * widget_height + i
    #     # print('i:',i)
    #     for j in range(0,column_count): #for循环语句循环不到最大值,即不取column_count
    #         w = QWidget(window)
    #         w.resize(widget_width,widget_height)
    #         widget_x = j * widget_width + j
    #         w.move(widget_x,widget_y)
    #         if i == j:
    #             w.setStyleSheet('background-color:red;')
    #         else:
    #             w.setStyleSheet('background-color:cyan;')
    #         # if j / 2 == 0:
    #         #     w.setStyleSheet('background-color:cyan;')
    #         # else:
    #         #     w.setStyleSheet('background-color:red;')
    #         w.show()
    #         # print(widget_x,widget_y)
    #         # print('j:',j)
    # range(0,3)
    # window.show()
    # window.setGeometry(0,0,150,150)
    # print('-' * 40)
    # print(window.x())
    # print(window.width())
    # print(window.geometry())
    # window = QWidget()
    # window.setWindowTitle('内容边距的设定')
    # window.resize(500,500)
    # label = QLabel(window)
    # label.setText('社会我顺哥，人狠话不多')
    # label.resize(300,300)
    # label.setStyleSheet('background-color:cyan;')
    # label.setContentsMargins(100,200,0,0)  #设置文本内容的边框间距 文本内容靠左，水平居中
    
    # print(label.contentsRect())
    # print(label.getContentsMargins())
    # window.show()
    # sys.exit(app.exec_())
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('事件消息的学习')
#         self.resize(500,500)
#         self.setup_ui()
#     def setup_ui(self):
#         pass
#     def showEvent(self,QShowEvent): #事件响应函数
#         print('窗口被展示了出来')
#     def closeEvent(self,QCloseEvent):
#         print('窗口被关闭了')
#     def moveEvent(self,QMoveEvent):
#         print('窗口被移动了')
#     def resizeEvent(self,QResizeEvent):
#         print('窗口被改变了尺寸大小')
#     def enterEvent(self,QEvent):
#         print('鼠标进来了')
#         self.setStyleSheet('background-color:red;')
#     def leaveEvent(self,QEvent):
#         print('鼠标移开了')
#         self.setStyleSheet('background-color:green;')
#     def mousePressEvent(self,QMouseEvent):
#         print('鼠标被按下')
#     def mouseReleaseEvent(self,QMouseEvent):
#         print('鼠标被释放')
#     def mouseDoubleClickEvent(self,QMouseEvent):
#         print('鼠标双击')
#     def mouseMoveEvent(self,QMouseEvent):
#         print('鼠标移动了')
#     def keyPressEvent(self,QKeyEvent):
#         print('键盘上某个按键被按下了')
#     def keyReleaseEvent(self,QKeyEvent): #涉及到方法的重写
#         print('键盘上某个键被释放')
# class Window(QWidget):
#     def mousePressEvent(self,QMouseEvent):
#         print('顶层窗口鼠标被按下')
# class MidWindow(QWidget):
#     def mousePressEvent(self,QMouseEvent):
#         print('中间控件鼠标按下')
# class Label(QLabel):
#     def mousePressEvent(self,evt):
#         print('标签控件鼠标按下')
        # evt.accept() #标记控件事件消息已被处理，不再向上传输
        # print(evt.isAccepted())
        # evt.ignore()
        # print(self.objectName())
import sys
from PyQt5.Qt import *
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.move(200,200)
        self.setWindowTitle('鼠标相关的操作')
        self.setMouseTracking(True)
        pixmap = QPixmap('C:\\Users\\asus\\Pictures\\Saved Pictures\\jason-chen-22141-unsplash-1024x577.jpg').scaled(50,50)
        cursor = QCursor(pixmap)
        self.setCursor(cursor)
        self.label = QLabel(self)
        self.label.setText('社会我顺哥，人狠话不多')
        self.label.move(100,100)
        self.label.setStyleSheet('background-color:cyan;')
    def mouseMoveEvent(self,evt):
        # print('鼠标移动了',evt.localPos()) #返回鼠标的位置
        print('鼠标移动',evt.localPos())
        # label = self.findChild(QLabel)
        self.label.move(evt.localPos().x(),evt.localPos().y())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    
    # window = MyWindow()
    # window.setWindowTitle('鼠标操作')
    # window.resize(500,500)
    # window.setMouseTracking(True) #鼠标跟踪
    # print(window.hasMouseTracking())
    # pixmap = QPixmap('C:\\Users\\asus\\Pictures\\Saved Pictures\\jason-chen-22141-unsplash-1024x577.jpg') #图片对象,图片的地址
    # new_pixmap = pixmap.scaled(50,50) #设置鼠标图标的大小
    # cursor = QCursor(new_pixmap,0,0) #鼠标对象 0，0对应鼠标图标的左上角,鼠标生效的点
    # window.setCursor(cursor) #设置鼠标图标样式
    # current_cursor = window.cursor()
    # current_cursor.setPos(100,100)
    # print(current_cursor.pos())
    # window.unsetCursor()
    # window.setCursor(Qt.ForbiddenCursor)
    # label = QLabel(window)
    # label.setText('社会顺哥')
    # label.resize(100,100)
    # label.setStyleSheet('background-color:cyan;')
    # label.setCursor(Qt.ForbiddenCursor)
    # mid_window = MidWindow(window)
    # mid_window.resize(300,300)
    # mid_window.setAttribute(Qt.WA_StyledBackground,True) #生效中间控件的样式
    # mid_window.setStyleSheet('background-color:yellow;')
    # label = Label(mid_window)
    # # label = QLabel(mid_window)
    # label.setText('这是一个标签')
    # label.setStyleSheet('background-color:red;')
    # label.move(100,100)
    # # label.setObjectName('test')
    # btn = QPushButton(mid_window)
    # btn.setText('我是按钮')
    # btn.move(50,50)
    window.show()
    sys.exit(app.exec_())