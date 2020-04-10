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

## 数控系统界面框架

### 界面的尺寸

|-|710|340|
|-|-|-|
|425|-|-|
|40|-|-|
|340|-|-|

### 界面框架如图

![界面框架](Doc/images_2020-4-7.png)

1、界面基本的框架雏形已经出来了：左上角的CRT界面以及CRT下侧的软按键；左下角的输入面板部分；右侧的操作面板；

2、问题：

1> 右侧控制部分的急停按钮：样式与实际的急停按钮差别较大，且操作时的动态特效不佳。

2> 右侧的表盘控件：表盘控件一般用于展示，此处将其用作输入控件，效果不好，展示的效果较差，比如没有刻度显示，没有底部说明字符串等等。

3> 按钮控件的点击动效一般不太美观

NOTES：界面颜色会再调。

### 界面输入检测问题

PLAN：

1> 输入类的按键，设置**role**属性：input；控制类的按键包括表盘控件（可能不使用），设置**role**属性：control；对于CRT界面下方的软按键，设置**role**属性w为position，从左到右依次为1到10，另外注意两侧的软按键，设置**role**属性，back和go; 还有一类用于查看的，比如翻页，移动光标等等，认为应当设置**role**属性为view，应当与control区别，view侧重于CRT，control侧重于机床；

2> 键值部分，暂时打算创建和ObjectName相关的可遍历字典；

3> 信号与槽函数部分，自定义信号应当发送**role**属性和**ObjectName**两部分；

4> 注意RESET，ALTER，HELP键当作control类看待，在设置属性时设置为control；

5> **position**属性的信号发送时，发送position固定字符串和其值；

### 关于旋转选择开关

1> 当下，打算将其只是用QDial控件实现。存在两方面问题：一方面，刻度不能显示的问题；另一个是不能插入图片在刻度部分

2> 不打算在这个方面纠缠

### 关于控制面板的按钮设置

1> 设置checkable为True：Shift、Emergency_STOP、DRIVE（机床锁住）、PROTECT（程序保护）、RAPID（快速进给）、ON（主轴正转）、STOP（主轴停止）、COW（主轴反转）、DRN(空运行)、COOL（冷却液）、MSTLOCK（MST锁住）、SBK（单步）、SKIP（跳步）、M01（M01选择停）；

2> 不确定是否设置checkable为True：TOOL（手动换刀）、//（复位）；

3> 按钮SRN含义不清，暂不处理；并未设置手轮，MPG（手轮脉冲）按钮不处理；DNC（文件传输）暂时使用不明，目前不设置checkable；

4> 选择开关部分需要在开机时程序设置初值，暂定为：进给速度为10（100%），主轴转速为10（100%），模式选择为12（REF）；

### 界面效果

![未加优化的界面效果图](graduation&#32;project/Doc/images_2020-04-09_23-19-31.png)

问题：

1> 旋转选择开关的问题较大，主要是刻度显示的问题。

2> SBK（单步）与SKIP（跳步）按钮我认为应当是互斥的，但是互斥设置之后，会导致check选中功能异常，表现为在一组按钮组中有且必须有一个按钮处于check状态，不能使所有按键处于uncheck状态；

### 信号测试

![信号测试图](graduation&#32;project/Doc/images_2020-04-09_23-28-37.png)

经过测试，所有信号都已经正常运行；

## CRT部分

### 软件上电操作之前

1> 模式介绍：EDIT（编辑模式）、MDI（手动数据输入）、JOG（手动）、INC（增量进给）、AUTO（自动循环）（MEM）、REF（回参考点）；

2> 急停按钮处于按下状态，DRIVE和PROTECT都处于关闭状态（改为打开）；

3> 应当编写上电前的初始化函数，PowerOffInit(), 目前遇到，参数为对象的情况；

### 软件上电之后的初始状态

1> 机床的舱门部分不处理（暂时当作不存在），主轴STOP按钮按下，CRT界面处于POS界面，模式处于REF，进给倍率和主轴倍率都是100%；

NOTES:

1> 发现8个轴选按钮长按是不合逻辑的问题，即当这八个按钮长按时不能正常地发送对应信号，打算单独取出来处理; 

![QPushButton的信号说明](graduation&#32;project/Doc/images_2020-04-10_21-56-17.png)

