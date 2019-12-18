import os
import re
from termcolor import colored

# Lettura stringa da comando nmap. I tempi di attesa si aggirano introno ai 20 secondi.
stringa = os.popen('nmap -sP 192.168.1.0/24').read()

# Dizionario generale di tutti i dispositivi consciuti.
# Questo dizionario va modificato a seconda dei propri dispositivi
# ed è puramente illustrativo.
ipdict = {
    "FireTv_2°": "192.168.1.245",
    "Macbook": "192.168.1.238",
    "Switch": "192.168.1.158",
    "Ipcam1": "192.168.1.136",
    "Ipcam2": "192.168.1.147",
    "Echo": "192.168.1.142",
    "HubHue": "192.168.1.191",
    "DesktopPC": "192.168.1.145",
    "Stampante": "192.168.1.173",
    "Thosiba": "192.168.1.107",
    "Note9": "92.168.1.87",
    "Fritz!": "192.168.1.172",
    "SmartPlug": "192.168.1.182",
    "Televisore": "192.168.1.160",
    "Fastgate": "192.168.1.254",
    "Kobo": "192.168.1.161",
    "Ipad": "192.168.1.126",
    "PS4": "192.168.1.137"
}

# Lista dispositivi offline
offline = []

                        # Lista dispositivi online
                        # Gli elementi in questa lista verrano comparati ai dispositivi online rilevati da nmap.
online = []             # Nel caso coincidessero verrà interpretato
                        # come un comportamento nella norma. Tutti i dispositivi online sono presenti nel dizionario.

                        # Lista di confronto
confronto = []          # Questa lista serve per effetuare un confronto tra i dispositivi online trovati da nmap
                        # e quelli presenti in dizionario.
                        # Nel caso non coincidessero l'ip risultante sara l'indirizzo di un dispositivo non consciuto.


# Iteazioni logiche per definire quali sono i dispositivi online rilevati da nmap, se sono presenti nel dizionario o meno.
for x in ipdict:
    result = stringa.find(ipdict[x])
    if result == -1:
        print("Il dispositivo:", colored("{}".format(x), "red"),
              "risulta", colored("offline", "red"))
        offline.append(x)
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', stringa)
        for x in ip:
            for z in ipdict:
                if x in ipdict[z]:
                    # Aggiunti alla lista online tutti i dispostivi presenti sia nella stringa nmap che nel dizionario
                    confronto.append(x)
    else:
        print("Il dispositivo:", colored("{}".format(x), "green"), "è", colored(
            "online", "green"), "con l'IP:", colored("{}".format(ipdict[x]), "green"))
        # Aggiunta alla lista confronto gli ip dei dispositivi online ma non presenti nel dizionario personale.
        online.append(x)


def Diff(ip, confronto):
    return (list(set(ip) - set(confronto)))


# Decisamente confusionario. Processo per estrarre il numero totale di dispositivi connessi ---- INIZIO
primaestrazione = "done:"

output_1 = stringa[stringa.find(primaestrazione):]

secondaestrazione = "("

output_2 = output_1[output_1.find(secondaestrazione):]

print(output_2)

terzaestrazione = ")"

output_3 = output_2[:output_2.find(terzaestrazione)]

                                        # Il numero che si ottine è il caclolo complessivo
finale = re.findall('\d+', output_3)    # dei dispositivi online.
                                        # Verrà usato in seguito per effetuare un confronto
                                        # tra la lista online del dizionario e
                                        # i dispositivi online rilevati da nmap.

# ---- FINE


# Differenze tra la la lista di dispositivi online rilevati internamente e quelli evidenziati da nmap
sconosciuto = Diff(ip, confronto)

# Iterazione logica per procedere alla visualizzazione. Nel caso il numero dei dispositivi online 
# rilevati da nmap corrisponde al numero totale di elementi presenti nella lista di dipsositivi online,
# tutto è nella norma perchè non ci sono discrepanze.
# Nel caso invece il numero fosse diverso, viene visuazlizzato l'IP differente ottentuto dalla 
# comparazione della lista dispositivi online e quella di confronto.

norma = ""

for x in range(len(finale)):
    if int(finale[x]) == len(online):
        print("Tutto nella norma")
        norma = "Norma"
    else:
        print("Attenzione")
        for x in range(len(sconosciuto)):
            print("Nuovo dispositivo non presente in dizionario. IP:",
                  colored("{}".format(sconosciuto[x]), "yellow"))

