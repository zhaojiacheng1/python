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
# import sys
# from PyQt5.Qt import *
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(500,500)
#         self.move(200,200)
#         self.setWindowTitle('鼠标相关的操作')
#         self.setMouseTracking(True)
#         pixmap = QPixmap('C:\\Users\\asus\\Pictures\\Saved Pictures\\jason-chen-22141-unsplash-1024x577.jpg').scaled(50,50)
#         cursor = QCursor(pixmap)
#         self.setCursor(cursor)
#         self.label = QLabel(self)
#         self.label.setText('社会我顺哥，人狠话不多')
#         self.label.move(100,100)
#         self.label.setStyleSheet('background-color:cyan;')
#     def mouseMoveEvent(self,evt):
#         # print('鼠标移动了',evt.localPos()) #返回鼠标的位置
#         print('鼠标移动',evt.localPos())
#         # label = self.findChild(QLabel)
#         self.label.move(evt.localPos().x(),evt.localPos().y())

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()

#     # window = MyWindow()
#     # window.setWindowTitle('鼠标操作')
#     # window.resize(500,500)
#     # window.setMouseTracking(True) #鼠标跟踪
#     # print(window.hasMouseTracking())
#     # pixmap = QPixmap('C:\\Users\\asus\\Pictures\\Saved Pictures\\jason-chen-22141-unsplash-1024x577.jpg') #图片对象,图片的地址
#     # new_pixmap = pixmap.scaled(50,50) #设置鼠标图标的大小
#     # cursor = QCursor(new_pixmap,0,0) #鼠标对象 0，0对应鼠标图标的左上角,鼠标生效的点
#     # window.setCursor(cursor) #设置鼠标图标样式
#     # current_cursor = window.cursor()
#     # current_cursor.setPos(100,100)
#     # print(current_cursor.pos())
#     # window.unsetCursor()
#     # window.setCursor(Qt.ForbiddenCursor)
#     # label = QLabel(window)
#     # label.setText('社会顺哥')
#     # label.resize(100,100)
#     # label.setStyleSheet('background-color:cyan;')
#     # label.setCursor(Qt.ForbiddenCursor)
#     # mid_window = MidWindow(window)
#     # mid_window.resize(300,300)
#     # mid_window.setAttribute(Qt.WA_StyledBackground,True) #生效中间控件的样式
#     # mid_window.setStyleSheet('background-color:yellow;')
#     # label = Label(mid_window)
#     # # label = QLabel(mid_window)
#     # label.setText('这是一个标签')
#     # label.setStyleSheet('background-color:red;')
#     # label.move(100,100)
#     # # label.setObjectName('test')
#     # btn = QPushButton(mid_window)
#     # btn.setText('我是按钮')
#     # btn.move(50,50)
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# class MyLabel(QLabel):
#     def enterEvent(self,*args,**kwargs):
#         print('鼠标进入')
#         self.setText('欢迎光临')
#     def leaveEvent(self,*args,**kwargs):
#         print('鼠标离开')
#         self.setText('谢谢惠顾')
#     def keyPressEvent(self,evt): #QKeyEvent
#         print('xx')
#         if evt.key() == Qt.Key_Tab: #获取按键值 普通键、修饰键
#             print('用户按下了Tab键')
#         if evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_A: #修饰键Ctrl,Shift
#             print('Ctrl+Shift+A 被按下')
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle('鼠标操作')
#     window.resize(500,500)

#     label = MyLabel(window)
#     label.resize(200,200)
#     label.move(100,100)
#     label.setStyleSheet('background:cyan;')
#     label.grabKeyboard() #打开捕获键盘数值

#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.move_flag = False #针对鼠标跟踪
#         self.setWindowTitle('窗口移动的学习')
#         self.resize(500,500)
#         self.setup_ui()
#     def setup_ui(self):
#         pass
#     def mousePressEvent(self,evt):
#         if evt.button() == Qt.LeftButton: #针对鼠标右键不能移动窗口
#             self.move_flag = True
#             print('鼠标按下')
#             self.mouse_x = evt.globalX() # 确定两个点，鼠标第一次按下的点。窗口当前的位置
#             self.mouse_y = evt.globalY()
#             print(self.mouse_x,self.mouse_y)
#             self.origin_x = self.x()
#             self.origin_y = self.y()
#     def mouseMoveEvent(self,evt):
#         print('鼠标移动')
#         print(evt.globalX(),evt.globalY())
#         if self.move_flag:
#             move_x = evt.globalX() - self.mouse_x #获取坐标的变化
#             move_y = evt.globalY() - self.mouse_y
#             dest_x = self.origin_x + move_x
#             dest_y = self.origin_y + move_y
#             self.move(dest_x,dest_y)
#     def mouseReleaseEvent(self,evt):
#         self.move_flag = False
#         print('鼠标释放')
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle('父子关系的学习')
#     window.resize(500,500)

#     label1 = QLabel(window)
#     label1.setText('标签1')
#     label2 = QLabel(window)
#     label2.setText('标签2')
#     label2.move(50,50)
#     label3 = QLabel(window)
#     label3.setText('标签3')
#     label3.move(100,100)

#     # print(window.childAt(250,250))
#     # print(label2.parentWidget())
#     print(window.childrenRect())
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# # class MyLabel(QLabel):
# #     def mousePressEvent(self,evt):
# #         self.setStyleSheet('background-color:red;')
# class Window(QWidget):
#     def mousePressEvent(self,evt):
#         local_x = evt.x()
#         local_y = evt.y()
#         sub_widget = self.childAt(local_x,local_y)
#         if sub_widget is not None: #容错，通过子控件是否存在
#             sub_widget.setStyleSheet('background-color:red;')
#             print('被点击了',local_x,local_y)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.setWindowTitle('父子关系案例')
#     window.resize(500,500)
#     for i in range(1,11):
#         label = QLabel(window)
#         label.setText('标签' + str(i))
#         label.move(40*i,40*i)
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle('层级关系调整')
#     window.resize(500,500)

#     label1 = QLabel(window)
#     label1.setText('标签1')
#     label1.resize(200,200)
#     label1.setStyleSheet('background-color:red;')

#     label2 = QLabel(window)
#     label2.setText('标签2')
#     label2.resize(200,200)
#     label2.setStyleSheet('background-color:green;')
#     label2.move(100,100)
#     label1.raise_() #层级提高至最上层
#     # label2.lower() #层级降低至最底层
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = QWidget()
#     # window.setWindowTitle('')
#     window.resize(500,500)
#     # icon = QIcon('C:\\Users\\asus\\Pictures\\Saved Pictures\\jason-chen-22141-unsplash-1024x577.jpg') #图标的路径
#     # window.setWindowIcon(icon) #设置图标
#     # window.setWindowTitle('icon')
#     # window.setWindowOpacity(0.5) #设置窗口的透明度 1.0不透明，0.0 透明
#     # print(window.windowOpacity())
#     # print(window.windowState() == Qt.WindowNoState)  #窗口状态获取
#     # window.setWindowState(Qt.WindowFullScreen) #全屏显示
#     # window.setWindowState(Qt.WindowMaximized)   #最大化显示
#     # window.setWindowState(Qt.WindowMinimized)   #窗口最小化
#     # w2 = QWidget(window)
#     # w2.setWindowTitle('w2')
#     # w2.show()
#     window.show()
#     # window.showMaximized() #最大化展示
#     # w2.setWindowState(Qt.WindowActive)
#     # print(window.windowIcon())
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# class Window(QWidget):
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.setWindowFlags(Qt.FramelessWindowHint)
#         self.setWindowOpacity(1)
#         self.setWindowTitle('顶层窗口操作')
#         self.resize(500,500)
#         self.setup_ui()
#     def setup_ui(self):
#         #公共数据
#         self.top_margin = 10
#         self.btn_w = 80
#         self.btn_h = 40
#         #添加三个子控件按钮-窗口右上角
#         self.close_btn = QPushButton(self)
#         self.close_btn.setText('关闭')
#         self.close_btn.resize(self.btn_w,self.btn_h)

#         self.max_btn = QPushButton(self)
#         self.max_btn.setText('最大化')
#         self.max_btn.resize(self.btn_w,self.btn_h)

#         self.mini_btn = QPushButton(self)
#         self.mini_btn.setText('最小化')
#         self.mini_btn.resize(self.btn_w,self.btn_h)

#         # def close():
#         #     window.close()
#         self.close_btn.pressed.connect(self.close)
#         def max_normal():
#             if self.isMaximized(): #判断窗口是否最大化
#                 self.showNormal()
#                 self.max_btn.setText('最大化')
#             else:
#                 self.showMaximized()
#                 self.max_btn.setText('恢复')
#         self.max_btn.pressed.connect(max_normal)
#         self.mini_btn.pressed.connect(self.showMinimized)
#     def resizeEvent(self,QResizeEvent): #窗口大小发生变化的事件
#         print('窗口大小发生了改变')
#         close_btn_w = self.close_btn.width()
#         window_w = self.width()
#         close_btn_x = window_w - close_btn_w
#         close_btn_y = self.top_margin
#         self.close_btn.move(close_btn_x,close_btn_y)

#         max_btn_x = close_btn_x - self.max_btn.width()
#         max_btn_y = self.top_margin
#         self.max_btn.move(max_btn_x,max_btn_y)

#         mini_btn_x = max_btn_x - self.btn_w
#         mini_btn_y = self.top_margin
#         self.mini_btn.move(mini_btn_x,mini_btn_y)
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     # window = QWidget(flags=Qt.FramelessWindowHint)
#     window = Window()

#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# class Window(QWidget):
#     def paintEvent(self,evt):
#         print('窗口被绘制了')
#         return super().paintEvent(evt)
# class Btn(QPushButton):
#     def paintEvent(self,evt):
#         print('按钮被绘制了')
#         return super().paintEvent(evt)
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.setWindowTitle('[*]交互状态')
#     window.setWindowModified(True)
#     window.resize(500,500)
#     # btn = Btn(window)
#     # btn.setText('按钮')
#     # btn.pressed.connect(lambda : print('按钮被点击'))
#     # btn.setEnabled(False)
#     # print(btn.isEnabled())
#     w2 = QWidget()
#     w2.show()
#     window.show()
#     print(w2.isActiveWindow())
#     # window.setVisible(True)
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('交互状态')
#         self.resize(500,500)
#         self.setup_ui()
#     def setup_ui(self):
#         label = QLabel(self) #标签
#         label.setText('标签')
#         label.move(100,50)
#         label.hide()
#         le = QLineEdit(self)
#         # le.setText('文本框')
#         le.move(100,100)
#         btn = QPushButton(self)
#         btn.setText('登录')
#         btn.move(100,150)
#         btn.setEnabled(False)
#         def text_cao(text):
#             print('文本内容发生了改变',text)
#             # if len(text) > 0:
#             #     btn.setEnabled(True)
#             # else:
#             #     btn.setEnabled(False)
#             btn.setEnabled(len(text) > 0)
#         le.textChanged.connect(text_cao)
#         def check():
#             print('按钮被点击了')
#             content = le.text()
#             if content == 'Sz':
#                 label.setText('登录成功')
#             else:
#                 label.setText('登录失败')
#             label.show()
#             label.adjustSize()
#         btn.pressed.connect(check)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = QMainWindow() #组合控件 懒加载，用到的时候才会创建
#     # window.setWindowFlags(Qt.WindowContextHelpButtonHint | Qt.WindowCloseButtonHint | Qt.WindowMaximizeButtonHint)
#     window.statusBar() #状态栏
#     window.resize(500,500)
#     window.setWindowTitle('信息提示')
#     window.setStatusTip('这是一个窗口')
#     print(window.statusTip())
#     label = QLabel(window)
#     label.setText('社会我顺哥')
#     label.setStatusTip('这是标签') #状态栏提示
#     label.setToolTip('这是一个提示标签') #工具提示  悬浮在控件附近
#     label.setToolTipDuration(2000) #设置工具提示2S
#     label.setWhatsThis('这是啥？这是标签') #设置点击帮助提示
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# class Window(QWidget):
#     def mousePressEvent(self,evt):
#         print(self.focusWidget())
#         # self.focusNextChild()
#         # self.focusPreviousChild()
#         self.focusNextPrevChild(True)
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.setWindowTitle('焦点控制')
#     window.resize(500,500)
#     le1 = QLineEdit(window)
#     le1.move(50,50)
#     le2 = QLineEdit(window)
#     le2.move(100,100)
#     le3 = QLineEdit(window)
#     le3.move(150,150)
#     print(le1,le2,le3)
#     QWidget.setTabOrder(le1,le3)  #焦点le1后是le3
#     QWidget.setTabOrder(le3,le2)
#     # le2.setFocus() #设置焦点
#     # le2.setFocusPolicy(Qt.TabFocus)
#     # le2.setFocusPolicy(Qt.ClickFocus)
#     # le2.setFocusPolicy(Qt.StrongFocus)
#     print(window.focusWidget())
#     window.show()
#     le2.setFocus()
#     # le1.clearFocus()

#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# class Btn(QAbstractButton):  #抽象类子类化，不然不能使用
#     def paintEvent(self,evt): #绘制事件，抽象子类化必须自定义该函数
#         print('绘制按钮')
#         #绘制界面
#         painter = QPainter(self) #画家,绘制者，self是画纸，即画的位置
#         pen = QPen(QColor(11,200,20),5) #设置颜色和线条的宽度
#         painter.setPen(pen) #给画家一个笔
#         painter.drawText(50,50,self.text()) #绘制简单文本
#         painter.drawEllipse(0,0,100,100) #绘制内切椭圆
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle('QAbstractButton')
#     window.resize(500,500)
#     btn = Btn(window)
#     btn.setText('xxx')
#     btn.resize(100,100)
#     window.show()

#     sys.exit(app.exec_())
# import sys
# import  math
# from PyQt5.Qt import *
# class Btn(QPushButton):
#     def hitButton(self,point):  #
#         # print(point)
#         # # return True #返回有效,然后信号有效可以运行对应的槽函数
#         # if point.x() > self.width()/2:
#         #     return True
#         # else:
#         #     return False
#         center_x = self.width()/2 #计算圆心点
#         center_y = self.height()/2
#         hit_x = point.x() #获取点击点的相对x
#         hit_y = point.y() #获取点击点的相对y
#         distance = math.sqrt(pow(hit_x - center_x,2) + pow(hit_y-center_y,2))
#         print(distance)
#         if distance < self.width()/2:
#             return True
#         return False
#     def paintEvent(self,evt):
#         super().paintEvent(evt) #调用父类的绘制函数
#         painter = QPainter(self) #创建画家 参数是画布
#         painter.setPen(QPen(QColor(100,150,200),5))
#         painter.drawEllipse(self.rect()) #绘制椭圆，参数为矩形范围
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle('按钮功能测试')
#     window.resize(500,500)
#     btn = Btn(window)
#     btn.setText('点击')
#     btn.move(100,100)
#     btn.resize(200,200)
#     btn.pressed.connect(lambda : print('按钮被点击了'))
#     # for i in range(0,3):
#     #     btnx = QPushButton(window)
#     #     btnx.setText('btnx' + str(i))
#     #     btnx.move(50*i,50*i)
#     #     btnx.setAutoExclusive(True)
#     #     print(btnx.autoExclusive()) #排他性 同级排他
#     #     btnx.setCheckable(True)
#     # btnx = QPushButton(window)
#     # btnx.setText('btn3')
#     # btnx.move(250,250)
#     # btnx.setCheckable(True)
#     # btn = QPushButton(window)
#     # btn.setText('1')
#     # def plus_one():
#     #     print('+1')
#     #     num = int(btn.text()) + 1
#     #     btn.setText(str(num))
#     #     # push_button.animateClick(2000) #点击按钮，维持点击状态2s
#     # btn.pressed.connect(plus_one)
#     # btn.released.connect(lambda : print('按键被释放了'))
#     # btn.clicked.connect(lambda : print('按钮被点击')) #鼠标点击事件，指在控件范围内按下鼠标，并且在控件范围内松开鼠标
#     # btn.setCheckable(True)
#     # btn.toggled.connect(lambda value: print('按钮选中状态发生了改变',value)) #value为信号值，
#     # icon = QIcon('C:\\Users\\asus\\Pictures\\Saved Pictures\\jason-chen-22141-unsplash-1024x577.jpg') #创建图标类
#     # btn.setIcon(icon) #设置图标
#     # size = QSize(50,50) #参数为宽高
#     # btn.setIconSize(size) #设置图标的大小
#     # print(btn.icon())
#     # print(btn.iconSize())
#     # btn.pressed.connect(lambda : print('按钮被点击了'))
#     # # btn.setText('a&bc')   #添加快捷键alt + b
#     # btn.setShortcut('Alt+a') #设置快捷键Alt+a
#     # btn.setAutoRepeat(True) #设置自动重复
#     # btn.setAutoRepeatDelay(2000) #设置自动重复2s 即长按后2s才触发自动重复
#     # btn.setAutoRepeatInterval(1000) #每隔1s检测一次
#     # print(btn.autoRepeat())
#     # print(btn.autoRepeatInterval())
#     # print(btn.autoRepeatDelay())
#     # push_button = QPushButton(window) #普通按钮
#     # push_button.setText('这是QPushButton')
#     # push_button.move(100,100)
#     # radio_button = QRadioButton(window) #单选按钮
#     # radio_button.setText('这是一个radio')
#     # radio_button.move(100,150)
#     # checkbox = QCheckBox(window) #多选按钮
#     # checkbox.setText('这是一个checkbox')
#     # checkbox.move(100,200)
#     # push_button.setStyleSheet('QPushButton:pressed{background-color:red;}') #QPushButton按下是的样式
#     # print(push_button.isCheckable()) #判断是否可以被选中
#     # print(radio_button.isCheckable())
#     # print(checkbox.isCheckable())
#     # radio_button.setChecked(True) #设置处于被选中状态
#     # def cao():
#     #     # push_button.toggle() #切换未选中与选中状态
#     #     # radio_button.toggle()
#     #     # checkbox.toggle()
#     #     push_button.setChecked(not push_button.isChecked())
#     #     print('cao')
#     # btn.pressed.connect(cao)
#     # # push_button.setDown(True) #设置为按下，选中状态
#     # push_button.setCheckable(True) #设置push_button为可以选中
#     # # print(push_button.isCheckable())
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# class Window(QWidget):
#     def contextMenuEvent(self,evt): #右键菜单设置
#         print('展示菜单')
#         menu = QMenu() #创建菜单
#         open_recent_menu = QMenu(menu) #设置父对象为menu
#         open_recent_menu.setTitle('最近打开')

#         new_cation = QAction() #创建一个动作
#         new_cation.setText('新建')
#         # new_cation.setIcon(QIcon('C:\\Users\\asus\\Pictures\\Saved Pictures\\jason-chen-22141-unsplash-1024x577.jpg'))
#         open_action = QAction() #创建一个动作
#         open_action.setText('打开')
#         exit_action = QAction() #创建一个动作
#         exit_action.setText('退出')

