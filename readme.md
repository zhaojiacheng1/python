# Git is a version control system

## git工具学习

Git is free software  
Git is a test!  
Git在ubuntu上的实验  
Creating a new branch is quick!  
git pull test  
branch merge test

# 项目进度

[GitHUb仓库](https://github.com/zhaojiacheng1/python)

## 2020.1.3

至目前为之，所有的开发环境已经搭建完毕
当前首要任务是寻找Fanuc数控系统模拟器

## 2020.1.4

购买Fanuc数控系统模拟器
对模拟器界面进行切片

## 2020.1.5

昨日HMI切片并未完成，今天继续选择的数控系统型号为Fanuc 0iT，了解操作面板操作

## 2020.1.6

数控系统的基本操作已经学习完毕，对模拟器界面进行切片，首先选择设计除开CRT的部分，以用作后期操作
基本界面在文件界面切片图中

## 2020.1.9

界面切片中断，并未全部完成。正在学习python的GUI设计以及学习python语法，估计需要花费些时间

## 2020.1.16

至目前为之，python语法学习结束

## 2020.2.10

正式启动项目开发

## 2020.3.18

项目程序编写，首先编写UI界面，遇到界面尺寸适应的问题，还包括界面内部添加容器的问题，光标位置的问题

## 2020.3.19

项目界面程序编写没有进展，主要体现在几个方面：界面尺寸问题没有得到解决、界面容器问题没有解决

## 2020.3.21

连续两天学习PyQt5教程、项目没有进展 QTextEdit、QPlainTextEdit

## 2020.3.22

学习了QAbstractSpinBox, 掌握其基本用法

## 2020.3.23

学习了QSpinBox、QDoubleSpinBox，掌握其基本用法

## 2020.3.24

学习了QDateTimeEdit、QComboBox及其子类QFontComboBox，掌握其基本用法

## 2020.3.25

学习了QAbstractSlider、QRubberBand，掌握其基本用法

## 2020.3.26

学习了QDialog对话框控件，包括QColorDialog、QFontDialog、QFileDialog、QInputDialog控件，掌握其基本用法

## 2020.3.27

学习了展示控件QLabel、QLCDNumber、QProgressBar、QErrorMessage、QProgressDialog和QMessageBox控件，掌握其基本用法

## 2020.3.28

学习了布局管理器QLayout和QBoxLayout，掌握其基本用法

## 2020.3.29

学习了QFormLayout、QGridLayout、QStackedLayout和布局管理器的尺寸策略, 掌握其基本用法

## 2020.3.30

学习了QSS的组成部分、选择器、伪状态，掌握其基本用法，并确定项目使用Fanuc 18iMB数控系统

## 2020.4.1

学习了QTDesigner工具的使用、pyuic5、pyrcc5工具的使用

## 2020.4.2

学习了自定义信号、动画的使用，掌握其基本用法

## 2020.4.3

学习综合案例，了解项目整体设计流程以及文件夹结构

## 2020.4.4

学习动画、页面跳转、UI文件产生的类封装

## 2020.4.5

学习了程序打包

# FANUC Series 18i MB

## 1、数控系统界面框架

* 界面的尺寸

|-|710|340|
|-|-|-|
|425|-|-|
|40|-|-|
|340|-|-|

* 界面框架如图

![界面框架](graduation%20project/Doc/images_2020-4-7.png)

1、界面基本的框架雏形已经出来了：左上角的CRT界面以及CRT下侧的软按键；左下角的输入面板部分；右侧的操作面板；

2、问题：

    1> 右侧控制部分的急停按钮：样式与实际的急停按钮差别较大，且操作时的动态特效不佳。

    2> 右侧的表盘控件：表盘控件一般用于展示，此处将其用作输入控件，效果不好，展示的效果较差，比如没有刻度显示，没有底部说明字符串等等。

    3> 按钮控件的点击动效一般不太美观

NOTES：界面颜色会再调。

