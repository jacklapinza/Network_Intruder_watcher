import os
import re
from termcolor import colored

stringa = os.popen('nmap -sP 192.168.1.0/24').read()


ipdict = {
    "FireTv": "192.168.1.195",
    "S8 Lavoro": "192.168.1.105",
    "Macbook": "192.168.1.196",
    "Switch": "192.168.1.158",
    "Ipcam1": "192.168.1.136",
    "Ipcam2": "192.168.1.147",
    "Echo": "192.168.1.122",
    "HubHue": "192.168.1.149",
    "DesktopPC": "192.168.1.145",
    "Stampante": "192.168.1.173",
    "Thosiba": "192.168.1.107",
    "Note9": "192.168.1.156",
    "Fritz!": "192.168.1.172",
    "SmartPlug": "192.168.1.182",
    "Televisore": "192.168.1.160",
    "Fastgate": "192.168.1.254"
}

offline = []
online = []
confronto = []

for x in ipdict:
    result = stringa.find(ipdict[x])
    if result == -1:
        print("Il dispositivo:", colored("{}".format(x), "red"), "risulta", colored("offline", "red"))
        offline.append(x)
        ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', stringa )
        for x in ip:
            for z in ipdict:
                if x in ipdict[z]:
                    confronto.append(x)
    else:
        print ("Il dispositivo:", colored("{}".format(x), "green"), "è", colored("online", "green"), "con l'IP:", colored("{}".format(ipdict[x]), "green"))
        online.append(x)

def Diff(ip, confronto): 
    return (list(set(ip) - set(confronto)))


primaestrazione = "done:"

output_1 = stringa[stringa.find(primaestrazione):]

secondaestrazione = "("

output_2 = output_1[output_1.find(secondaestrazione):]

finale = output_2[1:4]

conversione = int(finale)

sconosciuto = Diff(ip, confronto)



if conversione == len(online):
    print("Tutto nella norma")
else:
    print("Attenzione")
    print(conversione)
    