#         file_action = QAction('Python-GUI编程-PyQt5')
#         open_recent_menu.addAction(file_action)
#         menu.addAction(new_cation) #为菜单添加动作
#         menu.addAction(open_action) #为菜单添加动作
#         menu.addMenu(open_recent_menu)
#         menu.addSeparator() #在open_action和exit_action之间添加分割线
#         menu.addAction(exit_action) #为菜单添加动作
#         new_cation.triggered.connect(lambda : print('新建文件'))
#         open_action.triggered.connect(lambda : print('打开文件'))
#         exit_action.triggered.connect(lambda : print('退出'))
#         open_recent_menu.triggered.connect(lambda : print('子菜单'))
#         # btn.setMenu(menu) #菜单为btn的菜单
#         menu.exec_(evt.globalPos()) #展示右键菜单 参数是位置 全局位置,即鼠标的位置
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.setWindowTitle('按钮的功能')
#     window.resize(500,500)
#     #使用构造函数
#     btn = QPushButton(QIcon('C:\\Users\\asus\\Pictures\\Saved Pictures\\jason-chen-22141-unsplash-1024x577.jpg'),'xxx',window)
#     # btn = QPushButton(window)
#     # btn.setText('xxx')
#     # menu = QMenu() #创建菜单
#     # open_recent_menu = QMenu(menu) #设置父对象为menu
#     # open_recent_menu.setTitle('最近打开')

#     # new_cation = QAction() #创建一个动作
#     # new_cation.setText('新建')
#     # # new_cation.setIcon(QIcon('C:\\Users\\asus\\Pictures\\Saved Pictures\\jason-chen-22141-unsplash-1024x577.jpg'))
#     # open_action = QAction() #创建一个动作
#     # open_action.setText('打开')
#     # exit_action = QAction() #创建一个动作
#     # exit_action.setText('退出')

#     # file_action = QAction('Python-GUI编程-PyQt5')
#     # open_recent_menu.addAction(file_action)
#     # menu.addAction(new_cation) #为菜单添加动作
#     # menu.addAction(open_action) #为菜单添加动作
#     # menu.addMenu(open_recent_menu)
#     # menu.addSeparator() #在open_action和exit_action之间添加分割线
#     # menu.addAction(exit_action) #为菜单添加动作
#     # new_cation.triggered.connect(lambda : print('新建文件'))
#     # open_action.triggered.connect(lambda : print('打开文件'))
#     # exit_action.triggered.connect(lambda : print('退出'))
#     # open_recent_menu.triggered.connect(lambda : print('子菜单'))
#     # btn.setMenu(menu) #菜单为btn的菜单

#     print(btn.menu())
#     # btn.setFlat(True)
#     # print(btn.isFlat()) #获取是否扁平化
#     btn2 = QPushButton(window)
#     btn2.setText('btn2')
#     btn2.move(200,200)
#     btn2.setAutoDefault(True) #点击后，设置为默认状态
#     print(btn.autoDefault())
#     print(btn2.autoDefault())
#     btn2.setDefault(True) #自动设置为默认状态
#     window.setContextMenuPolicy(Qt.CustomContextMenu) #方法为上下文菜单策略参数为自定义上下文菜单
#     def show_menu(point): #point为鼠标相对位置
#         print('自定义上下文菜单',point)
#         menu = QMenu() #创建菜单
#         open_recent_menu = QMenu(menu) #设置父对象为menu
#         open_recent_menu.setTitle('最近打开')

#         new_cation = QAction() #创建一个动作
#         new_cation.setText('新建')
#         # new_cation.setIcon(QIcon('C:\\Users\\asus\\Pictures\\Saved Pictures\\jason-chen-22141-unsplash-1024x577.jpg'))
#         open_action = QAction() #创建一个动作
#         open_action.setText('打开')
#         exit_action = QAction() #创建一个动作
#         exit_action.setText('退出')

