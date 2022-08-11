from PyQt5 import QtWidgets,  QtCore, QtGui,QtPrintSupport
from PyQt5.QtWidgets import QMessageBox
import time
import openpyxl
import datetime
from Main_Face import Ui_MainWindow
import PythonDLL3X as device
import serial
import sys
import os
import numpy as np
import binascii
sys.path.append('../')
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *



class EventMessageBox(QtWidgets.QMessageBox):
    def __init__(self, timeout=3, parent=None, msg="", event=None, param=None):
        super(EventMessageBox, self).__init__(parent)
        self.setWindowTitle("Scanning…………")
        self.setStandardButtons(QtWidgets.QMessageBox.NoButton)

    def closeEvent(self, event):
        event.accept()

class EventMessageBox2(QtWidgets.QMessageBox):
    def __init__(self, timeout=3, parent=None, msg="", event=None, param=None):
        super(EventMessageBox2, self).__init__(parent)
        # self.critical(self, "错误", "有害垃圾已满")
        self.setWindowTitle("程序正在运行")
        self.setStandardButtons(QtWidgets.QMessageBox.NoButton)

    def closeEvent(self, event):
        event.accept()



def createFolder(directory):
    try:
        path=r'D:/Pukon/'
        if not os.path.exists(directory):
           os.makedirs(path+directory,exist_ok=True)
    except OSError:
        print('Error: Creating directory. ' + directory)


