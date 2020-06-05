#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import time
from PyQt5.Qt import *
from Mylib.Interface_framework_pane import InterfaceFrameworkPane


class CNCData(QObject):  # 继承QObject类 可以使用信号与槽机制
	""" CNC数据类：存储CNC重要的临时数据"""
	# 数据处理结束信号 主要是指无效数据
	DataStateDone = pyqtSignal(bool)
	# CNC的电源信号传递 参数有电源状态 数据对象,界面对象(父对象)(可以不传递 应为CNCProcess类的父对象与CNCData的父对象一致)
	CNCPowerSignal = pyqtSignal(bool, object)
	# CRT界面的软按键信号 参数为 按钮对象名 按钮内容 数据对象(可不必)
	CRTSoftBtnSignal = pyqtSignal(str, str)
	# CNC急停信号
	CNCEmergencySTOPSignal = pyqtSignal(bool)
	# CNC模式选择信号 参数为模式值
	CNCModeChangeSignal = pyqtSignal(str)
	# CNC进给速度信号 参数为进给倍率值
	CNCFeedSpeedSignal = pyqtSignal(str)
	# CNC主轴倍率信号 参数为主轴倍率值
	CNCSpindleSpeedSignal = pyqtSignal(str)
	# CNC轴选信号 参数为轴对象名 状态
	CNCAxisSignal = pyqtSignal(str, bool)
	# CNC界面切换信号 参数为界面缩写如POS PROG等
	CNCCRTChangeSignal = pyqtSignal(str)
	# CNC输入信号 比如G S 等英文字符或是1 2 3 等阿拉伯数字
	CNCInputSignal = pyqtSignal(str)
	# CNC光标移动信号 参数为键的id名称
	CNCCursorMoveSignal = pyqtSignal(str)
	# CNC翻页操作信号 参数为键的ID名称
	CNCPageChangeSignal = pyqtSignal(str)
	# 刀具参数设置 采用字典的存储方式 key值表示番号 采用数字 value值采用列表 按照列号减一的顺序存储
	CNCParameterToolDict = { 1: [ 0.001, 0.000, 0.000, 0.000 ], 2: [ 0.000, 0.000, 0.000, 0.000 ], 3: [ 0.000, 0.000, 0.000, 0.000 ], 4: [ 0.000, 0.000, 0.000, 0.000 ], 5: [ 0.000, 0.000, 0.000, 0.000 ], 6: [ 0.000, 0.000, 0.000, 0.000 ], 7: [ 0.000, 0.000, 0.000, 0.000 ], 8: [ 0.000, 0.000, 0.000, 0.000 ], 9: [ 0.000, 0.000, 0.000, 0.000 ], 10: [ 0.000, 0.000, 0.000, 0.000 ], 11: [ 0.000, 0.000, 0.000, 0.000 ], 12: [ 0.000, 0.000, 0.000, 0.000 ], 13: [ 0.000, 0.000, 0.000, 0.000 ], 14: [ 0.000, 0.000, 0.000, 0.000 ], 15: [ 0.000, 0.000, 0.000, 0.000 ], 16: [ 0.000, 0.000, 0.000, 0.016 ],
	                         17: [ 0.002, 0.000, 0.000, 0.000 ], 18: [ 0.000, 0.000, 0.000, 0.000 ], 19: [ 0.000, 0.000, 0.000, 0.000 ], 20: [ 0.000, 0.000, 0.000, 0.000 ], 21: [ 0.000, 0.000, 0.000, 0.000 ], 22: [ 0.000, 0.000, 0.000, 0.000 ], 23: [ 0.000, 0.000, 0.000, 0.000 ], 24: [ 0.000, 0.000, 0.000, 0.000 ], 25: [ 0.000, 0.000, 0.000, 0.000 ], 26: [ 0.000, 0.000, 0.000, 0.000 ], 27: [ 0.000, 0.000, 0.000, 0.000 ], 28: [ 0.000, 0.000, 0.000, 0.000 ], 29: [ 0.000, 0.000, 0.000, 0.000 ], 30: [ 0.000, 0.000, 0.000, 0.000 ], 31: [ 0.000, 0.000, 0.000, 0.000 ], 32: [ 0.000, 0.000, 0.000, 0.032 ],
	                         33: [ 0.003, 0.000, 0.000, 0.000 ], 34: [ 0.000, 0.000, 0.000, 0.000 ], 35: [ 0.000, 0.000, 0.000, 0.000 ], 36: [ 0.000, 0.000, 0.000, 0.000 ], 37: [ 0.000, 0.000, 0.000, 0.000 ], 38: [ 0.000, 0.000, 0.000, 0.000 ], 39: [ 0.000, 0.000, 0.000, 0.000 ], 40: [ 0.000, 0.000, 0.000, 0.000 ], 41: [ 0.000, 0.000, 0.000, 0.000 ], 42: [ 0.000, 0.000, 0.000, 0.000 ], 43: [ 0.000, 0.000, 0.000, 0.000 ], 44: [ 0.000, 0.000, 0.000, 0.000 ], 45: [ 0.000, 0.000, 0.000, 0.000 ], 46: [ 0.000, 0.000, 0.000, 0.000 ], 47: [ 0.000, 0.000, 0.000, 0.000 ], 48: [ 0.000, 0.000, 0.000, 0.000 ],
	                         49: [ 0.000, 0.000, 0.000, 0.000 ], 50: [ 0.000, 0.000, 0.000, 0.000 ], 51: [ 0.000, 0.000, 0.000, 0.000 ], 52: [ 0.000, 0.000, 0.000, 0.000 ], 53: [ 0.000, 0.000, 0.000, 0.000 ], 54: [ 0.000, 0.000, 0.000, 0.000 ], 55: [ 0.000, 0.000, 0.000, 0.000 ], 56: [ 0.000, 0.000, 0.000, 0.000 ], 57: [ 0.000, 0.000, 0.000, 0.000 ], 58: [ 0.000, 0.000, 0.000, 0.000 ], 59: [ 0.000, 0.000, 0.000, 0.000 ], 60: [ 0.000, 0.000, 0.000, 0.000 ], 61: [ 0.000, 0.000, 0.000, 0.000 ], 62: [ 0.000, 0.000, 0.000, 0.000 ], 63: [ 0.000, 0.000, 0.000, 0.000 ], 64: [ 0.000, 0.000, 0.000, 0.000 ],
	                         65: [ 0.000, 0.000, 0.000, 0.000 ], 66: [ 0.000, 0.000, 0.000, 0.000 ], 67: [ 0.000, 0.000, 0.000, 0.000 ], 68: [ 0.000, 0.000, 0.000, 0.000 ], 69: [ 0.000, 0.000, 0.000, 0.000 ], 70: [ 0.000, 0.000, 0.000, 0.000 ], 71: [ 0.000, 0.000, 0.000, 0.000 ], 72: [ 0.000, 0.000, 0.000, 0.000 ], 73: [ 0.000, 0.000, 0.000, 0.000 ], 74: [ 0.000, 0.000, 0.000, 0.000 ], 75: [ 0.000, 0.000, 0.000, 0.000 ], 76: [ 0.000, 0.000, 0.000, 0.000 ], 77: [ 0.000, 0.000, 0.000, 0.000 ], 78: [ 0.000, 0.000, 0.000, 0.000 ], 79: [ 0.000, 0.000, 0.000, 0.000 ], 80: [ 0.000, 0.000, 0.000, 0.000 ],
	                         81: [ 0.000, 0.000, 0.000, 0.000 ], 82: [ 0.000, 0.000, 0.000, 0.000 ], 83: [ 0.000, 0.000, 0.000, 0.000 ], 84: [ 0.000, 0.000, 0.000, 0.000 ], 85: [ 0.000, 0.000, 0.000, 0.000 ], 86: [ 0.000, 0.000, 0.000, 0.000 ], 87: [ 0.000, 0.000, 0.000, 0.000 ], 88: [ 0.000, 0.000, 0.000, 0.000 ], 89: [ 0.000, 0.000, 0.000, 0.000 ], 90: [ 0.000, 0.000, 0.000, 0.000 ], 91: [ 0.000, 0.000, 0.000, 0.000 ], 92: [ 0.000, 0.000, 0.000, 0.000 ], 93: [ 0.000, 0.000, 0.000, 0.000 ], 94: [ 0.000, 0.000, 0.000, 0.000 ], 95: [ 0.000, 0.000, 0.000, 0.000 ], 96: [ 0.000, 0.000, 0.000, 0.000 ],
	                         97: [ 0.000, 0.000, 0.000, 0.000 ], 98: [ 0.000, 0.000, 0.000, 0.000 ], 99: [ 0.000, 0.000, 0.000, 0.000 ], 100: [ 0.000, 0.000, 0.000, 0.000 ], 101: [ 0.000, 0.000, 0.000, 0.000 ], 102: [ 0.000, 0.000, 0.000, 0.000 ], 103: [ 0.000, 0.000, 0.000, 0.000 ], 104: [ 0.000, 0.000, 0.000, 0.000 ], 105: [ 0.000, 0.000, 0.000, 0.000 ], 106: [ 0.000, 0.000, 0.000, 0.000 ], 107: [ 0.000, 0.000, 0.000, 0.000 ], 108: [ 0.000, 0.000, 0.000, 0.000 ], 109: [ 0.000, 0.000, 0.000, 0.000 ], 110: [ 0.000, 0.000, 0.000, 0.000 ], 111: [ 0.000, 0.000, 0.000, 0.000 ], 112: [ 0.000, 0.000, 0.000, 0.000 ],
	                         113: [ 0.000, 0.000, 0.000, 0.000 ], 114: [ 0.000, 0.000, 0.000, 0.000 ], 115: [ 0.000, 0.000, 0.000, 0.000 ], 116: [ 0.000, 0.000, 0.000, 0.000 ], 117: [ 0.000, 0.000, 0.000, 0.000 ], 118: [ 0.000, 0.000, 0.000, 0.000 ], 119: [ 0.000, 0.000, 0.000, 0.000 ], 120: [ 0.000, 0.000, 0.000, 0.000 ], 121: [ 0.000, 0.000, 0.000, 0.000 ], 122: [ 0.000, 0.000, 0.000, 0.000 ], 123: [ 0.000, 0.000, 0.000, 0.000 ], 124: [ 0.000, 0.000, 0.000, 0.000 ], 125: [ 0.000, 0.000, 0.000, 0.000 ], 126: [ 0.000, 0.000, 0.000, 0.000 ], 127: [ 0.000, 0.000, 0.000, 0.000 ], 128: [ 0.000, 0.000, 0.000, 0.000 ],
	                         129: [ 0.000, 0.000, 0.000, 0.000 ], 130: [ 0.000, 0.000, 0.000, 0.000 ], 131: [ 0.000, 0.000, 0.000, 0.000 ], 132: [ 0.000, 0.000, 0.000, 0.000 ], 133: [ 0.000, 0.000, 0.000, 0.000 ], 134: [ 0.000, 0.000, 0.000, 0.000 ], 135: [ 0.000, 0.000, 0.000, 0.000 ], 136: [ 0.000, 0.000, 0.000, 0.000 ], 137: [ 0.000, 0.000, 0.000, 0.000 ], 138: [ 0.000, 0.000, 0.000, 0.000 ], 139: [ 0.000, 0.000, 0.000, 0.000 ], 140: [ 0.000, 0.000, 0.000, 0.000 ], 141: [ 0.000, 0.000, 0.000, 0.000 ], 142: [ 0.000, 0.000, 0.000, 0.000 ], 143: [ 0.000, 0.000, 0.000, 0.000 ], 144: [ 0.000, 0.000, 0.000, 0.000 ],
	                         145: [ 0.000, 0.000, 0.000, 0.000 ], 146: [ 0.000, 0.000, 0.000, 0.000 ], 147: [ 0.000, 0.000, 0.000, 0.000 ], 148: [ 0.000, 0.000, 0.000, 0.000 ], 149: [ 0.000, 0.000, 0.000, 0.000 ], 150: [ 0.000, 0.000, 0.000, 0.000 ], 151: [ 0.000, 0.000, 0.000, 0.000 ], 152: [ 0.000, 0.000, 0.000, 0.000 ], 153: [ 0.000, 0.000, 0.000, 0.000 ], 154: [ 0.000, 0.000, 0.000, 0.000 ], 155: [ 0.000, 0.000, 0.000, 0.000 ], 156: [ 0.000, 0.000, 0.000, 0.000 ], 157: [ 0.000, 0.000, 0.000, 0.000 ], 158: [ 0.000, 0.000, 0.000, 0.000 ], 159: [ 0.000, 0.000, 0.000, 0.000 ], 160: [ 0.000, 0.000, 0.000, 0.000 ],
	                         161: [ 0.000, 0.000, 0.000, 0.000 ], 162: [ 0.000, 0.000, 0.000, 0.000 ], 163: [ 0.000, 0.000, 0.000, 0.000 ], 164: [ 0.000, 0.000, 0.000, 0.000 ], 165: [ 0.000, 0.000, 0.000, 0.000 ], 166: [ 0.000, 0.000, 0.000, 0.000 ], 167: [ 0.000, 0.000, 0.000, 0.000 ], 168: [ 0.000, 0.000, 0.000, 0.000 ], 169: [ 0.000, 0.000, 0.000, 0.000 ], 170: [ 0.000, 0.000, 0.000, 0.000 ], 171: [ 0.000, 0.000, 0.000, 0.000 ], 172: [ 0.000, 0.000, 0.000, 0.000 ], 173: [ 0.000, 0.000, 0.000, 0.000 ], 174: [ 0.000, 0.000, 0.000, 0.000 ], 175: [ 0.000, 0.000, 0.000, 0.000 ], 176: [ 0.000, 0.000, 0.000, 0.000 ],
	                         177: [ 0.000, 0.000, 0.000, 0.000 ], 178: [ 0.000, 0.000, 0.000, 0.000 ], 179: [ 0.000, 0.000, 0.000, 0.000 ], 180: [ 0.000, 0.000, 0.000, 0.000 ], 181: [ 0.000, 0.000, 0.000, 0.000 ], 182: [ 0.000, 0.000, 0.000, 0.000 ], 183: [ 0.000, 0.000, 0.000, 0.000 ], 184: [ 0.000, 0.000, 0.000, 0.000 ], 185: [ 0.000, 0.000, 0.000, 0.000 ], 186: [ 0.000, 0.000, 0.000, 0.000 ], 187: [ 0.000, 0.000, 0.000, 0.000 ], 188: [ 0.000, 0.000, 0.000, 0.000 ], 189: [ 0.000, 0.000, 0.000, 0.000 ], 190: [ 0.000, 0.000, 0.000, 0.000 ], 191: [ 0.000, 0.000, 0.000, 0.000 ], 192: [ 0.000, 0.000, 0.000, 0.000 ],
	                         193: [ 0.000, 0.000, 0.000, 0.000 ], 194: [ 0.000, 0.000, 0.000, 0.000 ], 195: [ 0.000, 0.000, 0.000, 0.000 ], 196: [ 0.000, 0.000, 0.000, 0.000 ], 197: [ 0.000, 0.000, 0.000, 0.000 ], 198: [ 0.000, 0.000, 0.000, 0.000 ], 199: [ 0.000, 0.000, 0.000, 0.000 ], 200: [ 0.000, 0.000, 0.000, 0.000 ], 201: [ 0.000, 0.000, 0.000, 0.000 ], 202: [ 0.000, 0.000, 0.000, 0.000 ], 203: [ 0.000, 0.000, 0.000, 0.000 ], 204: [ 0.000, 0.000, 0.000, 0.000 ], 205: [ 0.000, 0.000, 0.000, 0.000 ], 206: [ 0.000, 0.000, 0.000, 0.000 ], 207: [ 0.000, 0.000, 0.000, 0.000 ], 208: [ 0.000, 0.000, 0.000, 0.000 ],
	                         209: [ 0.000, 0.000, 0.000, 0.000 ], 210: [ 0.000, 0.000, 0.000, 0.000 ], 211: [ 0.000, 0.000, 0.000, 0.000 ], 212: [ 0.000, 0.000, 0.000, 0.000 ], 213: [ 0.000, 0.000, 0.000, 0.000 ], 214: [ 0.000, 0.000, 0.000, 0.000 ], 215: [ 0.000, 0.000, 0.000, 0.000 ], 216: [ 0.000, 0.000, 0.000, 0.000 ], 217: [ 0.000, 0.000, 0.000, 0.000 ], 218: [ 0.000, 0.000, 0.000, 0.000 ], 219: [ 0.000, 0.000, 0.000, 0.000 ], 220: [ 0.000, 0.000, 0.000, 0.000 ], 221: [ 0.000, 0.000, 0.000, 0.000 ], 222: [ 0.000, 0.000, 0.000, 0.000 ], 223: [ 0.000, 0.000, 0.000, 0.000 ], 224: [ 0.000, 0.000, 0.000, 0.000 ],
	                         225: [ 0.000, 0.000, 0.000, 0.000 ], 226: [ 0.000, 0.000, 0.000, 0.000 ], 227: [ 0.000, 0.000, 0.000, 0.000 ], 228: [ 0.000, 0.000, 0.000, 0.000 ], 229: [ 0.000, 0.000, 0.000, 0.000 ], 230: [ 0.000, 0.000, 0.000, 0.000 ], 231: [ 0.000, 0.000, 0.000, 0.000 ], 232: [ 0.000, 0.000, 0.000, 0.000 ], 233: [ 0.000, 0.000, 0.000, 0.000 ], 234: [ 0.000, 0.000, 0.000, 0.000 ], 235: [ 0.000, 0.000, 0.000, 0.000 ], 236: [ 0.000, 0.000, 0.000, 0.000 ], 237: [ 0.000, 0.000, 0.000, 0.000 ], 238: [ 0.000, 0.000, 0.000, 0.000 ], 239: [ 0.000, 0.000, 0.000, 0.000 ], 240: [ 0.000, 0.000, 0.000, 0.000 ],
	                         241: [ 0.000, 0.000, 0.000, 0.000 ], 242: [ 0.000, 0.000, 0.000, 0.000 ], 243: [ 0.000, 0.000, 0.000, 0.000 ], 244: [ 0.000, 0.000, 0.000, 0.000 ], 245: [ 0.000, 0.000, 0.000, 0.000 ], 246: [ 0.000, 0.000, 0.000, 0.000 ], 247: [ 0.000, 0.000, 0.000, 0.000 ], 248: [ 0.000, 0.000, 0.000, 0.000 ], 249: [ 0.000, 0.000, 0.000, 0.000 ], 250: [ 0.000, 0.000, 0.000, 0.000 ], 251: [ 0.000, 0.000, 0.000, 0.000 ], 252: [ 0.000, 0.000, 0.000, 0.000 ], 253: [ 0.000, 0.000, 0.000, 0.000 ], 254: [ 0.000, 0.000, 0.000, 0.000 ], 255: [ 0.000, 0.000, 0.000, 0.000 ], 256: [ 0.000, 0.000, 0.000, 0.000 ],
	                         257: [ 0.000, 0.000, 0.000, 0.000 ], 258: [ 0.000, 0.000, 0.000, 0.000 ], 259: [ 0.000, 0.000, 0.000, 0.000 ], 260: [ 0.000, 0.000, 0.000, 0.000 ], 261: [ 0.000, 0.000, 0.000, 0.000 ], 262: [ 0.000, 0.000, 0.000, 0.000 ], 263: [ 0.000, 0.000, 0.000, 0.000 ], 264: [ 0.000, 0.000, 0.000, 0.000 ], 265: [ 0.000, 0.000, 0.000, 0.000 ], 266: [ 0.000, 0.000, 0.000, 0.000 ], 267: [ 0.000, 0.000, 0.000, 0.000 ], 268: [ 0.000, 0.000, 0.000, 0.000 ], 269: [ 0.000, 0.000, 0.000, 0.000 ], 270: [ 0.000, 0.000, 0.000, 0.000 ], 271: [ 0.000, 0.000, 0.000, 0.000 ], 272: [ 0.000, 0.000, 0.000, 0.000 ],
	                         273: [ 0.000, 0.000, 0.000, 0.000 ], 274: [ 0.000, 0.000, 0.000, 0.000 ], 275: [ 0.000, 0.000, 0.000, 0.000 ], 276: [ 0.000, 0.000, 0.000, 0.000 ], 277: [ 0.000, 0.000, 0.000, 0.000 ], 278: [ 0.000, 0.000, 0.000, 0.000 ], 279: [ 0.000, 0.000, 0.000, 0.000 ], 280: [ 0.000, 0.000, 0.000, 0.000 ], 281: [ 0.000, 0.000, 0.000, 0.000 ], 282: [ 0.000, 0.000, 0.000, 0.000 ], 283: [ 0.000, 0.000, 0.000, 0.000 ], 284: [ 0.000, 0.000, 0.000, 0.000 ], 285: [ 0.000, 0.000, 0.000, 0.000 ], 286: [ 0.000, 0.000, 0.000, 0.000 ], 287: [ 0.000, 0.000, 0.000, 0.000 ], 288: [ 0.000, 0.000, 0.000, 0.000 ],
	                         289: [ 0.000, 0.000, 0.000, 0.000 ], 290: [ 0.000, 0.000, 0.000, 0.000 ], 291: [ 0.000, 0.000, 0.000, 0.000 ], 292: [ 0.000, 0.000, 0.000, 0.000 ], 293: [ 0.000, 0.000, 0.000, 0.000 ], 294: [ 0.000, 0.000, 0.000, 0.000 ], 295: [ 0.000, 0.000, 0.000, 0.000 ], 296: [ 0.000, 0.000, 0.000, 0.000 ], 297: [ 0.000, 0.000, 0.000, 0.000 ], 298: [ 0.000, 0.000, 0.000, 0.000 ], 299: [ 0.000, 0.000, 0.000, 0.000 ], 300: [ 0.000, 0.000, 0.000, 0.000 ], 301: [ 0.000, 0.000, 0.000, 0.000 ], 302: [ 0.000, 0.000, 0.000, 0.000 ], 303: [ 0.000, 0.000, 0.000, 0.000 ], 304: [ 0.000, 0.000, 0.000, 0.000 ],
	                         305: [ 0.000, 0.000, 0.000, 0.000 ], 306: [ 0.000, 0.000, 0.000, 0.000 ], 307: [ 0.000, 0.000, 0.000, 0.000 ], 308: [ 0.000, 0.000, 0.000, 0.000 ], 309: [ 0.000, 0.000, 0.000, 0.000 ], 310: [ 0.000, 0.000, 0.000, 0.000 ], 311: [ 0.000, 0.000, 0.000, 0.000 ], 312: [ 0.000, 0.000, 0.000, 0.000 ], 313: [ 0.000, 0.000, 0.000, 0.000 ], 314: [ 0.000, 0.000, 0.000, 0.000 ], 315: [ 0.000, 0.000, 0.000, 0.000 ], 316: [ 0.000, 0.000, 0.000, 0.000 ], 317: [ 0.000, 0.000, 0.000, 0.000 ], 318: [ 0.000, 0.000, 0.000, 0.000 ], 319: [ 0.000, 0.000, 0.000, 0.000 ], 320: [ 0.000, 0.000, 0.000, 0.000 ],
	                         321: [ 0.000, 0.000, 0.000, 0.000 ], 322: [ 0.000, 0.000, 0.000, 0.000 ], 323: [ 0.000, 0.000, 0.000, 0.000 ], 324: [ 0.000, 0.000, 0.000, 0.000 ], 325: [ 0.000, 0.000, 0.000, 0.000 ], 326: [ 0.000, 0.000, 0.000, 0.000 ], 327: [ 0.000, 0.000, 0.000, 0.000 ], 328: [ 0.000, 0.000, 0.000, 0.000 ], 329: [ 0.000, 0.000, 0.000, 0.000 ], 330: [ 0.000, 0.000, 0.000, 0.000 ], 331: [ 0.000, 0.000, 0.000, 0.000 ], 332: [ 0.000, 0.000, 0.000, 0.000 ], 333: [ 0.000, 0.000, 0.000, 0.000 ], 334: [ 0.000, 0.000, 0.000, 0.000 ], 335: [ 0.000, 0.000, 0.000, 0.000 ], 336: [ 0.000, 0.000, 0.000, 0.000 ],
	                         337: [ 0.000, 0.000, 0.000, 0.000 ], 338: [ 0.000, 0.000, 0.000, 0.000 ], 339: [ 0.000, 0.000, 0.000, 0.000 ], 340: [ 0.000, 0.000, 0.000, 0.000 ], 341: [ 0.000, 0.000, 0.000, 0.000 ], 342: [ 0.000, 0.000, 0.000, 0.000 ], 343: [ 0.000, 0.000, 0.000, 0.000 ], 344: [ 0.000, 0.000, 0.000, 0.000 ], 345: [ 0.000, 0.000, 0.000, 0.000 ], 346: [ 0.000, 0.000, 0.000, 0.000 ], 347: [ 0.000, 0.000, 0.000, 0.000 ], 348: [ 0.000, 0.000, 0.000, 0.000 ], 349: [ 0.000, 0.000, 0.000, 0.000 ], 350: [ 0.000, 0.000, 0.000, 0.000 ], 351: [ 0.000, 0.000, 0.000, 0.000 ], 352: [ 0.000, 0.000, 0.000, 0.000 ],
	                         353: [ 0.000, 0.000, 0.000, 0.000 ], 354: [ 0.000, 0.000, 0.000, 0.000 ], 355: [ 0.000, 0.000, 0.000, 0.000 ], 356: [ 0.000, 0.000, 0.000, 0.000 ], 357: [ 0.000, 0.000, 0.000, 0.000 ], 358: [ 0.000, 0.000, 0.000, 0.000 ], 359: [ 0.000, 0.000, 0.000, 0.000 ], 360: [ 0.000, 0.000, 0.000, 0.000 ], 361: [ 0.000, 0.000, 0.000, 0.000 ], 362: [ 0.000, 0.000, 0.000, 0.000 ], 363: [ 0.000, 0.000, 0.000, 0.000 ], 364: [ 0.000, 0.000, 0.000, 0.000 ], 365: [ 0.000, 0.000, 0.000, 0.000 ], 366: [ 0.000, 0.000, 0.000, 0.000 ], 367: [ 0.000, 0.000, 0.000, 0.000 ], 368: [ 0.000, 0.000, 0.000, 0.000 ],
	                         369: [ 0.000, 0.000, 0.000, 0.000 ], 370: [ 0.000, 0.000, 0.000, 0.000 ], 371: [ 0.000, 0.000, 0.000, 0.000 ], 372: [ 0.000, 0.000, 0.000, 0.000 ], 373: [ 0.000, 0.000, 0.000, 0.000 ], 374: [ 0.000, 0.000, 0.000, 0.000 ], 375: [ 0.000, 0.000, 0.000, 0.000 ], 376: [ 0.000, 0.000, 0.000, 0.000 ], 377: [ 0.000, 0.000, 0.000, 0.000 ], 378: [ 0.000, 0.000, 0.000, 0.000 ], 379: [ 0.000, 0.000, 0.000, 0.000 ], 380: [ 0.000, 0.000, 0.000, 0.000 ], 381: [ 0.000, 0.000, 0.000, 0.000 ], 382: [ 0.000, 0.000, 0.000, 0.000 ], 383: [ 0.000, 0.000, 0.000, 0.000 ], 384: [ 0.000, 0.000, 0.000, 0.000 ],
	                         385: [ 0.000, 0.000, 0.000, 0.000 ], 386: [ 0.000, 0.000, 0.000, 0.000 ], 387: [ 0.000, 0.000, 0.000, 0.000 ], 388: [ 0.000, 0.000, 0.000, 0.000 ], 389: [ 0.000, 0.000, 0.000, 0.000 ], 390: [ 0.000, 0.000, 0.000, 0.000 ], 391: [ 0.000, 0.000, 0.000, 0.000 ], 392: [ 0.000, 0.000, 0.000, 0.000 ], 393: [ 0.000, 0.000, 0.000, 0.000 ], 394: [ 0.000, 0.000, 0.000, 0.000 ], 395: [ 0.000, 0.000, 0.000, 0.000 ], 396: [ 0.000, 0.000, 0.000, 0.000 ], 397: [ 0.000, 0.000, 0.000, 0.000 ], 398: [ 0.000, 0.000, 0.000, 0.000 ], 399: [ 0.000, 0.000, 0.000, 0.000 ], 400: [ 0.000, 0.000, 0.000, 0.000 ] }
	# 当前聚焦的列表项 先行后列
	ParameterToolShowList = [ 1, 1 ]
	# 当前显示的列表页数 默认为1 最大为25 400/16
	ParameterToolShowPage = 1
	# 当前程序文件的路径 字符串
	FilePath = './resource/src/'
	# 当前系统存在的程序文件列表
	FileNameList = [ ]
	# 文件名称和大小对应字典
	FileSizeDict = { }
	# 文件名称和修改时间字典
	FileUpdateTime = { }
	# 文件总数或是文件大小或是文件修改时间发生变化的标志位 默认为False
	FilePropertyChangeFlag = False
	# 文件的总数量 默认为0 即一个文件也没有
	FileTotalNum = 0
	# 系统支持的最大文件数量
	FileTotalMaxNum = 320
	# 当前文件占用的内存大小 默认为0 需要计算
	FileTotalMemoryUsed = 0
	# 当前系统可以使用的总内存
	FileTotalMemoryMax = 4000000
	# 当前程序文件的后缀名 字符串
	FileNamePostfix = '.txt'
	# 当前文件名和行号发生改变的标志位 True表示发生改变但未发生显示改变 False表示显示修改完毕或是未发生修改 默认为False
	FileNameOrLineChangeFlag = False
	# 当前打开程序文件的名称 不带后缀名 默认O0001
	FileName = 'O0001'
	# 当前光标指针在显示程序文件的行号 N + 五位数字 默认 00000 特指行号
	FileLineNum = 'N00000'
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
	# CNC控制面板的输入键值表 此处键值均采用英文字符 双字典
	CNCDataKeysList = { False: { 'Btn_O': 'O', 'Btn_N': 'N', 'Btn_G': 'G', 'Btn_P': 'P', 'Btn_X': 'X', 'Btn_Y': 'Y',
	                             'Btn_Z': 'Z', 'Btn_Q': 'Q', 'Btn_I': 'I', 'Btn_J': 'J', 'Btn_K': 'K', 'Btn_R': 'R',
	                             'Btn_M': 'M', 'Btn_S': 'S', 'Btn_T': 'T', 'Btn_L': 'L', 'Btn_F': 'F', 'Btn_D': 'D',
	                             'Btn_H': 'H', 'Btn_B': 'B', 'Btn_0': '0', 'Btn_1': '1', 'Btn_2': '2', 'Btn_3': '3',
	                             'Btn_4': '4', 'Btn_5': '5', 'Btn_6': '6', 'Btn_7': '7', 'Btn_8': '8', 'Btn_9': '9',
	                             'Btn_Minus': '-', 'Btn_Dot': '.', 'Btn_Slash': '/', 'Btn_EOB': ';', 'Btn_CAN': 'CAN',
	                             'Btn_ALTER': 'ALTER', 'Btn_INSERT': 'INSERT', 'Btn_DELETE': 'DELETE', 'Btn_INPUT': 'INPUT' },
	                    True: { 'Btn_O': '(', 'Btn_N': ')', 'Btn_G': 'E', 'Btn_P': 'C', 'Btn_X': 'U', 'Btn_Y': 'V',
	                            'Btn_Z': 'W', 'Btn_Q': '?', 'Btn_I': ',', 'Btn_J': 'A', 'Btn_K': '@', 'Btn_R': 'R',
	                            'Btn_M': '#', 'Btn_S': '=', 'Btn_T': '*', 'Btn_L': '+', 'Btn_F': '[', 'Btn_D': ']',
	                            'Btn_H': '&', 'Btn_B': ' ', 'Btn_0': '0', 'Btn_1': '1', 'Btn_2': '2', 'Btn_3': '3',
	                            'Btn_4': '4', 'Btn_5': '5', 'Btn_6': '6', 'Btn_7': '7', 'Btn_8': '8', 'Btn_9': '9',
	                            'Btn_Minus': '-', 'Btn_Dot': '.', 'Btn_Slash': '/', 'Btn_EOB': ';', 'Btn_CAN': 'CAN',
	                            'Btn_ALTER': 'ALTER', 'Btn_INSERT': 'INSERT', 'Btn_DELETE': 'DELETE', 'Btn_INPUT': 'INPUT' } }
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
	# CNC的CRT界面显示分支 为了简化程序 当切换完全不同的界面时将放弃原界面未保存的修改 指的是CRT界面完全变化 其值为POS、PROG、PROG_Program、Message
	CNCCRTState = 'POS'
	# CRT界面的数量 默认为0 即无界面 但是其值最大为1
	CRTWindowNum = 0
	# CNC的CRT界面软按键信息
	SoftButtonTempInfo = { 'Btn_One': '', 'Btn_Two': '', 'Btn_Three': '', 'Btn_Four': '', 'Btn_Five': '',
	                       'Btn_Six': '', 'Btn_Seven': '', 'Btn_Eight': '', 'Btn_Nine': '', 'Btn_Ten': '' }
	# CRT软按键当前按下的按键 默认没有按下的
	SoftBtnCheckedInfo = { 'Btn_One': False, 'Btn_Two': False, 'Btn_Three': False, 'Btn_Four': False, 'Btn_Five': False,
	                       'Btn_Six': False, 'Btn_Seven': False, 'Btn_Eight': False, 'Btn_Nine': False, 'Btn_Ten': False }
	# CRT软按键的按下造成的界面分支 主要指的是坐标的界面显示 其值为绝对、相对、综合
	CRTPageState = ''
	# CRT软按键本身的状态分支 用于back go的软按键的翻页操作 默认空白
	CRTSoftBtnMenu = ''
	# CNC的绝对坐标位置
	CNCPosAbs = { 'X': 1.000, 'Y': 2.000, 'Z': 3.000 }
	# CNC的相对坐标位置
	CNCPosRelative = { 'X': 4.000, 'Y': 5.000, 'Z': 6.000 }
	# CNC的机械坐标位置
	CNCPosMechanical = { 'X': 7.000, 'Y': 8.000, 'Z': 9.000 }
	# CNC报警信息显示 默认False 即无报警信息
	CNCALMState = False
	# 报警信息存储
	CNCAlarmMessage = ''
	CNCMSGMessage = ''
	CNCHistoryMessage = ''
	# CNC在编辑模式下 单行输入文本框的内容临时存储在此处 字符格式
	CRTTemporaryInputData = '123456'

	def __init__(self, parent, Pane, *args, **kwargs):
		super().__init__(parent, *args, **kwargs)
		# InterfaceFrameworkPane
		self.InterfacePane = Pane
		pass

	# 在上电前将控制面板固定按钮 如急停按钮，模式选择，主轴、进给倍率
	def PowerOffInit(self, Pane):
		"""	PowerOffInit(self, InterfaceFrameworkPane)-> None """
		# 初始化程序文件
		self.FileListInit()
		# 设置急停按钮
		Pane.Btn_Emergency_STOP.blockSignals(True)
		Pane.Btn_Emergency_STOP.setChecked(self.CNCEmergencySTOP)
		Pane.Btn_Emergency_STOP.blockSignals(False)
		# 设置模式值 根据默认的模式推断字典相应的键然后设置
		value = list(self.CNCModeAll.keys())[ list(self.CNCModeAll.values()).index(self.CNCNowMode) ]
		Pane.Btn_Mode.blockSignals(True)
		Pane.Btn_Mode.setValue(value)
		Pane.Btn_Mode.blockSignals(False)
		# 设置进给倍率和主轴倍率
		value = list(self.CNCFeedSpeedAll.keys())[ list(self.CNCFeedSpeedAll.values()).index(self.CNCFeedSpeed) ]
		Pane.Btn_Speed.blockSignals(True)
		Pane.Btn_Speed.setValue(value)
		Pane.Btn_Speed.blockSignals(False)
		value = list(self.CNCSpindleSpeedAll.keys())[ list(self.CNCSpindleSpeedAll.values()).index(self.CNCSpindleSpeed) ]
		Pane.Btn_Spindle_Speed.blockSignals(True)
		Pane.Btn_Spindle_Speed.setValue(value)
		Pane.Btn_Spindle_Speed.blockSignals(False)

		Pane.Btn_SHIFT.blockSignals(True)
		Pane.Btn_SHIFT.setChecked(self.CNCShiftState)
		Pane.Btn_SHIFT.blockSignals(False)

		Pane.Btn_RAPID.blockSignals(True)
		Pane.Btn_RAPID.setChecked(self.CNCRAPIDState)
		Pane.Btn_RAPID.blockSignals(False)

		Pane.Btn_COOL.blockSignals(True)
		Pane.Btn_COOL.setChecked(self.CNCCOOLState)
		Pane.Btn_COOL.blockSignals(False)

		Pane.Btn_DRIVE.blockSignals(True)
		Pane.Btn_DRIVE.setChecked(self.CNCDRIVEState)
		Pane.Btn_DRIVE.blockSignals(False)

		Pane.Btn_PROTECT.blockSignals(True)
		Pane.Btn_PROTECT.setChecked(self.CNCPROTECTState)
		Pane.Btn_PROTECT.blockSignals(False)

		Pane.Btn_DRN.blockSignals(True)
		Pane.Btn_DRN.setChecked(self.CNCDRNState)
		Pane.Btn_DRN.blockSignals(False)

		Pane.Btn_MSTLOCK.blockSignals(True)
		Pane.Btn_MSTLOCK.setChecked(self.CNCMSTLOCKState)
		Pane.Btn_MSTLOCK.blockSignals(False)

		Pane.Btn_SBK.blockSignals(True)
		Pane.Btn_SBK.setChecked(self.CNCSBKState)
		Pane.Btn_SBK.blockSignals(False)

		Pane.Btn_SKIP.blockSignals(True)
		Pane.Btn_SKIP.setChecked(self.CNCSKIPState)
		Pane.Btn_SKIP.blockSignals(False)

		Pane.Btn_M01.blockSignals(True)
		Pane.Btn_M01.setChecked(self.CNCM01State)
		Pane.Btn_M01.blockSignals(False)
		pass

	# 文件列表初始化
	def FileListInit(self):
		# 获取对应路径下的文件列表
		self.FileNameList = os.listdir(self.FilePath)
		# 获取对应文件的大小
		for i in self.FileNameList:
			# self.FileSizeDict[ i ] = round(os.path.getsize(self.FilePath + i) / float(1024), 2)  # 文件大小单位为KB
			self.FileSizeDict[ i ] = os.path.getsize(self.FilePath + i)  # 文件大小单位为char
			self.FileUpdateTime[ i ] = time.strftime('%Y/%m/%d %H:%M', time.localtime(os.path.getmtime(self.FilePath + i)))
			self.FileTotalNum += 1
			self.FileTotalMemoryUsed += self.FileSizeDict[ i ]
			pass
		print(self.FileSizeDict)
		print(self.FileUpdateTime)
		print(self.FileTotalNum)
		print(self.FileTotalMemoryUsed)
		# print(self.FileNameList[ 0 ])
		pass

	# 在上电后将控制面板的部分按键初始化
	def PowerOnInit(self, Pane):
		# 设置主轴停止按钮按下
		Pane.Btn_STOP.setChecked(True)
		pass

	# control角色类处理,并发送信号
	def CNCDataControl(self, *args):
		Data = args
		# 电源状态处理
		if Data[ 1 ] == 'Btn_Power_ON':
			self.CNCPowerState = True
			self.CRTPageState = '绝对'
			self.CNCPowerSignal.emit(self.CNCPowerState, self)
		if Data[ 1 ] == 'Btn_Power_OFF':
			self.CNCPowerState = False
			self.CNCCRTState = 'POS'
			self.CNCPowerSignal.emit(self.CNCPowerState, self)
		# 急停按钮处理
		if Data[ 1 ] == 'Btn_Emergency_STOP':
			self.CNCEmergencySTOP = Data[ 2 ]
			if self.CNCCRTState == 'Message' or not self.CNCEmergencySTOP:  # 界面没有发生变化
				self.DataStateDone.emit(True)
			else:
				self.CNCCRTState = 'Message'
				self.CNCCRTChangeSignal.emit('Message')
			self.CNCEmergencySTOPSignal.emit(Data[ 2 ])
		# 模式选择处理
		if Data[ 1 ] == 'Btn_Mode':
			self.CNCNowMode = self.CNCModeAll[ Data[ 2 ] ]
			if self.CNCNowMode == 'INC':
				self.CNCINCSpeed = self.CNCINCSpeedAll[ Data[ 2 ] ]
			else:
				self.CNCINCSpeed = '0'
			self.CNCModeChangeSignal.emit(self.CNCNowMode)
		# 进给倍率处理
		if Data[ 1 ] == 'Btn_Speed':
			self.CNCFeedSpeed = self.CNCFeedSpeedAll[ Data[ 2 ] ]
			self.CNCFeedSpeedSignal.emit(self.CNCFeedSpeed)
		# 主轴倍率处理
		if Data[ 1 ] == 'Btn_Spindle_Speed':
			self.CNCSpindleSpeed = self.CNCSpindleSpeedAll[ Data[ 2 ] ]
			self.CNCSpindleSpeedSignal.emit(self.CNCSpindleSpeed)
		# 帮助信息显示
		if Data[ 1 ] == 'Btn_HELP':
			self.DataStateDone.emit(True)
		# 复位键按下
		if Data[ 1 ] == 'Btn_Reset' or Data[ 1 ] == 'Btn_RESET':
			self.DataStateDone.emit(True)
		# 数据锁操作
		if Data[ 1 ] == 'Btn_PROTECT':
			self.CNCPROTECTState = Data[ 2 ]
			self.DataStateDone.emit(True)
		pass

	# view角色类按键处理，并发送信号
	def CNCDataView(self, *args):
		# 切换至坐标显示界面
		if args[ 1 ] == 'Btn_POS':
			if self.CNCCRTState == 'POS':  # 界面没有发生变化
				self.DataStateDone.emit(True)
			else:
				self.CNCCRTState = 'POS'
				self.CNCCRTChangeSignal.emit('POS')
		# 切换至程式显示界面
		if args[ 1 ] == 'Btn_PROG':
			if self.CNCCRTState == 'PROG':  # 界面没有发生变化
				self.DataStateDone.emit(True)
			else:
				self.CNCCRTState = 'PROG'
				self.CNCCRTChangeSignal.emit('PROG')
		# 切换至信息显示界面 Message
		if args[ 1 ] == 'Btn_MESSAGE':
			if self.CNCCRTState == 'Message':  # 界面没有发生变化
				self.DataStateDone.emit(True)
			else:
				self.CNCCRTState = 'Message'
				self.CNCCRTChangeSignal.emit('Message')
		# 切换至参数设置界面 Parameter 该界面为参数设置基础界面 显示刀补参数
		if args[ 1 ] == 'Btn_SETTING':
			if self.CNCCRTState == 'Parameter':  # 界面没有发生变化
				self.DataStateDone.emit(True)
			else:
				self.CNCCRTState = 'Parameter'
				self.CNCCRTChangeSignal.emit('Parameter')
		# 切换至系统信息界面 System
		if args[ 1 ] == 'Btn_SYSTEM':
			# 不进行任何处理
			self.DataStateDone.emit(True)
		# 切换至 Graph 界面
		if args[ 1 ] == 'Btn_GRAPH':
			# 不进行处理
			self.DataStateDone.emit(True)
		# 按下了上下左右键 光标移动操作
		if args[ 1 ] == 'Btn_UP' or args[ 1 ] == 'Btn_LEFT' or args[ 1 ] == 'Btn_RIGHT' or args[ 1 ] == 'Btn_DOWN':
			self.CNCCursorMoveSignal.emit(args[ 1 ])
		# 按下了翻页键 翻页操作
		if args[ 1 ] == 'Btn_PAGE_UP' or args[ 1 ] == 'Btn_PAGE_DOWN':
			self.CNCPageChangeSignal.emit(args[ 1 ])
		pass

	# position back go 角色类软按键处理 多用于CRT本身界面切换，并发送信号 role name
	def CNCDataPosition(self, *args):
		if self.CNCCRTState == 'POS':
			if args[ 1 ] != 'Btn_BACK' and args[ 1 ] != 'Btn_GO':
				value = self.SoftButtonTempInfo[ args[ 1 ] ]
				if value == '绝对' or value == '相对' or value == '综合':
					self.CRTPageState = value
				self.CRTSoftBtnSignal.emit(args[ 1 ], value)
			else:
				self.CRTSoftBtnSignal.emit(args[ 0 ], args[ 1 ])
		if self.CNCCRTState == 'PROG':
			if args[ 1 ] != 'Btn_BACK' and args[ 1 ] != 'Btn_GO':
				value = self.SoftButtonTempInfo[ args[ 1 ] ]
				if value == '程序':
					self.CNCCRTState = 'PROG_Program'
					self.CNCCRTChangeSignal.emit('PROG_Program')
					return None  # 发送界面改变信号 不能视为单纯的软按键处理 应当截断信号传输
				if value == 'DIR':
					self.CNCCRTState = 'PROG_DIR'
					self.CNCCRTChangeSignal.emit('PROG_DIR')
					return None  # 发送界面改变信号 不能视为单纯的软按键处理 应当截断信号传输
				if value == '绝对' or value == '相对' or value == '综合':
					self.CRTPageState = value
				self.CRTSoftBtnSignal.emit(args[ 1 ], value)
			else:
				self.CRTSoftBtnSignal.emit(args[ 0 ], args[ 1 ])
		if self.CNCCRTState == 'PROG_DIR':
			if args[ 1 ] != 'Btn_BACK' and args[ 1 ] != 'Btn_GO':
				value = self.SoftButtonTempInfo[ args[ 1 ] ]
				if value == '程序':
					self.CNCCRTState = 'PROG'
					self.CNCCRTChangeSignal.emit('PROG')
					return None
				self.CRTSoftBtnSignal.emit(args[ 1 ], value)
			else:
				self.CRTSoftBtnSignal.emit(args[ 0 ], args[ 1 ])
		if self.CNCCRTState == 'PROG_Program':
			if args[ 1 ] != 'Btn_BACK' and args[ 1 ] != 'Btn_GO':
				value = self.SoftButtonTempInfo[ args[ 1 ] ]
				if value == '程序':
					self.CNCCRTState = 'PROG'
					self.CNCCRTChangeSignal.emit('PROG')
					return None  # 发送界面改变信号 不能视为单纯的软按键处理 应当截断信号传输
				self.CRTSoftBtnSignal.emit(args[ 1 ], value)
			else:
				self.CRTSoftBtnSignal.emit(args[ 0 ], args[ 1 ])
		if self.CNCCRTState == 'Message':
			if args[ 1 ] != 'Btn_BACK' and args[ 1 ] != 'Btn_GO':
				value = self.SoftButtonTempInfo[ args[ 1 ] ]
				if value == '绝对' or value == '相对' or value == '综合':
					self.CRTPageState = value
				self.CRTSoftBtnSignal.emit(args[ 1 ], value)
			else:
				self.CRTSoftBtnSignal.emit(args[ 0 ], args[ 1 ])
		pass

	# input 角色类按键处理 多是编辑、输入、修改之类的操作，并发送信号
	def CNCDataInput(self, *args):
		if args[ 1 ] == 'Btn_SHIFT':
			self.CNCShiftState = args[ 2 ]
			print('shift状态', self.CNCShiftState)
			self.DataStateDone.emit(True)
		else:
			value = self.CNCDataKeysList[ self.CNCShiftState ][ args[ 1 ] ]
			if not self.CNCPROTECTState:
				if self.CNCNowMode == 'EDIT' or self.CNCCRTState == 'Parameter':
					# 程序编辑处理
					print('当前输入键值：', value)
					self.CNCInputSignal.emit(value)
				else:
					QMessageBox.warning(None, 'CNC提醒', '当前模式不可编辑，请打开到EDIT模式', QMessageBox.Yes | QMessageBox.No)
			else:
				QMessageBox.warning(None, 'CNC提醒', '程序保护已经打开!', QMessageBox.Yes | QMessageBox.No)  # 阻塞运行，结束自动杀死
			self.DataStateDone.emit(True)
		pass

	# axis 角色类按键的处理 为轴选信号
	def CNCDataAxis(self, *args):
		if self.CNCNowMode == 'REF' or self.CNCNowMode == 'JOG' or self.CNCNowMode == 'INC':
			if args[ 1 ] == 'Btn_X_Positive':
				self.CNCAxisXPState = args[ 2 ]
			if args[ 1 ] == 'Btn_X_Negative':
				self.CNCAxisXNState = args[ 2 ]
			if args[ 1 ] == 'Btn_Y_Positive':
				self.CNCAxisYPState = args[ 2 ]
			if args[ 1 ] == 'Btn_Y_Negative':
				self.CNCAxisYNState = args[ 2 ]
			if args[ 1 ] == 'Btn_Z_Positive':
				self.CNCAxisZPState = args[ 2 ]
			if args[ 1 ] == 'Btn_Z_Negative':
				self.CNCAxisZNState = args[ 2 ]
			if args[ 1 ] == 'Btn_A_Positive':
				self.CNCAxisAPState = args[ 2 ]
			if args[ 1 ] == 'Btn_A_Negative':
				self.CNCAxisANState = args[ 2 ]
			self.CNCAxisSignal.emit(args[ 1 ], args[ 2 ])
		self.DataStateDone.emit(True)
		pass

	# 该函数负责将传递的参数修改到CNCData类中 如果电源未开 所有信号均不处理
	def CNCDataProcess(self, *args):
		Data = args
		if self.CNCPowerState:
			# 先分角色处理 先处理 control 之后处理 view 再处理position back go 最后处理input角色
			if Data[ 0 ] == 'control':
				self.CNCDataControl(*args)
			if Data[ 0 ] == 'view':
				self.CNCDataView(*args)
			if Data[ 0 ] == 'back' or Data[ 0 ] == 'go' or Data[ 0 ] == 'position':
				self.CNCDataPosition(*args)
			if Data[ 0 ] == 'input':
				self.CNCDataInput(*args)
			if Data[ 0 ] == 'axis':
				self.CNCDataAxis(*args)
		elif Data[ 1 ] == 'Btn_Power_ON':
			# 先分角色处理 先处理 control 之后处理 view 再处理position back go 最后处理input角色
			if Data[ 0 ] == 'control':
				self.CNCDataControl(*args)
			if Data[ 0 ] == 'view':
				self.CNCDataView(*args)
			if Data[ 0 ] == 'back' or Data[ 0 ] == 'go' or Data[ 0 ] == 'position':
				self.CNCDataPosition(*args)
			if Data[ 0 ] == 'input':
				self.CNCDataInput(*args)
			if Data[ 0 ] == 'axis':
				self.CNCDataAxis(*args)
		else:
			if Data[ 1 ] == 'Btn_Emergency_STOP':
				self.CNCEmergencySTOP = Data[ 2 ]
			self.DataStateDone.emit(True)
		pass

	# 接受信号传递过来的参数
	def CNCDataSignalAcceptSlot(self, *args):
		# DataAccept = args
		print(args)
		self.CNCDataProcess(*args)
		pass

	def SignalConnectCNCProcess(self, CNCProcess):
		self.CNCPowerSignal.connect(CNCProcess.CNCPowerProcessSlot)
		self.CRTSoftBtnSignal.connect(CNCProcess.CRTSoftBtnProcessSlot)
		self.CNCEmergencySTOPSignal.connect(CNCProcess.EmergencySTOPSlot)
		self.CNCModeChangeSignal.connect(CNCProcess.CNCModeChangeSlot)
		self.CNCFeedSpeedSignal.connect(CNCProcess.CNCFeedSpeedSlot)
		self.CNCSpindleSpeedSignal.connect(CNCProcess.CNCSpindleSpeedSlot)
		self.CNCAxisSignal.connect(CNCProcess.CNCAxisSlot)
		self.CNCCRTChangeSignal.connect(CNCProcess.CNCCRTChangeSlot)
		self.CNCInputSignal.connect(CNCProcess.CNCInputSlot)
		self.CNCCursorMoveSignal.connect(CNCProcess.CNCCRTCursorMoveSlot)
		self.CNCPageChangeSignal.connect(CNCProcess.CNCCRTPageChangeSlot)
		pass

	def SignalConnectCNCPane(self, CNCPane):
		self.DataStateDone.connect(CNCPane.InfoTransStateSlot)
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
