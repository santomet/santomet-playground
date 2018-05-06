#!/usr/bin/python3

import sys
import json
from urllib import request as urlrequest

def getPlaylist(prog, prnt):
    url = "http://www.rtvs.sk/json/live5.json?c={}&b=chrome&p=linux&v=64&f=0&d=1".format(prog)
    req = urlrequest.Request(url)
#    req.set_proxy("195.146.133.90:3128", "http")
    resp = urlrequest.urlopen(req)

    resp_string = resp.read().decode("utf-8")
    json_obj = json.loads(resp_string)[0]

    if prnt:
        print("detekovany program je {}. FullHD stream by mal byt:".format(json_obj["mediaid"]))
    m3u8_source = json_obj["sources"][0]

    playlist_url = m3u8_source["file"]
    last_lomitko = playlist_url.rfind("/")
    url_base = playlist_url[:last_lomitko+1]

    resp = urlrequest.urlopen(playlist_url)
    resp_string = resp.read().decode("utf-8")

    lines = resp_string.split('\n')

    best_line = 5
    
    for i in range(len(lines)):
        if "1920" in lines[i]:
            best_line = i+1

    final_url = url_base + lines[best_line]

    print(final_url)

def main():
    
    txt = """
                              tttt                                       
                          ttt:::t                                       
                          t:::::t                                       
                          t:::::t                                       
rrrrr   rrrrrrrrr   ttttttt:::::tttttttvvvvvvv           vvvvvvv        
r::::rrr:::::::::r  t:::::::::::::::::t v:::::v         v:::::v  :::::: 
r:::::::::::::::::r t:::::::::::::::::t  v:::::v       v:::::v   :::::: 
rr::::::rrrrr::::::rtttttt:::::::tttttt   v:::::v     v:::::v    :::::: 
 r:::::r     r:::::r      t:::::t          v:::::v   v:::::v            
 r:::::r     rrrrrrr      t:::::t           v:::::v v:::::v             
 r:::::r                  t:::::t            v:::::v:::::v              
 r:::::r                  t:::::t    tttttt   v:::::::::v        :::::: 
 r:::::r                  t::::::tttt:::::t    v:::::::v         :::::: 
 r:::::r                  tt::::::::::::::t     v:::::v          :::::: 
 r:::::r                    tt:::::::::::tt      v:::v                  
 rrrrrrr                      ttttttttttt         vvv

                          ____        _      
                         |___ \__   _| | ___ 
                           __) \ \ / / |/ __|
                          / __/ \ V /| | (__ 
                         |_____| \_/ |_|\___|
                                             github.com/santomet

    Nazdar! pre ukončenie programu vlož "e"!
    """
    print(txt)
    while True:
        num = input("Zvoľ si program (STV1 = 1) Program: ")
        if num == 'e':
            break
        if not num.isnumeric():
            continue

        num = int(num)
        getPlaylist(num, True)
        
if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isnumeric():
        getPlaylist(int(sys.argv[1]), False)
    else:
        print(len(sys.argv))
        main()