#         file_action = QAction('Python-GUI编程-PyQt5')
#         open_recent_menu.addAction(file_action)
#         menu.addAction(new_cation) #为菜单添加动作
#         menu.addAction(open_action) #为菜单添加动作
#         menu.addMenu(open_recent_menu)
#         menu.addSeparator() #在open_action和exit_action之间添加分割线
#         menu.addAction(exit_action) #为菜单添加动作
#         new_cation.triggered.connect(lambda : print('新建文件'))
#         open_action.triggered.connect(lambda : print('打开文件'))
#         exit_action.triggered.connect(lambda : print('退出'))
#         open_recent_menu.triggered.connect(lambda : print('子菜单'))
#         btn.setMenu(menu) #菜单为btn的菜单
#         dest_point = window.mapToGlobal(point) #将鼠标的相对位置点映射成全局的鼠标点,参数为相对鼠标位置点
#         menu.exec_(dest_point) #展示右键菜单 参数是位置 全局位置,即鼠标的位置
#     window.customContextMenuRequested.connect(show_menu)
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle('QToolButton使用') #该按钮继承QAbstractButton
#     window.resize(500,500)
#     # btn = QCommandLinkButton('标题','描述',window) #命令链接按钮
#     # btn.setText('标题2')
#     # btn.setDescription('社会我顺哥')
#     # btn.setIcon(str)
#     tb = QToolButton(window) #工具菜单按钮
#     tb.setText('工具')
#     #默认只显示图标，不显示文字
#     tb.setIcon(QIcon('C:\\Users\\asus\\Pictures\\Saved Pictures\\jason-chen-22141-unsplash-1024x577.jpg'))
#     tb.setIconSize(QSize(60,60))
#     tb.setToolTip('这是一个新建按钮') #悬浮图标
#     tb.setAutoRaise(True)
#     # tb.setToolButtonStyle(Qt.ToolButtonIconOnly)
#     tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
#     tb.setArrowType(Qt.UpArrow)
#     btn = QPushButton(window)
#     btn.setText('一般按钮')
#     btn.move(100,100)
#     # btn.setFlat(True) #扁平化处理，当点击时显示3D效果
#     # menu = QMenu(btn)
#     menu = QMenu(tb)
#     # menu.setTitle('菜单')
#     sub_menu = QMenu(menu)
#     sub_menu.setTitle('子菜单')
#     sub_menu.setIcon(QIcon('C:\\Users\\asus\\Pictures\\Saved Pictures\\jason-chen-22141-unsplash-1024x577.jpg'))
#
#     action = QAction(QIcon('C:\\Users\\asus\\Pictures\\Saved Pictures\\jason-chen-22141-unsplash-1024x577.jpg'),'行为',menu)
#     action.setData([1,2,3])
#     action.triggered.connect(lambda : print('点击了行为菜单选项'))
#     action2 = QAction('行为2',menu)
#     action2.setData(['name','Sz'])
#     menu.addMenu(sub_menu)
#     menu.addSeparator()
#     menu.addAction(action)
#     menu.addAction(action2)
#     # btn.setMenu(menu)
#     tb.setMenu(menu)
#     tb.setPopupMode(QToolButton.MenuButtonPopup) #菜单的弹出方式 InstantPopup
#     tb.clicked.connect(lambda : print('工具按钮被点击'))
#     def do_action(action):
#         print('点击了行为',action.data())
#     tb.triggered.connect(do_action) #行为触发信号
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle('QRadioButton-功能测试')
#     window.resize(500,500)
#     red = QWidget(window)
#     red.resize(200,200)
#     red.setStyleSheet('background-color:red')
#     red.move(50,50)
#     green = QWidget(window)
#     green.resize(200, 200)
#     green.setStyleSheet('background-color:green')
#     green.move(red.x()+red.width(),red.y()+red.height())
#     rb_nan = QRadioButton('男',red)
#     rb_nan.move(10,10)
#     rb_nan.setChecked(True)
#     rb_nv = QRadioButton('女',red) #单选框，具有排他性，不可取消
#     rb_nv.move(10,50)
#     rb_nv.setShortcut('Alt+F')  #设置快捷键
#     # rb_nv.setIcon(str)
#     rb_nv.toggled.connect(lambda isChecked: print(isChecked))
#     # rb_nv.setAutoExclusive(False)
#     rb_yes = QRadioButton('yes',green)
#     rb_yes.move(10,10)
#     rb_no = QRadioButton('no',green)
#     rb_no.move(10,50) #参数时针对父控件的相对位置
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle('按钮组的使用')
#     window.resize(500,500)
#     r_male = QRadioButton('男',window)
#     r_female = QRadioButton('女',window)
#     r_female.setChecked(True)
#     r_male.move(100,100)
#     r_female.move(100,150)
#     sex_group = QButtonGroup(window) #创建按钮组
#     sex_group.addButton(r_male,1)
#     sex_group.addButton(r_female,2)
#     r_yes = QRadioButton('yes', window)
#     r_no = QRadioButton('no', window)
#     r_yes.move(300, 100)
#     r_no.move(300, 150)
#     #answer_group为组名
#     answer_group = QButtonGroup(window) #window为父控件，但是是虚拟的组
#     answer_group.addButton(r_yes)
#     answer_group.addButton(r_no)
#     answer_group.setId(r_yes,1)
#     answer_group.setId(r_no,2)
#     def test(val):
#         print(val,sex_group.id(val))
#     # sex_group.buttonClicked[int].connect(test)
#     sex_group.buttonClicked.connect(test)
#     print(answer_group.id(r_yes))
#     print(answer_group.id(r_no))
#     print(sex_group.buttons())
#     print(sex_group.button(1))
#     print(r_female.isChecked())
#     r_no.setChecked(True) #设置为选中状态
#     print(answer_group.checkedId()) #查看组中选中控件的id值，没有选中时返回值为-1
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle('QCheckBox功能测试')
#     window.resize(500, 500)
#     cb = QCheckBox('Python', window)  # 创建复选框按钮
#     cb.setIcon(QIcon('C:\\Users\\asus\\Pictures\\Saved Pictures\\jason-chen-22141-unsplash-1024x577.jpg'))
#     cb.setIconSize(QSize(60, 60))
#     cb.setTristate(True)
#     # cb.setCheckState(Qt.Checked) #选中状态
#     cb.setCheckState(Qt.PartiallyChecked)  # 部分选中状态
#     # cb.stateChanged.connect(lambda state: print(state))
#     cb.toggled.connect(lambda isChecked: print(isChecked))
#     window.show()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.Qt import *
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle('QLineEdit功能测试')
#     window.resize(500, 500)
#     # le = QLineEdit(window)  # 创建单行输入文本框
#     # le.setText('Sz')
#     # le.insert('18')  # 在原有基础上插入
#     # btn = QPushButton(window)
#     # btn.setText('按钮')
#     # btn.move(100, 100)
#     # # btn.pressed.connect(lambda: le.insert('18'))
#     # # btn.pressed.connect(lambda: print(le.text()))
#     # btn.pressed.connect(lambda: print(le.displayText()))
#     le_a = QLineEdit(window)
#     le_a.move(100, 200)
#     le_b = QLineEdit(window)
#     le_b.move(100, 300)
#     # le_b.setEchoMode(QLineEdit.PasswordEchoOnEdit)  # 设置输入框的输入模式，明文，密文，输入明文输入后密文 NoEcho Password
#
#     copy_btn = QPushButton(window)
#     copy_btn.setText('复制')
#     copy_btn.move(100, 400)
#     le_a.setMaxLength(3)
#     print(le_a.maxLength())
#     le_a.setReadOnly(True)  # 设置只读
#     le_a.setText('王炸，要不起')  # 可以程序设置，但不能超过字符数量限制
#
#     # le_b设置掩码
#     # 总共输入5位，左边2（必须大写）右边2（必须是一个数字
#     # le_b.setInputMask('>AA-99;_')  # 每一位都需要掩码字符表述 掩码使用 > 表示以下大写字母，A表示字母，- 为分隔符 9表示数字 ;号后是空白时的占位字符
#     # le_b.setInputMask('9999-9999999;0')
#
#     def copy_cao():
#         content = le_a.text()
#         # le_b.setText(content)
#         # le_b.setText('')
#         # le_b.insert(content)
#         # print(le_b.text(), le_b.displayText())
#         print(le_b.isModified())
#         le_b.setModified(False)
#
#     copy_btn.clicked.connect(copy_cao)
#     window.show()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.Qt import *
#
#
# class AccountTool:
#     ACCOUNT_ERROR = 1
#     PWD_ERROR = 2
#     SUCCESS = 3
#
#     @staticmethod
#     def check_login(account, pwd):  # 静态方法 参数不含self
#         # 把账号和密码发送给服务器，等待服务器返回结果
#         if account != 'sz':
#             return AccountTool.ACCOUNT_ERROR
#         if pwd != 'itlike':
#             return AccountTool.PWD_ERROR
#         return AccountTool.SUCCESS
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('登录案例')
#         self.resize(500, 500)
#         self.setMinimumSize(400, 400)
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.account_le = QLineEdit(self)
#         self.pwd_le = QLineEdit(self)
#         self.pwd_le.setEchoMode(QLineEdit.Password)
#         self.login_btn = QPushButton(self)
#         self.login_btn.setText('登录')
#         self.login_btn.clicked.connect(self.login_cao)
#         # 占位文本的提示
#         self.account_le.setPlaceholderText('请输入账号')
#         self.pwd_le.setPlaceholderText('请输入密码')
#         # 设置密码框，显示清空按钮
#         self.pwd_le.setClearButtonEnabled(True)
#         # 为密码文本框添加显示按钮
#         action = QAction(self.pwd_le)
#         action.setIcon(QIcon('C:\\Users\\asus\\Pictures\\Camera Roll\\close.jpg'))
#
#         def change():
#             print('改变明文和密文')
#             if self.pwd_le.echoMode() == QLineEdit.Normal:
#                 self.pwd_le.setEchoMode(QLineEdit.Password)
#                 action.setIcon(QIcon('C:\\Users\\asus\\Pictures\\Camera Roll\\close.jpg'))
#             else:
#                 self.pwd_le.setEchoMode(QLineEdit.Normal)
#                 action.setIcon(QIcon('C:\\Users\\asus\\Pictures\\Camera Roll\\open.jpg'))
#
#         action.triggered.connect(change)
#         self.pwd_le.addAction(action, QLineEdit.TrailingPosition)  # 图片显示在尾部
#         # 为账号文本框设置自动补齐
#         completer = QCompleter(['sz', 'shunzi', 'wangzha'], self.account_le)
#         self.account_le.setCompleter(completer)
#
#     def login_cao(self):
#         # print('xxx', self)
#         account = self.account_le.text()
#         pwd = self.pwd_le.text()
#         print(account, pwd)
#         state = AccountTool.check_login(account, pwd)
#         if state == AccountTool.ACCOUNT_ERROR:
#             print('账号错误')
#             self.account_le.setText('')
#             self.pwd_le.setText('')
#             self.account_le.setFocus(True)
#             return None
#         if state == AccountTool.PWD_ERROR:
#             print('密码错误')
#             self.pwd_le.setText('')
#             self.pwd_le.setFocus(True)
#             return None
#         if state == AccountTool.SUCCESS:
#             print('登录成功')
#         # if account != 'sz':
#         #     print('账号错误')
#         #     self.account_le.setText('')
#         #     self.pwd_le.setText('')
#         #     self.account_le.setFocus(True)
#         #     return None
#         # if pwd != 'itlike':
#         #     print('密码错误')
#         #     self.pwd_le.setText('')
#         #     self.pwd_le.setFocus(True)
#         #     return None
#         # print('登录成功')
#
#     def resizeEvent(self, evt):  # 窗口尺寸改变事件
#         widget_w = 150
#         widget_h = 40
#         margin = 60
#         self.account_le.resize(widget_w, widget_h)
#         self.pwd_le.resize(widget_w, widget_h)
#         self.login_btn.resize(widget_w, widget_h)
#         x = int((self.width() - widget_w) / 2)
#         self.account_le.move(x, int(self.height() / 4))
#         self.pwd_le.move(x, self.account_le.y() + widget_h + margin)
#         self.login_btn.move(x, self.pwd_le.y() + widget_h + margin)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class AgeVadidator(QValidator):
#     # 验证器判断数据是否合法
#     def validate(self, input_str, pos_int):
#         print(input_str, pos_int)
#         # 判断结果字符串，应该是有纯数字组成
#         try:
#             if 18 <= int(input_str) <= 180:
#                 return QValidator.Acceptable, input_str, pos_int  # 返回元组 对输入文本框有影响 ,输入正确
#                 # return QValidator.Acceptable, 'itlike', 1
#             elif 1 <= int(input_str) <= 17:
#                 return QValidator.Intermediate, input_str, pos_int
#             else:
#                 return QValidator.Invalid, input_str, pos_int  # 返回元组 对输入文本框有影响，输入错误
#         except:  # 程序异常进入，比如字符串转成整型数据
#             if len(input_str) == 0:
#                 return QValidator.Intermediate, input_str, pos_int
#             return QValidator.Invalid, input_str, pos_int
#
#     # 输入结束，判断最终结果是否符合状态 ,不合格才会进入 修复只会进行一次
#     def fixup(self, p_str):
#         print('修正', p_str)
#         try:
#             if int(p_str) < 18:
#                 return '18'
#             return '180'
#         except:
#             return '18'
#
#
# class MyAgeVadidator(QIntValidator):
#     def fixup(self, p_str):
#         print('修正', p_str)
#         # if int(p_str) <= 18 or len(p_str) == 0: #错误
#         if len(p_str) == 0 or int(p_str) < 18:  # 正确
#             return '18'
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QLineEdit-验证器使用')
#         self.resize(500, 500)
#         self.setup_ui()
#
#     def setup_ui(self):
#         le = QLineEdit(self)
#         le.move(100, 100)
#         # 18 - 180
#         # vadidator = AgeVadidator()
#         vadidator = MyAgeVadidator(18, 180)
#         le.setValidator(vadidator)
#         le2 = QLineEdit(self)
#         le2.move(100, 200)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.Qt import *
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle('QLineEdit-功能测试')
#     window.resize(640, 480)
#     le = QLineEdit(window)
#     le.move(100, 100)
#     le.resize(300, 300)
#     # le.setContentsMargins(100, 0, 0, 0)  # 文本边距设置
#     le.setStyleSheet('background-color:cyan;')
#     le.setTextMargins(0, 0, 50, 50)
#     le.setAlignment(Qt.AlignRight | Qt.AlignBottom)  # 设置输入文本框的对齐方式
#     le.setDragEnabled(True)  # 设置鼠标选中拖拽可行
#     le2 = QLineEdit(window)
#     le2.resize(50, 50)
#     le2.move(200, 0)
#     btn = QPushButton(window)
#     btn.setText('按钮')
#     btn.move(50, 50)
#
#
#     def cursor_cao():
#         # le.cursorBackward(True, 2)  # 设置光标向后移动，两个字符
#         # le.cursorForward(True, 3)
#         # le.cursorWordBackward(True)
#         # le.cursorWordForward(True)
#         # le.home(True) #行首
#         # le.end(True)  # 行尾
#         # le.setCursorPosition(len(le.text()) / 2)
#         # print(le.cursorPositionAt(QPoint(55, 5)))
#         # le.setCursorPosition(QPoint(55,5))
#         # le.setFocus()
#         # print(le.cursorPosition())
#         # le.cursorBackward(True, 2)
#         # le.backspace()
#         # le.del_()
#         # le.clear()
#         # le.cursorBackward(True, 3)
#         # # le.setFocus()
#         # le.cut()
#         # le.setCursorPosition(0)
#         # le.paste()
#         # le.setFocus()
#         # le.setSelection(2, 2)  # 起始位置和长度 2是位置，1是长度
#         # le.selectAll()  # 全选
#         # le.deselect()
#         le.setSelection(2, 3)
#         print(le.selectedText())
#         print(le.selectionStart())
#         print(le.selectionEnd())
#         print(le.selectionLength())
#
#
#     btn.clicked.connect(cursor_cao)
#     le.textEdited.connect(lambda val: print('文本框编辑的时候', val))  # 用户改变，非程序改变触发
#     le.textChanged.connect(lambda val: print('文本框内容改变的时候', val))
#     # le.returnPressed.connect(lambda : print('回车键被按下'))
#     # le.editingFinished.connect(lambda: print('结束编辑')) #结束编辑信号
#     # le.cursorPositionChanged.connect(lambda old_pos, new_pos: print(old_pos, new_pos))
#     le.selectionChanged.connect(lambda: print('选中文本改变', le.selectedText()))
#     le.setText('xxx')
#
#     window.show()
#     # print(window.width(),window.height())
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle('QFrame-功能测试')
#     window.resize(640, 480)
#     frame = QFrame(window)  # 边框样式
#     frame.resize(100, 100)
#     frame.move(100, 100)
#     frame.setStyleSheet('background-color:cyan;')
#     # frame.setFrameShape(QFrame.Box)  # 设置外边框
#     # frame.setFrameShape(QFrame.Panel)  # 设置外边框
#     # frame.setFrameShadow(QFrame.Raised)  # 设置阴影样式
#     frame.setFrameStyle(QFrame.Box | QFrame.Raised)
#     frame.setLineWidth(6)  # 外线 与内线宽相同
#     frame.setMidLineWidth(12)  # 中线
#     print(frame.frameWidth())
#     frame.setFrameRect(QRect(20,20,60,60))
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle('QTextEdit-父类功能测试')
#     window.resize(640, 480)
#     te = QTextEdit(window)
#     te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 垂直滚动策略
#     te.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)  # 水平滚动策略
#     btn = QPushButton(window)
#     btn.setIcon(QIcon('C:\\Users\\asus\\Pictures\\Camera Roll\\open.jpg'))
#     btn.pressed.connect(lambda: print('xxx'))
#     te.setCornerWidget(btn)
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class MyTextEdit(QTextEdit):
#     def mousePressEvent(self, evt):
#         print(evt.pos())  # 获取鼠标位置，相对位置
#         link_str = self.anchorAt(evt.pos())  # 获取鼠标相对位置处的锚点
#         if len(link_str):
#             QDesktopServices.openUrl(QUrl(link_str))  # 通过浏览器打开超链接地址
#         return super().mousePressEvent(evt)  # 解决鼠标不能使用的问题
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QTextEdit-功能测试')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         # self.te = QTextEdit(self)
#         self.te = MyTextEdit(self)
#         self.te.move(50, 50)
#         self.te.resize(300, 300)
#         self.te.setStyleSheet('background-color:cyan;')
#         self.te.textChanged.connect(self.text_change)
#         self.te.copyAvailable.connect(lambda: print('复制文本可用'))
#         self.zhanweiText()
#         self.textsetting()
#         test_btn = QPushButton(self)
#         test_btn.move(10, 10)
#         test_btn.setText('测试按钮')
#         test_btn.pressed.connect(self.btn_cao)
#
#     def text_change(self):
#         print('文本内容发生了改变')
#
#     def btn_cao(self):
#         print('按钮测试')
#         # self.te.setText('')
#         # self.te.clear()
#         # print(self.te.document())
#         # print(self.te.textCursor())
#         # self.cursortext()
#         # self.geshi_merge()
#         # self.getformat()
#         # self.text_secl()
#         # self.text_other()
#         # self.remove_text()
#         # self.postionlike()
#         # self.start_end()
#         # self.auto_format()
#         # self.soft_chalin()
#         # self.overwrimode()
#         # self.cursorseti()
#         # self.way_format()
#         # self.fontset()
#         # self.colorset()
#         # self.charset()
#         # self.oftenaction()
#         # self.setonlyread()
#         # self.tab_function()
#         self.web_superlink()
#
#     def web_superlink(self):
#         self.te.insertHtml('<a href="http://www.itlike.com">撩课</a>')
#
#     def tab_function(self):
#         # self.te.setTabChangesFocus(True)  # 设置tab键的功能为改变焦点
#         print(self.te.tabStopDistance())
#         self.te.setTabStopDistance(100)  # 设置tab键的大小为100像素
#
#     def setonlyread(self):
#         self.te.setReadOnly(True)  # 设置文本编辑器为只读模式 可以通过程序写入文本
#
#     def oftenaction(self):
#         # self.te.copy()
#         # self.te.setFocus()
#         # self.te.paste()
#         # self.te.selectAll()
#         # self.te.setFocus()
#         self.te.find('xx', QTextDocument.FindBackward)  # 设置查找方向为光标向前查找
#         self.te.setFocus()
#
#     def charset(self):
#         tcf = QTextCharFormat()
#         tcf.setFontFamily('宋体')
#         tcf.setFontPointSize(20)
#         tcf.setFontCapitalization(QFont.Capitalize)  # 首字母大写
#         tcf.setForeground(QColor(100, 200, 0))  # 设置字体颜色
#         self.te.setCurrentCharFormat(tcf)
#         tcf2 = QTextCharFormat()
#         tcf2.setFontOverline(True)
#         self.te.mergeCurrentCharFormat(tcf2)
#
#     def colorset(self):
#         self.te.setTextBackgroundColor(QColor(200, 10, 10))  # 设置背景颜色
#         self.te.setTextColor(QColor(10, 10, 200))  # 设置字体颜色
#
#     def fontset(self):
#         # QFontDialog.getFont()
#         # self.te.setFontFamily('幼圆')
#         # self.te.setFontWeight(QFont.Black)
#         # self.te.setFontItalic(True)
#         # self.te.setFontPointSize(30)
#         # self.te.setFontUnderline(True)
#         font = QFont()
#
#         self.te.setFont(font)
#
#     def way_format(self):
#         self.te.setAlignment(Qt.AlignCenter)  # 设置当前段落的对齐方式
#
#     def cursorseti(self):
#         if self.te.overwriteMode():
#             self.te.setOverwriteMode(False)
#             self.te.setCursorWidth(1)
#         else:
#             self.te.setOverwriteMode(True)
#             self.te.setCursorWidth(10)
#
#     def overwrimode(self):
#         self.te.setOverwriteMode(True)  # 设置覆盖模式 ubuntu下可以正常运行，window下不能正常运行
#         print(self.te.overwriteMode())
#         self.te.setFocus()
#
#     def soft_chalin(self):
#         # self.te.setLineWrapMode(QTextEdit.NoWrap)  # 禁止软换行
#         # self.te.setLineWrapMode(QTextEdit.FixedPixelWidth)  # 设置固定的像素宽度
#         self.te.setLineWrapMode(QTextEdit.FixedColumnWidth)  # 设置固定的宽度
#         self.te.setLineWrapColumnOrWidth(8)  # 设置软换行的列数或是像素宽度
#         self.te.setWordWrapMode(QTextOption.WordWrap)  # 设置保持单词的完整性
#
#     def auto_format(self):
#         # tc = self.te.textCursor()
#         self.te.setAutoFormatting(QTextEdit.AutoBulletList)  # 设置自动格式化
#
#     def start_end(self):
#         tc = self.te.textCursor()
#         tc.beginEditBlock()
#         tc.insertText('123\r\n')
#         tc.insertText('456\r\n')
#         tc.insertText('789\r\n')
#         tc.endEditBlock()
#
#     def postionlike(self):
#         tc = self.te.textCursor()
#         print('是否在段落的结尾：', tc.atBlockEnd())
#         print('是否在段落的开始：', tc.atBlockStart())
#         print('是否在文档的结尾：', tc.atEnd())
#         print('是否在文档的开始：', tc.atStart())
#         print('在第几列：', tc.columnNumber())
#         print('光标位置：', tc.position())  # 回车占用一个位置
#         print('在文本块中的位置：', tc.positionInBlock())
#
#     def remove_text(self):
#         tc = self.te.textCursor()
#         # tc.deleteChar()  # 删除光标后的字符和选中字符串
#         tc.deletePreviousChar()  # 删除光标前的字符和选中文本
#         self.te.setFocus(True)
#
#     def text_other(self):
#         tc = self.te.textCursor()
#         # print(tc.selectionStart())
#         # print(tc.selectionEnd())
#         print(tc.hasSelection())  # 判断是否选中文本
#         tc.removeSelectedText()  # 删除选中文本
#         self.te.setFocus(True)
#
#     def get_select(self):
#         tc = self.te.textCursor()
#         # print(tc.selectedText())
#         print(tc.selection())  # 返回的是对象名
#         print(tc.selection().toPlainText())
#
#     def text_secl(self):
#         tc = self.te.textCursor()
#         # tc.setPosition(6, QTextCursor.KeepAnchor)  # 设置锚点不动，改为选中效果
#         # tc.movePosition(QTextCursor.StartOfLine, QTextCursor.MoveAnchor, 1)  # 设置一行的开始，移动锚点
#         # tc.movePosition(QTextCursor.Up, QTextCursor.MoveAnchor, 1)  # 向上移动一行，移动锚点
#         # tc.select(QTextCursor.BlockUnderCursor)  # 向上选中一个段落
#         tc.select(QTextCursor.WordUnderCursor)  # 向上选中一个词
#         self.te.setTextCursor(tc)  # 反向设置 在界面上显示
#         self.te.setFocus(True)
#
#     def getformat(self):
#         tc = self.te.textCursor()
#         print(tc.block().text(), tc.blockNumber(), tc.currentList())
#
#     def geshi_merge(self):
#         print('块内格式设置')
#         tc = self.te.textCursor()
#         tcf = QTextCharFormat()
#         tcf.setFontFamily('幼圆')
#         tcf.setFontPointSize(30)
#         tcf.setFontOverline(True)  # 上划线
#         tcf.setFontUnderline(True)  # 下划线
#         tc.setCharFormat(tcf)
#
#         tcf2 = QTextCharFormat()
#         tcf2.setFontStrikeOut(True)
#         tc.mergeCharFormat(tcf2)
#         return None
#         tbf = QTextBlockFormat()
#         tbf.setAlignment(Qt.AlignCenter)
#         # tbf.setIndent(2)
#         tc.setBlockFormat(tbf)
#         return None
#         tcf = QTextCharFormat()
#         tcf.setFontFamily('幼圆')
#         tcf.setFontPointSize(30)
#         tcf.setFontOverline(True)  # 上划线
#         tcf.setFontUnderline(True)  # 下划线
#         tc.setBlockCharFormat(tcf)
#
#     def cursortext(self):
#         tc = self.te.textCursor()
#         tff = QTextFrameFormat()  # 设置文本框格式
#         tff.setBorder(10)
#         tff.setBorderBrush(QColor(100, 50, 50))
#         tff.setRightMargin(50)
#         tc.insertFrame(tff)
#         doc = self.te.document()
#         print(doc.rootFrame())
#         root_frame = doc.rootFrame()
#         root_frame.setFrameFormat(tff)
#         return None
#         tc = self.te.textCursor()
#         tbf = QTextBlockFormat()  # 段落设置
#         tcf = QTextCharFormat()  # 字符设置
#         tcf.setFontFamily('隶书')
#         tcf.setFontItalic(True)  # 设置斜体
#         tcf.setFontPointSize(16)
#         tbf.setAlignment(Qt.AlignRight)  # 对齐方式 右对齐
#         tbf.setRightMargin(100)  # 右边距
#         tbf.setIndent(3)  # 缩进长度 3个tab长度
#         tc.insertBlock(tbf, tcf)
#         self.te.setFocus()
#         return None
#         tc = self.te.textCursor()
#         # tc.insertTable(5,3)
#         ttf = QTextTableFormat()
#         ttf.setAlignment(Qt.AlignRight)  # 右对齐
#         ttf.setCellPadding(6)  # 内边距
#         ttf.setCellSpacing(3)  # 外边距
#         ttf.setColumnWidthConstraints((QTextLength(QTextLength.PercentageLength, 50),
#                                        QTextLength(QTextLength.PercentageLength, 40),
#                                        QTextLength(QTextLength.PercentageLength, 10)))
#         # print(tc.insertTable(5, 3, ttf))
#         table = tc.insertTable(5, 3, ttf)
#         # table.appendColumns(2)  # 追加列
#         return None
#         tc = self.te.textCursor()
#         # tl = tc.insertList(QTextListFormat.ListCircle)  # 插入列表
#         # tl = tc.insertList(QTextListFormat.ListDecimal)  # 插入带序列列表
#         # tl = tc.createList(QTextListFormat.ListCircle)  # 创建列表
#         tlf = QTextListFormat()
#         tlf.setIndent(3)
#         tlf.setNumberPrefix('<<')
#         tlf.setNumberSuffix('>>')
#         tlf.setStyle(QTextListFormat.ListDecimal)
#         tl = tc.createList(tlf)  # 创建列表
#         print(tl)
#         return None
#         tc = self.te.textCursor()
#         # tdf = QTextDocumentFragment.fromHtml('<h1>xxx</h1>')  # 插入html文本块
#         tdf = QTextDocumentFragment.fromPlainText('<h1>xxx</h1>')  # 插入普通文本块
#         tc.insertFragment(tdf)
#         return None
#         tc = self.te.textCursor()
#         tif = QTextImageFormat()
#         tif.setName('C:\\Users\\asus\\Pictures\\Camera Roll\\open.jpg')  # 图片名称即路径
#         tif.setWidth(100)  # 设置宽度
#         tif.setHeight(100)  # 设置高度
#         tc.insertImage(tif)
#         return None
#         tc = self.te.textCursor()  # 获取文本光标对象
#         tcf = QTextCharFormat()
#         tcf.setToolTip('撩课学院网址')  # 设置悬浮提示
#         tcf.setFontFamily('隶书')  # 设置字体格式
#         tcf.setFontPointSize(16)  # 设置字体大小
#         tc.insertText('itlike.com', tcf)  # 插入文本
#         tc.insertHtml('<a href="http://www.itlike.com" > 撩课 </a>')  # 添加超链接
#
#     def textsetting(self):
#         # 设置普通文本内容
#         # self.te.setPlainText('<h1>xxx</h1>')
#         # self.te.insertPlainText('<h1>xxx</h1>')
#         # self.te.insertPlainText('<h1>ooo</h1>')
#         # print(self.te.toPlainText())
#         # self.te.setHtml('<h1>xxx</h1>')
#         # self.te.insertHtml('<h4>xxx</h4>')
#         # print(self.te.toHtml())
#         # self.te.setText('<h1>xxx</h1>')  # 自动判断txt和html格式
#         # self.te.append('ooo')  # 添加，会在文本最后添加且会自动检查文本格式
#         pass
#
#     def zhanweiText(self):
#         self.te.setPlaceholderText('请输入你的个人简介：')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QPlainTextEdit-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         pte = QPlainTextEdit(self)
#         self.pte = pte  # 将局部变量绑定到实例对象上
#         pte.resize(300, 300)
#         pte.move(100, 100)
#         line_num_parent = QWidget(self)
#         line_num_parent.resize(30, 300)
#         line_num_parent.move(70, 100)
#         line_num_parent.setStyleSheet('background-color:cyan')
#         self.line_label = QLabel(line_num_parent)
#         self.line_label.move(0, 5)
#         line_nums = '\n'.join([str(i) for i in range(1, 101)])
#         self.line_label.setText(line_nums)
#         self.line_label.adjustSize()
#         test_btn = QPushButton(self)
#         test_btn.setText('测试按钮')
#         test_btn.move(20, 20)
#         test_btn.pressed.connect(self.test_cao)
#         self.place_text()
#         # self.format_set()
#         # self.autochangeline()
#         # self.setcursorformat()
#
#     def test_cao(self):
#         print('测试按钮')
#         # self.pte.setPlainText('社会我顺哥，人狠话不多')  # 将原本的老内容清楚，添加新内容
#         # # self.pte.setFocus()
#         # self.pte.insertPlainText('itlike')  # 在光标出插入文本
#         # self.pte.appendHtml('<a href="http://www.itlike.com">撩课</a>')  # 在文本最后添加文本
#         # table_str = "<table border=2>" \
#         #             "<tr><td>1</td><td>2</td><td>3</td></tr>" \
#         #             "<tr><td>4</td><td>5</td><td>6</td></tr>" \
#         #             "</table>"
#         # self.pte.appendHtml(table_str)  # 不支持富文本，即表格
#         # print(self.pte.toPlainText())
#         # self.blockaction()
#         # self.zoom_set()
#         # self.scroll_test()
#         # self.cursor_action()
#         self.sign_action()
#
#     def sign_action(self):
#         # self.pte.textChanged.connect(lambda: print('文本改变了'))
#         # self.pte.cursorPositionChanged.connect(lambda: print('光标位置改变'))
#         # self.pte.blockCountChanged.connect(lambda bc: print('块的个数发生改变', bc))
#         # self.pte.selectionChanged.connect(lambda: print('选中内容发生改变', self.pte.textCursor().selectedText()))
#         # self.pte.modificationChanged.connect(lambda val: print('修改状态发生改变', val))
#         # doc = self.pte.document()
#         # doc.setModified(False)
#         self.pte.updateRequest.connect(lambda rect, dy: print('内容区域改变', rect, dy))  # 更新的区域和垂直方向的位移
#         self.pte.updateRequest.connect(lambda rect, dy: self.line_label.move(self.line_label.x(), self.line_label.y() + dy))  # 实现文本框行号功能
#
#     def cursor_action(self):
#         # tc = self.pte.textCursor()
#         # tc.insertImage('C:\\Users\\asus\\Pictures\\Camera Roll\\open.jpg')  # 不能插入图片
#         # tc.insertTable(5, 6)  # 不能插入表格
#         # tc = self.pte.cursorForPosition(QPoint(100, 60))  # 返回光标对象 相对光标位置，针对固定界面
#         # tc.insertText('xxx')
#         # self.pte.setCursorWidth(20)
#         self.pte.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)  # 移动光标位置，锚点不移动
#         self.pte.setFocus()
#         # print(tc)
#
#     def scroll_test(self):
#         self.pte.setCenterOnScroll(True)  # 设置光标末尾可以滚到文件的中间
#         self.pte.centerCursor()  # 设置光标所在的位置为文本框的中间
#         self.pte.ensureCursorVisible()  # 保证光标可见
#         self.pte.setFocus()
#
#     def zoom_set(self):
#         self.pte.zoomIn(1)  # 放大、缩小操作 正数放大，负数缩小
#
#     def blockaction(self):
#         print(self.pte.blockCount())  # 返回文本块的个数，文本块以回车区分
#         self.pte.setMaximumBlockCount(3)  # 设置块的最大个数
#
#     def setcursorformat(self):
#         self.pte.setOverwriteMode(True)  # 只对英文字符有效，对中文和数字无效
#
#     def format_set(self):
#         tcf = QTextCharFormat()
#         tcf.setFontUnderline(True)
#         tcf.setUnderlineColor(QColor(200, 100, 100))
#         self.pte.setCurrentCharFormat(tcf)
#
#     def autochangeline(self):
#         self.pte.setLineWrapMode(QPlainTextEdit.NoWrap)  # 关闭软换行
#
#     def place_text(self):
#         self.pte.setPlaceholderText('请输入你的个人信息')
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QKeySequenceEdit-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         kse = QKeySequenceEdit(self)  # 录制快捷键的类
#         # ks = QKeySequence(QKeySequence.Copy)
#         ks = QKeySequence(Qt.CTRL + Qt.Key_C, Qt.CTRL + Qt.Key_A)
#         # ks = QKeySequence('Ctrl+c')
#         kse.setKeySequence(ks)
#         kse.clear()
#         btn = QPushButton(self)
#         btn.setText('测试按钮')
#         btn.move(100, 100)
#         btn.clicked.connect(lambda: print(kse.keySequence().toString(), kse.keySequence().count()))
#         kse.editingFinished.connect(lambda: print('结束编辑'))
#         kse.keySequenceChanged.connect(lambda key_val: print('键位序列发生改变', key_val.toString()))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class MyASB(QAbstractSpinBox):
#     def __init__(self, parent=None, num='0', *args, **kwargs):  # 定义函数时，None的意思是不传值是None
#         super().__init__(parent, *args, **kwargs)  # 调用函数，参数需要传入
#         self.lineEdit().setText(num)
#
#     def stepEnabled(self):  # 属于自动调用
#         # current_num = int(self.text())
#         # if current_num == 0:
#         #     return QAbstractSpinBox.StepUpEnabled  # 仅向上有效
#         # elif current_num == 9:
#         #     return QAbstractSpinBox.StepDownEnabled  # 仅向下有效
#         # elif current_num < 0 or current_num > 9:
#         #     return QAbstractSpinBox.StepNone  # 无效
#         # else:
#         #     return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled  # 向上、向下都有效
#         return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled
#
#     def stepBy(self, p_int):  # 有效时才会调用该函数，属于自动调用
#         print(p_int)
#         current_num = int(self.text()) + p_int
#         self.lineEdit().setText(str(current_num))  # 首先获取单行文本控件对象
#
#     def validate(self, p_str, p_int):
#         num = int(p_str)
#         if num < 18:
#             return QValidator.Intermediate, p_str, p_int
#         elif num <= 180:
#             return QValidator.Acceptable, p_str, p_int
#         else:
#             return QValidator.Invalid, p_str, p_int
#
#     def fixup(self, p_str):
#         return '18'
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QAbstractSpinBox-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         asb = MyASB(self)  # 单位文本编辑器，右面带有调节器，是个组合控件，左边是个单行文本编辑器
#         self.asb = asb
#         asb.resize(100, 30)
#         asb.move(100, 100)
#         asb.editingFinished.connect(lambda: print('结束编辑'))
#         # asb.setAccelerated(True)  # 设置按钮使数据递增的数据速度加速
#         # print(asb.isAccelerated())
#         # asb.setReadOnly(True)
#         # print(asb.isReadOnly())  # 只读是针对按钮，不能通过键盘输入
#         test_btn = QPushButton(self)
#         test_btn.move(200, 200)
#         test_btn.setText('测试按钮')
#         test_btn.clicked.connect(self.btn_cao)
#
#     def btn_cao(self):
#         print('测试按钮')
#         # print(self.asb.text())
#         # print(self.asb.lineEdit().text())
#         # print(self.asb.lineEdit().setText('88'))
#         # cl = QCompleter(['sz', '123', '18'], self.asb)  # 自动匹配对象，需要输入元组
#         # self.asb.lineEdit().setCompleter(cl)  # 设置自动匹配，需要自动匹配的对象
#         # # self.asb.lineEdit().setAlignment(Qt.AlignCenter)  # 设置自动对齐方式
#         # self.asb.setAlignment(Qt.AlignCenter)
#         # print(self.asb.hasFrame())
#         # # self.asb.setFrame(False)  # 设置取消边框
#         # self.asb.setButtonSymbols(QAbstractSpinBox.NoButtons)  # 设置右侧按键样式
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class MySb(QSpinBox):
#     def textFromValue(self, p_int):  # 该函数可以自定义显示内容
#         print(p_int)
#         return str(p_int) + '*' + str(p_int)  # 本身数值没变，返回值需要显示在窗口上
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QSpinBox-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         sb = MySb(self)
#         self.sb = sb
#         sb.resize(100, 30)
#         sb.move(100, 100)
#         sb.valueChanged.connect(lambda val: print(type(val), val))  # 可以在信号添加[str]，将整型数据转化为str型
#         btn = QPushButton(self)
#         btn.setText('测试按钮')
#         btn.move(150, 150)
#         btn.clicked.connect(self.test_cao)
#         # self.max_min()
#
#     def test_cao(self):
#         print('测试按钮')
#         self.num_xuanhuan()
#         # self.step_log()
#         self.pre_suff()
#         # self.setjinzhi()
#         self.setnum_get()
#
#     def setnum_get(self):
#         # self.sb.setValue(66)  # 设置数值
#         print(self.sb.value())  # 该获取函数不能获取前缀和后缀
#         print(self.sb.text())  # 获取完整的内容
#         print(self.sb.lineEdit().text())  # 获取完整的内容
#
#     def setjinzhi(self):
#         self.sb.setDisplayIntegerBase(2)  # 设置显示数据的进制
#         print(self.sb.displayIntegerBase())
#
#     def pre_suff(self):
#         # self.sb.setRange(1, 12)
#         # self.sb.setSuffix('月')  # 设置后缀
#         self.sb.setRange(0, 6)
#         self.sb.setPrefix('周')  # 设置前缀
#         self.sb.setSpecialValueText('周日')  # 设置最小值为特殊显示文本
#
#     def step_log(self):
#         self.sb.setSingleStep(3)  # 设置按钮按下变化的单步步长
#
#     def num_xuanhuan(self):
#         print(self.sb.wrapping())
#         self.sb.setWrapping(True)  # 设置数值循环
#         print(self.sb.wrapping())
#
#     def max_min(self):
#         # self.sb.setMaximum(180)  # 设置范围的最大值
#         # print(self.sb.maximum())
#         # self.sb.setMinimum(18)  # 设置范围的最小值
#         # print(self.sb.minimum())
#         self.sb.setRange(18, 180)  # 设置范围，最大最小都可取
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class MyDsb(QDoubleSpinBox):
#     def textFromValue(self, p_float):
#         print('mydsb', p_float)
#         return str(p_float) + '*' + str(p_float)  # 文本框会显示的内容，但是不包括前后缀
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QDoubleSpinBox-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         dsb = MyDsb(self)
#         self.dsb = dsb
#         dsb.move(100, 100)
#         dsb.resize(100, 30)
#         # dsb.setRange(1.0, 2.0)
#         # dsb.setSingleStep(0.5)
#         # dsb.setSuffix('倍速')
#         # dsb.setSpecialValueText('正常')  # 设置特殊字符 指的是最小值
#         # dsb.setWrapping(True)
#         # dsb.setDecimals(1)  # 设置保留小数，1指一位小数
#         # dsb.setDecimals(8)  # 设置保留小数，8指八位小数
#         # dsb.setMaximum(99.99)
#         # dsb.setMinimum(0.00)
#         # dsb.setSingleStep(0.01)  # 设置步长为0.01
#         # dsb.setWrapping(True)  # 设置循环
#         dsb.setPrefix('$')  # 设置前缀
#         dsb.setSuffix('%')  # 设置后缀
#         btn = QPushButton(self)
#         btn.setText('测试按钮')
#         btn.move(100, 200)
#         btn.clicked.connect(self.test_cao)
#         dsb.valueChanged.connect(lambda val: print(type(val), val))  # 有效值改变信号，返回值为float
#         dsb.valueChanged[str].connect(lambda val: print(type(val), val))  # 有效值改变信号,返回值为str
#
#     def test_cao(self):
#         print('测试按钮')
#         self.get_value()
#
#     def get_value(self):
#         # self.dsb.setValue(66.666)  # 根据设置的小数位数自动四舍五入
#         print(type(self.dsb.value()), self.dsb.value())  # 仅仅是有效数字
#         print(type(self.dsb.cleanText()), self.dsb.cleanText())  # 不包括前后缀,但可以显示用户自定义的内容
#         print(type(self.dsb.text()), self.dsb.text())  # 显示什么返回什么
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QDataTimeEdit-学习')
#         # self.setWindowTitle('时间日期学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         # dte = QDateTimeEdit(QDateTime.currentDateTime(), self)  # 创建调节日期时间的控件
#         # dte = QDateTimeEdit(QDate.currentDate(), self)  # 创建调节日期时间的控件
#         # dte = QDateTimeEdit(QTime.currentTime(), self)  # 创建调节日期时间的控件
#         dte = QDateTimeEdit(self)
#         self.dte = dte
#         dte.move(100, 100)
#         dte.setDisplayFormat('yyyy-MM-dd $ h: m: ss: zzz')  # 年 月 日 时 分钟 秒 毫秒
#         print(dte.displayFormat())
#
#         # dt = QDateTime(2018, 12, 12, 12, 30)
#         # dt = QDateTime.currentDateTime()
#         # dt.addYears(2) #返回值是QDateTime对象
#         # print(dt.offsetFromUtc())  # 与标准时间的差值
#         # print(dt)
#         # QDateTimeEdit(dt, self)  # 显示在self对象上
#         # time = QTime.currentTime()
#         # time.start()
#         btn = QPushButton(self)
#         btn.setText('测试按钮')
#         btn.move(200, 200)
#         btn.clicked.connect(self.test_cao)  # 返回值是ms级
#
#     def test_cao(self):
#         print('测试按钮')
#         # if self.dte.currentSectionIndex() != 0:
#         #     self.dte.setCurrentSectionIndex(self.dte.currentSectionIndex() - 1)
#         # else:
#         #     self.dte.setCurrentSectionIndex(6)
#         # print(self.dte.currentSectionIndex())  # 获取当前索引部分
#         # print(self.dte.sectionText(QDateTimeEdit.DaySection))  # 获取日部分
#         # self.dte.setMaximumDateTime(QDateTime(2020, 8, 15, 12, 30))  # 设置日期的最大值
#         # self.dte.setMinimumDateTime(QDateTime.currentDateTime())  # 设置日期的最小值
#         # self.dte.setDateTimeRange(QDateTime.currentDateTime().addDays(-3), QDateTime.currentDateTime().addDays(3))  # 设置日期的范围
#         # print(QDateTime.currentDateTime())
#         self.dte.setCalendarPopup(True)  # 设置日历选择控件可以弹出
#         print(self.dte.dateTime())  # 可以获取到修改后的日期
#         self.dte.dateTimeChanged.connect(lambda: print(self.dte.dateTime()))
#         self.dte.dateChanged.connect(lambda val: print('日期发生改变', val))
#         self.dte.timeChanged.connect(lambda val: print('时间发生改变', val))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QTimeEdit-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         # de = QDateEdit(self)
#         # de.setDisplayFormat('yyyy-MMMM-dddd')  # 显示年 月 星期
#         # print(de.dateTime())
#         te = QTimeEdit(QTime.currentTime(), self)
#         te.setDisplayFormat('hh-m-ss:zzz a')
#         print(te.time())
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QComboBox-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         cb = QComboBox(self)  # 下拉选项列表
#         self.cb = cb
#         cb.resize(300, 30)
#         # cb.addItem('xx1')  # 添加下拉列表
#         # cb.addItem('xx2')  # 添加下拉列表
#         # cb.addItem(QIcon('C:\\Users\\asus\\Pictures\\Camera Roll\\open.jpg'),'xx3')  # 添加下拉列表,且携带图标
#         cb.addItems(['1', '2', '3'])  # []为列表,()为元组，都可迭代
#         cb.addItem(QIcon('C:\\Users\\asus\\Pictures\\Camera Roll\\close.jpg'), '撩课', {'name': 'itlike'})  # 1 图标 2 名称 3 附加额外数据
#         # cb.insertItem(1, QIcon('C:\\Users\\asus\\Pictures\\Camera Roll\\open.jpg'), 'xx')  # 1为索引值
#         # cb.insertItems(1, ['a', 'b', 'c'])
#         # cb.setItemIcon(2, QIcon('C:\\Users\\asus\\Pictures\\Camera Roll\\close.jpg'))  # 修改对应索引值的图标
#         # cb.setItemText(2, 'she')  # 修改对应索引值的文字
#         # cb.insertSeparator(2)  # 在对应的索引位置插入分割线
#         # cb.setCurrentIndex(1)  # 设置当前选中，有索引值和文本两种
#         # cb.setCurrentText('2')
#         # cb.setEditable(True)  # 设置可以编辑
#         # model = QStandardItemModel()
#         # item1 = QStandardItem('item1')
#         # item2 = QStandardItem('item2')
#         # item22 = QStandardItem('item22')
#         # item2.appendRow(item22)
#         # model.appendRow(item1)
#         # model.appendRow(item2)
#         # cb.setModel(model)  # 设置模型显示
#         # cb.setView(QTreeView(cb))  # 设置树形视图
#         btn = QPushButton(self)
#         btn.setText('测试按钮')
#         btn.move(200, 200)
#         btn.clicked.connect(self.test_cao)
#
#     def test_cao(self):
#         print('测试按钮')
#         # print(self.cb.count())
#         # print(self.cb.currentIndex())
#         # print(self.cb.currentText())
#         # print(self.cb.currentData())
#         # print(self.cb.itemIcon(self.cb.currentIndex()))
#         # print(self.cb.itemText(self.cb.count() - 1))
#         # print(self.cb.itemData(self.cb.count() - 1))
#
#         # self.cb.setMaxCount(6)  # 设置下拉文本框最大的下拉数量
#         self.cb.setEditable(True)
#         # self.cb.setMaxVisibleItems(5)  # 设置当前最大可以展示的条目个数
#         # self.cb.setIconSize(QSize(60, 60))  # 设置图标的尺寸大小
#         # self.cb.setSizeAdjustPolicy(QComboBox.AdjustToContents)  # 尺寸策略为参照内容
#         # self.cb.setFrame(False)  # 取消控件黑边框
#         # self.cb.setDuplicatesEnabled(True)  # 设置条目可以重复
#         # self.cb.addItem('it')
#         # self.cb.clear()  # 清空所有条目
#         # self.cb.showPopup()  # 弹出下拉列表
#         # self.cb.setCompleter(QCompleter(['123', '1', '2', '3']))  # 快速匹配
#         # QValidator
#         # self.cb.setValidator()  # 设置验证器
#         self.cb.activated.connect(lambda val: print('条目被激活', val))  # 返回索引值，用户交互产生的信号
#         self.cb.activated[str].connect(lambda val: print('条目被激活', val))  # 返回索引值
#         self.cb.currentIndexChanged.connect(lambda val: print('当前索引发生改变', val))
#         self.cb.currentIndexChanged[str].connect(lambda val: print('当前索引发生改变', val))  # 程序改变可以产生该信号
#         self.cb.currentTextChanged.connect(lambda val: print('当前文本发生改变', val))  # 文本改变就会发送信号
#         self.cb.editTextChanged.connect(lambda val: print('当前编辑的文本发生改变', val))
#         self.cb.highlighted.connect(lambda val: print('高亮', val))  # 谁是高亮打印谁，返回索引值
#         self.cb.highlighted[str].connect(lambda val: print('高亮', val))  # 谁是高亮打印谁，返回索引值
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('案例学习')
#         self.resize(640, 480)
#
#         self.city_dic = {'北京': {'东城': '001', '西城': '002', '朝阳': '003', '丰台': '004'},
#                          '上海': {'黄埔': '005', '徐汇': '006', '长宁': '007', '静安': '008', '松江': '009'},
#                          '广东': {'广州': '010', '深圳': '011', '湛江': '012', '佛山': '013'}}
#         self.setup_ui()
#
#     def setup_ui(self):
#         pro = QComboBox(self)
#         city = QComboBox(self)
#         self.pro = pro
#         self.city = city
#         pro.move(100, 100)
#         city.move(200, 100)
#         pro.currentIndexChanged[str].connect(self.pro_changed)
#         # pro.setCurrentIndex(0)
#         # self.pro_changed(pro.currentText())
#         city.currentIndexChanged[int].connect(self.city_changed)
#         # self.city_changed(city.currentIndex())
#         pro.addItems(self.city_dic.keys())  # 添加条目应当放在最后
#
#     def pro_changed(self, pro_name):
#         print(pro_name)
#         citys = self.city_dic[pro_name]
#         print(citys)
#         self.city.clear()
#         # self.city.addItems(citys)
#         for key, val in citys.items():
#             self.city.addItem(key, val)  # val为添加的额外数据
#
#     def city_changed(self, item_id):
#         # print(item_id)
#         if item_id == -1:
#             return None
#         print(self.city.itemData(item_id))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QFontComboBox-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         label = QLabel(self)
#         label.setText('社会我顺哥，人狠话不多')
#         label.move(100, 100)
#         fcb = QFontComboBox(self)  # 字体设置下拉选项
#         fcb.setEditable(False)  # 设置不可编辑
#         fcb.currentFontChanged.connect(lambda font: label.setFont(font))
#         fcb.currentFontChanged.connect(lambda font: print(font))  # 返回值为一个对象
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QAbstractSlider-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         label = QLabel(self)
#         label.setText('0')
#         label.move(200, 200)
#         label.resize(100, 30)
#         sd = QSlider(self)  # 滑块控件
#         sd.move(100, 100)
#         sd.valueChanged.connect(lambda val: label.setText(str(val)))
#         sd.setMaximum(100)  # 设置最大值
#         sd.setMinimum(1)  # 设置最小值
#         sd.setValue(88)  # 设置滑块当前值
#         sd.setSingleStep(5)  # 设置步长为5,针对键盘上下键而言
#         sd.setPageStep(10)  # 设置上下翻页的步长
#         # sd.setTracking(False)  # 设置数据跟踪
#         # sd.setSliderPosition(88)  # 设置滑块位置
#         sd.setInvertedAppearance(True)  # 设置倒立外观
#         sd.setInvertedControls(True)  # 反转上下的控制
#         sd.setOrientation(Qt.Horizontal)  # 设置滑块水平
#         # sd.sliderMoved.connect(lambda val: print(val))
#         # sd.actionTriggered.connect(lambda val: print(val))  # 返回值为1、2、7、3
#         sd.rangeChanged.connect(lambda min, max: print(min, max))  # 范围改变信号
#         sd.setMaximum(200)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Slider(QSlider):
#     def __init__(self, parent=None, *args, **kwargs):
#         super().__init__(parent, *args, **kwargs)
#         self.setTickPosition(QSlider.TicksBothSides)  # 添加控件刻度线
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.label = QLabel(self)
#         self.label.setText('0')
#         self.label.setStyleSheet('background-color:red;')
#         self.label.hide()
#
#     def mousePressEvent(self, evt):
#         super().mousePressEvent(evt)  # 继续向外界发射信号，保证父类方法完整性
#         x = (self.width() - self.label.width()) / 2
#         y = (1 - self.value() / (self.maximum() - self.minimum())) * self.height() - self.label.height()
#         self.label.show()
#         self.label.move(int(x), int(y))
#
#     def mouseMoveEvent(self, evt):
#         super().mouseMoveEvent(evt)
#         self.label.setText(str(self.value()))
#         self.label.adjustSize()
#         x = (self.width() - self.label.width()) / 2
#         y = (1 - self.value() / (self.maximum() - self.minimum())) * (self.height()-self.label.height())
#         self.label.show()
#         self.label.move(int(x), int(y))
#
#     def mouseReleaseEvent(self, evt):
#         super().mouseReleaseEvent(evt)
#         self.label.hide()
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QSlider-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         slider = Slider(self)
#         slider.move(200, 200)
#         slider.resize(30, 200)
#
#         # sd.valueChanged.connect(lambda val: print(val))
#         # sd.setTickInterval(5)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QScrollBar-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         sb = QScrollBar(self)  # 垂直滚动条
#         sb.resize(30, 200)
#         sb.move(100, 100)
#         sb1 = QScrollBar(Qt.Horizontal, self)  # 水平滚动条
#         sb1.resize(200, 30)
#         sb1.move(150, 100)
#         sb.valueChanged.connect(lambda val: print(val))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QDial-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         label = QLabel(self)
#         label.move(200, 200)
#         label.setText('社会我顺哥，人狠话不多')
#         label.setStyleSheet('font-size:30px;')
#         dia = QDial(self)  # 滚轮控件
#         dia.setRange(1, 100)  # 设置范围
#         dia.setNotchesVisible(True)  # 显示刻度
#         dia.valueChanged.connect(lambda val: print('值发生了改变', label.setStyleSheet('font-size:{}px;'.format(val)), label.adjustSize(), val))
#         # dia.setWrapping(True)
#         dia.setNotchTarget(2)  # 设置刻度密度
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QRubberBand-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         # rb = QRubberBand(QRubberBand.Rectangle, self)
#         # rb.setGeometry(10, 10, 60, 60)  # 设置大小
#         # print(rb.isVisible())
#         # rb.show()
#         for i in range(0, 30):
#             cb = QCheckBox(self)
#             cb.setText('{}'.format(i))
#             cb.move(i % 4 * 50, i // 4 * 60)
#         self.rb = QRubberBand(QRubberBand.Rectangle, self)
#
#     def mousePressEvent(self, evt):
#         self.origin_pos = evt.pos()
#         # self.rb = QRubberBand(QRubberBand.Rectangle, self)
#         self.rb.setGeometry(QRect(evt.pos(), QSize()))  # 设置尺寸,点坐标，尺寸
#         self.rb.show()
#
#     def mouseMoveEvent(self, evt):
#         self.rb.setGeometry(QRect(self.origin_pos, evt.pos()).normalized())  # 将可能产生的负数矩形框改为正数
#         self.rb.show()
#
#     def mouseReleaseEvent(self, evt):
#         rect = self.rb.geometry()  # 返回控件范围
#         for child in self.children():
#             if rect.contains(child.geometry()) and child.inherits('QCheckBox'):  # 前 判断child是否是在rect范围内，后 判断child是否是‘参数’对象
#                 # print(child)
#                 child.toggle()  # 切换选中状态
#         # self.rb.hide()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = QWidget()
#     window.setWindowTitle('QDialog-学习')
#     window.resize(640, 480)
#     d = QDialog(window)
#     btn1 = QPushButton(d)
#     btn1.setText('btn1')
#     btn1.move(20, 20)
#     btn1.clicked.connect(lambda: d.accept())  # 接收
#     btn2 = QPushButton(d)
#     btn2.setText('btn2')
#     btn2.move(60, 60)
#     btn2.clicked.connect(lambda: d.reject())  # 拒绝
#     # btn2.clicked.connect(lambda: print(d.result()))  # 获取数值
#     btn3 = QPushButton(d)
#     btn3.setText('btn3')
#     btn3.move(60, 120)
#     btn3.clicked.connect(lambda: d.done(8))  # 处理
#     d.accepted.connect(lambda: print('点击了接收按钮'))  # 会触发finished信号
#     d.rejected.connect(lambda: print('点击了拒绝按钮'))  # 会触发finished信号
#     d.finished.connect(lambda val: print('点击了完成按钮', val))
#     # btn3.clicked.connect(lambda: d.setResult(888))  # 设置数值
#     d.setWindowTitle('对话框')
#     # d.setModal(True)  # 将其设置为窗口级别的模态窗口
#     # d.setWindowModality(Qt.WindowModal)  # 设置为窗口级别的模态对话框
#     # d.setSizeGripEnabled(True)  # 改变整个窗口的尺寸大小
#     # d.exec()  # 应用程序级别的模态对话框
#     # d.open()  # 窗口级别的模态对话框
#     # d.show()  # 非模态的对话窗口
#     result = d.exec()
#     print(result)
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QFontDialog-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         font = QFont()
#         font.setFamily('宋体')
#         font.setPointSize(36)
#         fd = QFontDialog(font, self)  # 字体设置对话框 font为默认选中字体样式
#         fd.setCurrentFont(font)
#         # fd.setOption(QFontDialog.NoButtons, on=True)  # True是设置选项,取消按钮，应用于实时显示对应效果
#         fd.setOptions(QFontDialog.NoButtons | QFontDialog.MonospacedFonts)  # 取消按钮，应用于实时显示对应效果，等宽字体
#         self.fd = fd
#         btn = QPushButton(self)
#         btn.setText('按钮')
#         btn.move(100, 100)
#         btn.clicked.connect(self.test_cao)
#         # fd.show()
#         label = QLabel(self)
#         self.label = label
#         label.move(200, 200)
#         label.setText('社会顺哥')
#         fd.currentFontChanged.connect(self.font_cao)  # 当前字体改变信号
#
#     def font_cao(self, font):
#         self.label.setFont(font)
#         self.label.adjustSize()
#
#     def font_sel(self):
#         font = self.fd.selectedFont()  # 返回被选中的字体样式
#         print('字体已经被选择', font.family(), font.pointSize())
#
#     def test_cao(self):
#         self.fd.open(self.font_sel)  # 窗口级别模态对话框 参数为一个槽函数
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QFontDialog-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         btn = QPushButton(self)
#         btn.setText('按钮')
#         btn.move(100, 100)
#         btn.clicked.connect(self.font_sel)
#         label = QLabel(self)
#         self.label = label
#         label.move(200, 200)
#         label.setText('社会顺哥')
#
#     def font_sel(self):
#         print('font_sel')
#         font = QFont()
#         font.setFamily('宋体')
#         font.setPointSize(36)
#         result = QFontDialog.getFont(font, self, '选择一个好看的字体')  # 调用静态方法 参数为默认选中字体，父控件，窗口标题，阻塞式调用 返回值是元组
#         if result[1]:
#             self.label.setFont(result[0])
#             self.label.adjustSize()
#         print(result)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QColorDialog-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         btn = QPushButton(self)
#         self.btn = btn
#         btn.setText('按钮')
#         btn.move(100, 100)
#         btn.clicked.connect(self.font_sel)
#         label = QLabel(self)
#         self.label = label
#         label.move(200, 200)
#         label.setText('社会顺哥')
#         cd = QColorDialog(QColor(100, 200, 150), self)
#         self.cd = cd
#         cd.setWindowTitle('选择一个好看的颜色')  # 设置窗口标题
#         cd.colorSelected.connect(self.color)
#         # cd.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)  # 设置按钮 透明度分量
#         cd.currentColorChanged.connect(self.color)
#
#     def color(self, col):
#         print(col)
#         palette = QPalette()  # 调色板对象
#         palette.setColor(QPalette.Background, self.cd.currentColor())  # Background失效，但是WindowText正常
#         self.setPalette(palette)  # 设置颜色 对主控件有效但是对子控件可能无效
#         # self.label.show()
#         self.label.setStyleSheet('background-color:rgb({},{},{})'.format(col.red(), col.green(), col.blue()))
#         # print(col.getRgb(), col.red(), col.green(), col.blue())
#
#     def font_sel(self):
#         print('font_sel')
#         # self.cd.open()
#         # print(self.cd.customCount())  # 静态方法
#         # QColorDialog.setCustomColor(0, QColor(100, 200, 50))  # 静态方法，添加自定义颜色，0是指位置，上下顺序排列
#         # self.cd.show()
#         # QColorDialog.setStandardColor(0, QColor(255, 0, 0))  # 设置标准颜色，0是位置，上下顺序排列
#         # color = QColorDialog.getColor(QColor(10, 20, 100), self, '选择颜色')
#         # palette = QPalette()  # 调色板对象
#         # palette.setColor(QPalette.Background, color)  # Background失效，但是WindowText正常
#         # self.setPalette(palette)  # 设置颜色 对主控件有效但是对子控件可能无效
#         # self.label.show()
#         # self.label.setStyleSheet('background-color:rgb({},{},{})'.format(col.red(), col.green(), col.blue()))
#         # print(col.getRgb(), col.red(), col.green(), col.blue())
#         cd1 = QColorDialog(self)
#         cd1.setOption(QColorDialog.NoButtons)
#         cd1.setWindowTitle('选择喜欢的颜色')
#
#         def sel_color(color):
#             palette = QPalette()
#             palette.setColor(QPalette.ButtonText, color)
#             self.btn.setPalette(palette)
#
#         # cd1.colorSelected.connect(sel_color)
#         cd1.currentColorChanged.connect(sel_color)
#         cd1.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QFileDialog-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         btn = QPushButton(self)
#         btn.setText('按钮')
#         btn.move(100, 100)
#         btn.clicked.connect(self.test_cao)
#
#     def test_cao(self):
#         print('测试按钮')
#         # 静态方法
#         # result = QFileDialog.getOpenFileName(self, '选择一个py文件', './', 'All(*.*);;Images(*.png *.jpg);;Python(*.py)', 'Python(*.py)')  # 打开文件 参数说明 父对象 对话框窗口标题 当前路径 文件属性筛选可选项 默认文件属性  只能单选
#         # result = QFileDialog.getOpenFileNames(self, '选择一个py文件', './', 'All(*.*);;Images(*.png *.jpg);;Python(*.py)', 'Python(*.py)')  # 打开文件 参数说明 父对象 对话框窗口标题 当前路径 文件属性筛选可选项 默认文件属性  可以多选
#         # result = QFileDialog.getOpenFileUrl(self, '选择一个py文件', QUrl('./'), 'All(*.*);;Images(*.png *.jpg);;Python(*.py)', 'Python(*.py)')  # 打开文件 参数说明 父对象 对话框窗口标题 当前路径 文件属性筛选可选项 默认文件属性  只能单选
#         # result = QFileDialog.getSaveFileUrl(self, '选择一个py文件', QUrl('./'), 'All(*.*);;Images(*.png *.jpg);;Python(*.py)', 'Python(*.py)')  # 打开文件 参数说明 父对象 对话框窗口标题 当前路径 文件属性筛选可选项 默认文件属性  只能单选
#         # result = QFileDialog.getExistingDirectory(self, '选择一个py文件', './')  # 打开文件夹 参数说明 父对象 对话框窗口标题 当前路径  只能单选
#         # result = QFileDialog.getExistingDirectoryUrl(self, '选择一个py文件', QUrl('./'))  # 打开文件夹 参数说明 父对象 对话框窗口标题 当前路径  只能单选
#         fd = QFileDialog(self, '选择一个文件', './', 'All(*.*);;Images(*.png *.jpg);;Python(*.py)')
#         fd.fileSelected.connect(lambda file: print(file))  # 选中文件信号
#         # fd.setAcceptMode(QFileDialog.AcceptSave)  # 设置为保存文件对话框
#         # fd.setDefaultSuffix('txt')  # 设置默认的后缀名
#         # fd.setFileMode(QFileDialog.Directory)  # 选择文件夹模式
#         # fd.setNameFilter('IMG(*.jpg *.png *.jpeg)')  # 设置过滤器 不是追加
#         # fd.setNameFilters(['All(*.*)', 'Images(*.png *.jpg)', 'Python(*.py)'])  # 设置过滤器 不是追加
#         # fd.setViewMode(QFileDialog.List)  # 设置显示信息
#         # fd.setLabelText(QFileDialog.FileName, '顺哥文件')  # 将文件名字样替换为顺哥文件字样
#         # fd.setLabelText(QFileDialog.Accept, '顺哥文件')  # 将打开字样替换为顺哥文件字样
#         # fd.setLabelText(QFileDialog.Reject, '顺哥文件')  # 将取消字样替换为顺哥文件字样
#         # fd.currentChanged.connect(lambda path: print('当前路径字符串发生改变时', path))
#         # fd.currentUrlChanged.connect(lambda url: print('当前路径Qurl发生改变时', url))  # 路径改变信号
#         # fd.directoryEntered.connect(lambda path: print('当前路径Qurl进入时', path))  # 路径改变信号
#         # fd.directoryUrlEntered.connect(lambda url: print('当前路径Qurl进入时', url))  # 路径改变信号
#         # fd.filterSelected.connect(lambda url: print('当前名称过滤字符串被选中时', url))  # 过滤字符串改变信号
#         fd.setFileMode(QFileDialog.ExistingFiles)  # 设置多个文件选择模式
#         fd.fileSelected.connect(lambda url: print('单个文件被选中时-字符串', url))  # 文件选中信号
#         fd.filesSelected.connect(lambda url: print('多个文件被选中时-列表[字符串]', url))  # 文件选中信号
#         fd.urlSelected.connect(lambda url: print('单个文件被选中时-url', url))  # 文件选中信号
#         fd.urlsSelected.connect(lambda url: print('多个文件被选中时-列表[url]', url))  # 文件选中信号
#         result = fd.open()
#         print(result)  # 返回值为选中文件路径 或文件夹路径
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QInputDialog-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         btn = QPushButton(self)
#         btn.setText('按钮')
#         btn.move(100, 100)
#         btn.clicked.connect(self.test_cao)
#
#     def test_cao(self):
#         print('测试按钮')
#         # 静态方法
#         # result = QInputDialog.getInt(self, 'xxx1', 'xxx2', 888, 8)  # 获取整型数据 参数列表 父控件 窗口标题 调节参数的名称(提示文本) 默认值 最小值 最大值 步长
#         # result = QInputDialog.getInt(self, 'xxx1', 'xxx2', 888, 8)  # 获取浮点数据 参数列表 父控件 窗口标题 调节参数的名称(提示文本) 默认值 最小值 最大值 步长
#         # result = QInputDialog.getText(self, 'xxx1', 'xxx2',echo=QLineEdit.Password)  # 获取文本数据 参数列表 父控件 窗口标题 调节参数的名称(提示文本)
#         # result = QInputDialog.getMultiLineText(self, 'xxx1', 'xxx2','default')  # 获取多行文本数据 参数列表 父控件 窗口标题 调节参数的名称(提示文本)
#         # result = QInputDialog.getItem(self, 'xxx1', 'xxx2', ['1', '2', '3'], 0, True)  # 获取多行文本数据 参数列表 父控件 窗口标题 调节参数的名称(提示文本) 下拉列表 默认0 可编辑
#         # print(result)
#         input_d = QInputDialog(self, Qt.FramelessWindowHint)  # 设置隐藏边框
#         # input_d.setComboBoxItems(['1', '2', '3'])  # 设置下拉列表项
#         # input_d.setOption(QInputDialog.UseListViewForComboBoxItems)  # 设置下拉选项
#         # input_d.setLabelText('请输入你的姓名')  # 设置小标题
#         # input_d.setOkButtonText('好的')  # 设置确认按钮文本
#         # input_d.setCancelButtonText('我想取消')  # 设置取消按钮文本
#         # input_d.setInputMode(QInputDialog.DoubleInput)  # 设置输入模式
#         input_d.setInputMode(QInputDialog.TextInput)  # 设置输入模式
#         # input_d.setDoubleRange(9.9, 19.9)  # 设置范围
#         # input_d.setDoubleStep(2)  # 设置步长
#         # input_d.setDoubleDecimals(3)  # 设置保留的小数点后位数
#         input_d.setComboBoxItems(['abc', 'def', 'ccc'])
#         # input_d.setComboBoxEditable(True)  # 设置可以编辑
#         # input_d.intValueChanged.connect(lambda val: print('整型数据发生改变', val))
#         # input_d.intValueSelected.connect(lambda val: print('整型数据别选中', val))
#         # input_d.doubleValueChanged.connect(lambda val: print('浮点型数据发生改变', val))
#         # input_d.doubleValueSelected.connect(lambda val: print('浮点型数据别选中', val))
#         input_d.textValueChanged.connect(lambda val: print('字符串型数据发生改变', val))
#         input_d.textValueSelected.connect(lambda val: print('字符串型数据别选中', val))
#         input_d.open()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QCalendarWidget-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         btn = QPushButton(self)
#         btn.setText('按钮')
#         btn.move(100, 100)
#         btn.clicked.connect(self.test_cao)
#
#     def test_cao(self):
#         print('测试按钮')
#         cw = QCalendarWidget(self)  # 日历控件
#         # cw.setMinimumDate(QDate(1990, 1, 1))  # 设置最小日期
#         # cw.setMaximumDate(QDate(2022, 1, 1))  # 设置最大日期
#         # cw.setDateRange(QDate(1990, 1, 1), QDate(2022, 1, 1))  # 设置日期范围
#         # cw.setSelectedDate(QDate(2020, 1, 2))  # 设置默认选中日期
#         # # cw.setDateEditEnabled(False)
#         # # cw.setDateEditAcceptDelay(1000)  # 设置键盘直接编辑的延时时间 ms
#         # # cw.monthShown()  # 展示的月
#         # # cw.yearShown()  # 展示的年
#         # # cw.selectedDate()  # 选中的日期
#         # # cw.setNavigationBarVisible(False)  # 设置导航栏不可见
#         # cw.setFirstDayOfWeek(Qt.Sunday)  # 设置第一列
#         # cw.setGridVisible(True)  # 设置网格可见
#         # tcf = QTextCharFormat()
#         # tcf.setFontFamily('隶书')  # 设置字体
#         # tcf.setFontPointSize(16)  # 设置字体大小
#         # tcf.setFontUnderline(True)  # 设置下划线
#         # cw.setHeaderTextFormat(tcf)  # 设置头字符格式
#         # cw.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)  # 设置水平头字符格式
#         # cw.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)  # 设置垂直头字符格式 周数
#         # t_tcf = QTextCharFormat()
#         # t_tcf.setFontPointSize(20)
#         # t_tcf.setToolTip('这是星期二')  # 设置悬浮提示
#         # # cw.setWeekdayTextFormat(Qt.Tuesday, t_tcf)  # 设置特定字符格式
#         # cw.setDateTextFormat(QDate(2020, 1, 2), t_tcf)  # 设置特定日期格式
#         # cw.setSelectionMode(QCalendarWidget.NoSelection)  # 设置选中模式
#         # # cw.setSelectedDate()
#         # cw.move(200, 200)
#         cw.show()
#         # cw.showToday()  # 设置当天
#         # cw.showSelectedDate()  # 展示选中的一天
#         # cw.showNextYear()  # 显示下一年
#         # cw.showNextMonth()  # 展示下一月
#         # cw.setCurrentPage(2008, 8)  # 设置当前页年月
#         # cw.activated.connect(lambda date: print(date))
#         # cw.activated.connect(lambda date: print(date))
#         # cw.clicked.connect(lambda date: print(date))
#         # cw.currentPageChanged.connect(lambda y, m: print(y, m))
#         cw.selectionChanged.connect(lambda: print('选中日期', cw.selectedDate()))
#         cw.setSelectedDate(QDate(2020, 3, 28))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QLabel-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         btn = QPushButton(self)
#         btn.setText('按钮')
#         btn.move(100, 100)
#         btn.clicked.connect(self.test_cao)
#
#     def test_cao(self):
#         print('测试按钮')
#         # label = QLabel('社会我顺哥，人狠话不多', self)
#         # label = QLabel('账号(&s):', self)
#         # label = QLabel('<a href="http://www.itlike.com">撩课</a>', self)
#         label = QLabel('\n'.join('123456789'), self)
#         label.setStyleSheet('background-color:cyan;')
#         # label.adjustSize()
#         label.resize(200, 200)
#         label.move(200, 0)
#         # label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)  # 设置右对齐 垂直居中
#         # label.setIndent(30)  # 对齐一侧设置间距
#         # label.setMargin(20)  # 设置边距
#         # label.setTextFormat(Qt.PlainText)  # 设置显示普通文本解析
#         label.show()
#         le1 = QLineEdit(self)
#         le1.move(250, 250)
#         le1.show()
#         le2 = QLineEdit(self)
#         le2.move(250, 300)
#         le2.show()
#         label.setBuddy(le1)  # 设置小伙伴
#         # label.setPixmap(QPixmap('E:\\Pictures\\李梓2.jfif'))  # 显示图片
#         # label.adjustSize()
#         label.setScaledContents(True)  # 使显示的图片自动适应控件的大小
#         # label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)  # 设置鼠标和键盘可以选中文本 可编辑
#         # label.setSelection(1, 2)  # 选中文本 1指开始位置 2指选中的字符数
#         # label.setOpenExternalLinks(True)  # 设置可以打开外部超链接
#         # label.setText('<img src="E:\\Pictures\\李梓2.jfif" width=60 height=60>')
#         label.setNum(888.88)
#         label.setWordWrap(True)  # 设置软换行
#         # pic = QPicture()  # 图片对象
#         # painter = QPainter(pic)  # 画家
#         # painter.setBrush(QBrush(QColor(100, 200, 100)))  # 图刷
#         # painter.drawEllipse(0, 0, 200, 200)
#         # label.setPicture(pic)
#         # movie = QMovie('C:\\Users\\asus\\Pictures\\Camera Roll\\millie.gif')  # 视频对象 gif可行 mp4不可行
#         # print(movie)
#         # label.setMovie(movie)  # 设置视频
#         # movie.start()  # 设置视频播放
#         # movie.setSpeed(100)  # 设置播放速度 100为原速 200为2倍速
#         # label.clear()  # 设置清空
#         # label.adjustSize()
#         label.setText('<a href="http://www.itlike.com">撩课</a> 人狠话不多')
#         # label.linkHovered.connect(lambda a: print(a))  # 鼠标放上超链接的信号 返回对应的超链接
#         # label.linkActivated.connect(lambda a: print(a))  # 鼠标点击超链接信号 返回超链接
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QLCDNumber-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         btn = QPushButton(self)
#         btn.setText('按钮')
#         btn.move(50, 50)
#         btn.clicked.connect(self.test_cao)
#
#     def test_cao(self):
#         print('测试按钮')
#         lcd = QLCDNumber(5, self)  # 5代表显示的内容位数
#         lcd.show()
#         lcd.move(100, 100)
#         lcd.resize(300, 100)
#         # lcd.display('osgabcdefhlpruy')
#         # lcd.display(': \'')
#         lcd.display(99)  # 四舍五入
#         # print(lcd.value())  # 全部数据 十进制数据
#         # lcd.setDigitCount(5)  # 设置显示的位数
#         # lcd.setMode(QLCDNumber.Bin)  # 设置显示模式
#         # print(lcd.checkOverflow(99))
#         # print(lcd.checkOverflow(999999))
#         # lcd.overflow.connect(lambda: print('数值溢出'))
#         # lcd.display(888888)
#         lcd2 = QLCDNumber(self)
#         lcd2.show()
#         lcd2.move(100, 200)
#         lcd2.resize(300, 100)
#         lcd2.display(99)  # 四舍五入
#         lcd3 = QLCDNumber(self)
#         lcd3.show()
#         lcd3.move(100, 300)
#         lcd3.resize(300, 100)
#         lcd3.display(99)  # 四舍五入
#         lcd.setSegmentStyle(QLCDNumber.Outline)  # 设置分段样式
#         lcd2.setSegmentStyle(QLCDNumber.Filled)
#         lcd3.setSegmentStyle(QLCDNumber.Flat)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QProgressBar-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         btn = QPushButton(self)
#         btn.setText('按钮')
#         btn.move(50, 50)
#         btn.clicked.connect(self.test_cao)
#
#     def test_cao(self):
#         print('测试按钮')
#         pb = QProgressBar(self)
#         pb.show()
#         pb.move(100, 100)
#         pb.resize(300, 20)
#         # pb.setMinimum(0)  # 设置最小值
#         # pb.setMaximum(100)  # 设置最大值
#         pb.setRange(0, 100)  # 设置范围 最小值 最大值
#         pb.setValue(0)  # 设置当前值
#         # pb.setFormat('当前人数{} / 总人数 %m'.format(pb.value() - pb.minimum()))  # %p显示百分比 %v当前值 %m总值
#         # pb.reset()  # 清零 不改变区间范围 当前值置为最小值-1
#         # print(pb.minimum())
#         # print(pb.maximum())
#         # pb.setAlignment(Qt.AlignVCenter)  # 设置对齐方式
#         # pb.setTextVisible(False)  # 设置文本不可见
#         # print(pb.text())  # 获取显示文本
#         # pb.setOrientation(Qt.Vertical)  # 设置垂直方向
#         # pb.setTextDirection(QProgressBar.TopToBottom)
#         # pb.setInvertedAppearance(True)  # 反转
#         timer = QTimer(pb)
#
#         def change_progress():
#             # print(pb.value())
#             if pb.value() == pb.maximum():
#                 timer.stop()
#             pb.setValue(pb.value() + 1)
#             # print(pb.value())
#
#         timer.timeout.connect(change_progress)
#         timer.start(1000)  # 1s定时器
#         pb.valueChanged.connect(lambda val: print('当前的进度值', val))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QErrorMessage-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         btn = QPushButton(self)
#         btn.setText('按钮')
#         btn.move(50, 50)
#         btn.clicked.connect(self.test_cao)
#
#     def test_cao(self):
#         print('测试按钮')
#         em = QErrorMessage(self)
#         em.setWindowTitle('错误提示')  # 设置窗口标题
#         em.showMessage('社会我顺哥，人狠话不多')
#         em.open()
#         QErrorMessage.qtHandler()  # 输出级别信息
#         qDebug('XXX')  # 调试错误信息
#         qWarning('222')  # 警告信息
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QProgressDialog-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         btn = QPushButton(self)
#         btn.setText('按钮')
#         btn.move(50, 50)
#         btn.clicked.connect(self.test_cao)
#
#     def test_cao(self):
#         print('测试按钮')
#         pd = QProgressDialog(self)
#         # pd = QProgressDialog('xxx1', 'xxx2', 0, 100, self)
#         pd.setWindowTitle('xxx')
#         pd.setLabelText('下载进度')  # 设置提示文本
#         pd.setCancelButtonText('取消下载')  # 设置取消按钮
#         pd.setRange(0, 5)
#         # pd.setAutoClose(False)  # 取消自动关闭
#         # pd.setAutoReset(True)  # 设置自动重置
#         # pd.setMinimumDuration(0)  # 有多长时间显示多长时间
#         pd.show()
#
#         # pd.open(lambda: print('对话框被取消'))  # 关闭时才会执行print函数
#         # pd.setValue(50)
#         # for i in range(1, 101):
#         #     pd.setValue(i)
#         # def test():
#         #     pd.setValue(pd.value() + 1)  # 到不了最大值
#         #     print(pd.value())
#         #     if pd.value() == - 1 or pd.wasCanceled():  # 是否取值
#         #         timer.stop()
#         #     # else:
#         #     #     pd.setValue(pd.value() + 1)
#         def test():
#             # print(pd.value())
#             if pd.value() + 1 == pd.maximum():  # 是否取值
#                 timer.stop()
#                 print(pd.autoClose())
#             pd.setValue(pd.value() + 1)
#             if pd.value() == 3:
#                 pd.cancel()
#
#         timer = QTimer(pd)
#         timer.timeout.connect(test)
#         timer.start(1000)
#         pd.canceled.connect(timer.stop)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QMessageBox-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         # QMessageBox.about(self, 'xx1', 'xx2')  # 帮助对话框 窗口名称 主标题
#         result = QMessageBox.question(self, 'xx1', 'xx2', QMessageBox.Ok | QMessageBox.Discard)  # 疑问对话框 窗口名称 主标题 按钮 阻塞方法 返回按下按钮宏值
#         print(result, 'xxx')
#         return None
#         btn = QPushButton(self)
#         btn.setText('按钮')
#         btn.move(50, 50)
#         btn.clicked.connect(self.test_cao)
#
#     def test_cao(self):
#         print('测试按钮')
#         mb = QMessageBox(QMessageBox.Warning, 'xx1', '<h2>xx2</h2>', QMessageBox.Ok | QMessageBox.Discard, self)  # 窗口级别的模态对话框 参数 警告图标 窗口标题 提示文本 两个按钮
#         mb = QMessageBox(self)
#         mb.setWindowTitle('消息提示')  # 设置窗口标题
#         mb.setIconPixmap(QPixmap('E:\\Pictures\\041.jpg').scaled(100, 100))  # 设置自定义图标 设置尺寸
#         # mb.setIconPixmap(QPixmap('E:\\Pictures\\041.jpg'))  # 设置自定义图标
#         # mb.setTextFormat(Qt.PlainText)  # 设置为普通文本
#         mb.setText('<h3>文件内容已经被修改</h3>')  # 设置主标题
#         mb.setInformativeText('是否直接关闭')  # 设置副标题
#         mb.setCheckBox(QCheckBox('下次不再提醒', mb))  # 设置复选框
#         mb.setDetailedText('你修改的内容是个每一行代码加一个分号')  # 添加详细内容 不支持富文本
#         # mb.setIcon(QMessageBox.Information)  # 设置图标
#         # mb.setModal(False)  # 设置取消模态
#         # mb.setWindowModality(Qt.NonModal)  # 设置取消模态
#         mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)  # 设置标准按钮
#         # mb.addButton(QPushButton('xx1', mb), QMessageBox.YesRole)
#         # mb.addButton(QPushButton('xx2', mb), QMessageBox.NoRole)  # 添加按钮
#         # btn = mb.addButton('xx1', QMessageBox.YesRole)  # 添加按钮
#         # mb.removeButton(btn)  # 移除按钮
#         # mb.setDefaultButton(btn)  # 设置默认按钮
#         # mb.setEscapeButton(btn)  # 按ESC激活的按钮
#         # print(btn)
#         yes_btn = mb.button(QMessageBox.Yes)  # 获取标准按钮
#         # print(yes_btn)
#         no_btn = mb.button(QMessageBox.No)
#         # print(no_btn)
#         mb.setTextInteractionFlags(Qt.TextEditorInteraction)  # 设置文本交互标志 控制主标题
#
#         def test(btn1):
#             print(btn1)
#             role = mb.buttonRole(btn1)
#             if role == QMessageBox.YesRole:
#                 print('yes')
#             if role == QMessageBox.NoRole:
#                 print('no')
#             # if btn1 == yes_btn:
#             #     print('点击了yes_btn')
#             # if btn1 == no_btn:
#             #     print('点击了no_btn')
#             # if btn1 == btn:
#             #     print('xxx')
#
#         mb.buttonClicked.connect(test)
#         mb.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('布局管理-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         btn = QPushButton(self)
#         btn.setText('按钮')
#         btn.move(50, 50)
#         btn.clicked.connect(self.test_cao)
#
#     def test_cao(self):
#         print('测试按钮')
#         label1 = QLabel('标签1', self)
#         label1.show()
#         label1.setStyleSheet('background-color:cyan;')
#         label2 = QLabel('标签2', self)
#         label2.show()
#         label2.setStyleSheet('background-color:yellow;')
#         label3 = QLabel('标签3', self)
#         label3.show()
#         label3.setStyleSheet('background-color:red;')
#         # label_width = int(self.width())
#         # label_height = int(self.height() / 3)
#         # label1.resize(label_width, label_height)
#         # label2.resize(label_width, label_height)
#         # label3.resize(label_width, label_height)
#         # label1.move(0, 0)
#         # label2.move(0, label1.height())
#         # label3.move(0, label2.height() + label2.y())
#         # timer = QTimer(self)
#         # timer.timeout.connect(lambda: label1.setText(label1.text() + 'itlike\n'))
#         # timer.start(1000)
#         # 布局管理器
#         v_layout = QVBoxLayout()  # 垂直布局管理器 界面控件的定位策略
#         v_layout.addWidget(label1)  # 添加控件
#         v_layout.addWidget(label2)
#         v_layout.addWidget(label3)
#         v_layout.setContentsMargins(10, 10, 10, 10)  # 设置边距 左上右下
#         v_layout.setSpacing(10)  # 控件间的间距
#         self.setLayout(v_layout)  # 主控件添加布局管理器 自动添加父对象
#         self.setLayoutDirection(Qt.RightToLeft)  # 设置布局的方向
#         # label1.hide()
#         # print(self.children())
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('QLayout-学习')
#         self.resize(640, 480)
#         self.setup_ui()
#
#     def setup_ui(self):
#         btn = QPushButton(self)
#         btn.setText('按钮')
#         btn.move(50, 50)
#         btn.clicked.connect(self.test_cao)
#
#     def test_cao(self):
#         print('测试按钮')
#         label1 = QLabel('标签1')
#         # label1.show()
#         label1.setStyleSheet('background-color:cyan;')
#         label2 = QLabel('标签2')
#         # label2.show()
#         label2.setStyleSheet('background-color:yellow;')
#         label3 = QLabel('标签3')
#         # label3.show()
#         label3.setStyleSheet('background-color:red;')
#         label4 = QLabel('标签4')
#         # label4.show()
#         label4.setStyleSheet('background-color:orange;')
#         layout = QBoxLayout(QBoxLayout.BottomToTop)  # 设置排列顺序
#         self.setLayout(layout)
#         layout.addWidget(label1)  # 添加控件
#         layout.addWidget(label2)
#         layout.addWidget(label3)
#         layout.setSpacing(60)  # 设置控件之间的间距
#         # print(layout.contentsMargins().left(), layout.contentsMargins().top())
#         layout.setContentsMargins(11, 11, 11, 11)  # 设置文本边距
#         # print(layout.contentsMargins().left(), layout.contentsMargins().top())
#         # layout.replaceWidget(label2, label4)  # 替换控件 被换 换成
#         # label2.hide()  # 被换控件需要隐藏
#         label5 = QLabel('标签5')
#         # label5.show()
#         label5.setStyleSheet('background-color:pink;')
#         label6 = QLabel('标签6')
#         # label6.show()
#         label6.setStyleSheet('background-color:blue;')
#         label7 = QLabel('标签7')
#         # label7.show()
#         label7.setStyleSheet('background-color:cyan;')
#         h_layout = QBoxLayout(QBoxLayout.LeftToRight)
#         h_layout.addWidget(label5)
#         h_layout.addWidget(label6)
#         h_layout.addWidget(label7)
#         layout.addLayout(h_layout)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Window()
#
#     window.show()
#     sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setWindowTitle('QBoxLayout-学习')
# 		self.resize(640, 480)
# 		self.setup_ui()
#
# 	def setup_ui(self):
# 		btn = QPushButton(self)
# 		btn.setText('按钮')
# 		btn.move(50, 50)
# 		btn.clicked.connect(self.test_cao)
#
# 	def test_cao(self):
# 		print('测试按钮')
# 		label1 = QLabel('标签1')
# 		# label1.show()
# 		label1.setStyleSheet('background-color:cyan;')
# 		label2 = QLabel('标签2')
# 		# label2.show()
# 		label2.setStyleSheet('background-color:yellow;')
# 		label3 = QLabel('标签3')
# 		# label3.show()
# 		label3.setStyleSheet('background-color:red;')
# 		label4 = QLabel('标签4')
# 		# label4.show()
# 		label4.setStyleSheet('background-color:orange;')
# 		layout = QBoxLayout(QBoxLayout.LeftToRight)
# 		self.setLayout(layout)
# 		layout.addWidget(label1, 1)
# 		layout.addStretch(1)  # 添加空白伸缩 弹簧 1 为伸缩比例
# 		# layout.addSpacing(100)  # 添加100间距 索引计算不包括空白区域
# 		layout.addWidget(label2, 1)
# 		layout.addWidget(label3, 2)
# 		layout.setStretchFactor(label2, 1)
# 		# layout.addWidget(label4)
# 		# layout.insertWidget(1, label4)  # 插入控件 1 是指索引位置 插入的控件
# 		# label5 = QLabel('标签5')
# 		# # label5.show()
# 		# label5.setStyleSheet('background-color:pink;')
# 		# label6 = QLabel('标签6')
# 		# # label6.show()
# 		# label6.setStyleSheet('background-color:blue;')
# 		# label7 = QLabel('标签7')
# 		# # label7.show()
# 		# label7.setStyleSheet('background-color:cyan;')
# 		# h_layout = QBoxLayout(QBoxLayout.TopToBottom)
# 		# h_layout.addWidget(label5)
# 		# h_layout.addWidget(label6)
# 		# h_layout.addWidget(label7)
# 		# layout.insertLayout(2, h_layout)  # 插入布局 2 是索引位置 插入的布局
# 		# layout.removeWidget(label1)
# 		# label1.hide()
# 		# timer = QTimer(self)
# 		#
# 		# def test():
# 		# 	print('time')
# 		# 	layout.setDirection((layout.direction() + 1) % 4)
# 		#
# 		# timer.timeout.connect(test)
# 		# timer.start(1000)
#
#
# if __name__ == '__main__':
# 	app = QApplication(sys.argv)
# 	window = Window()
#
# 	window.show()
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget) :
# 	def __init__(self) :
# 		super().__init__()
# 		self.setWindowTitle('QFormLayout-学习')
# 		self.resize(640, 480)
# 		self.setup_ui()
#
# 	def setup_ui(self) :
# 		btn = QPushButton(self)
# 		btn.setText('按钮')
# 		btn.move(400, 400)
# 		btn.clicked.connect(self.test_cao)
#
# 	def test_cao(self) :
# 		print('测试按钮')
# 		name_label = QLabel('姓名：')
# 		age_label = QLabel('年龄：')
# 		submit_btn = QPushButton('提交')
# 		name_le = QLineEdit()
# 		age_sb = QSpinBox()
# 		sex_label = QLabel('性别')
# 		male_rb = QRadioButton('男')
# 		female_rb = QRadioButton('女')
# 		h_layout = QHBoxLayout()
# 		h_layout.addWidget(male_rb)
# 		h_layout.addWidget(female_rb)
# 		layout = QFormLayout()
# 		self.setLayout(layout)
# 		# layout.addRow(name_label, name_le)
# 		layout.addRow('姓名', name_le)
# 		layout.labelForField(name_le).setText('姓名：')
# 		# layout.setRowWrapPolicy(QFormLayout.WrapAllRows)  # 设置换行策略
# 		print(layout.formAlignment() == Qt.AlignLeft | Qt.AlignTop)
# 		print(layout.setFormAlignment(Qt.AlignLeft | Qt.AlignVCenter))  # 设置表单对齐方式
# 		layout.setLabelAlignment(Qt.AlignRight)  # 设置标签对齐方式
# 		layout.setHorizontalSpacing(20)  # 设置水平方向的间距
# 		layout.setVerticalSpacing(30)  # 设置垂直方向的间距
# 		layout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)  # 设置字段增长策略
# 		# layout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy)  # 设置字段增长策略
# 		layout.addRow(sex_label, h_layout)
# 		# layout.addWidget(name_label)
# 		# layout.addWidget(name_le)
# 		layout.addRow(age_label, age_sb)
# 		layout.addRow(submit_btn)
# 		# layout.insertRow(1, '性别:', h_layout)  # 插入行 1 为位置索引值
# 		# print(layout.rowCount())
# 		# print(layout.getWidgetPosition(age_sb))
# 		# print(layout.getLayoutPosition(h_layout))
# 		age_sb.destroyed.connect(lambda : print('年龄步长被释放'))
# 		age_label.destroyed.connect(lambda : print('年龄标签被释放'))
# 		# layout.removeRow(2)  # 移除行 2 为位置索引值
# 		# layout.takeRow(2)  # 设置移除不删除
# 		# print(dir(QFormLayout.TakeRowResult))
# 		pass
#
# 	def test(self) :
# 		pass
#
#
# if __name__ == '__main__' :
# 	app = QApplication(sys.argv)
# 	window = Window()
#
# 	window.show()
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget) :
# 	def __init__(self) :
# 		super().__init__()
# 		self.setWindowTitle('QGridLayout-学习')
# 		self.resize(640, 480)
# 		self.setup_ui()
#
# 	def setup_ui(self) :
# 		btn = QPushButton(self)
# 		btn.setText('按钮')
# 		btn.move(400, 400)
# 		btn.clicked.connect(self.test_cao)
#
# 	def test_cao(self) :
# 		print('测试按钮')
# 		gl = QGridLayout()  # 创建网格布局
# 		# self.gl = gl
# 		self.setLayout(gl)
# 		label1 = QLabel('标签1')
# 		label1.setStyleSheet('background-color:cyan;')
# 		label2 = QLabel('标签2')
# 		label2.setStyleSheet('background-color:yellow;')
# 		label3 = QLabel('标签3')
# 		label3.setStyleSheet('background-color:red;')
# 		label5 = QLabel('标签5')
# 		label5.setStyleSheet('background-color:pink;')
# 		label6 = QLabel('标签6')
# 		label6.setStyleSheet('background-color:blue;')
# 		label7 = QLabel('标签7')
# 		label7.setStyleSheet('background-color:cyan;')
# 		v_layout = QVBoxLayout()
# 		# v_layout.setDirection(QVBoxLayout.RightToLeft)
# 		v_layout.addWidget(label5)
# 		v_layout.addWidget(label6)
# 		v_layout.addWidget(label7)
# 		gl.addWidget(label1, 0, 0)  # 0行0列
# 		gl.addWidget(label2, 0, 1)  # 0行1列
# 		gl.addWidget(label3, 1, 0, 1, 2)  # 1，0起始，跨过1行 跨过2列
# 		gl.addLayout(v_layout, 2, 0, 1, 2)
# 		print(gl.getItemPosition(1))  # 1为索引值返回值 0行1列 占据1行 占据1列
# 		print(gl.itemAtPosition(0, 1).widget().text())  # 返回值为控件对象
# 		# gl.setColumnMinimumWidth(0, 100)  # 设置列的最小宽度 0值第0列
# 		# gl.setRowMinimumHeight(0, 100)  # 设置行的最小高度 0指第0行
# 		# gl.setColumnStretch(0, 1)  # 设置列的拉伸系数 第0列 拉伸系数设为1
# 		# gl.setColumnStretch(1, 1)
# 		# gl.setRowStretch(2, 1)  # 设置行的拉伸系数 第2行 拉伸系数设为1
# 		print(gl.spacing())  # 间距
# 		print(gl.horizontalSpacing())  # 水平间距
# 		print(gl.verticalSpacing())  # 垂直间距
# 		# gl.setOriginCorner(Qt.BottomLeftCorner)  # 设置原点角
# 		print(gl.rowCount())  # 行数
# 		print(gl.columnCount())  # 列数
# 		# print(gl.cellRect(0, 0))
# 		pass
#
#
# if __name__ == '__main__' :
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	# gl = window.layout()
# 	# print(gl.cellRect(0, 0))
# 	# print(window.layout())
# 	window.show()
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget) :
# 	def __init__(self) :
# 		super().__init__()
# 		self.setWindowTitle('QStackedLayout-学习')
# 		self.resize(640, 480)
# 		self.setup_ui()
# 		pass
#
# 	def setup_ui(self) :
# 		self.test_cao()
# 		# btn = QPushButton(self)
# 		# btn.setText('按钮')
# 		# btn.move(400, 400)
# 		# btn.clicked.connect(self.test_cao)
# 		pass
#
# 	def test_cao(self) :
# 		print('test')
# 		sl = QStackedLayout()
# 		self.setLayout(sl)  # 在添加子控件之前
# 		label1 = QLabel('标签1')
# 		label1.setStyleSheet('background-color:cyan;')
# 		label2 = QLabel('标签2')
# 		label2.setStyleSheet('background-color:yellow;')
# 		label3 = QLabel('标签3')
# 		label3.setStyleSheet('background-color:red;')
# 		label4 = QLabel('标签4')
# 		label4.setStyleSheet('background-color:green;')
# 		label5 = QLabel('标签5')
# 		label5.setStyleSheet('background-color:pink;')
# 		label6 = QLabel('标签6')
# 		label6.setStyleSheet('background-color:blue;')
# 		label7 = QLabel('标签7')
# 		label7.setStyleSheet('background-color:cyan;')
# 		v_layout = QVBoxLayout()
# 		v_layout.addWidget(label5)
# 		v_layout.addWidget(label6)
# 		v_layout.addWidget(label7)
# 		sl.addWidget(label1)
# 		sl.addWidget(label2)
# 		sl.addWidget(label3)
# 		sl.setStackingMode(QStackedLayout.StackAll)  # 设置堆叠模式
# 		label1.setFixedSize(100, 100)  # 设置固定显示尺寸
# 		label2.setFixedSize(200, 200)
# 		# print(sl.currentIndex())
# 		# sl.insertWidget(0, label4)
# 		# print(sl.currentIndex())
# 		# print(sl.widget(0).text())
# 		# sl.setCurrentIndex(0)  # 设置当前索引值
# 		# timer = QTimer(self)
# 		# timer.timeout.connect(lambda : sl.setCurrentIndex((sl.currentIndex() + 1) % sl.count()))
# 		# timer.start(1000)
# 		# sl.setCurrentWidget(label4)
# 		# sl.currentChanged.connect(lambda val : print(val))  # 传递索引值
# 		pass
#
#
# if __name__ == '__main__' :
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	window.show()
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Label(QLabel) :
# 	def minimumSizeHint(self) :  # 设置控件的最小尺寸
# 		return QSize(200, 200)
# 		pass
#
#
# class Window(QWidget) :
# 	def __init__(self) :
# 		super().__init__()
# 		self.setWindowTitle('QStackedLayout-学习')
# 		self.resize(640, 480)
# 		self.setup_ui()
# 		pass
#
# 	def setup_ui(self) :
# 		self.test_cao()
# 		# btn = QPushButton(self)
# 		# btn.setText('按钮')
# 		# btn.move(400, 400)
# 		# btn.clicked.connect(self.test_cao)
# 		pass
#
# 	def test_cao(self) :
# 		print('test')
# 		label1 = QLabel('标签1')
# 		label1.setStyleSheet('background-color:cyan;')
# 		label2 = QLabel('标签2')
# 		label2.setStyleSheet('background-color:yellow;')
# 		label3 = QLabel('标签3')
# 		label3.setStyleSheet('background-color:red;')
# 		label4 = QLabel('标签4')
# 		label4.setStyleSheet('background-color:green;')
# 		label5 = QLabel('标签5')
# 		label5.setStyleSheet('background-color:pink;')
# 		label6 = QLabel('标签6')
# 		label6.setStyleSheet('background-color:blue;')
# 		label7 = QLabel('标签7')
# 		label7.setStyleSheet('background-color:cyan;')
# 		layout = QVBoxLayout()
# 		self.setLayout(layout)
# 		layout.addWidget(label1)
# 		layout.addWidget(label2)
# 		layout.addWidget(label3)
# 		# label1.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)  # 设置尺寸策略 水平策略 垂直策略
# 		sp = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
# 		sp.setRetainSizeWhenHidden(True)  # 当控件隐藏时保留位置
# 		label1.setSizePolicy(sp)  # 设置尺寸策略 水平策略 垂直策略
# 		label1.setFixedSize(200, 200)  # 设置固定的尺寸，可以覆盖尺寸策略
# 		# label1.hide()
# 		# label2.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)  # 尽可能获取控件
# 		pass
#
#
# if __name__ == '__main__' :
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	window.show()
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# from Tool import QSSTool
#
#
# class Window(QWidget) :
# 	def __init__(self) :
# 		super().__init__()
# 		self.setWindowTitle('QSS-学习')
# 		self.resize(640, 480)
# 		self.setup_ui()
# 		pass
#
# 	def setup_ui(self) :
# 		self.test_cao()
# 		# btn = QPushButton(self)
# 		# btn.setText('按钮')
# 		# btn.move(400, 400)
# 		# btn.clicked.connect(self.test_cao)
# 		pass
#
# 	def test_cao(self) :
# 		print('test')
# 		box1 = QWidget(self)
# 		box2 = QWidget(self)
# 		box2.setObjectName('box2')
# 		box3 = QWidget(box2)
# 		box3.resize(150, 150)
# 		# box3.setStyleSheet('background-color:lightgray;')
# 		# box1.setStyleSheet('QPushButton { background-color:orange; }')
# 		# box2.setStyleSheet('background-color:yellow;')
# 		label1 = QLabel('标签1', box1)
# 		label1.setObjectName('l1')  # 设置控件名称
# 		label1.setProperty('notice_level', 'warning')  # 设置属性值
# 		label1.resize(200, 60)
# 		label1.move(50, 50)
# 		btn1 = QPushButton('按钮1', box1)
# 		btn1.setObjectName('btn1')
# 		btn1.move(150, 50)
# 		cb = QCheckBox('python', box1)
# 		cb.setTristate(True)  # 设置三态
# 		cb.move(0, 0)
# 		cb.resize(200, 50)
# 		label2 = QLabel('标签2', box3)
# 		label2.setProperty('notice_level', 'error')  # 设置notice_level属性为error
# 		# label2.notice_level = 'error'
# 		label2.resize(100, 60)
# 		label2.move(50, 50)
# 		label3 = QLabel('标签3', box2)
# 		label3.move(200, 200)
# 		# label3.setStyleSheet('background-color:yellow;')
# 		btn2 = QPushButton('按钮2', box2)
# 		btn2.setObjectName('btn2')
# 		btn2.move(150, 50)
# 		v_layout = QVBoxLayout()
# 		self.setLayout(v_layout)
# 		v_layout.addWidget(box1)
# 		v_layout.addWidget(box2)
# 		# self.other_btn = QPushButton('按钮3')
# 		# self.other_btn.show()
# 		# self.setStyleSheet('QPushButton { background-color:orange; }')
# 		pass
#
#
# if __name__ == '__main__' :
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	window.show()
# 	QSSTool.setQssToObj('test.qss', app)
# 	# app.setStyleSheet('QPushButton { background-color:orange; }')
# 	# with open('test.qss', 'r') as f :
# 	# 	content = f.read()
# 	# 	app.setStyleSheet(content)
# 	# app.setStyleSheet('QLabel#l1 { background-color:orange; } QPushButton#b2 { background-color:cyan; }')  # 针对所有对象 #号后是对象名称
# 	# window.other_btn.setStyleSheet('background-color:orange;')
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# from Tool import QSSTool
#
#
# class Window(QWidget) :
# 	def __init__(self) :
# 		super().__init__()
# 		self.setWindowTitle('QSS-学习')
# 		self.resize(640, 480)
# 		self.setup_ui()
# 		pass
#
# 	def setup_ui(self) :
# 		self.test_cao()
# 		pass
#
# 	def test_cao(self) :
# 		print('test')
# 		label = QLabel('标签测试', self)
# 		label.resize(300, 300)
# 		label.move(100, 100)
# 		self.label_border(label)
# 		pass
#
# 	def label_border(self, label) :
# 		label.setStyleSheet("""       /* 三个双引号对定义多行字符串 */
# 			QLabel {
# 				background-color: qconicalgradient(cx:0.5, cy:0.5, angle:30, stop:0 red, stop:0.5 green, stop:1 orange); /* 设置背景颜色 角度渐变色 起点 角度 中断点*/
# 				/*background-color: qradialgradient(cx:0.7, cy:0.7, radius:0.5, fx:0.5, fy:0.5, stop:0 red, stop:0.5 green, stop:1 orange); /* 设置背景颜色 俯视渐变色 中心点 半径 交点 中断点*/
# 				/*background-color: qlineargradient(x1:0,y1:0, x2:1,y2:1, stop:0 red, stop:0.4 gray, stop:1 green);  /* 设置背景颜色 线性渐变色 */
# 				border-width: 26px;  /* 设置边框宽度 单个参数同时设置四条线，两个参数代表上下，左右，四个参数代表上右下左*/
# 				border-style: dotted dashed solid double;    /* 设置边框样式 单个参数同时设置四条线 四个参数为上右下左 点虚线 长虚线 实线 双线 */
# 				border-top-style: groove;   /* 单独设置上边框 3D效果 类似实线 */
# 				border-color: red;  /* 设置边框颜色 单个参数同时设置四条线，两个参数代表上下，左右，三个参数代表上右下，四个参数代表上右下左*/
# 				border-left-color: rgb(255, 0, 255);
# 				border-right-color: #00ff00;
# 			}
# 		""")
# 		pass
#
#
# if __name__ == '__main__' :
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	window.show()
# 	# QSSTool.setQssToObj('test.qss', app)
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# # from Tool import QSSTool
#
#
# class Window(QWidget) :
# 	def __init__(self) :
# 		super().__init__()
# 		self.setWindowTitle('QSS-学习')
# 		self.resize(640, 480)
# 		self.setup_ui()
# 		pass
#
# 	def setup_ui(self) :
# 		self.test_cao()
# 		pass
#
# 	def test_cao(self) :
# 		print('test')
# 		label = QLabel('标签测试', self)
# 		label.resize(300, 300)
# 		label.move(0, 0)
# 		self.label_border(label)
# 		pass
#
# 	def label_border(self, label) :
# 		label.setStyleSheet("""       /* 三个双引号对定义多行字符串 */
# 			QLabel {
# 				/*background-color: qconicalgradient(cx:0.5, cy:0.7, angle:30, stop:0 red, stop:0.5 green, stop:1 orange); /* 设置背景颜色 角度渐变色 起点 角度 中断点*/
# 				background-color: red; /* 设置背景颜色 角度渐变色 起点 角度 中断点*/
# 				/*background-image: url(E:/Pictures/015.jpg); /* 设置背景图片  */
# 				image: url(E:/Pictures/015.jpg); /* 设置背景图片  */
# 				background-repeat:no-repeat; /*  设置重复  */
# 				background-position: right bottom;  /* 设置背景图片位置 对齐方式*/
# 				background-origin: border; /* 设置原始参照点为border  */
# 				background-clip: border; /*   设置裁剪方式  */
# 				/*color: orange; /* 设置边距颜色*/
# 				/*border:10px solid red;
# 				/*padding:20px; /*设置内边距*/
# 				/*padding-top:150px; /*设置上部内边距*/
# 				/*border-image: url(E:/Pictures/015.jpg) 30px 30px 30px 30+px repeat;    /* 设置边框图片 url为图片源 四个像素为切割图片 stretch为拉伸 round为平铺 repeat为重复 */
# 				/*border-width: 30px;     /* 确定边框宽度 */
# 				/*margin: 20px 40px 80px 160px; /*  设置外边距  */
# 				/*margin-left: 20px; /*  设置左外边距  */
# 			}
# 		""")
# 		pass
#
#
# if __name__ == '__main__' :
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	window.show()
# 	# QSSTool.setQssToObj('test.qss', app)
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget) :
# 	def __init__(self) :
# 		super().__init__()
# 		self.setWindowTitle('QSS-学习')
# 		# self.resize(640, 480)
# 		self.resize(1200, 936)
# 		self.setup_ui()
# 		pass
#
# 	def setup_ui(self) :
# 		self.test_cao()
# 		pass
#
# 	def test_cao(self) :
# 		print('test')
# 		self.setStyleSheet("""
# 			QPushButton {
# 				background-image: url(C:/Users/asus/Downloads/Image/puke1.jpg); /* 设置图片 */
# 				background-origin: content; /* 设置参考原点为内容区域 */
# 				background-clip: padding;   /* 设置裁剪边框为内边框 */
# 			}
# 		""")
# 		v_layout =QVBoxLayout(self)
# 		h_layout1 = QHBoxLayout()
# 		for i in range(0, 4) :
# 			btn = QPushButton()
# 			btn.setFixedSize(300, 468)
# 			btn.setStyleSheet("""
# 				QPushButton {
# 					padding-left: -%d px; /*  负值代表图片向右移动 正值代表图片向左移动  */
# 					padding-top: -%d px; /* 负值代表图片向下移动 正值代表图片向上移动  */
# 				}
# 			""" % (i * 300, 0))  # 字符串的拼接方式 format函数使用花括号拼接，%d使用%号拼接
# 			h_layout1.addWidget(btn)
# 		h_layout2 = QHBoxLayout()
# 		for i in range(0, 4) :
# 			btn = QPushButton()
# 			btn.setFixedSize(300, 468)
# 			btn.setStyleSheet("""
# 				QPushButton {
# 					padding-left: -%d px; /*  负值代表图片向右移动 正值代表图片向左移动  */
# 					padding-top: -%d px; /* 负值代表图片向下移动 正值代表图片向上移动  */
# 				}
# 			""" % (i * 300, 468))  # 字符串的拼接方式 format函数使用花括号拼接，%d使用%号拼接
# 			h_layout2.addWidget(btn)
# 		v_layout.addLayout(h_layout1)
# 		v_layout.addLayout(h_layout2)
# 		# self.label_border(label)
# 		pass
#
# 	def label_border(self, label) :
# 		label.setStyleSheet("""       /* 三个双引号对定义多行字符串 */
# 			QLabel {
#
# 			}
# 		""")
# 		pass
#
#
# if __name__ == '__main__' :
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	window.show()
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget) :
# 	def __init__(self) :
# 		super().__init__()
# 		self.setWindowTitle('QSS-学习')
# 		self.resize(640, 480)
# 		# self.resize(1200, 936)
# 		self.setup_ui()
# 		pass
#
# 	def setup_ui(self) :
# 		self.test_cao()
# 		pass
#
# 	def test_cao(self) :
# 		print('test')
# 		label = QCheckBox(self)
# 		# layout = QVBoxLayout(self)
# 		# layout.addWidget(label)
# 		label.resize(300, 300)
# 		label.move(0, 0)
# 		self.label_border(label)
# 		pass
#
# 	def label_border(self, label) :
# 		label.setStyleSheet("""       /* 三个双引号对定义多行字符串 */
# 			QCheckBox {
# 				color: gray;
# 				border: 10px double rgb(76,76,76);
# 				padding: 5px;
# 			}
# 			QCheckBox::indicator {
# 				subcontrol-origin: border;
# 				subcontrol-position: left center;
# 				background: white;
# 				border: 2px solid gray;
# 			}
# 			QCheckBox::indicator:checked {
# 				background-color: rgb(76,76,76);
# 			}
# 		""")
# 		# label.setStyleSheet("""       /* 三个双引号对定义多行字符串 */
# 		# 	QSpinBox {
# 		# 		font-size: 26px;
# 		# 		color: orange;
# 		# 		border: 10px double red;
# 		# 		border-radius: 10px; /* 边框圆角 */
# 		# 		/*background-color: gray;*/
# 		# 	}
# 		# 	QSpinBox::up-button, QSpinBox::down-button {
# 		# 		width: 50px;
# 		# 		height: 50px;
# 		# 	}
# 		# 	QSpinBox::up-button {
# 		# 		subcontrol-origin: padding;
# 		# 		subcontrol-position: left center; /* 设置对齐方式 水平对齐方式 垂直对齐方式 */
# 		# 		image: url(E:/Pictures/041.jpg);
# 		# 	}
# 		# 	QSpinBox::up-button:hover {
# 		# 		bottom: 10px;
# 		# 	}
# 		# 	QSpinBox::down-button {
# 		# 		subcontrol-origin: padding;
# 		# 		subcontrol-position: right center;
# 		# 		image: url(E:/Pictures/015.jpg);
# 		# 	}
# 		# 	QSpinBox::down-button:hover {
# 		# 		position: absolute; /*  */
# 		# 		top: 10px;
# 		# 	}
# 		# """)
# 		# label.setStyleSheet("""       /* 三个双引号对定义多行字符串 */
# 		# 	QSpinBox {
# 		# 		font-size: 26px;
# 		# 		color: orange;
# 		# 		border: 10px double red;
# 		# 		border-radius: 10px; /* 边框圆角 */
# 		# 		background-color: gray;
# 		# 		/*font-family: 隶书;    /* 设置字体家族 */
# 		# 		/*font-size: 30px;     /*  设置字体大小 */
# 		# 		/*font-style: italic;  /*  设置字体样式 italic 斜体 */
# 		# 		/*font-weight: bold;    /*    设置字体粗细 也可写数值*/
# 		# 		/*color: orange;      /*  设置字体颜色 */
# 		# 		/*min-width: 200px;   /* 设置最小宽度 */
# 		# 		/*min-height: 200px;   /* 设置最小高度 */
# 		# 		/*max-width: 600px;   /* 设置最大宽度 */
# 		# 		/*max-height: 600px;   /* 设置最大高度 */
# 		# 		/*background-color: red; */
# 		# 	}
# 		# """)
# 		# label.setStyleSheet("""       /* 三个双引号对定义多行字符串 */
# 		# 	QTextEdit {
# 		# 		background-color: red; /* 设置背景颜色 角度渐变色 起点 角度 中断点*/
# 		# 		background-image: url(E:/Pictures/015.jpg); /* 设置背景图片  */
# 		# 		background-repeat:no-repeat; /*  设置重复  */
# 		# 		background-position: left top;  /* 设置背景图片位置 对齐方式*/
# 		# 		background-origin: border; /* 设置原始参照点为border  */
# 		# 		background-clip: content; /*   设置裁剪方式  */
# 		# 		background-attachment: fixed; /*  禁止背景跟随滚动  */
# 		# 	}
# 		# """)
# 		pass
#
#
# if __name__ == '__main__' :
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	window.show()
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setWindowTitle('级联与冲突-学习')
# 		self.resize(640, 480)
# 		# self.resize(1200, 936)
# 		self.setup_ui()
# 		pass
#
# 	def setup_ui(self):
# 		self.test_cao()
# 		pass
#
# 	def test_cao(self):
# 		print('test')
# 		btn1 = QPushButton('b1', self)
# 		btn2 = QPushButton('b2', self)
# 		btn1.setObjectName('b1')
# 		btn2.setObjectName('b2')
# 		btn1.move(100, 100)
# 		btn2.move(200, 200)
# 		self.setStyleSheet("""
# 			QPushButton {
# 				color: red;
# 			}
# 			QAbstractButton {
# 				color: blue;
# 			}
# 		""")
# 		# self.setStyleSheet("""
# 		# 	QPushButton:enabled:hover {
# 		# 		color: blue;
# 		# 	}
# 		# 	QPushButton:hover {
# 		# 		color: red;
# 		# 	}
# 		# """)
# 		pass
#
# 	def label_border(self, label):
# 		pass
#
#
# if __name__ == '__main__':
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	window.show()
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# import qdarkgraystyle

