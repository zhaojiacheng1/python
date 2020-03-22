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
import sys
from PyQt5.Qt import *


class MyASB(QAbstractSpinBox):
    def __init__(self, parent=None, num='0', *args, **kwargs):  # 定义函数时，None的意思是不传值是None
        super().__init__(parent, *args, **kwargs)  # 调用函数，参数需要传入
        self.lineEdit().setText(num)

    def stepEnabled(self):  # 属于自动调用
        # current_num = int(self.text())
        # if current_num == 0:
        #     return QAbstractSpinBox.StepUpEnabled  # 仅向上有效
        # elif current_num == 9:
        #     return QAbstractSpinBox.StepDownEnabled  # 仅向下有效
        # elif current_num < 0 or current_num > 9:
        #     return QAbstractSpinBox.StepNone  # 无效
        # else:
        #     return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled  # 向上、向下都有效
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, p_int):  # 有效时才会调用该函数，属于自动调用
        print(p_int)
        current_num = int(self.text()) + p_int
        self.lineEdit().setText(str(current_num))  # 首先获取单行文本控件对象


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QAbstractSpinBox-学习')
        self.resize(640, 480)
        self.setup_ui()

    def setup_ui(self):
        asb = MyASB(self)  # 单位文本编辑器，右面带有调节器，是个组合控件，左边是个单行文本编辑器
        self.asb = asb
        asb.resize(100, 30)
        asb.move(100, 100)
        # asb.setAccelerated(True)  # 设置按钮使数据递增的数据速度加速
        # print(asb.isAccelerated())
        # asb.setReadOnly(True)
        # print(asb.isReadOnly())  # 只读是针对按钮，不能通过键盘输入
        test_btn = QPushButton(self)
        test_btn.move(200, 200)
        test_btn.setText('测试按钮')
        test_btn.clicked.connect(self.btn_cao)

    def btn_cao(self):
        print('测试按钮')
        print(self.asb.text())
        print(self.asb.lineEdit().text())
        print(self.asb.lineEdit().setText('88'))
        cl = QCompleter(['sz', '123', '18'], self.asb)  # 自动匹配对象，需要输入元组
        self.asb.lineEdit().setCompleter(cl)  # 设置自动匹配，需要自动匹配的对象
        self.asb.lineEdit().setAlignment(Qt.AlignCenter)  # 设置自动对齐方式


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())
