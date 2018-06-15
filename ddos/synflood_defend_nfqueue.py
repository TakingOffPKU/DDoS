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
        if src == '127.0.0.1':
            print('accept local package')
            # pkt.accept()
        elif src in white_list:
            print('{} is in white_list'.format(src))
            # pkt.accept()
        elif src in waitting_list:
            if tcp_pkt.flags == 'A':
                print('{} was moved to wait_list'.format(src))
                white_list.add(src)
                waitting_list.remove(src)
                # pkt.accept()
            else:
                print('{} has been filtered with no A flag'.format(src))
                # pkt.drop()
        else:
            if tcp_pkt.flags == 'S':
                print('{} was added to waitting_list'.format(src))
                waitting_list.add(src)
                # pkt.accept()
            else:
                print('{} has been filtered with no S flag'.format(src))
                # pkt.drop()

        raw_pkt = Raw(pkt.get_payload())
        if raw_pkt.load:
            print(raw_pkt.load)
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
