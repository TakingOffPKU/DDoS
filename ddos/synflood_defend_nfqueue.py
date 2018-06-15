from netfilterqueue import NetfilterQueue
from scapy.all import *
import os

SERVERPORT = 8010

iptables_init = 'iptables -I INPUT -p tcp --dport {} -j NFQUEUE --queue-num 1'.format(SERVERPORT)
iptables_clean = 'iptables -F'

white_list = set([])
waitting_list = set([])

def print_and_accept(pkt):
    hw = pkt.get_hw()
    if hw:
        ip_pkt = IP(pkt.get_payload())
        tcp_pkt = TCP(pkt.get_payload())

        src = ip_pkt.src
        if src in white_list:
            pkt.accept()
        elif src in waitting_list:
            if tcp_pkt.flags == 'A':
                white_list.add(src)
                waitting_list.remove(src)
                pkt.accept()
            else:
                pkt.drop()
        else:
            if tcp_pkt.flags == 'S':
                white_list.add(src)
            else:
                pkt.drop()

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
