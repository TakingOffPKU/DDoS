from netfilterqueue import NetfilterQueue
from scapy.all import *
import os

# SERVERIP = "47.94.138.231"
SERVERPORT = 8010


def print_and_accept(pkt):
    print(pkt)
    hw = pkt.get_hw()
    if hw:
        print(":".join("{:02x}".format(ord(c)) for c in hw[0:6]))
    pkt.accept()

def main():
    nfqueue = NetfilterQueue()
    nfqueue.bind(1, print_and_accept)
    try:
        nfqueue.run()
    except KeyboardInterrupt:
        print('Keyboard Interrrupt.')
        exit(1)

    nfqueue.unbind()


if __name__ == "__main__":
    main()
