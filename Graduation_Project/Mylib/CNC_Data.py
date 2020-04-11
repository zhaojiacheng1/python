#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *
from Mylib.Interface_framework_pane import InterfaceFrameworkPane


class CNCData(QObject):  # 继承QObject类 可以使用信号与槽机制
	""" CNC数据类：存储CNC重要的临时数据"""
	# CNC具有的模式
	CNCModeAll = { 0: 'EDIT', 1: 'MDI', 2: 'MDI', 3: 'JOG',
	               4: 'INC', 5: 'INC', 6: 'INC', 7: 'INC', 8: 'INC',
	               9: 'MDI', 10: 'MEM', 11: 'MEM', 12: 'REF' }  # 其中 4：1，5：10，6：100，7：1000，8：10000
	# CNC在INC模式下的增量倍率
	CNCINCSpeedAll = { 4: '1', 5: '10', 6: '100', 7: '1000', 8: '10000' }
	# CNC具有的进给倍率
	CNCFeedSpeedAll = { 0: '0', 1: '2', 2: '6', 3: '10', 4: '20',
	                    5: '40', 6: '60', 7: '70', 8: '80', 9: '90', 10: '100', 11: '110', 12: '120' }
	# CNC具有的主轴倍率
	CNCSpindleSpeedAll = { 0: '50', 1: '60', 2: '70', 3: '80', 4: '90', 5: '100', 6: '110', 7: '120' }
	# CNC具有的主轴状态 on属于正转 cow属于反转
	CNCSpindleStateAll = { 'Btn_STOP': 'STOP', 'Btn_ON': 'SpindleOn', 'Btn_COW': 'SpindleCOW' }
	# CNC自动加工的所有状态
	CNCAutoProcessStateAll = { 'Btn_Auto_Start': 'Start', 'Btn_Auto_End': 'STOP' }

	# CNC当前的电源按钮状态 默认为False 即电源关闭
	CNCPowerState = False
	# CNC当前的急停按钮状态 默认为True 即急停打开
	CNCEmergencySTOP = True
	# CNC的回零状态 False未回零，True回零
	CNCZeroState = False
	# CNC当前的模式 默认为REF
	CNCNowMode = 'REF'
	# CNC当前的主轴倍率 默认为100 %
	CNCSpindleSpeed = '100'
	# CNC当前的进给倍率 默认为100%
	CNCFeedSpeed = '100'
	# CNC当前INC模式下的速度 默认为0
	CNCINCSpeed = '0'
	# CNC当前机械锁的位置 默认True 即机床锁住
	CNCDRIVEState = True
	# CNC当前程序保护的状态 默认True 即开启程序保护
	CNCPROTECTState = True
	# CNC当前快速进给的状态 默认False 即关闭快速进给
	CNCRAPIDState = False
	# CMC当前的主轴状态 默认为STOP 即主轴停止转动
	CNCSpindleState = 'STOP'
	# CNC当前的空运行状态 默认False 即不空运行
	CNCDRNState = False
	# CNC当前的冷却液状态 默认False 即冷却液关
	CNCCOOLState = False
	# CNC当前的MST状态 默认False 即关闭MST锁
	CNCMSTLOCKState = False
	# CNC当前的SBK单步运行状态 默认False 即关闭单步运行
	CNCSBKState = False
	# CNC当前的SKIP跳步运行状态 默认False 即关闭跳步运行
	CNCSKIPState = False
	# CNC当前M01选择停状态 默认False 即关闭M01选择停
	CNCM01State = False
	# CNC当前的自动换到状态 默认False 即自动换刀停 按下才能打开 松开即False
	CNCTOOLState = False
	# CNC轴选状态 默认False 即未选中 按下才能选中 松开即False
	CNCAxisAPState = False  # A轴正向
	CNCAxisANState = False  # A轴反向
	CNCAxisXPState = False  # x轴正向
	CNCAxisXNState = False  # X轴反向
	CNCAxisYPState = False  # Y轴正向
	CNCAxisYNState = False  # Y轴反向
	CNCAxisZPState = False  # Z轴正向
	CNCAxisZNState = False  # Z轴反向

	# CNC的手轮模式 默认False 即不使用手轮
	CNCMPGState = False
	# CNC的shift状态 默认False 即并未按下shift键
	CNCShiftState = False
	# CNC的CRT界面显示分支 为了简化程序 当切换完全不同的界面时将放弃原界面未保存的修改
	CNCCRTState = 'POS'
	# CNC的CRT界面软按键信息
	SoftButtonTempInfo = { 'Btn_One': '', 'Btn_Two': '', 'Btn_Three': '', 'Btn_Four': '', 'Btn_Five': '',
	                       'Btn_Six': '', 'Btn_Seven': '', 'Btn_Eight': '', 'Btn_Nine': '', 'Btn_Ten': '' }
	# CRT软按键的按下造成的界面分支
	CRTPageState = ''

	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		pass

	# 在上电前将控制面板固定按钮 如急停按钮，模式选择，主轴、进给倍率
	def PowerOffInit(self, InterfaceFrameworkPane):
		"""	PowerOffInit(self, InterfaceFrameworkPane)-> None """
		# 设置急停按钮
		InterfaceFrameworkPane.Btn_Emergency_STOP.setChecked(self.CNCEmergencySTOP)
		# 设置模式值 根据默认的模式推断字典相应的键然后设置
		value = list(self.CNCModeAll.keys())[ list(self.CNCModeAll.values()).index(self.CNCNowMode) ]
		InterfaceFrameworkPane.Btn_Mode.setValue(value)
		# 设置进给倍率和主轴倍率
		value = list(self.CNCFeedSpeedAll.keys())[ list(self.CNCFeedSpeedAll.values()).index(self.CNCFeedSpeed) ]
		InterfaceFrameworkPane.Btn_Speed.setValue(value)
		value = list(self.CNCSpindleSpeedAll.keys())[ list(self.CNCSpindleSpeedAll.values()).index(self.CNCSpindleSpeed) ]
		InterfaceFrameworkPane.Btn_Spindle_Speed.setValue(value)

		InterfaceFrameworkPane.Btn_SHIFT.setChecked(self.CNCShiftState)
		InterfaceFrameworkPane.Btn_RAPID.setChecked(self.CNCRAPIDState)
		InterfaceFrameworkPane.Btn_COOL.setChecked(self.CNCCOOLState)
		InterfaceFrameworkPane.Btn_DRIVE.setChecked(self.CNCDRIVEState)
		InterfaceFrameworkPane.Btn_PROTECT.setChecked(self.CNCPROTECTState)
		InterfaceFrameworkPane.Btn_DRN.setChecked(self.CNCDRNState)
		InterfaceFrameworkPane.Btn_MSTLOCK.setChecked(self.CNCMSTLOCKState)
		InterfaceFrameworkPane.Btn_SBK.setChecked(self.CNCSBKState)
		InterfaceFrameworkPane.Btn_SKIP.setChecked(self.CNCSKIPState)
		InterfaceFrameworkPane.Btn_M01.setChecked(self.CNCM01State)
		pass

	# 在上电后将控制面板的部分按键初始化
	def PowerOnInit(self, InterfaceFrameworkPane):
		# 设置主轴停止按钮按下
		InterfaceFrameworkPane.Btn_STOP.setChecked(True)
		pass

	pass


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QWidget()
	window.show()
	test = CNCData()
	# print(test.CNCFeedSpeed)
	# test.CNCFeedSpeed = test.CNCFeedSpeedAll[0]
	# print(test.CNCFeedSpeed)
	sys.exit(app.exec_())