class MainUI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.device = device.Device()
        self.setupUi(self)
        # self.showMaximized()
        self.init_ui()
        self.contrl_com_enable = 0
        self.moto_com_enable = 0
        self.density_com_enable = 0
        self.COM_Moto = str(self.comboBox_Moto_COM.currentText())
        self.comboBox_Moto_COM_indexChange()
        self.comboBox_density_COM()
        # self.COM_duoji()
        # self.COM_jidainqi()
        self.connectionTimer = QtCore.QTimer()
        self.connectionTimer.setInterval(2000)
        self.connectionTimer.timeout.connect(self._timeout)
        #self.connectionTimer.start()
        self.time_cnt = 0
        self.effective_cnt = 0
        self.message = EventMessageBox()
        self.message2 = EventMessageBox2()
        self.Intensities = [0.0] * 1595
        self.Intensities = np.array(self.Intensities)
        '''
        self.ScanTimer = QtCore.QTimer()
        self.ScanTimer.setInterval(5000)
        self.ScanTimer.timeout.connect(self.pushButton_scan_one)
        self.ScanTimer.start()
        '''

    def create_Folter(self):                  #创建文件目录
        createFolder("Pukon")
        folder_name = "Pukon_" + str("谷物预处理吸收光谱")
        createFolder(folder_name)
        folder_name = "Pukon_" + str("谷物透射光谱")
        createFolder(folder_name)
        createFolder("Pukon_" + str("谷物原始吸收光谱"))
        createFolder("Beijing")
        createFolder("测试文件")
        createFolder("Zhijian")
        # for i in range(0, len(self.device.LoadConfig.Pre_Function)):
        #     if self.device.LoadConfig.Pre_Function[i] != '':
        #         folder_name = "Pukon_" + str(self.device.LoadConfig.Pre_Function[i])
        #         createFolder(folder_name)

    def init_ui(self):
        self.setWindowTitle("中科谱康 小麦质检仪 API   V1.0.0")
        self.pushButton_Stop.clicked.connect(self.Button_Stop)
        self.pushButton_press.clicked.connect(self.print)
        self.pushButton_Start.clicked.connect(self.Button_Start)
        self.pushButton_breakdown.clicked.connect(self.breakdown)
        self.pushButton_updata.clicked.connect(self.Quality_dataupload)
        self.comboBox_Moto_COM.currentIndexChanged.connect(self.comboBox_Moto_COM_indexChange)
        #Initialize
        # time.sleep(1)
        self.SetUiInfo()
        self.create_Folter()

    def SetUiInfo(self):
        if self.device.IsConnected():
            # self.label_connected.setText('Connected!')
            self.label_connected.setStyleSheet(
                "min-width:20px;min-height:20px;max-width:20px;max-height:20px;border-radius:10px;border:1px solid black;background:green")
        else:
            # self.label_connected.setText('No Connected!')
            self.label_connected.setStyleSheet(
                "min-width:20px;min-height:20px;max-width:20px;max-height:20px;border-radius:10px;border:1px solid black;background:red")
            return

    def comboBox_Control_COM_indexChange(self):
        if(self.contrl_com_enable == 1):
            self.contrl_com.close()
        try:
            self.COM_ControlBoard = self.comboBox_Control_COM.currentText()
            self.contrl_com = serial.Serial(self.COM_ControlBoard, 9600, timeout=1)
            self.label_COM_connected.setText(' ')
            self.contrl_com_enable = 1
        except:
            self.contrl_com_enable = 0
            self.label_COM_connected.setText('串口打开失败!')

    def Contrl_Communication(self, data):
        if(self.contrl_com_enable == 1):
            self.contrl_com.write(data.encode())
            print(data)
            self.label_COM_connected.setText(' ')
            try:
                receive_frame = self.contrl_com.read(5)
                if receive_frame == b'WOK\r\n':
                    print(type(receive_frame))
                    print(receive_frame)
                else:
                    QMessageBox.information(self,  "提示", "数据接收错误！")
            except:
                print('error')
            '''
            byte_number_1 = 0
            tmp_cnt = 0
            while True:
                byte_number_1 = self.contrl_com.inWaiting()
                print(byte_number_1)
                time.sleep(1)
                tmp_cnt += 1
                if tmp_cnt == 10:
                    tmp_cnt = 0
                    break
                if byte_number_1 != 0:
                    receive_frame = self.contrl_com.readline()
                    print(receive_frame)
            '''
        else:
            self.label_COM_connected.setText('串口打开失败!')

    def comboBox_Moto_COM_indexChange(self):
        if(self.moto_com_enable == 1):
            self.moto_com.close()
        try:
            self.COM_Moto = self.comboBox_Moto_COM.currentText()
            self.moto_com = serial.Serial(self.COM_Moto, 9600)
            self.label_COM2_connected.setText(' ')
            self.moto_com_enable = 1
            self.D1close = [0x55, 0x55, 0x08, 0x03, 0x01, 0xC8, 0x00, 0x00, 0xE0, 0x03]
            self.D2middle = [0x55, 0x55, 0x08, 0x03, 0x01, 0x01, 0x00, 0x07, 0xEE, 0x02]
            self.D3middle = [0x55, 0x55, 0x08, 0x03, 0x01, 0xF4, 0x01, 0x04, 0xD4, 0x04]
            self.moto_com.write(self.D3middle)
            time.sleep(0.1)
            self.moto_com.write(self.D2middle)
            time.sleep(0.1)
            self.moto_com.write(self.D1close)
        except:
            self.moto_com_enable = 0
            self.label_COM2_connected.setText('串口打开失败!')

    def MOTO_Communication(self, data):
        if(self.moto_com_enable == 1):
            self.moto_com.write(data)
            self.label_COM2_connected.setText(' ')
        else:
            self.label_COM2_connected.setText('串口打开失败!')

    def comboBox_density_COM(self):      #称重仪
        if(self.density_com_enable == 1):
            self.density_com.close()
        try:
            # self.COM_Moto = self.comboBox_Moto_COM.currentText()
            self.density_com = serial.Serial('com29', 9600)
            self.label_density_com.setText(' ')
            self.density_com_enable = 1
        except:
            self.density_com_enable = 0
            self.label_density_com.setText('未连接!')

    def density_com_Communication(self, data):
        if(self.density_com_enable == 1):
            self.density_com.write(data)
            data = str(binascii.b2a_hex(self.density_com.read(10)))[12:16]
            self.density_receive = (int(data, 16))/ 0.71
            self.density_receive=str(self.density_receive)
            self.lineEdit_density.setText(self.density_receive)
            print(self.density_receive)
            self.label_density_com.setText(' ')
        else:
            self.label_density_com.setText('串口打开失败!')

    def COM_duoji(self):      #舵机
        try:
            self.duoji = serial.Serial('com2', 9600)
        except:
            print('舵机未连接')
            # self.density_com_enable = 0
            # self.label_density_com.setText('未连接!')

    def _timeout(self):
        self.message2.show()
        # 指令
        if self.time_cnt == 0:
            self.current = str(datetime.datetime.now().replace(microsecond=0))
            self.current = self.current.replace(':', '-')
            self.background_intensity = self.Button_Beijing()
            self.D1open = [0x55, 0x55, 0x08, 0x03, 0x01, 0xC8, 0x00, 0x00, 0x46, 0x05]
            self.D1close = [0x55, 0x55, 0x08, 0x03, 0x01, 0xC8, 0x00, 0x00, 0xE0, 0x03]
            self.D2right = [0x55, 0x55, 0x08, 0x03, 0x01, 0x01, 0x00, 0x07, 0xF6, 0x03]
            self.D2middle = [0x55, 0x55, 0x08, 0x03, 0x01, 0x01, 0x00, 0x07, 0xEE, 0x02]
            self.D2left = [0x55, 0x55, 0x08, 0x03, 0x01, 0x01, 0x00, 0x07, 0xF6, 0x01]
            self.D3right = [0x55, 0x55, 0x08, 0x03, 0x01, 0xF4, 0x01, 0x04, 0x40, 0x06]
            self.D3left = [0x55, 0x55, 0x08, 0x03, 0x01, 0xF4, 0x01, 0x04, 0xB0, 0x04]
            self.D3middle = [0x55, 0x55, 0x08, 0x03, 0x01, 0xF4, 0x01, 0x04, 0xD4, 0x04]
            self.moto_start = [0x01, 0x06, 0x00, 0x0d, 0x00, 0x01, 0xd9, 0xc9]
            self.density = bytes.fromhex('AA AA AA 01 B1 00 00 1A')  # 称重
            self.density_calibration = bytes.fromhex('AA AA AA 01 A7 00 00 0C')  # 称重校准
            self.MOTO_Communication(self.D1open)  # 写数据
            time.sleep(4)
            self.IntergrationTime_Grain = 1000
            self.Intensities_x = self.device.GetIntensity_Grain(self.IntergrationTime_Grain)      #计算最高点积分时间
            self.IntergrationTime_Grain = int(40000/max(self.Intensities_x))
            print(self.IntergrationTime_Grain)
            # print(self.Intensities_max)
            self.density_com_Communication(self.density_calibration)

        self.Intensities_temp = self.device.GetIntensity_Grain(self.IntergrationTime_Grain)
        Intensities_MAX = max(self.Intensities_temp) * int(self.IntergrationTime_Grain)
        print(Intensities_MAX)
        if Intensities_MAX < 60000:
            self.effective_cnt += 1
            self.Save_ceshiExcel(("D:/Pukon/" + "测试文件/" + self.current +"-"+ str(self.effective_cnt) + ".xlsx"),self.Intensities_temp)
            self.Intensities_temp = np.array(self.Intensities_temp)
            print(self.effective_cnt)
            self.Intensities += self.Intensities_temp
        self.MOTO_Communication(self.D2right)  # 写数据
        time.sleep(1)
        self.MOTO_Communication(self.D2middle)
        time.sleep(self.device.LoadConfig.LoopTime)
        self.SetUiInfo()
        self.time_cnt += 1
        # time.sleep(1)
        if self.time_cnt == 10:
            self.Intensities_Sum = self.Intensities.tolist()
            self.Intensities = self.Intensities / self.effective_cnt
            print(self.effective_cnt)
            self.device.WriteDataToExcl(self.Intensities,self.background_intensity,self.current)
            self.Intensities = [0.0] * 1595
            self.Intensities = np.array(self.Intensities)
            self.MOTO_Communication(self.D2right)  # 写数据
            time.sleep(2)
            self.MOTO_Communication(self.D2left)
            time.sleep(0.5)
            self.MOTO_Communication(self.D2right)
            time.sleep(0.5)
            self.density_com_Communication(self.density)
            time.sleep(0.5)
            self.MOTO_Communication(self.D3right)
            time.sleep(10)
            self.MOTO_Communication(self.D3left)
            time.sleep(1)
            self.MOTO_Communication(self.D3middle)
            time.sleep(0.1)
            self.MOTO_Communication(self.D2middle)
            time.sleep(0.1)
            self.MOTO_Communication(self.D1close)
            self.time_cnt = 0
            self.effective_cnt = 0
            self.message2.done(1)
            self.Water = str(12.2)
            self.lineEdit_number.setText("1")
            self.lineEdit_density.setText("710g")
            self.lineEdit_Statue.setText("26.7%")
            self.lineEdit_Water.setText("12.2%")

            self.lineEdit_hardness.setText("5.1")
            self.lineEdit_gluten.setText("22.2")
            self.lineEdit_protein.setText("14.3")
            self.Quality_dataupload(self.Water)
            # self.density_com_Communication(self.density)
            # self.device.SaveJiancezhi(re.split('[:|\n]', self.editor.toPlainText()))
            self.connectionTimer.stop()
            # for i in range(4):
            #     self.MOTO_Communication(self.moto_start)
            #     self.message2.show()
            #     time.sleep(3)
            # self.message2.done(1)
            # time.sleep(1)
    def Save_ceshiExcel(self, excel_name, indesity_data):
        wb = openpyxl.Workbook()
        Work_Excel = wb.active
        self.WaveLenth = self.device.GetLambda()
        for j in range(0, len(self.WaveLenth)):
            Work_Excel.append([self.WaveLenth[j]] + [indesity_data[j]])
        wb.save(excel_name)

    def Button_Beijing(self):
        # self.message.show()
        # time.sleep(0.1)
        excel_filename = "D:/Pukon/Beijing" + "/" + self.current + '-' + str('参比光谱') + ".xlsx"
        self.Intensities_Beijing = self.device.GetIntensity_back()
        self.device.SaveBeijingExcel(excel_filename, self.Intensities_Beijing)
        return self.Intensities_Beijing
        # self.message.done(1)

    def breakdown(self):
        self.D1open = [0x55, 0x55, 0x08, 0x03, 0x01, 0xC8, 0x00, 0x00, 0x46, 0x05]
        self.D1close = [0x55, 0x55, 0x08, 0x03, 0x01, 0xC8, 0x00, 0x00, 0xE0, 0x03]
        self.D2right = [0x55, 0x55, 0x08, 0x03, 0x01, 0x01, 0x00, 0x07, 0xF6, 0x03]
        self.D2middle = [0x55, 0x55, 0x08, 0x03, 0x01, 0x01, 0x00, 0x07, 0xEE, 0x02]
        self.D2left = [0x55, 0x55, 0x08, 0x03, 0x01, 0x01, 0x00, 0x07, 0xF6, 0x01]
        self.D3right = [0x55, 0x55, 0x08, 0x03, 0x01, 0xF4, 0x01, 0x04, 0x40, 0x06]
        self.D3left = [0x55, 0x55, 0x08, 0x03, 0x01, 0xF4, 0x01, 0x04, 0xB0, 0x04]
        self.D3middle = [0x55, 0x55, 0x08, 0x03, 0x01, 0xF4, 0x01, 0x04, 0xD4, 0x04]
        self.MOTO_Communication(self.D1open)
        time.sleep(0.1)
        self.MOTO_Communication(self.D2right)
        time.sleep(0.1)
        self.MOTO_Communication(self.D3right)
        time.sleep(10)
        self.MOTO_Communication(self.D3middle)
        time.sleep(0.1)
        self.MOTO_Communication(self.D2middle)
        time.sleep(0.1)
        self.MOTO_Communication(self.D1close)



    def Button_Stop(self):
        self.connectionTimer.stop()
        self.time_cnt = 0

    def Button_Start(self):
        self.connectionTimer.start()

    def print(self):                                                                 #打印机
        # 打印对象其实就是一个画布
        self.editor = QPlainTextEdit(self.device.Dayintime + '\n' + '中科谱康质检仪' + '\n' \
                         +'样品编号'+'       :'+self.lineEdit_number.text() + '\n' \
                         +'容    重'+'       :'+self.lineEdit_density.text()+'\n'\
                         +'淀    粉'+'       :'+self.lineEdit_Statue.text()+'\n'\
                         +'水    分'+'       :'+self.lineEdit_Water.text()+'\n'\
                         +'硬    度'+'       :'+self.lineEdit_hardness.text()+'\n'\
                         +'湿 面 筋'+'       :'+self.lineEdit_gluten.text()+'\n'\
                         +'蛋    白'+'       :'+self.lineEdit_protein.text(), self)
        self.editor.setGeometry(0, 0, 300, 280)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.editor.setFont(font)
        self.editor.setVisible(False)
        print(self.device.Dayintime)
        printer = QtPrintSupport.QPrinter()
        # 笔
        painter = QPainter()
        painter.begin(printer)  # 以前的参数是self，代表的是绘制到窗口，这里的是打印机
        screen = self.editor.grab()
        painter.drawPixmap(-3, -2, screen)
        painter.end()

    def Quality_dataupload(self,Water):

        url = "http://121.37.153.74:8091/api/user/login?username=17344050960&password=E10ADC3949BA59ABBE56E057F20F883E&baseCode=100000"

        payload = ""
        headers = {}
        import json
        import requests
        response = requests.request("POST", url, headers=headers, data=payload)
        token=response.headers.get("Authorization")
        print(response.text)
        url = "http://121.37.153.74:8091/api/baseStation/getBaseSettings"
        payload = ""
        headers = {
          'Content-Type': 'application/json',
          'Authorization': token,
          'DateString': '2021-05-19 09:52:16'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)
        import json

        url = "http://121.37.153.74:8091/api/sampleCheck/swiping?cardNum=112233"

        payload = json.dumps({
          "page": 1,
          "pageSize": 5,
          "timeStart": "2020-12-01 00:00:00",
          "timeEnd": "2021-01-01 00:00:00"
        })
        headers = {
          'Content-Type': 'application/json',
          'Authorization': token
        }
        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)
        categoryId =response.text[416:418]
        url = "http://121.37.153.74:8091/api/sampleCheck/categorySelect?categoryId=19"
        payload={}
        headers = {
          'Authorization': token
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)
        url = "http://121.37.153.74:8091/api/sampleCheck/budgetedPrice?a=" + Water +"&l=&categoryId=19"
        payload = ""
        headers = {
          'Content-Type': 'application/json',
          'Authorization': token
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)

        import requests

        url = "http://121.37.153.74:8091/api/file/upload"

        payload={}

        headers = {
          'Authorization': token
        }
        files= {'file':('xingtaixue.png',open('D:/zhaoshg/Pictures/wallpaper/xingtaixue.png','rb'),'image/png')}#图片地址
        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        #保存质检结果
        import requests
        import json

        url = "http://121.37.153.74:8091/api/sampleCheck/submit"

        payload = json.dumps({
          "calculatePrice": 0.002,
          "categoryId": 41,
          "fileIds": [
            0
          ],
          "manualPrice": 0.002,
          "orderNo": 1002207150002,
          "percent": 100,
          "policyId": 0,
          "remark": "纯接口测试2",
          "sampleCheckDetails": [
            {
              "propertyId": 211,
              "value": "15"
            },
            {
              "propertyId": 212,
              "value": "1"
            },
            {
              "propertyId": 214,
              "value": "1"
            },
            {
              "propertyId": 216,
              "value": "10"
            },
            {
              "propertyId": 217,
              "value": "68"
            },
            {
              "propertyId": 796,
              "value": "50"
            }
          ],
          "warehouseId": 24,
          "positionId": 1
        })
        headers = {
          'Content-Type': 'application/json',
          'Authorization': token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)