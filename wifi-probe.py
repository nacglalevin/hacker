"""
========================================
Name:Shenji Arrow Author: Lalevin Martin
 Mailbox: zzlyxht@outlook.com                                                
 Github: http://github.com/nacglalevin
Written in 2022-11-28
==================NACG==================
"""
from scapy.all import *

def Probe_packet(packet):
    probeReqs = []
    if packet.haslayer(Dot11Beacon):
        if packet.getlayer(Dot11Beacon).info == "":
            addr2 = packet.getlayer(Dot11).addr2
            if addr2 not in hiddenNets:
                print "[-] Detected Hidden SSID: with MAC:"+addr2
        else:
            netName = p.getlayer(Dot11Beacon).info
            if netName not in probeReqs:
                probeReqs.append(netName)
                print "[+] Detected New Probe Request:" + netName

sniff(prn=Probe_packet)
