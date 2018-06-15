from netfilterqueue import NetfilterQueue
from scapy.all import *
import os

SERVERPORT = 8010

iptables_init = 'iptables -I INPUT -p tcp --dport {} -j NFQUEUE --queue-num 1'.format(SERVERPORT)
iptables_clean = 'iptables -F'


def print_and_accept(pkt):
    print(pkt)
    hw = pkt.get_hw()
    if hw:
        print(":".join("{:02x}".format(ord(c)) for c in hw[0:6]))
        scpkt = IP(hw)
        print(scpkt)
    pkt.accept()

def main():
    print('iptables init: {}'.format(iptables_init))
    os.system(iptables_init)
    nfqueue = NetfilterQueue()
    nfqueue.bind(1, print_and_accept)
    try:
        nfqueue.run()
    except KeyboardInterrupt:
        print('\nKeyboard Interrrupt.')
        print('iptables clean: {}'.format(iptables_clean))
        os.system(iptables_clean)
        exit(1)

    nfqueue.unbind()
    os.system(iptables_clean)

if __name__ == "__main__":
    main()
