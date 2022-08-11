import serial #导入模块
import time
import string
import binascii
# import matplotlib.pyplot as plt
import numpy as np
from math import *

try:
  portx="COM25"
  bps=9600
  #超时设置,None：永远等待操作，0为立即返回请求结果，其他值为等待超时时间(单位为秒）
  timex=None
  ser1=serial.Serial(portx,bps,timeout=timex)
  print("串口详情参数：", ser1)
  open1 = ('#01P0500!,\r\n')  # 1号舵机开
  close1= ('#01P1400!,\r\n')  # 1号舵机横扫
  close2 = ('#00P1440!,\r\n')  # 1号舵机关
  open2 = ('#00P1200!,\r\n')  # 2号舵机开
  duoji = ['#00P1500!']
  str1 = ('#00P1500!,\r\n')
  jidianqi = [0xA0,0x01,0x01,0xA2]
  # ser1.write(str1.encode('utf-8'))

  D1open = [0x55, 0x55, 0x08, 0x03, 0x01, 0xC8, 0x00, 0x00, 0xEC, 0x04]
  D1close = [0x55, 0x55, 0x08, 0x03, 0x01, 0xC8, 0x00, 0x00, 0xE0, 0x03]
  D2right = [0x55, 0x55, 0x08, 0x03, 0x01, 0x01, 0x00, 0x07, 0xF6, 0x03]
  D2middle = [0x55, 0x55, 0x08, 0x03, 0x01, 0x01, 0x00, 0x07, 0xEE, 0x02]
  D2left = [0x55, 0x55, 0x08, 0x03, 0x01, 0x01, 0x00, 0x07, 0xF6, 0x01]
  D3right = [0x55, 0x55, 0x08, 0x03, 0x01, 0xF4, 0x01, 0x04, 0x40, 0x06]
  D3left = [0x55, 0x55, 0x08, 0x03, 0x01, 0xF4, 0x01, 0x04, 0xB0, 0x04]
  D3middle = [0x55, 0x55, 0x08, 0x03, 0x01, 0xF4, 0x01, 0x04, 0xD4, 0x04]
  # # [0x01, 0x06, 0x00, 0x0d, 0x00, 0x01, 0xd9, 0xc9]
  # ser1.write(open1.encode('utf-8'))  # 写数据
  # exp_val=15
  # while True:
  ser1.write(D3middle)
  time.sleep(0.1)
  ser1.write(D2middle)
  time.sleep(0.1)
  ser1.write(D1close)
  time.sleep(1)
  ser1.write(D1open)  # 写数据
  # time.sleep(1)
  # ser1.write(D1close)  # 写数据
  time.sleep(6)
  # ser1.write(D2right)  # 写数据
  # time.sleep(1)
  for i in range(10):
      ser1.write(D2right)  # 写数据
      time.sleep(1)
      ser1.write(D2middle)
      time.sleep(4)
  ser1.write(D2right)  # 写数据
  time.sleep(5)
  ser1.write(D2left)
  time.sleep(0.5)
  ser1.write(D2right)
  time.sleep(1)
  ser1.write(D3right)
  time.sleep(10)
  ser1.write(D3left)
  time.sleep(1)
  ser1.write(D3middle)
  time.sleep(0.1)
  ser1.write(D2middle)
  time.sleep(0.1)
  ser1.write(D1close)
except:
  print(1)