#!/usr/bin/python3 
# -*- coding: utf-8 -*-
'''
class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee",Employee.empCount)

    def displayEmployee(self):
        print("Name:",self.name,",Salary:",self.salary)  

emp1 = Employee("Zara",2000)
emp2 = Employee("Manni",5000)
  
emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee:",Employee.empCount)
'''
import sys
from PyQt5.Qt import *
# sys.path.append(r'C:\Users\asus\.PyCharmCE2019.2\system\python_stubs\-643338342\PyQt5')
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QLabel的学习')
        self.resize(500,500)
        # self.setup_ui()
        # self.QObject信号的操作()
        # self.QObject类型判定()
        # self.QObject对象删除()
    def setup_ui(self):
        label = QLabel(self)
        label.setText('xxx')
    def QObject信号的操作(self):
        pass
        # self.obj = QObject()
        # # def destory_cao(obj):
        # #     print('对象被释放了',obj)
        # # self.obj.destroyed.connect(destory_cao)
        # # del self.obj
        # def obj_name_cao(name):
        #     print('对象名称发生了改变',name)
        # def obj_name_cao2(name):
        #     print('对象名称发生了改变',name)
        # self.obj.objectNameChanged.connect(obj_name_cao)
        # self.obj.objectNameChanged.connect(obj_name_cao2)
        # print(self.obj.receivers(self.obj.objectNameChanged)) #连接槽的个数
        # self.obj.setObjectName('xxx')
        # # print(self.obj.signalsBlocked(),'1')
        # # self.obj.blockSignals(True)
        # # # self.obj.objectNameChanged.disconnect()
        # # self.obj.setObjectName('ooo')
        # # print(self.obj.signalsBlocked(),'2')
        # # self.obj.blockSignals(False)
        # # # self.obj.objectNameChanged.connect(obj_name_cao)
        # # self.obj.setObjectName('xxoo')
        # btn = QPushButton(self)
        # btn.setText('点击我')
        # def cao():
        #     print('点我做什么？')
        # btn.clicked.connect(cao)
    def QObject类型判定(self):
        pass
        # # obj = QObject()
        # # w = QWidget()
        # # btn = QPushButton()
        # # label = QLabel()

        # # objs = [obj,w,btn,label]
        # # for o in objs:
        # #     # print(o,o.isWidgetType())
        # #     print(o.inherits('QWidget'))
        # label1 = QLabel(self)
        # label1.setText('社会我顺哥')
        # label1.move(100,100)
        # label2 = QLabel(self)
        # label2.setText('人狠话不多')
        # label2.move(150,150)
        # btn = QPushButton(self)
        # btn.setText('点我')
        # btn.move(200,200)
        # for widget in self.findChildren(QLabel):
        #     # print(widget)
        #     # if widget.isWidgetType():
        #     if widget.inherits('QLabel'):
        #         # print('是')
        #         widget.setStyleSheet('background-color:cyan;')
    def QObject对象删除(self):
        pass
        # obj1 = QObject()
        # self.obj1 = obj1
        # obj2 = QObject()
        # obj3 = QObject()
        # obj3.setParent(obj2)
        # obj2.setParent(obj1)
        # obj1.destroyed.connect(lambda : print('obj1被释放了'))
        # obj2.destroyed.connect(lambda : print('obj2被释放了'))
        # obj3.destroyed.connect(lambda : print('obj3被释放了'))
        # # del obj2
        # obj2.deleteLater()
        # print(obj1.children())
        # print(obj2)
# class App(QApplication):
#     def notify(self,receiver,evt):
#         if receiver.inherits('QPushButton') and evt.type() == QEvent.MouseButtonPress:
#             print(receiver,evt)
#         return super().notify(receiver,evt)
# class Btn(QPushButton):
#     def event(self,evt):
#         if evt.type() == QEvent.MouseButtonPress:
#             print(evt)
#         return super().event(evt)
#     def mousePressEvent(self, *args,**kwargs):
#         print('鼠标被按下了。。。')
#         return super().mousePressEvent(*args,**kwargs)
class MyObject(QObject):
    def timerEvent(self,evt):
        print(evt,'1')
# class MyLabel(QLabel):
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.setText('10')
#         self.move(100,100)
#         self.setStyleSheet('font-size:22px;')       
#     def timerEvent(self, *args, **kwargs):
#         # print('xxx')
#         current_sec = int(self.text())
#         current_sec -= 1
#         self.setText(str(current_sec))
#         if current_sec == 0:
#             print('停止')
#             self.killTimer(self.timer_id)
#     def setSec(self,sec):
#         self.setText(str(sec))
#     def startMyTimer(self,ms):
        # self.timer_id = self.startTimer(ms)
class MyWidget(QWidget):
    def timerEvent(self, *args, **kwargs):
        print('xx')
        current_w = self.width()
        current_h = self.height()
        self.resize(current_w + 10,current_h + 10)
if __name__ == '__main__':
    app = QApplication(sys.argv)

        # win1 = QWidget()
        # win1.setStyleSheet('background-color:red;') #设置控件窗口的颜色
        # win1.resize(500,500) #设置控件的大小尺寸
        # win1.setWindowTitle('red')
        # win1.show()

        # win2 = QWidget()
        # win2.setStyleSheet('background-color:green;')
        # #win2.setParent(win1)
        # win2.setWindowTitle('green')
        # win2.resize(500,500)
        # win2.show()
        
        # win_root = QWidget()

        # label1 = QLabel()
        # label1.setText('label1')
        # label1.setParent(win_root)

        # label2 = QLabel()
        # label2.setText('label2')
        # label2.move(50,50)
        # label2.setParent(win_root)

        # label3 = QLabel()
        # label3.setText('label2')
        # label3.move(30,30)
        # label3.setParent(win_root)

        # btn = QPushButton(win_root)
        # btn.move(100,100)
        # btn.setText('btn')
        # win_root.show()

        # for sub_widget in win_root.findChildren(QLabel):
        #     print(sub_widget)
        #     sub_widget.setStyleSheet('background-color:cyan;')
        # btn = QPushButton(self)
        # btn.setText('点击我')
        # window = Window()
        # window = QWidget()
        # def cao(title):
        #     print('标题改变了',title)
        #     window.blockSignals(True)
        #     window.setWindowTitle('撩课-' + title)
        #     window.blockSignals(False)
        # window.windowTitleChanged.connect(cao)
        # window.setWindowTitle('Hello Sz')
        # window.setWindowTitle('Hello Sz1')
        # window.setWindowTitle('Hello Sz2')
        # window.show()
    window = MyWidget()
    # btn = Btn(window)
    # btn.setText('按钮')
    # btn.move(100,100)
    # def cao():
    #     print('按钮被点击了')
    # btn.pressed.connect(cao)
    window.setWindowTitle('QObject定时器的使用')
    window.resize(500,500)
    # label = MyLabel(window)
    # label.setSec(5)
    # label.startMyTimer(500)
    # obj = MyObject()
    # timer_id = obj.startTimer(1000) #参数，第一个是毫秒间隔的时间 第二个参数是充分值
    # obj.killTimer(timer_id)
    window.startTimer(1000)
    window.show()
    sys.exit(app.exec_())
