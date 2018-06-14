# DDoS in Lab

![image](https://github.com/TakingOffPKU/DDoS/blob/master/img/icon.ico)



## Goal

Our goal is to build a safe environment to perform toy-like DDoS attack and defence. Such goal requires a Web server, many computers (perform as bots in a botnet), and two groups (one for attacking and one for defense) of geniuses.



## Web Server

The web server, along with the monitor server (which is a twin server of the web server) are built by the defense group.

The web server performs as the server to be attacked, and the monitor server monitors the CPU utilization, RAM utilization, network utilization and etc of the server. When the attack begins, the defenders are able to decide which defense policy to apply, basing on the data provided by the monitor server.

The web server is just a demo server run on apache + PHP. The monitor server uses Linux dash to retrieve the utilizations, as shown below. Based on the servers, the defense group are able to carry out several defense policies.



Linux dash board
![image](https://github.com/TakingOffPKU/DDoS/blob/master/img/linux_dash.png)



The servers and the sites are in the directory 'server'. The implementations of the defense policies are in the directory 'ddos', which would be mentioned later.



## DDoS Attack

Three DDoS approaches are carried out -- SYNFlood, HTTPFlood, and slowloris. SYNFlood and HTTPFlood are flooding attacks, and slowloris is a slow-connection attack.

The implementations are in directory 'ddos'. Use the following commands to begin the attack, or use '-h' argument for help.

```
> python3 synflood.py -H TARGET_IP -P TARGET_PORT -T N_THREADS -V VERBOSE_MODE
> python3 httpflood.py -H TARGET_IP -P TARGET_PORT -T N_THREADS -V VERBOSE_MODE
> python3 slowloris.py -H TARGET_IP -P TARGET_PORT -T N_THREADS -V VERBOSE_MODE
```

In order to carry out DDoS attack with control, a botnet is necessary. We build the botnet with the structure shown below. The bots are seperated on many PCs or servers. When the bots are online, they send a "I am alive!" message every hour to the manager server, which is a permanent and persistent server. The manager server maintains an alive-bot table. The attacker may start the attack anywhere on this planet. He only needs to download the alive-bot table, and use it to control the botnet.



Botnet
![image](https://github.com/TakingOffPKU/DDoS/blob/master/img/botnet.png)



The implementation of the bots are in 'ddos/attack_bot.py'. The implementation of the manager is in 'ddos/bot_manage.py'. The control program, which is a command line program, is in 'ddos/attacker.py'.  The GUI version of the control program is implemented with PyQT5 in 'ddos/attacker_ui.py'. Use the following commands to run the bots, the manager and the controller.

```
> python3 attack_bot.py	% Run this command on the bots.
> python3 bot_manage.py	% Run this command on the manager server.
> python3 attacker.py	% Run this command on the attacker's equippment to start a DDoS attack with command-line.
> python3 attacker_ui.py	% Run this command on the attacker's equippment to start a DDoS attack with GUI.
```

HTTPFlood and slowloris attacks are presented in the GIFs below. The first visiting is fluent and without DDoS attack, and the second is inaccessible and with DDoS.



HTTPFlood
![image](https://github.com/TakingOffPKU/DDoS/blob/master/img/httpflood.gif)

Slowloris
![image](https://github.com/TakingOffPKU/DDoS/blob/master/img/slowloris.gif)



## DDoS Defense

Three defense policies against the SYNFlood, HTTPFlood and slowloris attacks are implemented in 'ddos/synflood_defend.py' and 'ddos/httpflood_defend.py'. They are filtration-based.

Run these programs as proxy before the web-server to defend it.

