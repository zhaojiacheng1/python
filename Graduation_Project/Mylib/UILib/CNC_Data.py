#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.Qt import *


class CNCData(QObject):  # 继承QObject类 可以使用信号与槽机制
	# CNC具有的模式
	CNCModeAll = { 0: 'EDIT', 1: 'MDI', 2: 'MDI', 3: 'JOG',
	               4: 'INC', 5: 'INC', 6: 'INC', 7: 'INC', 8: 'INC',
	               9: 'MDI', 10: 'MEM', 11: 'MEM', 12: 'REF' }  # 其中 4：1，5：10，6：100，7：1000，8：10000
	# CNC具有的进给倍率
	CNCFeedSpeedAll = { 0: '0', 1: '2', 2: '6', 3: '10', 4: '20',
	                    5: '40', 6: '60', 7: '70', 8: '80', 9: '90', 10: '100', 11: '110', 12: '120' }
	# CNC具有的主轴倍率
	CNCSpindleSpeedAll = { 0: '50', 1: '60', 2: '70', 3: '80', 4: '90', 5: '100', 6: '110', 7: '120' }
	# CNC具有的主轴状态 on属于正转 cow属于反转
	CNCSpindleStateAll = { 'Btn_STOP': 'STOP', 'Btn_ON': 'SpindleOn', 'Btn_COW': 'SpindleCOW' }
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

	def __init__(self, parent=None, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		pass

	def PowerOffInit(self):
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