# class Window(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setWindowTitle('样式表-学习')
# 		self.resize(640, 480)
# 		self.setup_ui()
# 		pass

# 	def setup_ui(self):
# 		layout = QVBoxLayout(self)
# 		label = QLabel('xxx')
# 		layout.addWidget(label)
# 		btn = QPushButton('xx2')
# 		layout.addWidget(btn)
# 		cb = QComboBox()
# 		cb.addItems([ '1', '2', '3' ])
# 		layout.addWidget(cb)
# 		sb = QSpinBox()
# 		layout.addWidget(sb)
# 		self.test_cao()
# 		pass

# 	def test_cao(self):
# 		print('test')

# if __name__ == '__main__':
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	window.show()
# 	style_sheet = qdarkgraystyle.load_stylesheet_pyqt5()
# 	print(style_sheet)
# 	app.setStyleSheet(style_sheet)
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# import qdarkgraystyle
# from Tool import QSSTool
# 
# 
# class Window(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setWindowTitle('案例-学习')
# 		self.resize(640, 480)
# 		self.setup_ui()
# 		pass
# 
# 	def setup_ui(self):
# 		w = QSlider(Qt.Horizontal, self)
# 		w.resize(200, 200)
# 		w.move(100, 100)
# 		pass
# 
# 	def test_cao(self):
# 		print('test')
# 
# 
# if __name__ == '__main__':
# 	app = QApplication(sys.argv)
# 	QSSTool.setQssToObj('demo.qss', app)
# 	window = Window()
# 	window.show()
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Btn(QPushButton):
# 	# rightClicked = pyqtSignal(str)  # 自定义信号，必须定义为类属性 向外发射的数据类型
# 	rightClicked = pyqtSignal([ str ], [ int, str ])  # 自定义信号，必须定义为类属性 向外发射的数据类型 只发送一个数据但是数据格式有可能是str也有可能是int
#
# 	def mousePressEvent(self, evt):
# 		super().mousePressEvent(evt)
# 		if evt.button() == Qt.RightButton:
# 			# print('右击信号')
# 			self.rightClicked[ str ].emit(self.text())  # 发射信号
# 			self.rightClicked[ int, str ].emit(888, 'itlike')  # 发射信号
# 		pass
#
#
# class Window(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setWindowTitle('信号-学习')
# 		self.resize(640, 480)
# 		self.setup_ui()
# 		pass
#
# 	def setup_ui(self):
# 		btn = Btn('xx', self)
# 		# btn.clicked.connect(lambda: print('按钮被点击了'))
# 		btn.rightClicked[ int, str ].connect(lambda content, p_str: print('按钮右键被点击了', content, p_str))
# 		btn.pressed.connect(lambda: print('按钮被按下'))
# 		pass
#
#
# if __name__ == '__main__':
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	window.show()
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setWindowTitle('动画-学习')
# 		self.resize(640, 480)
# 		self.setup_ui()
# 		pass
#
# 	def setup_ui(self):
# 		btn = QPushButton('测试按钮', self)
# 		btn.resize(100, 100)
# 		btn.move(100, 100)
# 		btn.setStyleSheet('background-color:cyan;')
# 		animation = QPropertyAnimation(self)  # 创建动画对象 设置父控件
# 		animation.setTargetObject(btn)  # 设置目标对象
# 		animation.setPropertyName(b'pos')  # 设置属性windowOpacity,不透明度
# 		# animation.setStartValue(1)  # 设置开始不透明度
# 		# animation.setKeyValueAt(0.5, 0.5)
# 		# animation.setKeyValueAt(1, 1)
# 		# animation.setEndValue(1)  # 设置结束不透明度
# 		# animation.setTargetObject(btn)  # 设置目标对象
# 		# animation.setPropertyName(b'geometry')  # 设置属性geometry
# 		# animation.setStartValue(QRect(0, 0, 100, 100))  # 设置动画的起始位置
# 		# animation.setEndValue(QRect(200, 200, 300, 300))  # 设置动画的结束位置
# 		# animation.setPropertyName(b'size')  # 设置属性size
# 		# animation.setStartValue(QSize(0, 0))  # 设置动画的起始位置
# 		# animation.setEndValue(QSize(300, 300))  # 设置动画的结束位置
# 		# animation.setDuration(3000)  # 设置动画的持续市场
# 		# animation.setEasingCurve(QEasingCurve.InQuad)
# 		# animation.start()
# 		# animation.setPropertyName(b'pos')  # 设置属性pos
# 		# animation = QPropertyAnimation(btn, b'pos', self)  # 创建动画对象 设置父控件
# 		animation.setStartValue(QPoint(0, 0))  # 设置动画的起始位置
# 		animation.setEndValue(QPoint(300, 300))  # 设置动画的结束位置
# 		animation.setDuration(3000)  # 设置动画的持续市场
# 		# animation.setEasingCurve(QEasingCurve.OutQuad)
# 		animation.setLoopCount(3)  # 设置循环的次数
# 		animation.setEasingCurve(QEasingCurve.OutBounce)  # 设置动画的运动过程
# 		animation.setDirection(QAbstractAnimation.Backward)  # 设置动画额运动方向
# 		animation.start()
#
# 		# print(animation.totalDuration(), animation.duration())
# 		# btn.clicked.connect(lambda: print(animation.loopCount(), animation.currentLoop()))  # 循环次数 当前循环次数
# 		# btn.clicked.connect(lambda: print(animation.currentTime(), animation.currentLoopTime()))  # 循环时间
# 		# self.flag = True
# 		#
# 		# def animation_operation():
# 		# 	if self.flag:
# 		# 		animation.pause()  # 设置动画暂停
# 		# 		self.flag = False
# 		# 	else:
# 		# 		animation.resume()  # 设置动画继续运行
# 		# 		self.flag = True
# 		# 	pass
#
# 		def animation_operation():
# 			if animation.state() == QAbstractAnimation.Running:
# 				animation.pause()  # 设置动画暂停
# 			elif animation.state() == QAbstractAnimation.Paused:
# 				animation.resume()  # 设置动画继续运行
# 			pass
#
# 		btn.clicked.connect(animation_operation)
# 		animation.currentLoopChanged.connect(lambda val: print('当前循环次数发生改变', val))
# 		animation.finished.connect(lambda: print('动画执行完毕'))
# 		animation.stateChanged.connect(lambda ns, os: print('状态改变', ns, os))
# 		pass
#
#
# if __name__ == '__main__':
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	window.show()
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
#
#
# class Window(QWidget):
# 	def __init__(self):
# 		super().__init__()
# 		self.setWindowTitle('动画组-学习')
# 		self.resize(640, 480)
# 		self.setup_ui()
# 		pass
#
# 	def setup_ui(self):
# 		red_btn = QPushButton('红色按钮', self)
# 		green_btn = QPushButton('绿色按钮', self)
# 		red_btn.resize(100, 100)
# 		green_btn.resize(100, 100)
# 		green_btn.move(150, 150)
# 		red_btn.setStyleSheet("""
# 			background-color:red;
# 		""")
# 		green_btn.setStyleSheet("""
# 			background-color:green;
# 		""")
# 		animation = QPropertyAnimation(green_btn, b'pos', self)
# 		animation.setKeyValueAt(0, QPoint(150, 150))
# 		animation.setKeyValueAt(0.25, QPoint(320, 150))  # 前一个参数指的是时间点，总时间的0.25处
# 		animation.setKeyValueAt(0.5, QPoint(320, 240))
# 		animation.setKeyValueAt(0.75, QPoint(150, 240))
# 		animation.setKeyValueAt(1, QPoint(150, 150))
# 		animation.setDuration(5000)
# 		# animation.setLoopCount(3)
# 		# animation.start()
# 		animation2 = QPropertyAnimation(red_btn, b'pos', self)
# 		animation2.setKeyValueAt(0, QPoint(0, 0))
# 		animation2.setKeyValueAt(0.25, QPoint(0, 380))  # 前一个参数指的是时间点，总时间的0.25处
# 		animation2.setKeyValueAt(0.5, QPoint(540, 380))
# 		animation2.setKeyValueAt(0.75, QPoint(540, 0))
# 		animation2.setKeyValueAt(1, QPoint(0, 0))
# 		animation2.setDuration(5000)
# 		# animation2.setLoopCount(3)
# 		# animation2.start()
# 		# animation_group1 = QParallelAnimationGroup(self)  # 设置并行动画组
# 		animation_group1 = QSequentialAnimationGroup(self)  # 设置串行动画组
# 		animation_group1.addAnimation(animation)
# 		# animation_group1.addPause(5000)  # 设置暂停时间 只有串行动画才有
# 		pause_animation = QPauseAnimation()
# 		pause_animation.setPaused(5000)
# 		animation_group1.addAnimation(pause_animation)
# 		animation_group1.addAnimation(animation2)
# 		animation_group1.start()
# 		red_btn.clicked.connect(animation_group1.pause)
# 		green_btn.clicked.connect(animation_group1.resume)
# 		pass
#
#
# if __name__ == '__main__':
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	window.show()
# 	sys.exit(app.exec_())
# import sys
# from PyQt5.Qt import *
# from Mylib.Interface_framework_pane import InterfaceFrameworkPane
# if __name__ == '__main__':
# 	app = QApplication(sys.argv)
# 	window = InterfaceFrameworkPane()
# 	window.show()
# 	sys.exit(app.exec_())
# !/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *

