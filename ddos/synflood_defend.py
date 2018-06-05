# -*- coding: utf-8 -*-
"""
@author: Veronica ZHANG
"""
import sys
import threading
import argparse
import socket
import random
import scapy.all as sca

mapping = {}
ports = []
SERVERIP = "47.94.138.231"
SERVERPORT = 80
FIREIP = "127.0.0.1"
FIREPORT = 9645

def help():
	print("-h, --help            show this help message and exit")
	print("--port PORT, -p PORT  port of firewall")
	print("--ip IP, -i IP        IP of firewall")

def parsearg():
	parser = argparse.ArgumentParser()

	parser.add_argument('--port', '-p', help="port of firewall")
	parser.add_argument('--ip', '-i', help="IP of firewall")

	args = parser.parse_args()
	return args

def sendTCP(dst, src, dport, sport, flags):
	try:
		i = sca.IP()
		t = sca.TCP()
		i.src = src
		i.dst = dst
		t.sport = sport
		t.dport = dport
		t.flags = flags
		sca.send(i/t, verbose=0)
		return
	except KeyboardInterrupt:
		print("\nSYN attack defend ends!")
		exit(0)

def connectServer(port):
	sendTCP(SERVERIP, FIREIP, SERVERPORT, port, 'S')
	
	while True:
		finish = False
		pkt = sca.sniff(filter = "(ip dst host %s) and (tcp dst port %d)" %(SERVERIP, port), count=1)
		for r in pkt.res:
			if r['TCP'].flags == 'SA':
				sendTCP(SERVERIP, FIREIP, SERVERPORT, port, 'A')
				finish = True
				break
		if finish:
			break

def tcplink(Saddr, Sport):
	print("Accept new connection from %s..." % Saddr)
	port = 0
	while True: # 分配端口
		port = random.randint(20000, 65535)
		if port not in ports:
			mapping[port] = [Saddr, Sport]
			ports.append(port)
			break

	connectServer(port)

	while True:
		quit = False
		pkts = sca.sniff(filter = "(ip dst host %s) and (tcp port %d)" %(FIREIP, FIREPORT), count=1)
		for r in pkts.res:
			# 转发给Server
			r['IP'].dst = SERVERIP
			r['TCP'].dport = SERVERPORT
			r['IP'].src = FIREIP
			r['TCP'].sport = port
			sca.send(r)
		pkts = sca.sniff(filter = "(ip dst host %s) and (tcp port %d)" %(FIREIP, port), count=1)
		for r in pkts.res:	
			# 发给Client
			r['IP'].dst = mapping[port][0]
			r['TCP'].dport = mapping[port][1]
			r['IP'].src = FIREIP
			r['TCP'].sport = FIREPORT
			sca.send(r)
			if (r['TCP'].flags == 'F'):
				quit = True
				break
		if quit:
			break

def catchPkt(fireip, fireport):
	while True:
		try:
			pkts = sca.sniff(filter = "(ip dst host %s) and (tcp dst port %d)" %(fireip, fireport), count=1)
			#pkts = sniff(filter = "(ip dst host 127.0.0.1) and (tcp port 9645)", count=1)
			for r in pkts.res:
				if r['TCP'].flags == 'S':
					#print(r['IP'].src)
					sendTCP(r['IP'].src, r['IP'].dst, r['TCP'].sport, r['TCP'].dport, 'SA')
				elif r['TCP'].flags == 'A':
					print(r['IP'].src)
					t = threading.Thread(target = tcplink, args = (r['IP'].src, r['TCP'].sport))
					t.start()

		except KeyboardInterrupt:
			print("\nSYN attack defend ends!")
			exit(0)

def main():
	args = parsearg()
	if args.port and args.ip:
		print("IP of firewall is %s; port of firewall is %s." %(args.ip, args.port))
		FIREIP = args.ip
		FIREPORT = int(args.port)
	else:
		pass
		help()
		exit(1)
	print("Now we are trying to defend SYN Flood Attack!")
	#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#s.bind((FIREIP, FIREPORT))
	#s.listen(5)

	catchPkt(FIREIP, FIREPORT)

if __name__ == '__main__':
	main()
