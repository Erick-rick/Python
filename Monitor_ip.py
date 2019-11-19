
#Monitoramento de ips dublicados 

#** Scapy - biblioteca de manipulação de pacote interativa com uma quantidade de protocolos (tcpp/ip)
#
from scapy.all import ARP, sniff

#sniff função usanda para monitorar os pacotes que trafegam na rede usando o protocolo ARP

sniff(prn=pacotes, filter="arp", iface= interface, timeout=10)

# prn    > função poara ser aplicada a cada pacote capturado pelo sniff
# filter > filtrar todos os pacote que contiverem o protocolo ARP
# iface  > interface de rede que será monitorada
# timeout> determina que o monitoramento da rede se dara por 60 seg

from collections import defaultdict
list_ips= defaultdict(set)

def pacotes(pacote):
    #Checa se o valor do opcode dentro do protocolo arp igual a 2

    if pacote[ARP].op ==2:
        # Se for adiciona o ip de origem e seu mac á dict list_ips
        list_ips[pacote[ARP].psrc].add(pacote[ARP].hwsrc)

import os
os.system('which arp')
/usr/sbin/arp

def monitorar(interface):
    
    # O comando arp no FreeBSD usa os paramentros:
    # 
    # -d para deletar as entradas  
    # -i para declarar a interface
    # -a representar todas entradas a serem deletas
    # #

    cmd = "/usr/sbin/arp -d -i {} -a".format(interface)
    os.system(cmd)
    sniff(prn=pacotes, filter='arp', iface= interface, timeout=10)

#monitorar a interface ex. em0
monitorar('em0')

for ip in list_ips:
    print('IP:{} -> MACs: {}').format(ip, ','.join(list(list_ips[ip])))

IP:192.168.231.1 -> MACs 00:90:0b:49:3d:0a
IP:192.168.213.10 ->MACs 08:00:27:bf:52:6d, a0:f3:c1:03:74:6a