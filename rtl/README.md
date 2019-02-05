# RTL helpers

# rtlswitch
script for switching between original DVB-T drivers and the osmo-sdr. Basically just loading and unloading driver modules. Supports classic RTL2382U and RTL2382P (Astrometa DVB-T2) for which it renames frontends to use built-in Panasonic DVB-T2 demodulator as default in VLC
### Enabling DVB-T:
- UNPLUG device!
- run rtlswitch -o
- PLUG IN device
- If your device is Astrometa DVB-T2 or clone, you have to rename your frontends to use it in vlc - run rtlswitch -o

### Enabling osmo-sdr:
- UNPLUG device!
- run rtlswitch -r
- PLUG in device!

# programstream
script which makes VLC to stream (via HTTP) a particular DVB-T/2 program very efficiently by using #transcode with video&audio copying - which actually remuxes these particular streams. This works in more cases than just #duplicate with a program specified and much better than tvheadend.

This way streaming 1080p/50fps channel consumes only 10-20% of one Cortex A53@1GHz (maybe up to 40% on A7) and it works flawlessly. Furthermore, VLC does this in multiple threads.
### programstream switches:
- -p | --program INT specifies program number in transponder
- -f | --frequency INT specifies frequency of transponder in Hz
- -t | --dvbttwo 1/0 specifies if using DVB-T2 (default is yes)
- -P | --port INT specifies open HTTP port for streaming

# SDRTrunk channels
backed up playlists of trunks i have found in my location