# class Window(QWidget):
# 	def __init__(self, parent=None, *args, **kwargs):
# 		super().__init__(parent, *args, **kwargs)
# 		self.setWindowTitle('文本编辑')
# 		self.resize(640, 480)
# 		self.setup_ui()
#
# 	def setup_ui(self):
# 		self.plaintext = QPlainTextEdit(self)
# 		self.plaintext = QTextDocument(self)
# self.plaintext.move(100, 100)
# self.plaintext.setStyleSheet("""
# 	background-color: rgb(192,192,192);
# 	color: black;
# """)
# pass
#
# pass
#
#
# if __name__ == '__main__':
# 	app = QApplication(sys.argv)
# 	window = Window()
# 	window.show()
# 	with open('E:/python/test/test.txt', 'r', encoding='utf-8') as f:  # 可以确保关闭句柄
# 		content = f.read()
# 		print(content[ 11 ])  # 回车换行算一个字符
# 		window.plaintext.setPlainText(content)
# window.plaintext.setPlainText(content)
#
# window.plaintext.setFocus(True)
# cursor = window.plaintext.textCursor()  # 获取文本光标
# print("在第几列", cursor.columnNumber())
# print("光标位置", cursor.position())
# print('块数量', cursor.blockNumber())
# sys.exit(app.exec_())

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QWidget()
	window.setStyleSheet('background-color:red;')
	window.show()
	mb = QMessageBox(QMessageBox.Warning, '提醒', '程序保护已打开', QMessageBox.Yes | QMessageBox.No, window)
	mb.show()
	mb.setStyleSheet('background-color:white;')
	# mb.show()


	def test_cao(state):
		print(state)
		print(window.children())
		mb.setParent(None)
		print(window.children())
		pass


	mb.buttonClicked.connect(test_cao)
	sys.exit(app.exec_())
